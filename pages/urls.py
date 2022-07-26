from django.urls import path
from .views import HomePageView, AboutPageView, LoginPageView, MenuPageView, SignUpPageView, CartPageView, ProfileEditPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('menu/', MenuPageView.as_view(), name='menu'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignUpPageView.as_view(), name='signup'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('ProfileEdit/', ProfileEditPageView.as_view(), name='ProfileEdit'),
]