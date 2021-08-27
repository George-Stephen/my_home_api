from django.conf.urls  import url
from django.contrib import admin
from .views import filter_apartments,apartments_list,single_apartment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/apartments/$',filter_apartments.as_view()),
    url(r'^api/apartment/(?P<pk>[0-9]+)/$',single_apartment.as_view()),
    url(r'^api/apartment/new/$',apartments_list.as_view()),
]