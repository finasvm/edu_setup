from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('userhome/',Home.as_view(),name='userhome'),
    path('adddprod/',addprod.as_view(),name='addprod'),
     path('delprod/<int:id>/',DelProd.as_view(),name='delprod'),

]