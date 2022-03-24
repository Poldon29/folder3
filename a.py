import datetime
from hashlib import new
e = datetime.datetime.now()
costs_ = []
class cost_obj:
    def __init__(self, date_: str, name_: str, cost_: float) -> None:
        self.date = date_
        self.name = name_
        self.cost = cost_

def add_new():
    return(1)

def delete_last():
    return(2)

def options(text: str):
    switch = {
        "add_new":add_new(),
        "delete_last":delete_last()
        }
    if switch.get(text):
        return  switch.get(text) 
    else: 
        return "INVALID VALUE"
#print(e.day, e.month, e.year, sep = "/")



while True:
    answer = input("wpisz se cos\n")
    print(options(answer))