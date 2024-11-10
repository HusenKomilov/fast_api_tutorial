from .models import Booking
from database import async_session_maker
from sqlalchemy import select
from dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Booking
