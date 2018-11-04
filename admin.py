from django.contrib import admin

#class Admin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ('name',)}

 class FoodComponentAdmin(admin.ModelAdmin):
     list_display = ('name', 'short_desc', 'qty', 'status', 'type')

class NutritionValueAdmin(admin.ModelAdmin):
    list_display = ('caloric_value', 'fat', 'carbohydrates', 'fibre', 'protein', 'salt')

class Mix(admin.ModelAdmin):
    list_display = ('name', 'short_desc', 'private')

# Register your models here.
from emusli.models import Food_Category, Food_Component, Mix, Nutrition_Value, UserProfile, Delivery, Order
admin.site.register(Food_Category)
admin.site.register(Food_Component, FoodComponentAdmin)
admin.site.register(Nutrition_Value, NutritionValueAdmin)
admin.site.register(Mix)
admin.site.register(UserProfile)
admin.site.register(User_Preference)
admin.site.register(Delivery)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(OrderRecord)
