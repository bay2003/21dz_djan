from django.db import models

class User(models.Model):
    uchastok = models.IntegerField(unique=True)
    vladelec = models.CharField(max_length=255, blank=True)
    area = models.FloatField(null=True)

    def __str__(self):
        return self.vladelec

class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    date = models.DateField()
    purpose_of_payment = models.CharField(max_length=255)
    the_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.vladelec} - {self.the_amount} - {self.date}"
