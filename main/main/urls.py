"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import PersonalInfo, Achs, Login, LeaderBoard, UserTeam, IdTeam, TaskUserView, TeamUserView, PlaceInTeam, AnalysisTime, ValuesView, ValuesGraphView, HandTaskUser, DocComplete, TeamLeaderBoard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', Login.as_view()),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('users/', PersonalInfo.as_view()),
    path('users/achievements/', Achs.as_view()),
    path('users/leaderboard/', LeaderBoard.as_view()),

    path('users/team/', UserTeam.as_view()),
    path('users/tasks/', TaskUserView.as_view()),
    path('users/time/', AnalysisTime.as_view()),
    path('users/values/', ValuesView.as_view()),
    path('users/graph_values/', ValuesGraphView.as_view()),

    path('team/', IdTeam.as_view()),
    path('team/myplace', PlaceInTeam.as_view()),
    path('team/tasks/', TeamUserView.as_view()),
    path('team/leaderboard/', TeamLeaderBoard.as_view()),

    path('task/successful/', HandTaskUser.as_view()),
    path('doc/', DocComplete.as_view())
]
