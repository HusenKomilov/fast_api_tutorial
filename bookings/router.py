from fastapi import APIRouter

from .dao import BookingDAO
from .schemas import SBooking

"""from sqlalchemy import select

from database import async_session_maker
from rooms import Rooms
from .models import Booking
from users.models import Users"""

router = APIRouter(
    prefix="/bookings",
    tags=['Booking 1.0']
)


@router.get("/", response_model=list[SBooking])
async def get_bookings():
    return await BookingDAO.find_all()


@router.get("/{model_id}")
async def get_booking_by_model_id(model_id: int):
    return await BookingDAO.find_by_id(model_id=model_id)
