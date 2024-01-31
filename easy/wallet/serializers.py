from rest_framework import serializers
from .models import Wallet, Transaction, Job, Bid

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        models = Transaction
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        models = Job
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        models = Bid
        fields = '__all__'
        

