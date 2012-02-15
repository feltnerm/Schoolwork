#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class Hotel(Base):
    
    __tablename__ = 'hotel'
    hotelNo = Column(Integer, primary_key=True)
    hotelName = Column(String)
    city = Column(String)

class Room(Base):

    __tablename__ = 'room'
    roomNo = Column(Integer, primary_key=True)
    hotelNo = Column(Integer, ForeignKey('hotel.hotelNo'))
    roomType = Column(String)
    price = Column(Integer)


class Booking(Base):

    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True)
    hotelNo = Column(Integer, ForeignKey('hotel.hotelNo'))
    guestNo = Column(Integer, ForeignKey('guest.guestNo'))
    dateFrom = Column(DateTime)
    dateTo = Column(DateTime)
    roomNo = Column(Integer, ForeignKey('room.roomNo'))

class Guest(Base):

    __tablename__ = 'guest'
    guestNo = Column(Integer, primary_key=True)
    guestName = Column(String)
    guestAddress = Column(String)

Base.metadata.create_all(engine)
