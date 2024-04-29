from config.database import engine
from models.city import City
from models.region import Region


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    City.metadata.create_all(bind=engine)
    Region.metadata.create_all(bind=engine)
