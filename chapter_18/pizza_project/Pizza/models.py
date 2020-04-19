from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=400, default='Not given yet')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Toppings(models.Model):
    toppings = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'toppings'

    def _str__(self):
        if len(self.toppings) > 50:
            return self.toppings[:50] + "..."
        else:
            return self.toppings
