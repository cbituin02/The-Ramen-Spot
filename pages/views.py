from pipes import Template
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class MenuPageView(TemplateView):
    template_name = 'menu.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class SignUpPageView(TemplateView):
    template_name = "signup.html"

class CartPageView(TemplateView):
    template_name = "cart.html"

class ProfileEditPageView(TemplateView):
    template_name = "ProfileEdit.html"