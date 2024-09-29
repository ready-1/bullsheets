from django.db import models

# Create your models here.
class Vet(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    title = models.CharField(max_length=16, blank=True)
    practice_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    website = models.URLField(blank=True)
    license = models.CharField(max_length=64)




    def full_name(self):
        return self.fname + " " + self.lname + " " + self.title
    
    def full_address(self):
        # TODO fix blank address2
        return self.address1 + "\n " +self.address2 + "\n " + self.city + ", " + self.state + " " + self.zip
    
    def __str__(self):
        return self.fname + " " + self.lname + " " + self.title + " " + self.practice_name
        
    def city_state_zip(self):
        return self.city + ", " + self.state + " " + self.zip
    

    def __str__(self):
        return self.full_name()