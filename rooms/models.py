from sqlalchemy import Integer, Column, String, VARCHAR, JSON, ForeignKey
from database import Base


class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    service = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
