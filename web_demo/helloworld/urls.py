from django.urls import re_path
from helloworld import views

urlpatterns = [
    re_path(r"^helloword/$", views.first_view_func),
    re_path(r"^index/$", views.index)
]