import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_ENGINE = {
        "SQLITE": 'sqlite:///project1.db'
    }

engine = create_engine(DB_ENGINE["SQLITE"])
db =scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE users (id  INTEGER PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (isbn VARCHAR NOT NULL,review VARCHAR NOT NULL, rating INTEGER NOT NULL,username VARCHAR NOT NULL)")
    db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")
    f=open("books.csv")
    reader =csv.reader(f)
    for isbn,title,author,year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)",{"a":isbn,"b":title,"c":author,"d":year})
        
    print("done")            
    db.commit()    


if __name__ == "__main__":
    main()