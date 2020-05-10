from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from .models import Floor, Room
from account.models import Account


class HomeListView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'order/home.html'

    def get_queryset(self):
        self.account = get_object_or_404(Account, email=self.request.user)
        return self.account.floors.all().first().room_set.all()


class RoomCreate(SuccessMessageMixin, generic.CreateView):
    model = Room
    fields = ['room_num', 'num_guest']
    template_name = 'order/create.html'
    success_url = reverse_lazy('home')
    success_message = "%(room_num)s has been created successfully"


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data
        )


class RoomDelete(SuccessMessageMixin, generic.DeleteView):
    model = Room
    template_name = 'order/delete.html'
    success_url = reverse_lazy('home')
    success_message = "Selected room has been deleted successfully"


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RoomDelete, self).delete(request, *args, **kwargs)
