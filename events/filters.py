from events.models import Event
import django_filters
class EventFilter (django_filters.FilterSet): 
    name = django_filters.CharFilter(field_name='name', lookup_expr='contains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='contains')
    address = django_filters.CharFilter(field_name='address', lookup_expr='contains')
    year__lte = django_filters.NumberFilter(label = 'Took Place Before', field_name = 'time', lookup_expr = 'year__lte')
    year__gte = django_filters.NumberFilter(label = 'Took Place After', field_name = 'time', lookup_expr = 'year__gte')
    month__lte = django_filters.NumberFilter(label = 'Took Place Before', field_name = 'time', lookup_expr = 'month__lte')
    month__gte = django_filters.NumberFilter(label = 'Took Place After', field_name = 'time', lookup_expr = 'month__gte')
    cost__lte = django_filters.NumberFilter(label='Cost Less Than', field_name='cost', lookup_expr='lte')
    cost__gte = django_filters.NumberFilter(label='Cost More Than', field_name='cost', lookup_expr='gte')

    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'address',
            'year__lte',
            'year__gte',
            'cost__lte',
            'cost__gte',
        ]


