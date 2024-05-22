from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Gender(Base):
    __tablename__ = 'gender'

    id = Column(String(1), primary_key=True)
    name = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }