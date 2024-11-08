from django.test import TestCase
from django.contrib.auth import login,logout, authenticate
# Create your tests here.
import django
django.settings.configure()
django.setup()
from django.contrib.auth.models import User
user = authenticate( username='admin', password='123')
print(user)