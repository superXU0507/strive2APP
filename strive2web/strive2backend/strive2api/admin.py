import datetime
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q
from django import forms
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.forms import ImportForm

# Register your models here.
from .models import Unit, Score_item, Score, Season_ranking, Annual_ranking

class UnitInline(admin.StackedInline):
    model = Unit
    can_delete = False
    verbose_name_plural = '评分身份'
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = (UnitInline,)

class ScoreInline(admin.TabularInline):
    model = Score
    extra = 0

class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_name', 'unit_cate', 'scorer_major_cate', 'scorer_cate')
    ordering = ('unit_cate', 'unit_name', 'scorer_major_cate')
    list_display_links = list_display
    list_filter = ('unit_cate', 'scorer_major_cate')
    search_fields = ('unit_name',)
    inlines = [ScoreInline]
    actions = ['batch_addScore']
    def batch_addScore(self, request, queryset):
        for unit in queryset:
            Score.objects.create(unit=unit, month_date=datetime.date.today())
    batch_addScore.short_description = '创建今日的评分对象'

class Score_itemInline(admin.TabularInline):
    model = Score_item
    fields = (
        'scorer',
        'major_term',
        'detail_cate',
        'detail_name',
        'description',
        'max_score',
    )
    extra = 0

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit', 'month_date', 'month_score_basis', 'month_score_instit', 'month_score_leader', 'month_score_other')
    readonly_fields = ('month_score_basis', 'month_score_instit', 'month_score_leader', 'month_score_other')
    ordering = ('-month_date',)
    list_display_links = list_display
    list_filter = ('unit__unit_cate', 'unit__scorer_major_cate')
    search_fields = ('unit__unit_name',)
    date_hierarchy = 'month_date'
    inlines = [Score_itemInline]

class Score_itemResource(resources.ModelResource):
    def __init__(self, request=None):
        super(Score_itemResource, self).__init__()
        self.request = request

    class Meta:
        model = Score_item

    def before_import_row(self, row, **kwargs):
        release_date = self.request.POST.get('release_date', None)
        if release_date:
            self.request.session['import_context_release_date'] = release_date
        else:
            try:
                release_date = self.request.session['import_context_release_date']
            except KeyError as e:
                raise Exception(f'release_date context failure on row import, check resources.py for more info: {e}')
        row['release_date'] = release_date

class Score_itemImportForm(ImportForm):
    release_date = forms.ModelChoiceField(
        queryset=Score.objects.filter(Q(month_date__month = datetime.date.today().month),
                                      Q(month_date__year = datetime.date.today().year),(Q(unit__scorer_major_cate = '基层')|Q(unit__scorer_major_cate = '机关'))),
	required=True
    )  

class Score_itemAdmin(ImportExportActionModelAdmin):
    resource_class = Score_itemResource
    def get_import_form(self):
        return Score_itemImportForm
    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        rk['request'] = request
        return rk
    list_display = ('id', 'unit_name', 'month_date', 'scorer', 'major_term', 'detail_cate', 'detail_name', 'max_score', 'unit_score')
    list_display_links = list_display
    list_filter = ('major_term', 'scorer')
    search_fields = ('release_date__unit__unit_name',)
    date_hierarchy = 'release_date__month_date'
    def unit_name(self, obj):
        return obj.release_date.unit.unit_name
    def month_date(self, obj):
        return obj.release_date.month_date

class Season_rankingAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_name', 'unit_cate', 'year', 'season', 'total_score', 'season_rank', 'update_time')
    ordering = ('total_score', 'season_rank')
    list_display_links = list_display
    list_filter = ('unit__unit_cate', 'year', 'season')
    search_fields = ('unit_name',)
    readonly_fields = (
        'year',
        'season',
        'total_basis',
        'total_instit',
        'total_leader',
        'total_other',
        'total_belief_basis',
        'total_faith_basis',
        'total_discipline_basis',
        'total_responsible_basis',
        'total_belief_instit',
        'total_faith_instit',
        'total_discipline_instit',
        'total_responsible_instit',
        'total_special',
        'total_comprenhensive',
        'total_institself',
        'total_basisevaluate',
        'total_leaderevaluate',
        'total_score',
        'season_rank',
    )
    def unit_name(self, obj):
        return obj.unit.unit_name
    def unit_cate(self, obj):
        return obj.unit.unit_cate


class Annual_rankingAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_name', 'unit_cate', 'year', 's1_score', 's2_score', 's3_score', 's4_score', 'annual_score')
    ordering = ('s1_score', 's2_score', 's3_score', 's4_score')
    list_display_links = list_display
    list_filter = ('unit__unit_cate', 'year')
    search_fields = ('unit_name',)
    readonly_fields = (
        'year',
        's1_score',
        's2_score',
        's3_score',
        's4_score',
    )
    def unit_name(self, obj):
        return obj.unit.unit_name
    def unit_cate(self, obj):
        return obj.unit.unit_cate
admin.site.site_header = '双争考评数据管理系统'
admin.site.site_title = '双争管理系统'
admin.site.register(Unit, UnitAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Score_item, Score_itemAdmin)
admin.site.register(Season_ranking, Season_rankingAdmin)
admin.site.register(Annual_ranking, Annual_rankingAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
