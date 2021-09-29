from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from pomagam_app.forms import RegisterForm, LoginForm, AddDonationForm
from pomagam_app.models import Category, Donation, Institution
from django.views import View


class LandingPage(View):

    def get(self,request):
        donations = Donation.objects.all().count()
        fundactions = Institution.objects.filter(type=1)
        organizations = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)
        return render(request, 'index.html', {'donations':donations, 'fundactions':fundactions, 'organizations':organizations, 'local_collections':local_collections})


class AddDonation(LoginRequiredMixin, FormView):
    login_url = '/login'
    template_name = 'form.html'
    form_class = AddDonationForm
    success_url = reverse_lazy('confirmation')
    extra_context = {'categories': Category.objects.all()}

    def form_valid(self, form):
        form.save()
        print("Gratulacje twój formularz został wysłany")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Błąd formularza")
        print(form.errors)
        return super().form_valid(form)


class ConfirmationView(View):
    
    def get(self, request):
        return render(request, 'form-confirmation.html')


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return redirect('/register')
            return redirect('/')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')


class Register(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['name']
            user.last_name = form.cleaned_data['surname']
            user.save()
            return redirect('/login')
        return render(request, 'register.html', {'form': form})


class Profile(View):

    def get(self, request, id):
        donations = Donation.objects.filter(pk=id)
        return render(request, 'profile.html',{'donations':donations} )


