from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View
from users.models import OpUser, Team, TeamTask
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


class Login(View):

    def get(self, request):
        pass

    def post(self, request):
        #body = json.loads(request.body)
        #user = OpUser.objects.filter(mail=body.get('email'), password=body.get('password')).first()

        #print(request.body)
        #print(user)
        #if user:
        return JsonResponse({"key": '123'})
        return JsonResponse({"msg": "Not found"}, status=400)


class PersonalInfo(View):

    def get(self, request):
        token = request.headers.get("key")
        user = OpUser.objects.filter(token=token).first()
        if user:
            return JsonResponse(model_to_dict(user))
        return JsonResponse({"msg": "Error"}, status=400)

class Achs(View):

    def get(self, request):
        token = request.headers.get("key")
        user = OpUser.objects.filter(token=token).first()
        achs = user.achievement_set.all().values()
        print(list(achs))
        #if user:
        #    return JsonResponse(model_to_dict(user))
        #return JsonResponse({"msg": "Error"}, status=400)
        return JsonResponse({"achievements": list(achs)}, safe=False)


class LeaderBoard(View):

    def get(self, request):
        best_user = OpUser.objects.order_by('score')[:10]
        return JsonResponse({'leaderboard':list(best_user)}, safe=False)    

class UserTeam(View):

    def post(self, request):
        body = json.loads(request.body)
        token = request.headers.get("key")
        team_name = body.get('name')
        user = OpUser.objects.filter(token=token).first()
        if user:
            team = Team(name=team_name, owner=user)
            team.save()
            return JsonResponse(model_to_dict(team))
        return JsonResponse({"msg": "Error"}, status=400)
    
    def get(self, request):
        token = request.headers.get("key")
        user = OpUser.objects.filter(token=token).first()
        if user:
            team = Team.objects.filter(owner=user).first()
            return JsonResponse(model_to_dict(team))
        return JsonResponse({"msg": "Error"}, status=400)
            
class IdTeam(View):

    def get(self, request):
        team = Team.objects.filter(id=request.GET.get('id')).first()
        if team:
            _team = model_to_dict(team)
            users = [model_to_dict(inst) for inst in team.opuser_set.all()]
            return JsonResponse({"team": _team, "users": users}, safe=False)
        return JsonResponse({"msg": "Error"}, status=400)
        
    

class TeamView(View):

    def get(self, request):
        teams = Team.objects.all()
        return JsonResponse({'teams':list(teams)}, safe=False)    

class TeamTasks(View):

    def get(self, request):
        token = request.headers.get("key")
        user = OpUser.objects.filter(token="123").first()
        tasks = user.get_team_tasks()
        if tasks:
            return JsonResponse(model_to_dict(tasks))
        return JsonResponse({"msg": "Not found"}, status=400)




def create_test():
    user = OpUser(mail='mail', score=1, money=1, password='123', token='123')
    user.save()
    team = Team(name='test_team', owner=user)
    team.save()
    user._team = team
    user.save()
    
