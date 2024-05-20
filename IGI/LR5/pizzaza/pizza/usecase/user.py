from pizza.repository import user as user_db, pizza as pizza_db, order as order_db, employee as employee_db
import datetime
import statistics
import numpy as np
from matplotlib import pyplot as plt
import ast
import datetime

def sign_up(data):
    birth_date = datetime.datetime.strptime(data["birthdate"], "%Y-%m-%d")
    today = datetime.datetime.now()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    if  age < 18 :
        return None, "вам должно быть более 18 лет"
    if len(data["name"]) < 5:
        return None, "имя должно быть больше 5 символов"
    if len(data["phone_number"]) != 13:
        return None, "неверно введен номер телефона"
    if not data["phone_number"].startswith("+37529"):
        return None, "номер должен начинаться с +37529"
    if len(data["email"]) < 7:
        return None, "почта должна быть больше 7 символов"
    if len(data["password"]) < 8:
        return None, "пароль должен быть больше 8 символов"
    user = user_db.getByEmail(data["email"])
    if user == None:
        user = user_db.create(data)  
        return user, None
    return None, "user exist"
    

def sign_in(data):
    if len(data["email"]) < 7:
        return None, "почта должна быть больше 7 символов"
    if len(data["password"]) < 8:
        return None, "пароль должен быть больше 8 символов"
    user =user_db .getByEmail(data["email"])
    if user == None:
        return None, "пользователь не найден"
    if user.password != data["password"]:
        return None, "неверный пароль"
    return user, None


def add_to_cart(userId, pizzaId):
    user = user_db.getById(userId)
    arr: dict[int, int] = ast.literal_eval(user.cart)
    try:
        arr[pizzaId] += 1
    except:
        arr[pizzaId] = 1
    user.cart = arr.__str__()
    user_db.update_cart(user)


def get_cart(userId):
    user = user_db.getById(userId)
    pizzas = {}
    cart: dict[int, int] = ast.literal_eval(user.cart)
    total = 0
    for id, count in cart.items():
        pizza = pizza_db.get(id)
        pizzas[pizza] = count
        total += pizza.price * count

    return pizzas, total

def remove_from_cart(userId, pizzaId):
    user = user_db.getById(userId)
    arr: dict[int, int] = ast.literal_eval(user.cart)
    try:
        arr[pizzaId] -= 1
        if arr[pizzaId] <= 0:
            del arr[pizzaId]
    except:
        pass
    user.cart = arr.__str__()
    user_db.update_cart(user)

def get_orders(userId):
    user = user_db.getById(userId)
    return user_db.get_orders(user)

def buy(userId, address, coupon):
    user = user_db.getById(userId)
    try:
        c = user_db.getCoupon(coupon)
    except:
        c = []
    cart = user.cart
    user.cart = "{}"
    user_db.update_cart(user)
    employee = order_db.get_order_employee()
    
    arr: dict[int, int] = ast.literal_eval(cart)
    total = 0
    for id, count in arr.items():
        pizza = pizza_db.get(id)
        total += pizza.price * count
    if len(c) > 0:
        total = total - total * c[0].discount / 100
    data = {
        "date": datetime.datetime.now(),
        "customer": user,
        "employee": employee,
        "pizza": cart,
        "total": total,
        "address": address,
    }
    order_db.create(data)


def clear():
    user_db.clear()


def statistic_age():
    arr = user_db.getAges()
    ages = []
    for i in range(len(arr)):
        ages.append(datetime.date.today().year - arr[i].year)
    print(ages)
    return statistics.mean(ages), statistics.mode(ages)


def statistic_total():
    totals = np.array(order_db.get_totals())
    return statistics.mean(totals), statistics.mode(totals), statistics.median(totals)


def statistic_popular():
    all = {}
    pizzas = np.array(order_db.get_pizzas())
    for pizza in pizzas:
        arr: dict[int, int] = ast.literal_eval(pizza)
        for k,v in arr.items():
            try:
                all[k] += v
            except:
                all[k] = v
    all = dict(sorted(all.items(), key=lambda item: item[1], reverse=True))
    return pizza_db.get(list(all.keys())[0])
  

def get_totals():
    arrx = []
    arry = []
    for order in order_db.get_date_totals():
        arrx.append(order[0].strftime('%m/%d/%Y'))
        arry.append(order[1])

    plt.plot(arrx, arry, 'o')
    plt.ylabel("стоимость")
    plt.savefig("pizza/static/images/totals.png")
    plt.close()


def get_users():
    users = {}
    for order in order_db.get_users():
        user = user_db.getById(order[0])
        try:
            users[user.email] += order[1]
        except:
            users[user.email] = order[1]
    x = []
    y = []
    for k,v in users.items():
        x.append(k)
        y.append(v)
    print(x)
    print(y)
    _, ax = plt.subplots()
    ax.bar(x, y)
    plt.savefig("pizza/static/images/users.png")
    plt.close()

def new_review(userid, data):
    if int(data["rate"]) < 0 or int(data["rate"]) > 5:
        return "неверный рейтинг"
    user = user_db.getById(userid)
    data["customer"] = user
    user_db.new_review(data)

def delete_review(id):
    user_db.delete_review(id)