from django.urls import path
from. import views

app_name = 'users'

urlpatterns = [
        path('',views.sign_up,name="signup"),
        path('sign_in/',views.sign_in,name="sign_in"),
        path('login/',views.log_in,name="login")
]