from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('diagnose', DiagnosView.as_view(), name='diagnose'),
    path('reports', ReportView.as_view(), name='reports'),
    path('question', QuestionView.as_view(), name='question'),
    path('question/<pk>', QuestionDetailView.as_view(), name='question_details'),
    # path('output', display_img, name='disp'),
]