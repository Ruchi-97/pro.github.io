from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

# Levels data
class level1data(models.Model):
    img_name = models.CharField(max_length=60,default="")
    img_id = models.CharField(max_length=60,default="")
    img_data = models.TextField()
    img_src = models.ImageField(upload_to= "static/l1images",default="")

    def __str__(self):
        return self.img_name
    
class level2data(models.Model):
    img_name = models.CharField(max_length=60,default="")
    img_id = models.CharField(max_length=60,default="")
    img_data = models.TextField()
    img_src = models.ImageField(upload_to= "static/l2images",default="")

    def __str__(self):
        return self.img_name
    
class level3data(models.Model):
    img_name = models.CharField(max_length=60,default="")
    img_id = models.CharField(max_length=60,default="")
    img_data = models.TextField()
    img_src = models.ImageField(upload_to= "static/l3images",default="")

    def __str__(self):
        return self.img_name

class level4data(models.Model):
    img_name = models.CharField(max_length=60,default="")
    img_id = models.CharField(max_length=60,default="")
    img_data = models.TextField()
    img_src = models.ImageField(upload_to= "static/l4images",default="")

    def __str__(self):
        return self.img_name

class level5data(models.Model):
    img_name = models.CharField(max_length=60,default="")
    img_id = models.CharField(max_length=60,default="")
    img_data = models.TextField()
    img_src = models.ImageField(upload_to= "static/l3images",default="")

    def __str__(self):
        return self.img_name

class level6data(models.Model):
    img_name = models.CharField(max_length=60,default="")
    img_id = models.CharField(max_length=60,default="")
    img_data = models.TextField()
    img_src = models.ImageField(upload_to= "static/l3images",default="")

    def __str__(self):
        return self.img_name


# Answer Modal
class answers(models.Model):
     levels  = models.CharField(max_length=60,default="")
     answer = models.CharField(max_length=60,default="")

     def __str__(self):
        return self.levels
    
# Final Score
class FinalScore(models.Model):
    name =  models.CharField(max_length=60,default="")
    Fscore = models.IntegerField(default=0)
    def __str__(self):
        return self.name

# Player Details
class userInfo(models.Model):
    name =  models.CharField(max_length=60,default="")
    score = models.IntegerField(default=0)
    currentLevel = models.IntegerField(default=0)
    Clevel = models.CharField(max_length=60,default="level1")

    level1 = models.CharField(max_length=60,default="level1")
    level1ClickCount = models.IntegerField(default=3)
    level1AddClick =  models.IntegerField(default=0)
    level1score  = models.CharField(max_length=60,default="false")

    level2 = models.CharField(max_length=60,default="level2")
    level2ClickCount = models.IntegerField(default=3)
    level2AddClick =  models.IntegerField(default=0)
    level2score  = models.CharField(max_length=60,default="false")

    level3 = models.CharField(max_length=60,default="level3")
    level3ClickCount = models.IntegerField(default=3)
    level3AddClick =  models.IntegerField(default=0)
    level3score  = models.CharField(max_length=60,default="false")

    level4 = models.CharField(max_length=60,default="level4")
    level4ClickCount = models.IntegerField(default=3)
    level4AddClick =  models.IntegerField(default=0)
    level4score  = models.CharField(max_length=60,default="false")

    level5 = models.CharField(max_length=60,default="level5")
    level5ClickCount = models.IntegerField(default=3)
    level5AddClick =  models.IntegerField(default=0)
    level5score  = models.CharField(max_length=60,default="false")

    level6 = models.CharField(max_length=60,default="level6")
    level6ClickCount = models.IntegerField(default=3)
    level6AddClick =  models.IntegerField(default=0)
    level6score  = models.CharField(max_length=60,default="false")

    def __str__(self):
        return self.name

# ClickedImages
class clickedImages(models.Model):
    name =  models.CharField(max_length=60,default="")
    imgId =  models.CharField(max_length=60,default="")
    def __str__(self):
        return self.name

