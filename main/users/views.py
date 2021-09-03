from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View
from users.models import OpUser
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


class Login(View):

    def get(self, request):
        pass

    def post(self, request):
        body = json.loads(request.body)
        user = OpUser.objects.filter(mail=body.get('email'), password=body.get('password')).first()
        print(request.body)
        print(user)
        if user:
            return JsonResponse({"key": user.token})
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
        #token = request.headers.get("key")
        user = OpUser.objects.filter(token="123").first()
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
