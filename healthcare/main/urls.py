from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("doctors/", views.doctors, name='doctors'),
    path("pravacy/", views.privacy, name='privacy'),
    path("terms/", views.terms, name='terms'),
    path("services", views.services, name='services'),
    path("testimonials/", views.testimonials, name='testimonials'),
    path("depertment/", views.depertment, name='depertment'),
    path("appointment/", views.appointment, name='appointment'),

]