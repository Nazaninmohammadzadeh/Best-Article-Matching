from alchemy import User,engine,Article
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def login_user(name):
    user=session.query(User).filter_by(name=name).first()

    if user:
        print(f"Hello {user.name}!")
        return user
    else:
        print(f"Couldn't find user {name}") 
        return None   
    


def list_article(user_name):
    user=session.query(User).filter_by(name=user_name).first()

    if not user:
        print("Couldn't find user!")
        return None
    else:
        articles=user.articles
        print(f"Wroten articles by {user.name} : ")
        for article in articles:
            print(f"- {article.title}")

user_name="Roger C. Schank "
user=login_user(user_name)
if user:
    list_article(user_name)            
