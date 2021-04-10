from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from django.utils.decorators import method_decorator

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView

from .forms import UserForm, LoginForm
from .models import User

class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserForm
    success_url = reverse_lazy("articles:home")

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy("users:profile"))
        
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["password1"],
            name = form.cleaned_data["name"],
            lastname = form.cleaned_data["lastname"],
        )
        return super(RegisterView, self).form_valid(form)

class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            return reverse_lazy('admin:index')
        elif self.request.user.is_authenticated:
            return reverse_lazy("users:profile")

    def form_valid(self, form):
        user = authenticate(
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('users:login'))

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'users/profile.html'