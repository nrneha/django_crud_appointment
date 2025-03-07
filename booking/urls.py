from django.urls import path
from. import views


urlpatterns = [
    path('home/',views.home,name="home"),
    path('appointment/<int:doctor_id>',views.appointment_page,name="appointment")
]