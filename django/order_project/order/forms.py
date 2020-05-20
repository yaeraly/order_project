from django import forms
from .models import Tag, Order
from .models import Order, Starter, Main, Dessert


class LunchOrderForm(forms.ModelForm):
    starter = forms.ModelChoiceField(
        queryset=Starter.objects.filter(tags__tag_name='Lunch'),
        widget=forms.RadioSelect,
        empty_label=None,
        label='Starter',
        required = False,
        label_suffix = ''
    )
    main = forms.ModelChoiceField(
        queryset=Main.objects.filter(tags__tag_name='Lunch'),
        widget=forms.RadioSelect,
        empty_label=None,
        required = False,
        label='Main Course',
        label_suffix = ''
    )
    dessert = forms.ModelChoiceField(
        queryset=Dessert.objects.filter(tags__tag_name='Lunch'),
        widget=forms.RadioSelect,
        empty_label=None,
        required = False,
        label_suffix = ''

    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Please leave a comment',
            'class': 'form-control',
            'rows': 2,

        }),
        required = False,
        label_suffix = ''
    )
    class Meta:
        model = Order
        fields = ['starter', 'main', 'dessert', 'comment']

class DinnerOrderForm(forms.ModelForm):
    starter = forms.ModelChoiceField(
        queryset=Starter.objects.filter(tags__tag_name='Dinner'),
        widget=forms.RadioSelect,
        empty_label=None,
        required = False,
        label_suffix = ''
    )
    main = forms.ModelChoiceField(
        queryset=Main.objects.filter(tags__tag_name='Dinner'),
        widget=forms.RadioSelect,
        empty_label=None,
        required = False,
        label='Main Course',
        label_suffix = ''
    )
    dessert = forms.ModelChoiceField(
        queryset=Dessert.objects.filter(tags__tag_name='Dinner'),
        widget=forms.RadioSelect,
        empty_label=None,
        required = False,
        label_suffix = ''

    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Please leave a comment',
            'class': 'form-control',
            'rows': 2,

        }),
        required = False,
        label_suffix = ''
    )
    class Meta:
        model = Order
        fields = ['starter', 'main', 'dessert', 'comment']
