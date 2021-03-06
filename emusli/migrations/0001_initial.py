# Generated by Django 2.0.5 on 2018-06-11 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('address', models.CharField(max_length=256)),
                ('comments', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('district', models.CharField(max_length=128)),
                ('type', models.IntegerField(choices=[(0, 'Почта'), (1, 'Курьерская служба'), (2, 'Самовывоз')], default=1)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'food_categories',
            },
        ),
        migrations.CreateModel(
            name='Food_Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('img_url', models.URLField()),
                ('ico_url', models.URLField()),
                ('short_desc', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1000)),
                ('qty', models.IntegerField(default=1)),
                ('status', models.IntegerField(choices=[(0, 'Неактивный'), (1, 'Активный')], default=0)),
                ('type', models.IntegerField(choices=[(0, 'не определен'), (1, 'основа'), (2, 'дополнение основы'), (3, 'фрукты'), (4, 'орехи и семена'), (5, 'шоколад')], default=0)),
                ('portion', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('deprecated', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(to='emusli.Food_Category')),
            ],
            options={
                'verbose_name_plural': 'food_components',
            },
        ),
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('short_desc', models.CharField(max_length=256)),
                ('img_url', models.URLField()),
                ('private', models.BooleanField(default=True)),
                ('components', models.ManyToManyField(to='emusli.Food_Component')),
            ],
            options={
                'verbose_name_plural': 'mixes',
            },
        ),
        migrations.CreateModel(
            name='Nutrition_Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caloric_value', models.FloatField(default=0)),
                ('fat', models.FloatField(default=0)),
                ('carbohydrates', models.FloatField(default=0)),
                ('fibre', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('salt', models.FloatField(default=0)),
                ('food_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emusli.Food_Component')),
            ],
            options={
                'verbose_name_plural': 'nutrition_values',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sum', models.FloatField(default=0)),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emusli.Contact')),
                ('delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emusli.Delivery')),
            ],
        ),
        migrations.CreateModel(
            name='OrderRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('mix', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emusli.Mix')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emusli.Order')),
            ],
        ),
        migrations.CreateModel(
            name='User_Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emusli.Mix')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user_preferences',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
