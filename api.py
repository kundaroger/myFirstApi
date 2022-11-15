from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title="MY FASTAPI")



@storage.get('/')#Route
def index():
    return "My name is Roger, This my API"

@storage.get('/today')#route with GET METHOD
def today():
    return str(datetime.now())


@storage.get('/mynames')
def names(first_name: bool = False, last_name: bool = False, full_name: bool = False):
    full_names = ""
    if first_name:
        full_names += 'Roger'
    if last_name:
        full_names += ' Byakunda'
    if full_name:
        full_names = "Roger Byakunda"
    
    return full_names

if __name__=="__main__":
    storage.run()