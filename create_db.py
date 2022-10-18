from database import Base, engine
from models import Employees

print("Creating database...")

Base.metadata.create_all(engine)