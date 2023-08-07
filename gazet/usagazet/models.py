from django.db import models

# Create your models here.



class Gradutes(models.Model):
    roll_no=models.CharField(max_length=250, null=True, blank=True)
    name=models.CharField(max_length=250, null=True, blank=True)
    father_name=models.CharField(null=True, blank=True, max_length=250)
    cnic=models.CharField(null=True, blank=True, max_length=50)
    degree_title=models.CharField(null=True, blank=True, max_length=250)
    session_enrolment_date=models.CharField(max_length=250,null=True, blank=True)
    session_completion_date=models.CharField(max_length=250,null=True, blank=True)
    degree_no= models.CharField(max_length=250,null=True, blank=True)
    remark=models.CharField(max_length=250, null=True, blank=True)
    
    
    