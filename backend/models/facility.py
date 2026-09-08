from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class HealthcareFacility(Base):
    __tablename__ = "healthcare_facilities"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    facility_type = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    state = Column(String)
    district = Column(String)
    village = Column(String)
    contact_number = Column(String)
    services = Column(String)
    beds_available = Column(Integer, default=0)
    doctors_count = Column(Integer, default=0)
    telemedicine_enabled = Column(Integer, default=0)
    accessibility_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class ElderlyPatient(Base):
    __tablename__ = "elderly_patients"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    state = Column(String)
    district = Column(String)
    health_conditions = Column(String)
    mobility_status = Column(String)
    emergency_contact = Column(String)
    last_checkup = Column(DateTime)
    next_appointment = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)