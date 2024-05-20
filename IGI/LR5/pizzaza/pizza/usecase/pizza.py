from pizza.repository import pizza as r

def getAll():
    return r.getAll()

def get(data):
    return r.get(data)


def search(name):
    return r.search(name)

def add(data):
    r.add(data)

def edit(data):
    r.edit(data)

def delete(data):
    r.delete(data)


def clear():
    r.clear()