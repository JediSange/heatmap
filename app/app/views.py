from app.models import PlayerDeath
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def map(request):
  events = PlayerDeath.objects;
  params = {}
  params['events'] = events
  return render_to_response('map.html', params)

def api(request, **data):
  event = PlayerDeath()
  html = '<h2>Successfully saved event</h2>'
  for key in data:
    setattr(event, key, data[key])
    html += key + ': ' + data[key] + '<br/>'

  event.save()
  return HttpResponse(html)
  