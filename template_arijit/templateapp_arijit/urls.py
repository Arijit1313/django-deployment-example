from django.urls import path
from templateapp_arijit import views

# SET THE NAMESPACE!
app_name = 'templateapp_arijit'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
