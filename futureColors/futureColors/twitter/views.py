# coding: utf-8

from django.shortcuts import render_to_response, redirect
from futureColors.twitter.models import timeline
from django.template import RequestContext



def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
    
def getStatuses(request):
    if 'screen_name' in request.GET:
        
        t = [
             [
              {'text' : 'hi!'}, [[{'text' : 'reply1'}], [{'text' : 'reply2'}] ]
              ],
             ]
        t = timeline(request.GET['screen_name'])
        return render_to_response('statuses.html', {'t' : t.timeline}, context_instance=RequestContext(request))
    return redirect('http://futurecolors.ru')



