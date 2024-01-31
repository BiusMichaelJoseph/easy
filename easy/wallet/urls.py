from django.urls import path
from .views import WalletDetailView, TransactionListCreateView, JobListCreateView, BidListCreateView

urlpatterns = [
    path('wallet/', WalletDetailView.as_view(), name='wallet-detail'),
    path('transactions/', TransactionListCreateView.as_view(), name='tansaction-list-create'),
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('bids/', BidListCreateView.as_view(), name='bid-list-create'),
]

