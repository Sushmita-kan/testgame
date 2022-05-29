from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
path('',views.home,name='home'),
path('base/',views.base,name='base'),
path('UserLogin/',views.UserLogin,name='UserLogin'),
path('UserRegisteration/',views.UserRegisteration,name='UserRegisteration'),
path('Logout/',views.Logout,name='Logout'),
path('WordScrabble/',views.WordScrabble,name = 'WordScrabble'),
path('ScrabbleWords/',views.ScrabbleWords,name = 'ScrabbleWords'),
path('start/',views.generate_random_view,name='random'),
path('game/',views.scramble_game_view,name='game'),
path('game_result_a/',views.scramble_game_result_view,name='game_result_a'),

path('challengetab/',views.challengetab_view,name='challengetab'),
path('givechallenge/',views.givechallenge_view,name='randomchallenge'),
path('givechallengesubmit/',views.givechallenge_view,name='randomchallengesubmit'),
path('takechallenge/',views.takechallenge_view,name='takechallenge'),
path('viewscores/',views.viewscore_view,name='viewscore'),
path('<int:tid>',views.playchallenge_view,name='playchallenge'),
path('challengecheck/',views.challengecheck_view,name='challengecheck'),

url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)