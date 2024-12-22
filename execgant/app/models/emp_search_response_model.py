from pydantic import BaseModel


class EmployeeSearchResponse(BaseModel):

    employee_name: str
    employee_id: str
    gender: str
    address: str
    meta: dict | None = None
