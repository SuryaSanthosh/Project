from . import views
from django.urls import path
from .views import add_route 
from django.contrib.auth import views as auth_views
from .views import paydetails, payment
from myApp.views import trainview
from .views import user_search
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
    path('user_list', views.user_list, name="user_list"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('userview/',views.userview,name='userview'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback_thankyou/', views.feedback_thankyou, name='feedback_thankyou'), 
    path("adminfeedback",views.adminfeedback,name='adminfeedback'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addtrain/', views.add_train, name='addtrain'),
    path('trainview/', views.trainview, name='trainview'),
    path('myprofile',views.myprofile,name='myprofile'),
    path('add_station/', views.add_station, name='add_station'),
    path('station_list/', views.station_list, name='station_list'),
    path('add_route/', views.add_route, name='add_route'),
    path('train_search/', views.train_search, name='train_search'),
    path('display_route/', views.display_route, name='display_route'),
    path('search_train/', views.search_train, name='search_train'),
    path('user_index/', views.user_index, name='user_index'),
    path('seat_selection', views.seat_selection, name='seat_selection'),
    path('details', views.details, name='details'),
    path('payment/', views.payment_view, name='payment'),  
    path('payment_success/', views.payment_success_view, name='payment_success'),
    path('payment_cancel/', views.payment_cancel_view, name='payment_cancel'),
    path('paydetails/', paydetails, name='paydetails'),
    path('usersearch/', user_search, name='usersearch'),





]

