from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "cinema"
DB_USER = "postgres"
DB_PASSWORD = "12345678"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
Session = sessionmaker(engine)