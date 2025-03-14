from django.urls import path
from. import views



urlpatterns = [
    path('',views.home,name="home"),
    path('appointment/<int:doctor_id>',views.appointment_page,name="appointment"),
    path('book_appointment/',views.book_appointment,name="book_appointment"),
    path('my_appointments/',views.view_appointments,name="my_appointments"),
    path('cancel_appointment/<int:doctor_id>/<token_no>',views.cancel_appointment,name="cancel_appointment"),
    path('edit_appointment/<int:doctor_id>/<token_no>',views.edit_appointment,name="edit_appointment")
]