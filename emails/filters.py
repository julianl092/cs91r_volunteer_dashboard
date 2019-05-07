from volunteers.models import Volunteer
import django_filters
class VolunteerFilter (django_filters.FilterSet): 
    num_events = django_filters.NumberFilter(label = 'Has Attended At Least', lookup_expr='gte')
    num_hours = django_filters.NumberFilter(label = 'Has Volunteered For More Than', lookup_expr='gte')
    year_joined__lte = django_filters.NumberFilter(label = 'Joined Before', field_name = 'date_joined', lookup_expr = 'year__lte')
    year_joined__gte = django_filters.NumberFilter(label = 'Joined After', field_name = 'date_joined', lookup_expr = 'year__gte')
    birthday__lte = django_filters.NumberFilter(label = 'Was Born Before', field_name = 'birthday', lookup_expr = 'year__lte')
    birthday__gte = django_filters.NumberFilter(label = 'Was Born After', field_name = 'birthday', lookup_expr = 'year__gte')
    gender = django_filters.CharFilter(label = 'Is Of', field_name = 'gender', lookup_expr = 'exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Volunteer
        fields = ['num_events', 'num_hours', 'year_joined__lte', 'year_joined__gte', 'birthday__lte', 'birthday__gte', 'gender', 'name']


