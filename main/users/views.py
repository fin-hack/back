from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View
from users.models import OpUser, Team, TeamTask, UserTask, DocStatus
from django.views.decorators.csrf import csrf_exempt
import random
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
        best_users = OpUser.objects.order_by('score')
        token = request.headers.get("key")
        user = OpUser.objects.filte(token=token).first()

        if len(best_users) >= 10:
            ans = list(best_users[:3])

            for element in len(best_users):
                if user == best_users[element]:
                    for i in range(3,1, -1):
                        ans.append(best_users[element - i])
                    ans.append(user)
                    for i in range(1, 3):
                        ans.append(best_users[element + i])
            return JsonResponse({'leaderboard':list(best_users)}, safe=False)
        return JsonResponse({'leaderboard':list(best_users)}, safe=False)

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
        user = OpUser.objects.filter(token=token).first()
        tasks = user.get_team_tasks()
        if tasks:
            return JsonResponse(model_to_dict(tasks))
        return JsonResponse({"msg": "Not found"}, status=400)




def create_test():
    user = OpUser(mail='work-mail@mail.ru', score=2324, money=1239, password='test', token='123', first_name="Alex", last_name="John", docs_count_plan=10)
    user.save()
    team = Team(name='Dream Team', owner=user)
    team.save()
    user._team = team
    user.save()
    team_task = TeamTask(name="Test task", goal_score=1000, now_score=0, team=team, status=0, price=300)
    team_task.save()
    team_task = TeamTask(name="Test task 2", goal_score=1500, now_score=0, team=team, status=1, price=500)
    team_task.save()
    team_task = TeamTask(name="Test task 3", goal_score=1800, now_score=0, team=team, status=2, price=800)
    team_task.save()

    for i in range(20):
        for _ in range(10):
            _val = random.choice([True, False])
            doc = DocStatus(is_valid=_val, day_end=i, owner=user) 
            doc.save()
            

    
class TaskUserView(View):

    def post(self, request):
        body = json.loads(request.body)
        user = request.headers.get("key")
        name = body.get('name')
        goal_score = body.get('goal_score')
        if user:
            task = UserTask(name=name, goal_score=goal_score, user=user)
            task.save()
            return JsonResponse(model_to_dict(task))
        return JsonResponse({"msg": "Error"}, status=400)

    def get(self, request):
        token = request.headers.get('key')
        user = OpUser.objects.filter(token=token).first()
        if user:
            tasks = UserTask.objects.filter(user=user)
            _tasks = [model_to_dict(t) for t in tasks]
            return JsonResponse({'usertask': _tasks}, safe = False)
        return JsonResponse({"msg": "Error"}, status=400)    

    

class HandTaskUser(View):

    def get(self, request):
        _id = request.headers.get('key')
        us_task = UserTask.objects.filter(id=_id).first()
        if us_task:
            _usesr = us_task.user
            us_task.now_score = us_task.goal_score
            us_task.status = 1# 1 - finish, 0 - not finish
            winner = OpUser.objects.filter(_usesr).first()
            winner.money = winner.money + us_task.price
            winner.score = winner.score + 100 + random.randint(10, 50)
        return JsonResponse({'msg':'Error'}, status=400)

    
    
    
class TeamUserView(View):

    def post(self, request):
        body = json.loads(request.body)
        team = Team.objects.filter(id=body.get("id")).first()
        name = body.get('name')
        goal_score = body.get('goal_score')
        if user:
            task = TeamTask(name=name, goal_score=goal_score, user=user)
            task.save()
            return JsonResponse(model_to_dict(task))
        return JsonResponse({"msg": "Error"}, status=400)

    def get(self, request):
        status = int(request.GET.get('status'))
        team = Team.objects.filter(id=request.GET.get('id')).first()
        if team:
            tasks = TeamTask.objects.filter(team=team, status=status)
            _tasks = [model_to_dict(t) for t in tasks]
            return JsonResponse({'teamtask': _tasks}, safe = False)
        return JsonResponse({"teamtask": []}, status=200)
    
    
class PlaceInTeam(View):

    def get(self, request):
        token = request.headers.get('key')
        user = OpUser.objects.filter(token=token).first()
        if user:
            number_team =  user.get('_team')
            list_team = OpUser.objects.all().filter(_team = number_team).order_by('score')
            place = 1
            all = len(list_team)
            for now_user in list_team:
                if now_user.get('id') == user.get('id'):
                    if place<all//3:
                        return JsonResponse({'place':"В первых рядах"})
                    if all//3 < place and all*2//3>place:
                        return JsonResponse({'place':'Твердая середина'})
                    else:
                        return JsonResponse({'placce':'В конце списка'})
                place+=1
        return JsonResponse({"msg": "Error"}, status=400)    

class ValuesView(View):

    def get(self, request):
        token = request.headers.get('key')
        day = int(request.GET.get('day'))
        user = OpUser.objects.filter(token=token).first()
        if user:
            val_tr = user.count_docs_today(True, day)
            val_fl = user.count_docs_today(False, day)
            perc = sum([user.get_value(i) for i in range(day)])/0.2
            print(perc)
            return JsonResponse({"plan":user.docs_count_plan, "good": val_tr, "bad": val_fl, "percent": perc})
        return JsonResponse({}, status=400)
    
class ValuesGraphView(View):

    def get(self, request):
        token = request.headers.get('key')
        count = int(request.GET.get('count'))
        user = OpUser.objects.filter(token=token).first()
        if user:
            vals = [user.get_value(i) for i in range(1, count+1)]
            return JsonResponse({"values": vals})
        return JsonResponse({}, status=400)
            

    
    

class AnalysisTime(View):

        def get(self, request):
            token = request.headers.get('key')
            user = OpUser.objects.filter(token=token).first()

            if user:
                k = user.count_docs_today(is_valid=True)/user.docs_count_plan
                user.docs_score =  user.docs_score + k * 5
                return JsonResponse({'score':user.docs_score})
            return JsonResponse({'msg':'Error'}, status=400)

    
