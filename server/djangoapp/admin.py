from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

class CarModelInline(admin.StackedInline):
    model = CarModel
    sortable_field_name = "name"
    extra = 0


# Register your models here.

# CarModelAdmin class
class CarModelAdmin(admin.StackedInline):
    model = CarModel
    sortable_field_name = "name"
    extra = 0
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.StackedInline):
    make = CarMake
    sortable_field_name = "name"
    extra = 0
# Register models here
admin.site.register(CarMake)
admin.site.register(CarDealer)
admin.site.register(DealerReview)
admin.site.register(CarModel)