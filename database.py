from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:uzma@localhost/HR", echo=True)

Base = declarative_base()

sessionLocal = sessionmaker(bind = engine)
