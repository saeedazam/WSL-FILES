import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

DB_PATH = "test.db"
engine = create_engine(os.getenv("DB_PATH", f"sqlite:///{DB_PATH}"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    rls = db.execute(text("SELECT rank, peaking_rank, rank_id FROM rl")).fetchall()
    for rl in rls:
        rank, peaking_rank, rank_id = rl
        print(f"rank is: {rank}, peaking rank is: {peaking_rank} and rank id is: {rank_id}")

if __name__ == "__main__":
    main()
