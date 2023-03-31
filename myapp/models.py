from django.db import models
 
# Create your models here.
class Employee(models.Model):  
    Reference_No = models.CharField(max_length=8)
    Serial_No = models.CharField(max_length=20)    
    CMDB_item_type = models.CharField(max_length=20) 
    User_name= models.CharField(max_length=50)   
    Email_address = models.EmailField(50)  
    Organisation = models.CharField(max_length=60) 
   
    class Meta:  
        db_table = "tblemployee"
        
        
# python manage.py makemigrations
# python manage.py migrate

# PRAGMA table_info(tblemployee); 