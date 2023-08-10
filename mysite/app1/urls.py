from django.urls import path
from . import views


urlpatterns =[
    
    path('',views.home),
     path('a',views.about),
     path('pr',views.product,name="product")
]