from fastapi import APIRouter
from sqlalchemy import select

from database import async_session_maker
from rooms import Rooms
from .models import Booking
from users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=['Booking 1.0']
)


@router.get("/")
async def get_bookings():
    async with async_session_maker() as session:
        # query = select(Booking)
        #
        # result = await session.execute(query)
        # return result.scalars().all()
        query = (
            select(
                Booking,
                Rooms,
                Users,
            ).join(Rooms, Rooms.id == Booking.room_id, isouter=True).join(Users, Users.id == Booking.user_id, isouter=True)
        )
        result = await session.execute(query)
        return result.mappings().all()