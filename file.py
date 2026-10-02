import json 


def read_expenses():
        with open('expenses.json','r') as f  : 
                expenses = json.load(f)

        return expenses


def write_expenses(expenses):
        with open('expenses.json','w') as f :
                json.dump(expenses,f,indent=4) 
        return 



    
