from django.urls import path
from .views import my_view, my_view1, my_view2, operation, sos_help, square, shop, calculate, converter, event

urlpatterns = [
    path('', my_view, name='my_view'),
    path('hello/', my_view1, name='my_view1'),
    path('world/', my_view2, name='my_view2'),
    path('operation/', operation, name='operation'),
    path('sos/', sos_help, name='sos_help'),
    path('square/', square, name='square'),
    path('calculate/', calculate, name='calculate'),
    path('converter/', converter, name='converter'),
    path('events/', event, name='event'),
]