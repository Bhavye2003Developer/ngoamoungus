from django.db import models

# Create your models here.
class DonarsInfo(models.Model):
    customer_id = models.AutoField
    first_name = models.CharField(max_length=30,default="Not given")
    last_name = models.CharField(max_length=30,default="Not given")
    email_address = models.CharField(max_length=20,default="Not given")
    phone_num = models.IntegerField(default=0)
    state = models.CharField(max_length=20,default="Not given")
    city = models.CharField(max_length=20,default="Not given")
    skill_set = models.CharField(max_length=70,default="Not given")
    price = models.IntegerField(default=-1)

    def __str__(self) -> str:
        return (self.first_name+" "+self.last_name)



