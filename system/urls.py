
from django.urls import path
from . import views
app_name='system'
urlpatterns=[
    path('',views.homepage,name='home'),
    path('order',views.orderpage,name='order'),
    path('menu',views.menupage,name='menu'),
    path('about',views.aboutpage,name='about'),
    path('receipt/', views.receipt_view, name='receipt'),
 
]