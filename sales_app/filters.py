import django_filters
from .models import mobileproduct


# creating a dynamic filter form
class product_filter_form(django_filters.FilterSet):
    class Meta:
        model = mobileproduct
        fields = ['brand','name']