from django.db import models
from .db_connection import db
# Create your models here.


AllCoffeeData = db['CoffeeData']

MongoDynamicData = db['DynamicData']