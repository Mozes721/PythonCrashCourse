# Generated by Django 3.0.4 on 2020-04-11 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppings',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='toppings', to='Pizza.Pizza'),
        ),
    ]
