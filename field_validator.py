from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class User_info(BaseModel):
    # name: str=Field(max_length=20)
    name: str
    email: EmailStr
    weight: Optional[float]=None
    height: float
    married: bool
    alergics: List[str]
    contact: Dict[str, str]
     

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domain=["hdfc.com, icici.com"]
        domain_name=values.split("@")[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        return value
    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age>60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 must have emergency contact")
        return model

    @computed_field
    @property
    def calculate_bmi(self):
        bmi=round(self.weight/self.height)*2
    return bmi


def user_info(user: User_info):
    return {"name":user.name, "age":user.age, "married":user.married}



patient1={"name":"piyush", "email:"adc@gmail.com","age":21, "weight":70.5, "married":False, "alergics":["penicillin", "aspirin"], "contact":{"email":"piyush@gmail.com", "phone":"1234567890"}}


pat1=User_info(**patient1)

print(pat1)

print(user_info(pat1))