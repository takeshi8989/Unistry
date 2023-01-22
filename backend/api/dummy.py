from django.contrib.auth.models import User
from faker import Faker

def generateUser(n):
    fake = Faker()
    for i in range(n):
        User.objects.create(username=fake.name(), email=fake.email(), password=fake.password())