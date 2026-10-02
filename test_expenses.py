
from expenses import (add_expenses
                      ,delete_expenses,
                      update_expenses
                      ,caliculate_category_wise_total
                      ,caliculate_monthly_total)
                      




def test_add_expense():
    expense_list = []
    add_expenses(expense_list=expense_list,name="Went to movie", amount=200,category="Others")
    assert [] != expense_list
    assert expense_list[0]['name'] == "Went to movie"
    assert expense_list[0]['amount'] == 200
    assert expense_list[0]['category'] == "Others"



def test_delete_expense():
    expense_list = [{"name":"Went to Movie","amount":200,"category":"Others"}]
    delete_expenses(expense_list,index=0)
    assert [] == expense_list 

    
def test_update_expense():
    expense_list = [{"name":"Went to Movie","amount":200,"category":"Others"}]
    update_expenses(expense_list,index=0,name="Went to Lunch",category="Food")
    assert expense_list[0]['name'] == "Went to Lunch"
    assert expense_list[0]['category'] == "Food"


def test_montly_wise_total():
    expense_list = [ {
        "name": "snacks",
        "amount": 30.0,
        "time": "13:22:01",
        "category": "FOOD",
        "date": "01/10/2026"
    },
    {
        "name": "Vegetables Shopping ",
        "amount": 100.0,
        "time": "15:13:07",
        "category": "SHOPPING",
        "date": "01/10/2026"
    },
    {
        "name": "Went to Lunch ",
        "amount": 500.0,
        "time": "16:33:13",
        "category": "TRAVEL",
        "date": "01/10/2026"
    }]

    monthly_map = caliculate_monthly_total(expense_list=expense_list)

    assert monthly_map['10'] == 630 


def test_montly_wise_total():
    expense_list = [ {
        "name": "snacks",
        "amount": 30.0,
        "time": "13:22:01",
        "category": "FOOD",
        "date": "01/10/2026"
    },
    {
        "name": "Vegetables Shopping ",
        "amount": 100.0,
        "time": "15:13:07",
        "category": "SHOPPING",
        "date": "01/10/2026"
    },
    {
        "name": "Went to Lunch ",
        "amount": 500.0,
        "time": "16:33:13",
        "category": "TRAVEL",
        "date": "01/10/2026"
    }]

    category_map = caliculate_category_wise_total(expense_list=expense_list)

    assert category_map['FOOD'] == 30 
    assert category_map['SHOPPING'] == 100 
    assert category_map['TRAVEL'] == 500




