from django.urls import path

from .import views

urlpatterns = [
    
    path('',views.SignUp,name="signup"),
    path('login/',views.Login,name="login"),
    # path('error/',views.Error,name="error"),
    path('welcom/',views.Welcome,name="welcom"),
]
