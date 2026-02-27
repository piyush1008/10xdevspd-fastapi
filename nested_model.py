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

print(patient1.name)
print(patient1.address.city)
