from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View
from users.models import OpUser

# Create your views here.


class Login(View):

    def get(self, request):
        pass

    def post(self, request):
        user = OpUser.objects.filter(mail=request.POST.get('mail'), password=request.POST.get('password')).first()
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
