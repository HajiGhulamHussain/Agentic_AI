from dataclasses import dataclass
# from pydantic import BaseModel

#schema data class
@dataclass
class UserDataType:
    name:str
    age:int
    role:str 


# schema from pydantic BaseModel
# class UserDataType(BaseModel):
#     name:str
#     age:int
#     role:str 