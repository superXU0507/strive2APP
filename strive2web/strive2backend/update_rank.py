import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","strive2backend.settings")
import django
django.setup()
import datetime
import operator
from decimal import Decimal, getcontext
from django.db.models import Q
from strive2api.models import Unit, Score, Season_ranking, Annual_ranking

CATE_LIST = ['建制连队', '建制营', '非建制单位', '机关股室']
for cate in CATE_LIST:
    qs_unit_cate = cate
    # units = Score.objects.all()
    qs_year = int(datetime.datetime.now().year)
    qs_season = (int(datetime.datetime.now().month)-1)//3+1
    s1_start = datetime.date(qs_year, 1, 1)
    s2_start = datetime.date(qs_year, 4, 1)
    s3_start = datetime.date(qs_year, 7, 1)
    s4_start = datetime.date(qs_year, 10, 1)
    if qs_unit_cate == '建制营':
        if qs_season == 1:
            rank_units = Score.objects.filter(
                (Q(unit__unit_cate='建制连队')|Q(unit__unit_cate='非建制单位')),
                Q(month_date__gte=s1_start),
                Q(month_date__lt=s2_start)
            )
            rank_battalions = Score.objects.filter(
                Q(unit__unit_cate='建制营'),
                Q(month_date__gte=s1_start),
                Q(month_date__lt=s2_start)
            )
        elif qs_season == 2:
            rank_units = Score.objects.filter(
                (Q(unit__unit_cate='建制连队')|Q(unit__unit_cate='非建制单位')),
                Q(month_date__gte=s2_start),
                Q(month_date__lt=s3_start)
            )
            rank_battalions = Score.objects.filter(
                Q(unit__unit_cate='建制营'),
                Q(month_date__gte=s2_start),
                Q(month_date__lt=s3_start)
            )
        elif qs_season == 3:
            rank_units = Score.objects.filter(
                (Q(unit__unit_cate='建制连队')|Q(unit__unit_cate='非建制单位')),
                Q(month_date__gte=s3_start),
                Q(month_date__lt=s4_start)
            )
            rank_battalions = Score.objects.filter(
                Q(unit__unit_cate='建制营'),
                Q(month_date__gte=s3_start),
                Q(month_date__lt=s4_start)
            )
        elif qs_season == 4:
            rank_units = Score.objects.filter(
                (Q(unit__unit_cate='建制连队')|Q(unit__unit_cate='非建制单位')),
                Q(month_date__gte=s4_start),
                Q(month_date__lt=s1_start)
            )
            rank_battalions = Score.objects.filter(
                Q(unit__unit_cate='建制营'),
                Q(month_date__gte=s4_start),
                Q(month_date__lt=s1_start)
            )
    else:
        if qs_season == 1:
            rank_units = Score.objects.filter(
                Q(unit__unit_cate=qs_unit_cate),
                Q(month_date__gte=s1_start),
                Q(month_date__lt=s2_start)
            )
        elif qs_season == 2:
            rank_units = Score.objects.filter(
                Q(unit__unit_cate=qs_unit_cate),
                Q(month_date__gte=s2_start),
                Q(month_date__lt=s3_start)
            )
        elif qs_season == 3:
            rank_units = Score.objects.filter(
                Q(unit__unit_cate=qs_unit_cate),
                Q(month_date__gte=s3_start),
                Q(month_date__lt=s4_start)
            )
        elif qs_season == 4:
            rank_units = Score.objects.filter(
                Q(unit__unit_cate=qs_unit_cate),
                Q(month_date__gte=s4_start),
                Q(month_date__lt=s1_start)
            )
    rank_unit_list = []
    for rank_unit in rank_units.all():
        rank_unit_dict = {}
        if not any(d.get('unit_name', None) == rank_unit.unit.unit_name for d in rank_unit_list):
            #列表中未有的单位，初始化字典
            rank_unit_dict["unit_name"] = rank_unit.unit.unit_name
            rank_unit_dict["unit_cate"] = rank_unit.unit.unit_cate
            rank_unit_dict["year"] = qs_year
            rank_unit_dict["season"] = qs_season
            rank_unit_dict["total_basis"] = rank_unit.month_score_basis
            rank_unit_dict["total_instit"] = rank_unit.month_score_instit
            rank_unit_dict["total_leader"] = rank_unit.month_score_leader
            rank_unit_dict["total_other"] = rank_unit.month_score_other
            rank_unit_dict["total_belief_basis"] = rank_unit.month_score_belief_basis
            rank_unit_dict["total_faith_basis"] = rank_unit.month_score_faith_basis
            rank_unit_dict["total_discipline_basis"] = rank_unit.month_score_discipline_basis
            rank_unit_dict["total_responsible_basis"] = rank_unit.month_score_responsible_basis
            rank_unit_dict["total_belief_instit"] = rank_unit.month_score_belief_instit
            rank_unit_dict["total_faith_instit"] = rank_unit.month_score_faith_instit
            rank_unit_dict["total_discipline_instit"] = rank_unit.month_score_discipline_instit
            rank_unit_dict["total_responsible_instit"] = rank_unit.month_score_responsible_instit
            rank_unit_dict["total_special"] = rank_unit.month_score_special
            rank_unit_dict["total_comprenhensive"] = rank_unit.month_score_comprehensive
            rank_unit_dict["total_institself"] = rank_unit.month_score_institself
            rank_unit_dict["total_basisevaluate"] = rank_unit.month_score_basisevaluate
            rank_unit_dict["total_leaderevaluate"] = rank_unit.month_score_leaderevaluate
            rank_unit_list.append(rank_unit_dict)
        else:
            for d in rank_unit_list:
                if d.get('unit_name', None) == rank_unit.unit.unit_name:
                    d["total_basis"] += rank_unit.month_score_basis
                    d["total_instit"] += rank_unit.month_score_instit
                    d["total_leader"] += rank_unit.month_score_leader
                    d["total_other"] += rank_unit.month_score_other
                    d["total_belief_basis"] += rank_unit.month_score_belief_basis
                    d["total_faith_basis"] += rank_unit.month_score_faith_basis
                    d["total_discipline_basis"] += rank_unit.month_score_discipline_basis
                    d["total_responsible_basis"] += rank_unit.month_score_responsible_basis
                    d["total_belief_instit"] += rank_unit.month_score_belief_instit
                    d["total_faith_instit"] += rank_unit.month_score_faith_instit
                    d["total_discipline_instit"] += rank_unit.month_score_discipline_instit
                    d["total_responsible_instit"] += rank_unit.month_score_responsible_instit
                    d["total_special"] += rank_unit.month_score_special
                    d["total_comprenhensive"] += rank_unit.month_score_comprehensive
                    d["total_institself"] += rank_unit.month_score_institself
                    d["total_basisevaluate"] += rank_unit.month_score_basisevaluate
                    d["total_leaderevaluate"] += rank_unit.month_score_leaderevaluate
                    continue
    #当查询建制营排名时，初始化rank_battalion_list
    if qs_unit_cate == '建制营':
        rank_battalions = rank_battalions.all()
        rank_battalion_list = []
        for rank_battalion in rank_battalions:
            rank_battalion_dict = {}
            if not any(d.get('unit_name', None) == rank_battalion.unit.unit_name for d in rank_battalion_list):
                rank_battalion_dict["unit_id"] = rank_battalion.unit.id
                rank_battalion_dict["unit_name"] = rank_battalion.unit.unit_name
                rank_battalion_dict["unit_cate"] = rank_battalion.unit.unit_cate
                sub_units = []
                rank_battalion_dict["sub_units"] = sub_units
                rank_battalion_dict["sub_count"] = 0
                rank_battalion_dict["total_score"] = str(0)
                rank_battalion_dict["total_other"] = rank_battalion.month_score_other
                rank_battalion_list.append(rank_battalion_dict)
            else:
                for d in rank_battalion_list:
                    if d.get('unit_name', None) == rank_battalion.unit.unit_name:
                        d["total_other"] += rank_battalion.month_score_other
                        continue
    for rank_unit_dict in rank_unit_list:
        if qs_unit_cate == '机关股室':
            getcontext().prec = 2
            t_bs = Decimal(str(rank_unit_dict["total_basis"])) * Decimal('0.4') / Decimal('25')
            t_is = Decimal(str(rank_unit_dict["total_instit"])) * Decimal('0.3')
            t_ls = Decimal(str(rank_unit_dict["total_leader"])) * Decimal('0.3')
            t_os = Decimal(str(rank_unit_dict["total_other"]))
            rank_unit_dict["total_score"] = str(t_bs + t_is + t_ls + t_os)                       
        else:
            month = datetime.date.today().month % 3
            if month == 0:
                month = 3
            getcontext().prec = 2
            t_bs = Decimal(str(rank_unit_dict["total_basis"])) * Decimal('0.4') / Decimal(str(month)) 
            t_is = Decimal(str(rank_unit_dict["total_instit"])) * Decimal('0.6')
            t_os = Decimal(str(rank_unit_dict["total_other"]))
            rank_unit_dict["total_score"] = str(t_bs + t_is + t_os)
            if qs_unit_cate == '建制营':
                sub_unit_dict = {}
                for rank_battalion_dict in rank_battalion_list:
                    if rank_battalion_dict.get('unit_name', None) in rank_unit_dict.get('unit_name', None):
                        #因为是从sub_unit开始循环的，所以不用判断循环中是否出现sub_units[]里的重复项
                        sub_unit_dict["sub_unit_name"] = rank_unit_dict.get('unit_name', None)
                        sub_unit_dict["sub_unit_cate"] = rank_unit_dict.get('unit_cate', None)
                        sub_unit_dict["sub_unit_score"] = str(rank_unit_dict.get('total_score', None))
                        rank_battalion_dict["sub_units"].append(sub_unit_dict)
                        rank_battalion_dict["sub_count"] += 1
                        getcontext().prec = 2
                        rank_battalion_dict["total_score"] = str(Decimal(str(rank_battalion_dict["total_score"])) + Decimal(str(rank_unit_dict.get('total_score', None))))
                        #一个sub_unit只会是一个battalion的子项，所以匹配到直接跳出循环
                        continue
                    
    if qs_unit_cate == '建制营':
        for rank_battalion_dict in rank_battalion_list:
            total_other = str(rank_battalion_dict["total_other"])
            getcontext().prec = 2
            rank_battalion_dict["total_score"] = str(Decimal(rank_battalion_dict["total_score"]) / Decimal(str(rank_battalion_dict["sub_count"])) + Decimal(total_other))
        ranked_unit_list = sorted(rank_battalion_list, key=operator.itemgetter('total_score'), reverse=True)
    else:
        ranked_unit_list = sorted(rank_unit_list, key=operator.itemgetter('total_score'), reverse=True)
    #更新季度排名
    for i, unit_season in enumerate(ranked_unit_list):
        unit_obj = Unit.objects.get(unit_name=unit_season.get('unit_name', None))
        obj, _ = Season_ranking.objects.get_or_create(unit=unit_obj, year=qs_year, season=qs_season)
        obj.total_basis = Decimal(unit_season.get('total_basis', Decimal(0)))
        obj.total_instit = Decimal(unit_season.get('total_instit', Decimal(0)))
        obj.total_leader = Decimal(unit_season.get('total_leader', Decimal(0)))
        obj.total_other = Decimal(unit_season.get('total_other', Decimal(0)))
        obj.total_belief_basis = Decimal(unit_season.get('total_belief_basis', Decimal(0)))
        obj.total_faith_basis = Decimal(unit_season.get('total_faith_basis', Decimal(0)))
        obj.total_discipline_basis = Decimal(unit_season.get('total_discipline_basis', Decimal(0)))
        obj.total_responsible_basis = Decimal(unit_season.get('total_responsible_basis', Decimal(0)))
        obj.total_belief_instit = Decimal(unit_season.get('total_belief_instit', Decimal(0)))
        obj.total_faith_instit = Decimal(unit_season.get('total_faith_instit', Decimal(0)))
        obj.total_discipline_instit = Decimal(unit_season.get('total_discipline_instit', Decimal(0)))
        obj.total_responsible_instit = Decimal(unit_season.get('total_responsible_instit', Decimal(0)))
        obj.total_special = Decimal(unit_season.get('total_special', Decimal(0)))
        obj.total_comprenhensive = Decimal(unit_season.get('total_comprenhensive', Decimal(0)))
        obj.total_institself = Decimal(unit_season.get('total_institself', Decimal(0)))
        obj.total_basisevaluate = Decimal(unit_season.get('total_basisevaluate', Decimal(0)))
        obj.total_leaderevaluate = Decimal(unit_season.get('total_leaderevaluate', Decimal(0)))
        obj.total_score = Decimal(unit_season.get('total_score', Decimal(0)))
        obj.season_rank = i+1
        obj.save()
    #更新年度排名
    for i, unit_annual in enumerate(ranked_unit_list):
        unit_obj = Unit.objects.get(unit_name=unit_annual.get('unit_name', None))
        obj, _ = Annual_ranking.objects.get_or_create(unit=unit_obj, year=qs_year)
        if qs_season == 1:
            obj.s1_score = len(ranked_unit_list) - i
        elif qs_season == 2:
            obj.s2_score = len(ranked_unit_list) - i
        elif qs_season == 3:
            obj.s3_score = len(ranked_unit_list) - i
        elif qs_season == 4:
            obj.s4_score = len(ranked_unit_list) - i
        obj.save()
    # class DecimalEncoder(json.JSONEncoder):#使decimal数据能json化
    #     def default(self, o):# pylint: disable=E0202
    #         if isinstance(o, Decimal):
    #             return str(o)
    #         super(DecimalEncoder, self).default(o)
    # return HttpResponse(json.dumps(ranked_unit_list, ensure_ascii=False, cls=DecimalEncoder), content_type='application/json')
print('process is down')