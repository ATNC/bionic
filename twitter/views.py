# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from models import Twit
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def index(request, page_number=1):
    args = {}
    args.update(csrf(request))
    if 'text' in request.REQUEST:
        t = Twit(text = request.REQUEST['text'])
        t.twit_from = auth.get_user(request).username
        t.twit_User = User.objects.get(username = auth.get_user(request).username) #TEST
        t.save()
    all_twits = Twit.objects.all()
    current_page = Paginator(all_twits, 5)
    #args['twits'] = Twit.objects.all()
    args['username'] = auth.get_user(request).username
    args['pagin'] = current_page.page(page_number)
    return render_to_response("twitter/index.html", args)

def twitfilter(request, cur_user):
    args = {}
    args['user'] = cur_user
    args['twits'] = Twit.objects.filter(twit_from=cur_user)
    #args['date'] = Twit.objects.get(twit_date)
    return render_to_response('twitter/all.html', args)


# Create your views here.
