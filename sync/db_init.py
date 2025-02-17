from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

database_url=os.getenv("DATABASE_URL")



engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()
