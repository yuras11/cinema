from pydantic import BaseModel


class UserCommand(BaseModel):
    userlogin: str
    userpassword: str
    username: str
    useremail: str
    model_config = {'from_attributes': True}


class UserLoginCommand(BaseModel):
    userlogin: str
    userpassword: str