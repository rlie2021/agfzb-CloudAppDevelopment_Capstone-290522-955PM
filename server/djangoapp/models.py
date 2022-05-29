from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    dealership = models.IntegerField()
    _type = models.CharField(null=False, max_length=30, default='')
    _make = models.CharField(null=False, max_length=30, default='')
    _year =  models.DateField()
    def __str__(self):
            return "Name: " + self.name 
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    description = models.CharField(null=False, max_length=30, default='')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    def __str__(self):
        return "Name: " + self.name + ",Description: " + self.description

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    dealersip = models.IntegerField()
    city = models.CharField(null=False, max_length=30, default='')
    state = models.CharField(null=False, max_length=30, default='')
    st = models.CharField(null=False, max_length=30, default='')
    address = models.CharField(null=False, max_length=30, default='')
    _zip = models.CharField(null=False, max_length=30, default='')
    _lat = models.CharField(null=False, max_length=30, default='')
    _long = models.CharField(null=False, max_length=30, default='')
    short_name = models.CharField(null=False, max_length=30, default='')
    full_name = models.CharField(null=False, max_length=30, default='')

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    dealership = models.ForeignKey(CarDealer, on_delete=models.CASCADE)
    review = models.CharField(null=False, max_length=30, default='')
    purchase = models.BooleanField() 
    purchase_date = models.DateField(null=True)
    car_make = models.CharField(null=False, max_length=30, default='')
    car_year =  models.DateField()
