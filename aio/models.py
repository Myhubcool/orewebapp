from django.db import models

class all(models.Model):
    acompanyname = models.CharField(max_length=15)
    aname=models.CharField(max_length=30, null=True)
    ascity=models.CharField(max_length=30, null=True)
    aprice = models.CharField(max_length=30, null=True)
    amob = models.CharField(max_length=30, null=True)
    aaddress = models.CharField(max_length=30, null=True)
    auid=models.CharField(max_length=30, null=True)
    asstate=models.CharField(max_length=30, null=True)
    asdistrict=models.CharField(max_length=30, null=True)
    aspinno=models.CharField(max_length=30, null=True)
    ascolony=models.CharField(max_length=30, null=True)
    asshopname=models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.acompanyname


