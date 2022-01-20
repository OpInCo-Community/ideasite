import django_filters
from ideas.models import Idea
class IdeaFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    # author = django_filters.CharFilter(field_name="author", lookup_expr='exact')

    class Meta:
        model = Idea
        fields = ['title', 'description', 'author', ]