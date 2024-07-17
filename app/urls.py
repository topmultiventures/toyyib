from django.urls import path
from app.views import home, adamson, form



urlpatterns = [
    path("", home),
    path("welcome/<str:person>", adamson),
    path("yinmu", form, name="form"),
]
