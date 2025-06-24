import uuid
from uuid import uuid4

from pydantic import BaseModel, Field


class UserScheme(BaseModel):
    userid: uuid.UUID = Field(default_factory=lambda: uuid4().hex)
    userlogin: str
    userpassword: str
    username: str
    usersurname: str
    userrole: bool

    model_config = {'from_attributes': True}


#class UserAddScheme(BaseModel):
