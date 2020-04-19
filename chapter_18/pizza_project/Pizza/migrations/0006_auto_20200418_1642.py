# Generated by Django 3.0.4 on 2020-04-18 16:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0005_auto_20200411_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toppings',
            options={'verbose_name_plural': 'toppings'},
        ),
        migrations.RenameField(
            model_name='toppings',
            old_name='topping',
            new_name='toppings',
        ),
        migrations.RemoveField(
            model_name='toppings',
            name='name',
        ),
        migrations.AddField(
            model_name='pizza',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toppings',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toppings',
            name='pizza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pizza.Pizza'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(default='Not given yet', max_length=400),
        ),
    ]
