from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    points: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
