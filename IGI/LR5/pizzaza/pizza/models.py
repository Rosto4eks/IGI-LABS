from django.db import models
import django.utils.timezone as timezone

class VacancyInfo(models.Model):
    info = models.TextField()

class Vacancy(models.Model):    
    name = models.TextField()
    salary = models.FloatField()
    info = models.OneToOneField(VacancyInfo, primary_key=True, on_delete=models.CASCADE)


class Pizza(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=1000)
    price = models.FloatField()
    weight = models.FloatField()
    size = models.PositiveIntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    cart = models.TextField(default="{}")
    birthdate = models.DateField(default=timezone.now)


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField(blank=True)
    vacancy = models.ManyToManyField(Vacancy, blank=True)


class Order(models.Model):
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pizza = models.JSONField()
    address = models.CharField(max_length=50)
    status = models.TextField(max_length=50, default="created")
    total = models.FloatField(default=0)


class CompanyInfo(models.Model):
    text = models.TextField()


class News(models.Model):
    title = models.TextField()
    theme = models.TextField()
    text = models.TextField()
    image = models.ImageField(blank=True)
    date = models.DateTimeField(default=timezone.now)


class FAQ(models.Model):
    text = models.TextField()
    answer = models.TextField()
    date = models.DateTimeField(default=timezone.now)


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rate = models.IntegerField()
    text = models.TextField()
    date = models.DateField(default=timezone.now)


class Coupon(models.Model):
    number = models.IntegerField()
    deadline = models.DateTimeField(default=timezone.now)
    discount = models.IntegerField()
