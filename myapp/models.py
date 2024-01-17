from django.db import models

# Create your models here.


class TeamMember(models.Model):
    job = models.CharField(max_length = 255 )
    full_name =   models.CharField(max_length = 255 )   
    image = models.ImageField()
    created_at = models.DateField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.full_name


class Social_medias(models.Model):
    facebook = models.CharField(null = True)
    twitter = models.CharField(null = True)
    linkedin = models.CharField(null = True)
    instagram = models.CharField(null = True)
    youtube = models.CharField(null = True)
    telegram = models.CharField(null = True)
    teammember = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    

class Banner(models.Model):
    title = models.CharField(max_length = 255 )
    info = models.TextField()
    image = models.ImageField()
    created_at = models.DateField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title
    

class Service(models.Model): 
    title = models.CharField(max_length = 255 )
    info = models.TextField()
    image = models.ImageField()
    created_at = models.DateField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title
    
        
    
        
class Customer(models.Model):
    name = models.CharField(max_length = 255)
    info = models.TextField()
    image = models.ImageField()
    created_at = models.DateField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.info