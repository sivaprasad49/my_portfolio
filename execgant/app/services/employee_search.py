from sqlalchemy.ext.asyncio import AsyncSession

from app.models.employee_search_request import EmployeeSearchRequest
from app.models.employee_search_response import EmployeeSearchResponse
from app.services.ml_service import MLService

async def employee_search_service(
    emp_search_request: EmployeeSearchRequest,
    db_session: AsyncSession,
    ml_service: MLService,
) -> EmployeeSearchResponse:
    # run some query
    # hit the model 
    # return response 
    return EmployeeSearchResponse()
