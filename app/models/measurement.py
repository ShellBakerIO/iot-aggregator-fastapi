from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Measurement(Base):
    __tablename__ = 'measurement'

    id: Mapped[int] = mapped_column(auto_increment=True)
    device_id: Mapped[int] = mapped_column(foreign_key=True)
    value: Mapped[str] = mapped_column(String)
    timestamp: Mapped[DateTime] = mapped_column(DateTime)
