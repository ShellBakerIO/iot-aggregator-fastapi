from typing import TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .device import Device
from .base import Base
from datetime import datetime

if TYPE_CHECKING:
    from .device import Device


class Measurement(Base):
    __tablename__ = 'measurement'

    id: Mapped[int] = mapped_column(primary_key=True)
    device_id: Mapped[int] = mapped_column(ForeignKey('devices.id'))
    value: Mapped[str]
    timestamp: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)

    device: Mapped["Device"] = relationship(back_populates="measurements")
