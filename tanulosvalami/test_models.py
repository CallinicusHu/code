"""
Quick test to verify models work
"""
from tanulosvalami.database import engine, Base
from tanulosvalami.models import Event, Feedback

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
print(f"Tables: {Base.metadata.tables.keys()}")