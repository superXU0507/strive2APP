import django_filters
from django.db.models import Q
from strive2api import models

class getScoreListFilter(django_filters.rest_framework.FilterSet):
    unit_name = django_filters.CharFilter(field_name='unit__unit_name', label='单位名称')

class getSeason_rankingListFilter(django_filters.rest_framework.FilterSet):
    unit_name = django_filters.CharFilter(field_name='unit__unit_name', label='单位名称')
    unit_cate = django_filters.CharFilter(field_name='unit__unit_cate', label='单位类别')
    year = django_filters.Filter(field_name='year', label='年份')
    season = django_filters.Filter(field_name='season', label='季度')

class getHistory_rankListFilter(django_filters.rest_framework.FilterSet):
    unit_name = django_filters.CharFilter(field_name='unit__unit_name', label='单位名称')

class getAnnual_rankingListFilter(django_filters.rest_framework.FilterSet):
    unit_cate = django_filters.CharFilter(field_name='unit__unit_cate', label='单位类别')
    year = django_filters.Filter(field_name='year', label='年份')

class getScore_itemListFilter(django_filters.rest_framework.FilterSet):
    unit_name = django_filters.CharFilter(field_name='release_date__unit__unit_name', label='单位名称')
    date = django_filters.Filter(field_name='release_date', method='date_filter', label='发布时间')
    scorer = django_filters.CharFilter(field_name='scorer', label='打分者')
    class Meta:
        model = models.Score_item
        fields = [
            'unit_name',
            'date',
            'scorer',
        ]
    def date_filter(self, queryset, _, value):
        value_year = value.split('-')[0]
        value_month = value.split('-')[1]
        return queryset.filter(Q(release_date__month_date__year=value_year) &
                               Q(release_date__month_date__month=value_month))
