from django.shortcuts import render, redirect
from pizza.usecase import pizza as pizza_case, user as user_case, employee as employee_case
import requests
import calendar
import django.utils.timezone as timezone
import datetime
import pytz as tz
from pizza.models import *

def Auth(role):
    def decorator(func):
        def fn(*args, **kwargs):
            request = args[0]
            _, userrole = get_user_data(request)
            if userrole != role:
                return redirect("/sign-in")
            return func(*args, **kwargs)
        return fn
    return decorator

def get_user_data(request):
    id = ""
    role = ""
    try:
        id = request.session["id"] 
        role = request.session["role"] 
    except:
        id = ""
        role = ""
    return id, role

def index(request):
    _, role = get_user_data(request)
    pizzas = pizza_case.getAll()
    if request.GET.get("price-sort") != None:
        pizzas.sort(key=lambda p: p.price)
    return render(request, "index.html", context={"pizzas": pizzas, "role": role})


def search(request):
    _, role = get_user_data(request)
    name = request.POST.get("name")
    return render(request, "index.html", context={"pizzas": pizza_case.search(name), "role": role})


def sign_in(request):
    fact = requests.get("https://catfact.ninja/fact").json()
    if request.POST:
        data = {"email": request.POST.get("email", ""), "password": request.POST.get("password", "")}
        user, err = user_case.sign_in(data)
        if err != None:
            return render(request, "sign-in.html", context={"fact": fact, "error": err})
        request.session["role"] = "user"
        if user.name == "Rosto4eks":
            request.session["role"] = "admin"
        request.session["id"] = user.id
        return redirect("/")
    
    return render(request, "sign-in.html", context={"fact": fact, "error" : ""})


def sign_in_employee(request):
    if request.POST:
        data = {"email": request.POST.get("email", ""), "password": request.POST.get("password", "")}
        user, err = employee_case.sign_in(data)
        if err != None:
            return render(request, "sign-in-employee.html")
        request.session["role"] = "employee"
        request.session["id"] = user.id
        return redirect("/orders")
    
    return render(request, "sign-in-employee.html")


@Auth("employee")
def completed(request):
    userId, _ = get_user_data(request)
    orders = employee_case.get_completed(userId)
    return render(request, "get-orders.html", context={"orders": orders})

@Auth("employee")
def orders(request):
    userId, _ = get_user_data(request)
    orders = employee_case.get_orders(userId)
    return render(request, "get-orders.html", context={"orders": orders})

@Auth("employee")
def complete_order(request):
    orderId = request.GET.get("id")
    employee_case.complete_order(orderId)
    return redirect("/orders")


@Auth('user')
def profile(request):
    userId, _ = get_user_data(request)
    orders = user_case.get_orders(userId)
    info = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    tz_info = info.tzinfo

    response = requests.get("https://api.ipify.org/?format=json")

        # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        ip_address = data["ip"]
        response = requests.get(f"https://ipinfo.io/{ip_address}/geo")
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            tz = data["timezone"]

    date = datetime.datetime.now(tz_info).strftime("%d/%m/%y")
    time =datetime.datetime.now(tz_info).strftime("%H:%M:%S")

    return render(request, "profile.html", context={"orders": orders, "calendar": calendar.calendar(2024), "date": date, "time": time, "timezone": tz_info, "tz": tz})

def sign_up(request):
    fact = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    if request.POST:
        data = {"email": request.POST.get("email", ""), "password": request.POST.get("password", ""), "name": request.POST.get("name", ""), "phone_number": request.POST.get("phone_number", ""),"birthdate": request.POST.get("age", "")}
        user, err = user_case.sign_up(data)
        if err != None:
            return render(request, "sign-up.html", context={"fact": fact, "error": err})
        request.session["role"] = "user"
        request.session["id"] = user.id
        return redirect("/")
    return render(request, "sign-up.html", context={"fact": fact, "error": ""})


