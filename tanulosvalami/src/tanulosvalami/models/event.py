"""
Event database model.
"""
from datetime import datetime
from typing import List
from sqlalchemy import String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from tanulosvalami.database import Base


class Event(Base):
    """
    Rendezvény model.

    Attributes:
        id: Egyedi azonosító
        name: Rendezvény neve
        date: Rendezvény dátuma
        location: Helyszín (opcionális)
        description: Leírás (opcionális)
        created_at: Létrehozás időpontja
        updated_at: Utolsó módosítás időpontja
        feedbacks: Kapcsolódó visszajelzések (relationship)
    """
    __tablename__ = "events"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Kötelező mezők
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    gm: Mapped[str] = mapped_column(String(200), nullable=False)

    # Opcionális mezők
    location: Mapped[str | None] = mapped_column(String(200), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # Relationship: One-to-Many
    # back_populates: kétirányú kapcsolat
    # cascade: ha töröljük az eventet, a feedbackek is törlődnek
    feedbacks: Mapped[List["Feedback"]] = relationship(
        "Feedback",
        back_populates="event",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        """String reprezentáció debugginghoz."""
        return f"<Event(id={self.id}, name='{self.name}', date={self.date})>"