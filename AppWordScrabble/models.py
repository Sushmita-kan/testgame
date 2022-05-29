from django.db import models

# Create your models here.
# Create your models here.
class UserDetails(models.Model):
	Firstname = models.CharField(max_length = 100,default = None)
	Lastname = models.CharField(max_length = 100,default = None)
	Phone = models.CharField(max_length = 100,default = None)
	Email = models.EmailField(max_length = 100,default = None)
	Username = models.CharField(max_length = 100,default = None)
	Password = models.CharField(max_length = 100,default = None)
	

	class Meta:
		db_table = 'UserDetails'

class GameDetails(models.Model):

	ChallengedBy = models.CharField(max_length = 100,default = None,blank=True,null=True)
	WordToPlay = models.CharField(max_length = 100,default = None,blank=True,null=True)
	#MaxScorePossible = models.IntegerField(blank=True,null=True)
	PlayedBy = models.CharField(max_length = 100,default = 'No One',blank=True,null=True)
	ScoreGained = models.IntegerField(blank=True,null=True,default = -3)


