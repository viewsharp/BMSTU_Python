from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', FrontPage.as_view(), name='front'),
    url(r'^signup', SignUp.as_view(), name='sign_up'),
    url(r'^login', LogIn.as_view(), name='log_in'),
    url(r'^store/order', order),
    url(r'^store/id([0-9]+)', BookView.as_view(), name='books'),
    url(r'^store/add_author', add_author),
    url(r'^store/add', AddBook.as_view(), name='add_book'),
    url(r'^store', Store.as_view(), name='store'),
    url(r'^logout', logout_view, name='logout'),
]