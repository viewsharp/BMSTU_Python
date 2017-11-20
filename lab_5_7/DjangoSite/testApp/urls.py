from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^function_view/', function_view),
    url(r'^class_based_view/', ExampleClassBased.as_view()),
    url(r'^$', ExampleView.as_view()),
    url(r'^order/(?P<id>\d+)', OrderView.as_view(), name='order_url'),
    url(r'^orders/', OrdersView.as_view()),
    url(r'^reg/', registration),
    url(r'^login/', login)
]