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
    path('sbboktrain',views.sbooktrain,name="sbboktrain"),
    path('user_list/', views.user_list, name="user_list"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('userview/',views.userview,name='userview'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback_thankyou/', views.feedback_thankyou, name='feedback_thankyou'), 
    path("adminfeedback",views.adminfeedback,name='adminfeedback'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
