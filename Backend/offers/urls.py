from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'offers'

urlpatterns = [
    path('offers/', OfferList.as_view(), name='offers'),
    path('offers/<int:pk>/', OfferDetail.as_view(), name='offerdetail'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='categorydetail'),
    path('offerswithcategory/<int:category_id>/', OfferWithCategory.as_view(), name='offerwithcategory')
]
