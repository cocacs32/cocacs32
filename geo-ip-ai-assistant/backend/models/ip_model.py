from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class IPAddress(Base):
    __tablename__ = 'ip_addresses'

    id = Column(Integer, primary_key=True)
    ip = Column(String, unique=True, nullable=False)
    country = Column(String)
    city = Column(String)
    created_at = Column(DateTime)

    def __repr__(self):
        return f'<IPAddress(ip={self.ip}, country={self.country}, city={self.city})>'
