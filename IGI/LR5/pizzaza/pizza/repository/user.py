from pizza.models import Customer, Order, Review, Coupon

def create(data):
    return Customer.objects.create(**data)

def getCoupon(name):
    return Coupon.objects.filter(number=int(name))

def getByEmail(Email):
    try:
        return Customer.objects.get(email=Email)
    except:
        return None
    

def getById(Id):
    try:
        return Customer.objects.get(id=Id)
    except:
        return None
    

def getAges():
    return Customer.objects.values_list("birthdate", flat=True)


def update_cart(user):
    Customer.objects.filter(id=user.id).update(cart=user.cart)

def get_orders(user):
    return Order.objects.filter(customer=user)

def clear():
    Customer.objects.all().delete()

def new_review(data):
    return Review.objects.create(**data)

def delete_review(id):
    Review.objects.filter(id=id).delete()