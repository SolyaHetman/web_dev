from django.urls import path
from advert import views


app_name = 'adverts'


urlpatterns = [
    path('view/', views.AdvertList.as_view(), name='view'),
    path('create/', views.AdvertCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.AdvertUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.AdvertDelete.as_view(), name='delete'),
]
