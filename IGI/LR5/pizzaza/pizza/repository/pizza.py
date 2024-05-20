from pizza.models import Pizza

def getAll():
    return list(Pizza.objects.all())

def get(pizzaId):
    return Pizza.objects.get(id = pizzaId)


def search(name):
    return Pizza.objects.filter(ingredients__icontains=name)


def add(data):
    Pizza.objects.create(**data)

def edit(data):
    Pizza.objects.filter(id=data["id"]).update(
    name = data["name"],
    ingredients = data["ingredients"],
    price = data["price"],
    weight = data["weight"],
    size = data["size"]
    )

def delete(pizzaId):
    Pizza.objects.filter(id=pizzaId).delete()

def clear():
    Pizza.objects.all().delete()