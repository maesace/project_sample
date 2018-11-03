from django.urls import path
from project_sample.accounts.views import UserView

urlpatterns = [
    path('', UserView.as_view(), name='user-view'),
]