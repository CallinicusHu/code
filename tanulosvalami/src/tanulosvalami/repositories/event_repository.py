"""
Event Repository
Handles all database operations for Events
"""
from typing import Type

from sqlalchemy.orm import Session

from tanulosvalami.models.event import Event
from tanulosvalami.schemas.event import EventCreate, EventUpdate


class EventRepository:

    def __init__(self, db: Session):
        """
        db: SQLAlchemy Session - injected from FastAPI
        """
        self.db = db

    def get_all(self) -> list[Type[Event]]:
        """
        Fetch all events from the database
        """
        return self.db.query(Event).all()

    def get_by_id(self, event_id: int) -> Event | None:
        """
        Fetch a single event by its ID
        Returns None if not found
        """
        return self.db.query(Event).filter(Event.id == event_id).first()

    def create(self, event_data: EventCreate) -> Event:
        """
        Create a new event in the database
        1. Convert schema to model
        2. Add to database
        3. Commit transaction
        4. Return created event
        """
        db_event = Event(**event_data.model_dump())
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return db_event

    def update(self, event_id: int, event_data: EventUpdate) -> Event:
        """
        Updates an event in the database.
        """
        # 1. Fetch the existing event
        db_event = self.get(event_id)  # Or however you fetch by ID in this file

        if db_event:
            # 2. Extract only the fields the user actually sent in the PATCH request
            update_data = event_data.model_dump(exclude_unset=True)

            # 3. Apply those new values to the database object
            for key, value in update_data.items():
                setattr(db_event, key, value)

            # 4. Save and commit the changes
            self.db.add(db_event)
            self.db.commit()
            self.db.refresh(db_event)

        return db_event

    def delete(self, event_id: int) -> bool:
        """
        Delete an event by ID
        Returns True if deleted, False if not found
        """
        db_event = self.get_by_id(event_id)

        if not db_event:
            return False

        self.db.delete(db_event)
        self.db.commit()
        return True