@Auth("admin")
def add_pizza(request):
    if request.POST:
        data = {"name": request.POST.get("name", ""), "ingredients": request.POST.get("ingredients", ""), "price": request.POST.get("price", ""), "weight": request.POST.get("weight", ""), "size": request.POST.get("size", "")}
        err = pizza_case.add(data)
        if err != None:
            return render(request, "add-pizza.html")
        return redirect("/")

    return render(request, "add-pizza.html")


@Auth("admin")
def edit_pizza(request):
    if request.POST:
        data = {"id": request.POST.get("id"),"name": request.POST.get("name", ""), "ingredients": request.POST.get("ingredients", ""), "price": request.POST.get("price", ""), "weight": request.POST.get("weight", ""), "size": request.POST.get("size", "")}
        err = pizza_case.edit(data)
        if err != None:
            return render(request, "add-pizza.html")
        return redirect("/")
    
    data = request.GET.get("id")
    return render(request, "edit-pizza.html", context={"pizza": pizza_case.get(data)})


@Auth("admin")
def delete_pizza(request):
    name = request.GET.get("id")
    err = pizza_case.delete(name)
    return redirect("/")


@Auth("user")
def add_to_cart(request):
    userId, _ = get_user_data(request)
    pizzaId = request.GET.get("id")
    user_case.add_to_cart(userId, pizzaId)
    return redirect("/")


@Auth("user")
def get_cart(request):
    userId, _ = get_user_data(request)
    cart, total = user_case.get_cart(userId)
    return render(request, "get-cart.html", context={"cart": cart, "total": total})


@Auth("user")
def remove_from_cart(request):
    userId, _ = get_user_data(request)
    pizza_id = request.GET.get("id")
    user_case.remove_from_cart(userId, pizza_id)
    return redirect("/cart")

@Auth("user")
def buy(request):
    userId, _ = get_user_data(request)
    address = request.POST.get("address")
    coupon = request.POST.get("coupon")
    user_case.buy(userId, address, coupon)
    return redirect("/")


@Auth("admin")
def statistics(request):
    age_mean, age_mode = user_case.statistic_age()
    total_mean, total_mode, total_median = user_case.statistic_total()
    user_case.get_totals()
    user_case.get_users()

    return render(request, "statistics.html", context={"age_mean": age_mean, "age_mode": age_mode, "total_mean": total_mean, "total_mode": total_mode, "total_median": total_median})

def about(request):
    return render(request, "about.html", context={"data": CompanyInfo.objects.all(), "news": News.objects.last()})

def news(request):
    newsid = request.GET.get("id")
    if newsid != None:
        return render(request, "news-data.html", context={"data": News.objects.filter(id=newsid)})
    return render(request, "news.html", context={"data": News.objects.all().order_by("-date")})

def faq(request):
    return render(request, "faq.html", context={"data": FAQ.objects.all()})

def contacts(request):
    e = Employee.objects.all()
    for i in range(len(e)):
        e[i].vacancies = e[i].vacancy.all()
    return render(request, "contacts.html", context={"data": e})

def policy(request):
    return render(request, "policy.html")

def vacancies(request):
    return render(request, "vacancies.html", context={"data": Vacancy.objects.all()})

def reviews(request):
    id, _ = get_user_data(request)
    all = Review.objects.all()
    return render(request, "reviews.html", context={"data": all, "id": id})

@Auth("user")
def new_review(request):
    if request.POST:
        id, _ = get_user_data(request)

        data = {"rate": request.POST.get("rate", ""),"text": request.POST.get("text", "")}
        err = user_case.new_review(id, data)
        if err != None:
            return render(request, "new-review.html", context={"error": err})
        return redirect("/reviews")
    
    return render(request, "new-review.html")

@Auth("user")
def delete_review(request):
    id, _ = get_user_data(request)
    reviewId = request.GET.get("id")
    user_case.delete_review(reviewId)
    
    return redirect("/reviews")


def promo(request):
    return render(request, "promo.html", context={"data": Coupon.objects.all()})

        