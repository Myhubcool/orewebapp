from django.db import models
class usermodel(models.Model):
    username=                models.CharField(max_length=25)
    userid =                 models.CharField(max_length=25)
    userpassword =           models.CharField(max_length=25)
    userconfirmpassword =    models.CharField(max_length=25)
    useremail =              models.CharField(max_length=60)

    def __str__(self):
        return self.username

class rtlrmodel(models.Model):
    rtlrname =               models.CharField(max_length=25)
    rtlrid =                 models.CharField(max_length=25)
    rtlrpassword =           models.CharField(max_length=25)
    rtlrconfirmpassword =    models.CharField(max_length=25)
    rtlruseremail =          models.CharField(max_length=60)
    rtlrshopname =           models.CharField(max_length=50)
    rtlrshopid =             models.CharField(max_length=40)
    rtlrshoppassword =       models.CharField(max_length=40)
    rtlrshopconfirmpassword =models.CharField(max_length=40)
    rtlrshopcity =           models.CharField(max_length=30)
    rtlrshopno =             models.CharField(max_length=25)
    rtlrshopaddress =        models.CharField(max_length=80)
    rtlrstate=               models.CharField(max_length=25,null=True)
    rtlrdistrict =           models.CharField(max_length=25, null=True)
    rtlrpincode =            models.CharField(max_length=8, null=True)
    rtlrpcolony =            models.CharField(max_length=30, null=True)
    rtlrphoto=               models.ImageField(upload_to='images/')

    def __str__(self):
        return self.rtlrname
