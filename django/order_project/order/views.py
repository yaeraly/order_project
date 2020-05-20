from django import forms
from pprint import pprint
from django.db.models import Q
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404

from account.models import Account
from .models import Floor, Room, Order, Starter, Tag
from .forms import LunchOrderForm, DinnerOrderForm



class HomeListView(LoginRequiredMixin, generic.ListView):
    model = Floor
    template_name = 'order/home.html'
    paginate_by = 1

    def get_queryset(self):
        self.account = get_object_or_404(Account, email=self.request.user)
        return self.account.floors.all()


class ReportListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'order/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.account = get_object_or_404(Account, email=self.request.user)

        context['lunch_list'] = Order.objects.filter(
            user=self.account, tag__tag_name='Lunch'
        )

        context['dinner_list'] = Order.objects.filter(
            user=self.account, tag__tag_name='Dinner'
        )

        return context

class RoomCreate(SuccessMessageMixin, generic.CreateView):
    model = Room
    fields = ['floor', 'room_num', 'num_guest']
    template_name = 'order/create.html'
    success_url = reverse_lazy('order:home')
    success_message = "%(room_num)s has been created successfully"


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data
        )


class RoomUpdateView(generic.UpdateView):
    model = Room
    fields = ['room_num', 'num_guest']


class RoomDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Room
    success_url = reverse_lazy('order:home')
    success_message = "Selected room has been deleted successfully"


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RoomDeleteView, self).delete(request, *args, **kwargs)


class OrderDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy('order:report')
    success_message = "Selected order has been deleted successfully"
    template_name = 'order/delete.html'


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OrderDeleteView, self).delete(request, *args, **kwargs)


def create_db(request):
    # for fl in range(2, 19):
    #     floor = Floor(floor_num=fl)
    #     floor.save()
    #
    #     for num in range(1, 19):
    #         if fl != 2 and fl != 3:
    #             floor.room_set.create(room_num=fl*100+num)
    #             floor.save()

    return render(request, 'order/create_db.html')


@login_required
def menu(request, pk):
    context = {}
    room = Room.objects.get(id=pk)
    LunchOrderFormSet = inlineformset_factory(
        Room, Order, max_num=1, extra=1, can_delete=False,
        form=LunchOrderForm,
    )
    DinnerOrderFormSet = inlineformset_factory(
        Room, Order, max_num=1, can_delete=False,
        form=DinnerOrderForm
    )
    if request.method == 'POST':
        lunchformset = LunchOrderFormSet(request.POST, instance=room, prefix='lunchform')
        dinnerformset = DinnerOrderFormSet(request.POST, instance=room, prefix='dinnerform')

        if lunchformset.is_valid() and dinnerformset.is_valid():
            lunchformset.save()
            dinnerformset.save()
            return redirect('order:home')
    else:
        lunchformset = LunchOrderFormSet(prefix='lunchform')
        dinnerformset = DinnerOrderFormSet(prefix='dinnerform')


    context['lunchformset'] = lunchformset
    context['dinnerformset'] = dinnerformset
    context['room'] = room


    return render(request, 'order/menu.html', context)
