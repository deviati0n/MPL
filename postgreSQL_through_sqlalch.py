from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmarker

db_string = 'postgres://a:a@localhost/'

db = create_engine(db_string)
base = declarative_base()


class Player(base):
    __tablename_- = 'players'

    player_id = Column(String(15), primary_key=True)
    nickname = Column(String(30))
    position = Column(String) # or SmallInteger 

Session = sessionmarker(db)
session = Session()

base.metadata.create_all(db)

# create

player = Player(player_id='141690233', nickname='cancel^^', position='hard')
session.add(player)
session.commit()

# https://pythonru.com/biblioteki/crud-sqlalchemy-core
# https://pythonru.com/biblioteki/crud-sqlalchemy-orm