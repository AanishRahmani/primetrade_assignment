from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    content = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) )
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) )

    owner = relationship("User", back_populates="posts")
