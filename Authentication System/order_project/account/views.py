from django.core.cache import cache
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, views
from django.contrib.messages.views import SuccessMessageMixin

from order.models import Floor

from .models import Account
from .forms import (    RegistrationForm, SignInForm, PasswdChangeForm,
                        PasswdResetForm, PasswdResetConfirmForm)


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            floor = form.cleaned_data.get('floors')
            user = Account.objects.get(email=email)
            user.floors.add(floor)
            user.save()
            messages.success(request, f'Account "{email}" created successfully')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'GET':
        cache.set('next', request.GET.get('next', None))

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                next_url = cache.get('next')
                if next_url:
                    cache.delete('next')
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'account/login.html', {'form': form})


# class PasswordContextMixin:
#     extra_context = None
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'title': self.title,
#             **(self.extra_context or {})
#         })
#         return context
#

class LogoutView(views.LogoutView):
    next_page = '/'


class PasswdChangeView(SuccessMessageMixin, views.PasswordChangeView):
    form_class = PasswdChangeForm
    success_url = reverse_lazy('home')
    template_name = 'account/passwd_change.html'
    success_message = "Your password has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data
        )


class PasswordResetView(views.PasswordResetView):
    form_class = PasswdResetForm
    template_name = 'account/passwd_reset.html'
    email_template_name = 'account/passwd_reset_email.html'
    subject_template_name = 'account/passwd_reset_subject.txt'


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'account/passwd_reset_done.html'


class PasswordResetConfirmView(SuccessMessageMixin, views.PasswordResetConfirmView):
    form_class = PasswdResetConfirmForm
    template_name = 'account/passwd_reset_confirm.html'
    success_url = reverse_lazy('login')
    success_message = "Your password has been reset successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data
        )
