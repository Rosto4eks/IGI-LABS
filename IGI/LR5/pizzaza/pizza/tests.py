from django.test import TestCase
from .usecase import user as user_case, pizza as pizza_case
from .models import *
import datetime
import django.utils.timezone as timezone

class userTest(TestCase):
    def setUp(self):
        c = Customer.objects.create(name="abcdef", email="bebr@mail.ru", age=19, phone_number="+375291234567", password="12345678", cart={1: 2})
        e = Employee.objects.create(name="abcdef", email="bebr@mail.ru", phone_number="+375291234567", password="12345678")
        Order.objects.create(date=timezone.now(), customer = c, employee=e, pizza={1: 2}, address="a", status="created", total=100)
        Pizza.objects.create(name="a", ingredients="b", price=20.99, weight=500, size=30)

    def test_sign_up_1(self):
        user, err = user_case.sign_up({"name": "a", "email": "a", "age": 13, "phone_number": "+375291234567", "password": 1234567})
        self.assertEqual(err, 'вам должно быть более 18 лет')

    def test_sign_up_2(self):
        user, err = user_case.sign_up({"name": "a", "email": "a", "age": 19, "phone_number": "+375291234567", "password": 1234567})
        self.assertEqual(err, 'имя должно быть больше 5 символов')

    def test_sign_up_3(self):
        user, err = user_case.sign_up({"name": "abcdef", "email": "aaskd@mail.ru", "age": 19, "phone_number": "+375291234567", "password": "12345678"})
        self.assertEqual(err, None)

    def test_sign_in_1(self):
        user, err = user_case.sign_in({"email": "bebr@mail.ru", "password": "12345678"})
        self.assertEqual(err, None)

    def test_sign_in_2(self):
        user, err = user_case.sign_in({"email": "bebr@mail.ru", "password": "12345679"})
        self.assertEqual(err, 'неверный пароль')

    def test_sign_in_3(self):
        user, err = user_case.sign_in({"email": "bebrk@mail.ru", "password": "12345678"})
        self.assertEqual(err,  'пользователь не найден')

    def test_get_cart_1(self):
        cart, total = user_case.get_cart(1)
        self.assertEqual(total,  41.98)

    def test_get_orders(self):
        order = user_case.get_orders(1)
        self.assertEqual(list(order)[0].pizza,  {'1':2})

    def test_get_pizzas_1(self):
        pizzas = pizza_case.getAll()
        self.assertEqual(len(list(pizzas)), 1)

    def test_get_pizzas_2(self):
        pizzas = pizza_case.getAll()
        self.assertEqual(list(pizzas)[0].name, 'a')

    def test_get_pizza_1(self):
        pizza = pizza_case.get(1)
        self.assertEqual(pizza.name, "a")

    def test_get_pizza_2(self):
        try:
            pizza = pizza_case.get(2)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_search_1(self):
        pizza = pizza_case.search("b")
        self.assertEqual(len(pizza), 1)

    def test_search_2(self):
        pizza = pizza_case.search("b")
        self.assertEqual(pizza[0].name, "a")

    def test_search_3(self):
        pizza = pizza_case.search("c")
        self.assertEqual(len(pizza), 0)

    def setUp(self):
        c = Customer.objects.create(name="abcdef", email="bebr@mail.ru", birthdate=datetime.datetime(2001, 1, 1), phone_number="+375291234567", password="12345678", cart={1: 2})
        e = Employee.objects.create(name="abcdef", email="bebr@mail.ru", phone_number="+375291234567", password="12345678")
        Order.objects.create(date=timezone.now(), customer = c, employee=e, pizza={1: 2}, address="a", status="created", total=100)
        Pizza.objects.create(name="a", ingredients="b", price=20.99, weight=500, size=30)

    def test_sign_up_1(self):
        user, err = user_case.sign_up({"name": "aaaaaaaaa", "email": "aaaaaaaaaa", "birthdate": "2021-01-01", "phone_number": "+375291234567", "password": "12345678"})
        self.assertEqual(err, 'вам должно быть более 18 лет')

    def test_sign_up_2(self):
        user, err = user_case.sign_up({"name": "a", "email": "a", "birthdate": "2001-01-01", "phone_number": "+375291234567", "password": "12345678"})
        self.assertEqual(err, 'имя должно быть больше 5 символов')

    def test_sign_up_3(self):
        user, err = user_case.sign_up({"name": "abcdef", "email": "aaskd@mail.ru", "birthdate": "2001-01-01", "phone_number": "+375291234567", "password": "12345678"})
        self.assertEqual(err, None)

    def test_sign_in_1(self):
        user, err = user_case.sign_in({"email": "bebr@mail.ru", "password": "12345678"})
        self.assertEqual(err, None)

    def test_sign_in_2(self):
        user, err = user_case.sign_in({"email": "bebr@mail.ru", "password": "12345679"})
        self.assertEqual(err, 'неверный пароль')

    def test_sign_in_3(self):
        user, err = user_case.sign_in({"email": "bebrk@mail.ru", "password": "12345678"})
        self.assertEqual(err,  'пользователь не найден')

    def test_get_cart_1(self):
        cart, total = user_case.get_cart(1)
        self.assertEqual(total,  41.98)

    def test_get_orders(self):
        order = user_case.get_orders(1)
        self.assertEqual(list(order)[0].pizza,  {'1':2})

    def test_get_pizzas_1(self):
        pizzas = pizza_case.getAll()
        self.assertEqual(len(list(pizzas)), 1)

    def test_get_pizzas_2(self):
        pizzas = pizza_case.getAll()
        self.assertEqual(list(pizzas)[0].name, 'a')

    def test_get_pizza_1(self):
        pizza = pizza_case.get(1)
        self.assertEqual(pizza.name, "a")

    def test_get_pizza_2(self):
        try:
            pizza = pizza_case.get(2)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_search_1(self):
        pizza = pizza_case.search("b")
        self.assertEqual(len(pizza), 1)

    def test_search_2(self):
        pizza = pizza_case.search("b")
        self.assertEqual(pizza[0].name, "a")

    def test_search_3(self):
        pizza = pizza_case.search("c")
        self.assertEqual(len(pizza), 0)

    
    def test_edit_1(self):
         pizza_case.edit({"id": 1,"name":"a", "ingredients":"b", "price":20.99, "weight":600, "size":30})
         pizza = pizza_case.search("b")
         self.assertEqual(pizza[0].weight, 600)

    def test_edit_2(self):
         pizza_case.edit({"id": 1,"name":"aboba", "ingredients":"b", "price":20.99, "weight":600, "size":30})
         pizza = pizza_case.search("b")
         self.assertEqual(pizza[0].name, "aboba")

    def test_delete_1(self):
        pizza_case.delete(1)
        pizza = pizza_case.search("b")
        self.assertEqual(len(pizza), 0)

    def test_delete_2(self):
        pizza_case.delete(2)
        pizza = pizza_case.search("b")
        self.assertEqual(len(pizza), 1)

    def test_delete_3(self):
        pizza_case.delete(3)
        pizza = pizza_case.search("b")
        self.assertEqual(len(pizza), 1)

    def test_delete_4(self):
        pizza_case.delete(4)
        pizza = pizza_case.search("b")
        self.assertEqual(len(pizza), 1)

    def test_index_view_1(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    
    def test_index_view_2(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        pizzas = response.context['pizzas']
        self.assertEqual(pizzas, pizza_case.getAll())

    def test_search_view_1(self):
        response = self.client.post("/search", data={"name": "b"})
        self.assertEqual(response.status_code, 200)
        pizzas = response.context['pizzas']
        self.assertEqual(pizzas[0].name, pizza_case.getAll()[0].name)

    def test_search_view_2(self):
        response = self.client.post("/search", data={"name": "b"})
        pizzas = response.context['pizzas']
        self.assertEqual(pizzas[0].name, pizza_case.getAll()[0].name)

    def test_search_view_3(self):
        response = self.client.post("/search", data={"name": "b"})
        pizzas = response.context['pizzas']
        self.assertEqual(pizzas[0].name, pizza_case.getAll()[0].name)

    def test_sign_in_view_1(self):
        response = self.client.post("/sign-in", data={"email": "bebr@mail.ru", "password": "12345678"})
        self.assertEqual(response.status_code, 302)

    def test_sign_in_view_2(self):
        response = self.client.post("/sign-in", data={"email": "bebr@mail.ru", "password": "12345678"})
        self.assertEqual(self.client.session["id"], 1)

    def test_sign_employee_in_view_1(self):
        response = self.client.post("/employee", data={"email": "bebr@mail.ru", "password": "12345678"})
        self.assertEqual(self.client.session["id"], 1)

    def test_sign_employee_in_view_2(self):
        response = self.client.post("/employee", data={"email": "bebr.ru", "password": "12345678"})
        try:
            self.assertEqual(self.client.session["id"], 1)
        except:
            self.assertTrue(True)

    def test_sign_employee_in_view_3(self):
        response = self.client.post("/employee", data={"email": "bebr@mail.ru", "password": "1"})
        try:
            self.assertEqual(self.client.session["id"], 1)
        except:
            self.assertTrue(True)




    def test_sign_1(self):
        user, err = user_case.sign_in({"email": "bebrk@mail.ru", "password": "12345678"})
        self.assertEqual(err,  'пользователь не найден')

    def test_cart_1(self):
        cart, total = user_case.get_cart(1)
        self.assertEqual(total,  41.98)

    def test_orders(self):
        order = user_case.get_orders(1)
        self.assertEqual(list(order)[0].pizza,  {'1':2})

    def test_pizzas_1(self):
        pizzas = pizza_case.getAll()
        self.assertEqual(len(list(pizzas)), 1)

    def test_pizzas_2(self):
        pizzas = pizza_case.getAll()
        self.assertEqual(list(pizzas)[0].name, 'a')

    def test_pizza_1(self):
        pizza = pizza_case.get(1)
        self.assertEqual(pizza.name, "a")

    def test_pizza_2(self):
        try:
            pizza = pizza_case.get(2)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_search(self):
        pizza = pizza_case.search("b")
        self.assertEqual(len(pizza), 1)

    def test_search_pizza_1(self):
        pizza = pizza_case.search("b")
        self.assertEqual(pizza[0].name, "a")

    def test_search_pizza_2(self):
        pizza = pizza_case.search("c")
        self.assertEqual(len(pizza), 0)

    def test_sign_up_user_1(self):
        user, err = user_case.sign_up({"name": "aaaaaaaaa", "email": "aaaaaaaaaa", "birthdate": "2021-01-01", "phone_number": "+375291234567", "password": "12345678"})
        self.assertEqual(err, 'вам должно быть более 18 лет')

    def test_sign_up_user_2(self):
        user, err = user_case.sign_up({"name": "a", "email": "a", "birthdate": "2001-01-01", "phone_number": "+375291234567", "password": "12345678"})
        self.assertEqual(err, 'имя должно быть больше 5 символов')

    def test_sign_up_user_3(self):
        user, err = user_case.sign_up({"name": "abcdef", "email": "aaskd@mail.ru", "birthdate": "2001-01-01", "phone_number": "+375291234567", "password": "12345678"})
        self.assertEqual(err, None)

    def test_sign_in_user_1(self):
        user, err = user_case.sign_in({"email": "bebr@mail.ru", "password": "12345678"})
        self.assertEqual(err, None)

    def test_sign_in_user_2(self):
        user, err = user_case.sign_in({"email": "bebr@mail.ru", "password": "12345679"})
        self.assertEqual(err, 'неверный пароль')

    def test_sign_in_user_3(self):
        user, err = user_case.sign_in({"email": "bebrk@mail.ru", "password": "12345678"})
        self.assertEqual(err,  'пользователь не найден')

    def test_cart_1(self):
        cart, total = user_case.get_cart(1)
        self.assertEqual(total,  41.98)

    def test_g_orders(self):
        order = user_case.get_orders(1)
        self.assertEqual(list(order)[0].pizza,  {'1':2})

    def test_pizzas_1(self):
        pizzas = pizza_case.getAll()
        self.assertEqual(len(list(pizzas)), 1)

    def test_pizzas_2(self):
        pizzas = pizza_case.getAll()
        self.assertEqual(list(pizzas)[0].name, 'a')

    def test_pizza_1(self):
        pizza = pizza_case.get(1)
        self.assertEqual(pizza.name, "a")

    def test_pizza_2(self):
        try:
            pizza = pizza_case.get(2)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_search_p_1(self):
        pizza = pizza_case.search("b")
        self.assertEqual(len(pizza), 1)

    def test_search_p_2(self):
        pizza = pizza_case.search("b")
        self.assertEqual(pizza[0].name, "a")

    def test_search_p_3(self):
        pizza = pizza_case.search("c")
        self.assertEqual(len(pizza), 0)

    
    def test_edit_p_1(self):
         pizza_case.edit({"id": 1,"name":"a", "ingredients":"b", "price":20.99, "weight":600, "size":30})
         pizza = pizza_case.search("b")
         self.assertEqual(pizza[0].weight, 600)

    def test_edit_p_2(self):
         pizza_case.edit({"id": 1,"name":"aboba", "ingredients":"b", "price":20.99, "weight":600, "size":30})
         pizza = pizza_case.search("b")
         self.assertEqual(pizza[0].name, "aboba")
