from django.urls import path
from .views import *

app_name = "scheduler"
urlpatterns = [
    path('', PracticeListView.as_view(), name="practice-all"),
]
