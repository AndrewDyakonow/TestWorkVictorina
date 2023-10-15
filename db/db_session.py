from sqlalchemy.orm import sessionmaker

from db.db_engine import settings


session = sessionmaker(settings.create_engine)
