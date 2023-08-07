
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('import_csv', views.import_csv, name="import_csv"),
    path('recordPage', views.recordPage, name="recordPage"),
    path('summary', views.summaryPage, name="summary"),
    
]

