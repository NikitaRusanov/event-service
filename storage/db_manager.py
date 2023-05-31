from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config


engine = create_engine(config.DB_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


