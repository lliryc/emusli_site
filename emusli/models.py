from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Food_Category(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    img_src = models.CharField(max_length = 256)

    class Meta:
        verbose_name_plural = 'food_categories'

    def _str_(self):
        return self.name

class Food_Component(models.Model):
    DEFAULT_STATUS = 0 # draft
    INACTIVE_STATUS  = 0
    ACTIVE_STATUS  = 1

    STATUS_CHOICES = (
        (INACTIVE_STATUS, 'Неактивный'),
        (ACTIVE_STATUS, 'Активный')
    )

    DEFAULT_TYPE = 0
    BASE_TYPE = 1
    ADDITION_BASE_TYPE = 2
    FRUIT_TYPE = 3
    NUTS_AND_SEEDS_TYPE = 4
    CHOCO_TYPE = 5

    TYPE_CHOICES = (
        (DEFAULT_TYPE, 'не определен'),
        (BASE_TYPE, 'основа'),
        (ADDITION_BASE_TYPE, 'дополнение основы'),
        (FRUIT_TYPE, 'фрукты'),
        (NUTS_AND_SEEDS_TYPE, 'орехи и семена'),
        (CHOCO_TYPE, 'шоколад'),
    )

    DEFAULT_QTY = 1

    name = models.CharField(max_length = 128, unique=True)
    img_url = models.URLField()
    ico_url = models.URLField()
    short_desc = models.CharField(max_length = 500)
    desc = models.CharField(max_length = 1000) # worth to consider TextField
    qty = models.IntegerField(default = DEFAULT_QTY)
    status = models.IntegerField(
        choices = STATUS_CHOICES,
        default = DEFAULT_STATUS
    )
    type = models.IntegerField(
        choices = TYPE_CHOICES,
        default = DEFAULT_TYPE
    )
    portion = models.IntegerField(
        default = 0, # in grams
    )
    price = models.FloatField(
            default = 0,
    )
    categories = models.ManyToManyField(Food_Category)
    deprecated = models.BooleanField(default=False)
    new = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'food_components'


    def _str_(self):
        return self.name

class Nutrition_Value(models.Model):
    food_component = models.ForeignKey(Food_Component, on_delete=models.CASCADE)

    caloric_value = models.FloatField(default = 0) # in kilocalories
    fat = models.FloatField(default = 0) # in grams
    carbohydrates = models.FloatField(default = 0)# in grams
    fibre = models.FloatField(default = 0)# in grams
    protein = models.FloatField(default = 0)# in grams
    salt = models.FloatField(default = 0)# in grams

    class Meta:
        verbose_name_plural = 'nutrition_values'

    def _str_(self):
        return self.name

class Mix(models.Model):
    name = models.CharField(max_length = 128)
    short_desc = models.CharField(max_length = 256)
    img_url = models.URLField()
    components = models.ManyToManyField(Food_Component)
    private = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'mixes'

    def _str_(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256)

class User_Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mix = models.ForeignKey(Mix, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'user_preferences'

    def _str_(self):
        return 'user_preference'

class Delivery(models.Model):
    DEFAULT_TYPE = 1
    POST_TYPE = 0
    COURIER_TYPE = 1
    PICKUP_TYPE = 2

    TYPE_CHOICES = (
        (POST_TYPE, 'Почта'),
        (COURIER_TYPE, 'Курьерская служба'),
        (PICKUP_TYPE, 'Самовывоз')
    )

    country = models.CharField(max_length=128)

    city = models.CharField(max_length=128)

    district = models.CharField(max_length=128)

    type = models.IntegerField(
            choices = TYPE_CHOICES,
            default = DEFAULT_TYPE
    )

    price = models.FloatField(default = 0) # in rubles

class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    address = models.CharField(max_length=256)
    comments = models.CharField(max_length=256)

class Order(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL,null=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    total_sum = models.FloatField(default = 0) # in rubles

class OrderRecord(models.Model):
    mix = models.ForeignKey(Mix, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
