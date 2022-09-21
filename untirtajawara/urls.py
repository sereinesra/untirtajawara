from django.contrib import admin
from django.urls import path
from fkip.views import index
from faperta.views import indexfaperta
from feb.views import indexfeb
from fh.views import indexfh
from fisip.views import indexfisip
from pascasarjana.views import indexpascasarjana
from ft.views import indexft
from fk.views import indexfk
from profil.views import indexprofil
from about.views import indexabout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', index),
    path('faperta/', indexfaperta),
    path('feb/', indexfeb),
    path('fh/', indexfh),
    path('fisip/', indexfisip),
    path('pascasarjana/', indexpascasarjana),
    path('ft/', indexft),
    path('fk/', indexfk),
    path('profil/', indexprofil),
    path('about/', indexabout),



]
