from django.urls import path
from .views import homePageview, aboutPageview, contactPageview

urlpatterns = [
    path("", homePageview.as_view (), name="home"),
    path("about/", aboutPageview.as_view (), name="about"),
    path("contact/", contactPageview.as_view (), name="contact"),
    
]
