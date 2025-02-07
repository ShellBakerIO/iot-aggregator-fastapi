from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Measurement(Base):
    __tablename__ = 'measurement'

    id: Mapped[int] = mapped_column(auto_increment=True)
    device_id: Mapped[int] = mapped_column(ForeignKey('devices.id'))
    value: Mapped[str]
    timestamp: Mapped[DateTime] = mapped_column(DateTime)
