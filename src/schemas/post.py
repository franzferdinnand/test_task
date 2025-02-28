from pydantic import BaseModel, constr
# validation of fields
class PostCreate(BaseModel):
    text: constr(max_length=1000)

class PostResponse(BaseModel):
    id: int
    text: str
    user_id: int

    class Config:
        from_attributes = True