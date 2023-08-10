from django.db import models

# Create your models here.
class course(models.Model):
    cname = models.CharField(max_length=20) 

    def __str__(self) :
        return self.cname 

class place(models.Model):
    pname = models.CharField(max_length=30)

    def __str__(self) :
        return self.pname 

class student(models.Model):
    rollno = models.IntegerField()
    sname = models.CharField(max_length=30)  
    c_name = models.ForeignKey(course,on_delete=models.CASCADE) 
    p_name = models.ForeignKey(place,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname
    
    
       

