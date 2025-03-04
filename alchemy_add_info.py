from alchemy import User,engine,Article
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def add_user(name):
    user=User(name=name)
    session.add(user)
    session.commit
    print(f"User added : {user.name}")


def add_article(user_name,title,content):
    user=session.query(User).filter_by(name=user_name).first()
    if not user:
        print("User did not find!")
        return
    
    article=Article(title=title,content=content,user=user)
    session.add(article)
    session.commit()
    print(f"Article added: {title} - {user_name}")


# add_user("Nazanin Mohammadzadeh")
# add_user("Elon Musk")
#add_user("Roger C. Schank ")

# add_article("Nazanin Mohammadzadeh","Artifical intelligence","AI is developing rapidly...")
# add_article("Elon Musk","Deep learning","Deep learning is powered by big data... ")
#add_article("Roger C. Schank ","What Is AI, Anyway? ","A great many AI researchers believe strongly that knowledge representations used in AI programs must conform to previously established formalisms and logics, or the field is unprincipled and ad hoc. Many AI researchers believe that they know how the answer will turn out even before they have figured out what exactly the questions are. They know that some mathematical formalism or other must be the best way to express the contents of the knowledge which people have. Thus, to these researchers, AI is an exercise in the search for the proper formalisms to use in representing knowledge. Is AI software engineering? A great many AI practitioners seem to think so. If you can put knowledge into a program, then this program must be an AI program. This conception of AI, derived as it is from much of the work going on in industry in expert systems, has served to confuse AI people tremendously about what the correct focus of AI ought to be and what the fundamental issues in AI are. If AI is just so much software engineering, if building an AI program primarily means the addition of domain knowledge such that a program knows about insurance or geology, for example,then what differentiates an AI program in insurance from any other computer program which works with in the field of insurance? Under this conception, it is difficult to deter- mine where software engineering leaves off and where AI begins.")
add_article("Roger C. Schank ","Where's the AI? ","When someone who is not in AI asks where the AI is, what assumptions about AI are inherent in the question? There seem to be at least four prevailing viewpoints that I have to deal with, so this question assumes at least one of the following four things: (1) AI means magic bullets, (2) AI means inference engines, (3) AI means getting a machine to do something you didn’t think a machine could do (the “gee whiz” view), and (4) AI means having a machine learn. The magic bullet view of AI is as follows: Intelligence is actually difficult to put into a machine because it is knowledge dependent. Because the knowledge-acquisition process is complex, one way to address it is to finesse it. Let the machine be efficient computationally so that it can connect things to each other without having to explicitly represent anything. In this way, the intelligence comes for free as a by-product of unanticipated connections that the machine makes. An alternate version of this view is that AI is something that one could, in principle, discover in one’s garage. What the form of this discovery might be remains a mystery, but one would drop the discovered item or technique into the machine, and it would become intelligent. This view is held, quite firmly, by many people who write me letters after having read my name in a magazine article as well as by many venture capitalists (and, possibly, some connectionists).")
