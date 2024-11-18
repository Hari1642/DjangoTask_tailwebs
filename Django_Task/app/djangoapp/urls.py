from django.urls import path
from .import views
urlpatterns = [
    path('login_view',views.login_view,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('home',views.home,name='home'),
    path('registration_student_view',views.registration_student_view,name='registration_student_view'),
    path('details_view',views.details_view,name='details_view')
]