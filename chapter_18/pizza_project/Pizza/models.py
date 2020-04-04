from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    add_toppings = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def _str__(self):
        if len(self.add_toppings) > 50:
            return self.add_toppings[:50] + "..."
        else:
            return self.add_toppings