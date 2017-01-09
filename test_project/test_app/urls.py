from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.TestStaticView.as_view(), name="index"),
]
