from django.db import models
from django.contrib.auth.models import User

class TeamofDoctors(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    specialization = models.CharField(max_length=50,null=True,blank=True)
    op_date = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.name
    

class Token(models.Model):
    doctor = models.ForeignKey(TeamofDoctors,on_delete=models.CASCADE)
    token_number = models.PositiveIntegerField()
    op_day = models.CharField(max_length=50,null=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor.name} - {self.token_number}"
    
class Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact_no = models.PositiveIntegerField(null=True)
    doctor = models.ForeignKey(TeamofDoctors,on_delete=models.CASCADE)
    op_day = models.CharField(max_length=50,null=True)
    token = models.OneToOneField(Token,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.doctor.name} - {self.token.token_number}"

