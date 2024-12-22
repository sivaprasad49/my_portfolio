from pydantic import BaseModel
import datetime


class EmployeeSearchRequest(BaseModel):
    name_: str
    aadhar_number: str