import uuid
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class UserScheme(BaseModel):
    userid: uuid.UUID = Field(default_factory=lambda: uuid4().hex)
    userlogin: str
    userpassword: str
    username: str
    usersurname: str
    userrole: bool
    userphoto: Optional[str] = Field(None, max_length=100, description="User photo")
    model_config = {'from_attributes': True}


#class UserAddScheme(BaseModel):

class UserRegisterScheme(BaseModel):
    userlogin: str
    userpassword: str
    username: str
    usersurname: str
    model_config = {'from_attributes': True}


class UserLoginScheme(BaseModel):
    userlogin: str
    userpassword: str