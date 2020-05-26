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
from .models import Floor, Room, BreakfastOrder, LunchOrder, DinnerOrder
from .forms import BreakfastOrderForm, LunchOrderForm, DinnerOrderForm



class HomeListView(LoginRequiredMixin, generic.ListView):
    model = Floor
    template_name = 'order/home.html'
    paginate_by = 1

    def get_queryset(self):
        self.account = get_object_or_404(Account, email=self.request.user)
        return self.account.floors.all()


class ReportListView(LoginRequiredMixin, generic.ListView):
    model = LunchOrder
    template_name = 'order/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.account = get_object_or_404(Account, email=self.request.user)

        context['breakfast_list'] = BreakfastOrder.objects.filter(
            user=self.account
        )

        context['lunch_list'] = LunchOrder.objects.filter(
            user=self.account
        )

        context['dinner_list'] = DinnerOrder.objects.filter(
            user=self.account
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


class BreakfastOrderDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = BreakfastOrder
    success_url = reverse_lazy('order:report')
    success_message = "Selected order has been deleted successfully"
    template_name = 'order/delete.html'


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BreakfastOrderDeleteView, self).delete(request, *args, **kwargs)


class LunchOrderDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = LunchOrder
    success_url = reverse_lazy('order:report')
    success_message = "Selected order has been deleted successfully"
    template_name = 'order/delete.html'


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(LunchOrderDeleteView, self).delete(request, *args, **kwargs)


class DinnerOrderDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = DinnerOrder
    success_url = reverse_lazy('order:report')
    success_message = "Selected order has been deleted successfully"
    template_name = 'order/delete.html'


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DinnerOrderDeleteView, self).delete(request, *args, **kwargs)


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
    BreakfastOrderFormSet = inlineformset_factory(
        Room, BreakfastOrder, max_num=1, extra=1, can_delete=False,
        form=BreakfastOrderForm,
    )
    LunchOrderFormSet = inlineformset_factory(
        Room, LunchOrder, max_num=1, extra=1, can_delete=False,
        form=LunchOrderForm,
    )
    DinnerOrderFormSet = inlineformset_factory(
        Room, DinnerOrder, max_num=1, can_delete=False,
        form=DinnerOrderForm
    )
    if request.method == 'POST':
        breakfastformset = BreakfastOrderFormSet(request.POST, instance=room, prefix='breakfastform')
        lunchformset = LunchOrderFormSet(request.POST, instance=room, prefix='lunchform')
        dinnerformset = DinnerOrderFormSet(request.POST, instance=room, prefix='dinnerform')

        if lunchformset.is_valid() and dinnerformset.is_valid()  and breakfastformset.is_valid():
            breakfastformset.save()
            lunchformset.save()
            dinnerformset.save()
            return redirect('order:home')
    else:
        breakfastformset = BreakfastOrderFormSet(prefix='breakfastform')
        lunchformset = LunchOrderFormSet(prefix='lunchform')
        dinnerformset = DinnerOrderFormSet(prefix='dinnerform')

    context['breakfastformset'] = breakfastformset
    context['lunchformset'] = lunchformset
    context['dinnerformset'] = dinnerformset
    context['room'] = room


    return render(request, 'order/menu.html', context)
