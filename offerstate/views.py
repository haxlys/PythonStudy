from django.shortcuts import render
from django.db.models import Count
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse

from django.db import connections
from django.db import connection

import json

from .models import OfferSkills
# Create your views here.

def skill_list(request):
    skill_list = OfferSkills.objects.using("mysql").all().values('skill_name').annotate(total=Count('skill_name')).order_by('-total')
    paginator = Paginator(skill_list, 20) # 페이지당 20개씩 출력

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # page가 숫자가 아닐 경우 첫 페이지로 이동
        contacts = paginator.page(1)
    except EmptyPage:
        # 페이지가 없을 경우 마지막 페이지로 이동
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'offerstate/states_list.html', {"list":contacts})

def skill_relation(request):

    skill_name = request.POST.get('skill_name')
    sql_params = [skill_name , skill_name]
    sql = """
            select      id
            ,           count(B.skill_name) as cnt
            ,           B.skill_name
            from (
                select      offer_id
                from        offer_skills
                where       skill_name = %s
            )A
            left outer join offer_skills B
            on A.offer_id = B.offer_id
            where       B.skill_name != %s
            group by    B.skill_name
            order by    cnt desc
            limit 5
        """

    "connection 객체를 사용하여 질의한 경우"
    cursor = connections['mysql'].cursor() # 디비를 두개 이상 사용하는 환경일 때는 connections 하나일 경우 connection을 사용한다.
    cursor.execute(sql, sql_params)
    #row = cursor.fetchone() # row가 하나일 경우
    #row = cursor.fetchall() # row가 2개이상일 경우

    "raw() 함수를 사용하여 질의한 경우 - select 한 컬럼과 상관없이 모든 컬럼이 출력되므로 별도의 작업이 필요할 것 같다."
    #raw_data = OfferSkills.objects.using("mysql").raw(sql, sql_params)
    #json_data = json.dumps( json.loads( serializers.serialize('json', raw_data) ) )
    #return HttpResponse(json_data,  content_type='application/json' )

    return HttpResponse( json.dumps( dictfetchall(cursor)), content_type = "application/json")

# cursor.fetchall()을 사용하여 질의값을 가져올 경우 key:value 형태가 아닌 value list 형태로 넘어오기 때문에 만들어줌.
# key:value 형태로 리턴함
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
