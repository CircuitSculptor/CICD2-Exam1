from typing import Annotated

from pydantic import BaseModel, StringConstraints, ConfigDict, Field

NameStr = Annotated[str, StringConstraints(min_length=2, max_length=60)]
PurposeStr = Annotated[str, StringConstraints(min_length=5, max_length=100)]

class UserCreate(BaseModel):
    equipment_id: int
    borrower_name: NameStr
    loan_days: int
    purpose: PurposeStr
    status: int

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int 
    borrower_name: NameStr
    loan_days: int = Field(gt=1, lt=14)
    purpose: PurposeStr
    status: int