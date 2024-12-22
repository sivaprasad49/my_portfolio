import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Response, exceptions
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.util import get_logger

from app.dependencies import get_db_session, get_ml_service
from app.models.emp_search_req_model import EmployeeSearchRequest
from app.models.emp_search_response_model import EmployeeSearchResponse
from app.services.employee_search import employee_search_service
from app.services.ml_service import ml_service, MLService

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    ml_service.load_model()
    yield

app = FastAPI(
    title="Employee Search Service",
    lifespan=lifespan,
    root_path="/employee-search-service/v1",
)


@app.post("/employee-search")
async def get_employee(
    employee_search_request: EmployeeSearchRequest,
    db_session: AsyncSession = Depends(get_db_session),
    ml_service: MLService = Depends(get_ml_service),
) -> EmployeeSearchResponse:
    response = await employee_search_service(employee_search_request, db_session, ml_service)
    return response


@app.exception_handler(exceptions.RequestValidationError)
async def request_validation_exception_handler(
    request: Request, exc: exceptions.RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={
            "status": {
                "code": "REQUEST_VALIDATION_ERROR",
                "description": "Invalid request format",
                "data": jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
            }
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail,
    )


@app.get("/health")
async def health_check():
    return Response(content="ok", status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
