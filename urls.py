from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("",views.index,name="index"),
    
    path('register/',views.register,name="register"),
  
    path('login/',views.login,name="login"),
    path("handlelogout",views.handlelogout,name="handlelogout"),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('user_list/', views.user_list, name="user_list"),
]

