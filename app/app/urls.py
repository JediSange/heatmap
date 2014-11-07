from django.conf.urls import patterns, include, url

api_url = 'api/'
api_url += r'(?P<player_id>[0-9]+)/'
api_url += r'(?P<source_player_id>[0-9]+)/'
api_url += r'(?P<weapon_id>[0-9]+)/'
api_url += r'(?P<pos_x>\d+\.\d+)/'
api_url += r'(?P<pos_y>\d+\.\d+)'
api_url += r'$'

urlpatterns = patterns('',
  url(r'^$', 'app.views.map', name='map'),
  url(api_url, 'app.views.api', name='api'),
)
