from sqlalchemy import create_engine
import psycopg2
import pandas

from config import db_password


# Create connection to SQL database
engine = create_engine(f"postgresql://postgres:{db_password}@34.94.45.232:5432/Adly")

