from pydantic import BaseModel, EmailStr, Field, Field_validator
from typing import List, Dict, Optional, Annotated

class User_info(BaseModel):
    # name: str=Field(max_length=20)
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="give the name of the patient in less than 20 char")]
    age:int=Field(gt=0 , lt=20)
    email: EmailStr
    weight: Optional[float]=None
    married: Annotated[boo, Field(default=None, description="Is the patient married or not")]
    alergics: List[str]
    contact: Dict[str, str]


def user_info(user: User_info):
    return {"name":user.name, "age":user.age, "married":user.married}



patient1={"name":"piyush", "age":21, "weight":70.5, "married":False, "alergics":["penicillin", "aspirin"], "contact":{"email":"piyush@gmail.com", "phone":"1234567890"}}


pat1=User_info(**patient1)

print(pat1)

print(user_info(pat1))