from file import read_expenses,write_expenses
from datetime import datetime,date
from expenses import add_expenses,delete_expenses,update_expenses,add_category,delete_category,caliculate_monthly_total,caliculate_category_wise_total

expenses  = read_expenses()
categories = ['FOOD','TRAVEL','SHOPPING','GROCERIES','OTHERS']


class InvalidOperation(Exception):
    pass 


def set_operation(n):
    if n<1 :
        raise InvalidOperation("Enter an operation greater than 1")
    elif n>9 :
        raise   InvalidOperation("Enter an Operator Lessthan 8 ")
    else:
        return n 


def print_categories(categories):
    i = 1
    for category in categories:
        print(f"{i} - {category}")
        i+=1
    


def print_expenses(expenses):
    j = 1
    for i in  expenses :
        print(j,i['name'])
        j+=1

def print_expenses_detail(expenses):
    j=1
    for i in expenses : 
        print(f"ID : {j} ,NAME : {i['name']}, AMOUNT:{i['amount']}, CATEGORY : {i['category']},DATE: {i['date']}, TIME : {i['time']} ")
        j+=1


def print_map(expense_map):
    for k,v in expense_map.items():
        print(k,v)




run = True 


def exit():
    global run
    print(expenses)
    write_expenses(expenses=expenses)
    run = False



while run:
    print("""
            1) ADD EXPENSE 
            2) DELETE EXPENSE 
            3) UPDATE EXPENSE 
            4) ADD CATEGORY 
            5) DELETE CATEGORY 
            6) SHOW MONTHLY TOTAL 
            7) SHOW CATEGORYWISE TOTAL 
            8) SHOW EXPENSES
            9) DELETE EXPENSES  
            """)
    user_prompt = int(input("Enter your Operation ")) 

    try : 
        user_prompt  = set_operation(user_prompt)
    except InvalidOperation as e :
        print(e)
        print("Invalid Operator Entered ")
    else:
        if user_prompt == 1 : 
            #add expense 
            name = input("Enter your expense name: ")
            amount = float(input("Enter your Amount: "))
            print_categories(categories)
            category_no = int(input("Enter your Cateogory: "))
            now  =  datetime.now()
            date_ = date.today().strftime("%d/%m/%Y")
            time = now.strftime("%H:%M:%S")
            category = categories[category_no-1]

            add_expenses(expenses,name=name,amount=amount,time=time,category=category,date=date_)


            print(expenses)



        elif user_prompt == 2 : 
            #delete expense
            print_expenses(expenses=expenses)
            n = int(input("Enter the Expense id to delete"))
            try :
                delete_expenses(expense_list=expenses,index=n-1)
            except Exception as e : 
                print(e)



        elif user_prompt == 3:
            # update expense
            print_expenses(expenses)

            n = int(input("Enter ID of the expense you want to edit: "))

            name = None
            amount = None
            category = None

            name_edit = input("Enter Y to update name or N/anything to pass: ")

            if name_edit == "Y":
                name = input("Enter your expense name: ")

            amount_edit = input("Enter Y to update amount or N/anything to pass: ")

            if amount_edit == "Y":
                amount = float(input("Enter your amount: "))

            category_edit = input("Enter Y to update category or N/anything to pass: ")

            if category_edit == "Y":
                print_categories(categories)
                category_no = int(input("Enter your category: "))
                category = categories[category_no - 1]

            try:
                update_expenses(
                    expense_list=expenses,
                    index=n - 1,
                    name=name,
                    amount=amount,
                    category=category
                )

            except IndexError:
                print("Invalid expense ID.")


        elif user_prompt == 4 : 
            #add category
            print_categories(categories)
            category = input("Enter your Category name: ")
            categories = add_category(categories=categories,category=category)
            print_categories(categories)


        elif user_prompt == 5 : 
            # delete categories
            print_categories(categories)
            n = int(input("Enter your Category ID to Delete: "))
            delete_category(categories=categories,index=n-1)
            print_categories(categories)

        elif user_prompt == 6 : 
            #show monthly total 
            print_expenses_detail(expenses)
            expense_map = caliculate_monthly_total(expenses)
            print("### MONTHLY   EXPENSES")
            print_map(expense_map=expense_map)

        elif user_prompt == 7 : 
            print_expenses_detail(expenses)
            expense_map = caliculate_category_wise_total(expenses)
            print("### CATEGORY WISE EXPENSES")
            print_map(expense_map=expense_map)

        elif user_prompt == 8 :
            print_expenses_detail(expenses)

        elif user_prompt == 9:
            exit()

