from pydantic import BaseModel, EmailStr, constr
#validation of fields
class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=6)

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True