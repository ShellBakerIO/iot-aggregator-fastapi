from typing import TYPE_CHECKING
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .measurement import Measurement


class Device(Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    name: Mapped[str] = mapped_column(String(30))
    device_type: Mapped[str] = mapped_column(String(30))
    communication_type: Mapped[str] = mapped_column(String(15))
    registration_date: Mapped[str] = mapped_column(DateTime)

    measurements: Mapped[list["Measurement"]] = relationship(back_populates="device")
