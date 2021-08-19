from django.urls import path
from core.views import SignUpView, ProfileView, ActivateAccount, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
	path('logout/', LoginView.logout_view, name='logout'),

    # Main Page 
    path('', LoginView.as_view(), name='index'), 

    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]