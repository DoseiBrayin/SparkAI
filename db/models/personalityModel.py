from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Personality(Base):
    __tablename__ = 'personality'

    id = Column(String(36), primary_key=True)
    type = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type
        }