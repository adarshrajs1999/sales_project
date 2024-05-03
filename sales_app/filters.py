import django_filters
from .models import mobileproduct


class search_product(django_filters.FilterSet):
    class Meta:
        model = mobileproduct
        fields = ['brand']