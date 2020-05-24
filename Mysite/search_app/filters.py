from annonce.models import Annonce
import django_filters
from django_filters import DateFilter
from django.forms.widgets import TextInput, DateTimeInput


class AnnonceFilter(django_filters.FilterSet):
    date_gt = DateFilter(field_name='created', lookup_expr='gte', widget=TextInput(attrs={'placeholder': ' de la date '}))
    date_lt = DateFilter(field_name='created', lookup_expr='lte' , widget=TextInput(attrs={'placeholder': 'a la date'}))
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    
    class Meta:
        model = Annonce
        fields = ['categories', 'type_annonce']
