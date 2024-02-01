from django.contrib import admin
from .models import Wallet, Job, Bid, Transaction

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'user', 'balance')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'user', 'job_title', 'budget', 'duration_expected')

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('bid_id', 'job', 'user', 'status')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'transaction_type', 'sender_user', 'receiver_user', 'charges', 'bid_id', 'status')

