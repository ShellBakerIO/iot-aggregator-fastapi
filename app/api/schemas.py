from pydantic import BaseModel


class CreateDevice(BaseModel):
    name: str
    device_type: str
    communication_type: str
    registration_date: str


class CreateMeasurements(BaseModel):
    device_id: int
    value: str
    timestamp: str

