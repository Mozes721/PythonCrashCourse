# Generated by Django 3.0.4 on 2020-04-11 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0003_auto_20200411_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='toppings',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='toppings',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pizza.Pizza'),
        ),
    ]
