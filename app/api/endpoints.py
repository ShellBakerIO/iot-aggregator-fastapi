from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from .schemas import CreateDevice, CreateMeasurements
from app.models import Device, Measurement
from app.core import get_db
app = FastAPI()


@app.post('/devices')
async def create_device(device: CreateDevice, db: Session = Depends(get_db)):
    try:
        new_device = Device(**device.dict())
        new_device.registration_date = datetime.strptime(new_device.registration_date, '%d-%m-%Y')
        db.add(new_device)
        await db.commit()
        await db.refresh(new_device)
        return new_device
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'DD-MM-YYYY'.")


@app.get("/devices")
async def get_all_devices(db: Session = Depends(get_db)):
    res = await db.execute(select(Device))
    devices = res.scalars().all()
    return devices


@app.get("/devices/{device_id}")
async def get_device(device_id: int, db: Session = Depends(get_db)):
    res = await db.execute(select(Device).where(Device.id == device_id))
    device = res.scalars().first()

    if device is None:
        raise HTTPException(status_code=404, detail=f"Device with ID {device_id} not found")

    return device


@app.delete('/devices')
async def delete_device(device_id: int, db: Session = Depends(get_db)):
    res = await db.execute(select(Device).where(Device.id == device_id))
    device = res.scalars().first()

    if device is None:
        raise HTTPException(status_code=404, detail=f"Device with ID {device_id} not found")

    db.delete(device)
    await db.commit()
    await db.refresh(device)
    return device
