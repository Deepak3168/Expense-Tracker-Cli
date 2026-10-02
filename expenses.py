

def add_expenses(expense_list,**kwargs):
    expense_list.append(kwargs)
    return expense_list

def delete_expenses(expense_list,index):
    del expense_list[index]
    return expense_list


def update_expenses(expense_list,index,**kwargs):
    for i in kwargs :
        if kwargs[i] is not None:
            expense_list[index][i] = kwargs[i]
    return expense_list


def add_category(categories,category) :
    categories_set = set(categories)
    categories_set.add(category)
    categories = list(categories_set)
    return categories


def delete_category(categories,index):
    del categories[index]
    return categories


def caliculate_monthly_total(expense_list):
    month_map = {}
    for i in expense_list : 
        month = i['date'][3:5]
        if   month in month_map :
            month_map[month]+=i['amount']
        else:
            month_map[month] = i['amount']
    return month_map


        
def caliculate_category_wise_total(expense_list):
    category_map = {}
    for i in expense_list : 
        category = i['category']
        if   category in category_map :
            category_map[category]+=i['amount']
        else:
            category_map[category] = i['amount']
    return category_map







    


    
