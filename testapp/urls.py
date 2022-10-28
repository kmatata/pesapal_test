from django.urls import path 
from django.contrib import admin

from .views import PaymentView

admin.autodiscover()

app_name = 'testapp'

urlpatterns = [    
    path('', PaymentView.as_view(), name="payment"),
]
