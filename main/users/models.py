from django.db import models
from django.contrib.auth.models import User



class OpUser(models.Model):
    mail = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    score = models.IntegerField()
    money = models.IntegerField()
    token = models.CharField(max_length=255)
    password = models.CharField(max_length=250)
    _team = models.ForeignKey("Team", on_delete=models.CASCADE, blank=True, null=True)

    def create(self):
        pass

    def get_team_tasks(self):
        return _team.teamtask_set.all()



class Achievement(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey("OpUser", on_delete=models.CASCADE)



class Team(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey("OpUser", on_delete=models.CASCADE) 
    
    @property
    def total_score(self):
        return sum([sc.score for sc in self.opuser_set.all()])
    
    @property
    def size(self):
        return len(self.opuser_set.all())
    


class TeamTask(models.Model):
    name = models.CharField(max_length=250)
    goal_score = models.IntegerField()
    now_score = models.IntegerField(default=0)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    

class UserTask(models.Model):
    name = models.CharField(max_length=250)
    goal_score = models.IntegerField()
    now_score = models.IntegerField(default=0)
    user = models.ForeignKey("OpUser", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

