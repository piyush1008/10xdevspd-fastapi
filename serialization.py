from pydantic import BaseModel


class Address(BaseModel):
    city: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age:int
    address: Address

address_1={"city":"akb", "pin":"224122"}

address1=Address(**address_1)

patient_1={"name":"piyush", "gender":"male", "age":12, "address":address1}

patient1=Patient(**patient_1)



# temp=patient1.model_dump()
# 
# temp=patient1.model_dump(include=['name', 'gender'])4

temp=patient1.model_dump(exclude=['name', 'address':['pin']])



print(temp)

print(type(temp))