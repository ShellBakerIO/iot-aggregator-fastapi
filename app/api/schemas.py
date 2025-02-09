from pydantic import BaseModel


class CreateDevice(BaseModel):
    name: str
    device_type: str
    communication_type: str
    registration_date: str


class CreateMeasurement(BaseModel):
    value: str
    timestamp: str

