class UserCreate(BaseModel):
    username: str
    email: str
    password: str  # New field

class UserLogin(BaseModel):
    username: str
    password: str
