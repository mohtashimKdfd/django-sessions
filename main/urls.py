from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.home),
    path('set',views.setSession),
    path('get',views.getsession),
    path('del',views.delsession),
    path('auth',views.auth,name='auth'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('addnew',views.addnewUser,name='add'),
    path('user',views.user)
]
