from pizza.models import Employee

def getById(Id):
    try:
        return Employee.objects.get(id=Id)
    except:
        return None


def getByEmail(Email):
    try:
        return Employee.objects.get(email=Email)
    except:
        return None
    