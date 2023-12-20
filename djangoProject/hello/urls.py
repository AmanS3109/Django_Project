from django.urls import path  # import path function from django.urls module
from . import views  # from current directory import views

urlpatterns = [
    path("", views.index, name="index"),  # (filename.function_name, name="name")
    path("Shruti", views.Shruti, name="Shruti"),
    path("Stark", views.Stark, name="Stark"),
    path("<str:name>", views.greet, name="greet")  # <str:name> is a path converter that matches any string (except
    # for a /)
]
