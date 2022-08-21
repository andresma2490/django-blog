from django.contrib import auth
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from django.views.generic import ListView, View
from django.views.generic.edit import FormView

from .forms import UserForm, LoginForm
from .models import User
from .decorators import login_excluded
from apps.articles.models import Article


@method_decorator(login_excluded, name='dispatch')
class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserForm
    success_url = reverse_lazy("articles:home")

    def form_valid(self, form):
        user = User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["password1"],
            name = form.cleaned_data["name"],
            lastname = form.cleaned_data["lastname"],
        )
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)

@method_decorator(login_excluded, name='dispatch')
class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm

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

class ProfileView(ListView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/profile.html'
    context_object_name = 'articles'
    ordering = ['-id']
    paginate_by = 6

    def get_queryset(self):
        username = self.kwargs.get('username', '')
        articles = Article.objects.filter(author__username=username).order_by(*self.ordering)
        return articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username', '')
        context['user_profile'] = User.objects.get(username=username)
        return context
