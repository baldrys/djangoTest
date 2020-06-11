from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class User(models.Model):
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    totalReward = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def addPayment(self, amount):
        payment = Payment(
            author=self,
            amount=amount
        )
        payment.clean_fields()
        self.totalReward += amount*0.3
        self.save()
        payment.save()
        return payment


class Payment(models.Model):
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

    amount = models.FloatField(
        validators=[MinValueValidator(0)],
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Payout(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    amount = models.FloatField()
    dateCreate = models.DateTimeField(auto_now_add=True)
    dateProcess = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False, blank=False)
    account = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)
