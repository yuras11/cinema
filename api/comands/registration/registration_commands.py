from pydantic import BaseModel


class RegistrationCommand(BaseModel):
    userlogin: str
    userpassword: str
    username: str
    useremail: str
    model_config = {'from_attributes': True}


class LoginCommand(BaseModel):
    userlogin: str
    userpassword: str
    model_config = {'from_attributes': True}