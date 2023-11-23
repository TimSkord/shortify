from sqlalchemy import Column, Integer, String
from db.database import Base


class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    short_url = Column(String, unique=True, index=True)
    full_url = Column(String, index=True)

    def __repr__(self):
        return f"<URL(id='{self.id}', short_url='{self.short_url}', full_url='{self.full_url}')>"
