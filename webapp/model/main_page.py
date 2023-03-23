import datetime
from pydantic import BaseModel, Field, validator
from enum import Enum

from typing import Optional, List
from email_validator import validate_email

class Envs(Enum):
    Staging = 'Staging'
    Production = 'Production'

class MAINPAGE(BaseModel):
    product : str
    stack : str
    environments: Envs = Field(None, description='Available Environments')
    data_golive : datetime.date
    team_owner : str
    squad_owner : str
    team_lead_owner : str
    po_pm: str


    # @validator('po_pm')
    # def validateEmail(cls, po_pm):
    #     valid_email = validate_email(po_pm)
    #     return valid_email.po_pm


    