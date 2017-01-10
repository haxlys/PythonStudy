from django.shortcuts import render
from django.db.models import Count

from .models import OfferSkills
# Create your views here.

def skill_list(requeset, page):
    skill_list = OfferSkills.objects.using("mysql").all().values('skill_name').annotate(total=Count('skill_name')).order_by('-total')
    return render(requeset, 'offerstate/states_list.html', {"list":skill_list})
