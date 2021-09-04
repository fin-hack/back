from django.db import models
from django.contrib.auth.models import User
from datetime import datetime





class OpUser(models.Model):
    mail = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    score = models.IntegerField()
    money = models.IntegerField()
    token = models.CharField(max_length=255)
    password = models.CharField(max_length=250)
    _team = models.ForeignKey("Team", on_delete=models.CASCADE, blank=True, null=True)

    docs_count = models.FloatField(blank=True, null=True)
    attention = models.FloatField(blank=True, null=True)
    immersion = models.FloatField(blank=True, null=True)
    stress_tolerance = models.FloatField(blank=True, null=True)

    docs_count_plan = models.IntegerField(blank=True, null=True)   

    def create(self):
        pass

    def get_team_tasks(self):
        return _team.teamtask_set.all()

    def count_docs_today(self, is_valid, day):
        docs = self.docs.filter(day_end=day, is_valid=is_valid)
        return len(docs) 

    def get_value(self, day):
        _all = self.count_docs_today(True, day) + self.count_docs_today(False, day)
        if _all < -1:
            _all = -1
        try:
            res = ((self.count_docs_today(True, day)-10)/_all) + 1
            return res
        except:
            _all = -1
            res = ((self.count_docs_today(True, day)-10)/_all) + 1
            return 0
            

    def get_value_graph(self, day):
        return self.count_docs_today(True, day)/self.docs_count_plan

class DocStatus(models.Model):
    day_end = models.IntegerField(default=datetime.today().day, blank=True)
    is_valid = models.BooleanField(default=False)
    owner = models.ForeignKey("OpUser", on_delete=models.CASCADE, related_name='docs')
    
        


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
    status = models.IntegerField(default=0)
    price = models.IntegerField(default=1)
    

class UserTask(models.Model):
    name = models.CharField(max_length=250)
    goal_score = models.IntegerField()
    now_score = models.IntegerField(default=0)
    user = models.ForeignKey("OpUser", on_delete=models.CASCADE, related_name="tasks")
    status = models.IntegerField(default=0)
    price = models.IntegerField(default=1)



class Product(models.Model):
    pass
