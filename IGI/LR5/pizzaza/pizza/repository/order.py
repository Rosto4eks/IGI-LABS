from pizza.models import Order, Employee
from django.db.models import Count, Q

def get_order_employee():
    try:
        return Employee.objects.annotate(count=Count("order", filter=Q(order__status="created"))).order_by('count').first()
    except:
        return Employee.objects.first()
    
def complete_order(orderId):
    Order.objects.filter(id=orderId).update(status="completed")
 
def create(data):
    return Order.objects.create(**data)

def get_orders(user):
    try:
        return Order.objects.filter(employee=user, status="created")
    except:
        return []
    
def get_completed(user):
    try:
        return Order.objects.filter(employee=user, status="completed")
    except:
        return []
    

def get_totals():
    return Order.objects.values_list("total", flat=True)


def get_pizzas():
    return Order.objects.values_list("pizza", flat=True)


def get_date_totals():
    return Order.objects.values_list("date", "total")

def get_users():
    return Order.objects.values_list("customer", "total")