from fastapi import FastAPI

from best_matching_article import get_best_match  

app = FastAPI()

@app.get("/match/")
def match_article(query: str):
    best_article = get_best_match(query)
    return {"best_match": best_article}



