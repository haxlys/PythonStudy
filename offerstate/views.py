from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import OfferSkills
# Create your views here.

def skill_list(request):
    skill_list = OfferSkills.objects.using("mysql").all().values('skill_name').annotate(total=Count('skill_name')).order_by('-total')
    paginator = Paginator(skill_list, 20) # Show 20 contacts per page

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

def skill_relation(request, skillName):
    skill_list = OfferSkills.objects.using("mysql").all()
    return render(request, 'offerstate/skill_relation.html', {"list":skill_list})
