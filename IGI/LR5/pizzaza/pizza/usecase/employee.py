from pizza.repository import employee as employee_db, order as order_db, user as user_db


def sign_in(data):
    user =employee_db .getByEmail(data["email"])
    if user == None:
        return None, "user not found"
    if user.password != data["password"]:
        return None, "incorrect password"
    return user, None

def get_orders(userId):
    user = employee_db.getById(userId)
    return order_db.get_orders(user)


def get_completed(userId):
    user = employee_db.getById(userId)
    return order_db.get_completed(user)



def complete_order(orderId):
    order_db.complete_order(orderId)