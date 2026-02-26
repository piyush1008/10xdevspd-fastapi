from pydantic import BaseModel
from typing import List, Dict

class User_info(BaseModel):
    name: str
    age:int
    weight: float
    married: bool
    alergics: List[str]
    contact: Dict[str, str]


def user_info(user: User_info):
    return {"name":user.name, "age":user.age, "married":user.married}



patient1={"name":"piyush", "age":21, "weight":70.5, "married":False, "alergics":["penicillin", "aspirin"], "contact":{"email":"piyush@gmail.com", "phone":"1234567890"}}


pat1=User_info(**patient1)

print(pat1)

print(user_info(pat1))