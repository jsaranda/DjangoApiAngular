from django.db import models

class Expense(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   amount = models.DecimalField(max_digits=10, decimal_places=2)
   category = models.CharField(max_length=50)
   date = models.DateTimeField(auto_now_add=True)
