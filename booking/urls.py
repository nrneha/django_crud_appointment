from django.urls import path
from. import views



urlpatterns = [
    path('',views.home,name="home"),
    path('appointment/<int:doctor_id>',views.appointment_page,name="appointment"),
    path('book_appointment/',views.book_appointment,name="book_appointment"),
]