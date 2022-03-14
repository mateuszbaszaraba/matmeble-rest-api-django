from django.urls import path
from .views import BlacklistTokenUpdateView, MyTokenObtainPairView

app_name = 'users'

urlpatterns = [
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
