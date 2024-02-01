from django.db import models
from userAuth.models import CustomUser

class Wallet(models.Model):
    account_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_expected = models.IntegerField()

class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=255) #active or closed or etc.    

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=255)
    sender_user = models.ForeignKey(CustomUser, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver_user = models.ForeignKey(CustomUser, related_name='received_transactions', on_delete=models.CASCADE)
    charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bid_id = models.ForeignKey(Bid, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=255)