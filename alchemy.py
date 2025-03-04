from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship

engine = create_engine("sqlite:///database.db")  # Veritabanı dosyası oluştur
Base = declarative_base()


#kullanici modeli
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)

    articles=relationship("Article",back_populates="user")

#makale_modeli
class Article(Base):
    __tablename__="articles"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    content=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))

    user=relationship("User",back_populates="articles")


Base.metadata.create_all(engine)


