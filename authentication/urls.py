from django.urls import path
from .views import BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
