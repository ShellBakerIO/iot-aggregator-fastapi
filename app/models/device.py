from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Device(Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    name: Mapped[str] = mapped_column(String(30))
    device_type: Mapped[str] = mapped_column(String(30))
    communication_type: Mapped[str] = mapped_column(String(15))
    registration_date: Mapped[str] = mapped_column(DateTime)
