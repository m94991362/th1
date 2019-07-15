from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from web import views

urlpatterns = [
    url(r'^submit/expense/$',views.submit_expense,name='submit_expense'),
    url(r'^submit/income/$',views.submit_income,name='submit_income')
]