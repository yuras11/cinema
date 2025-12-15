from pydantic import BaseModel


class UserRegisterScheme(BaseModel):
    userlogin: str
    userpassword: str
    username: str
    useremail: str
    model_config = {'from_attributes': True}


class UserUpdateScheme(BaseModel):
    userid: str
    userlogin: str
    userpassword: str
    username: str
    useremail: str
    model_config = {'from_attributes': True}


class UserLoginScheme(BaseModel):
    userlogin: str
    userpassword: str