from pydantic import BaseModel


class customers(BaseModel):
    username: str
    password: str
    email: str
    phone_no: str


class Booking(BaseModel):
    name: str
    place: str
    number: str
