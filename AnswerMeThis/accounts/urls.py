from django.conf.urls import url
from . import views
import django.contrib.auth.views as auth_views

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^user/(?P<username>\w+)/(?P<question>\w+)/(?P<oneortwo>\w+)', views.get_question, name='2get_question'),
    url(r'^user/(?P<username>\w+)/(?P<question>\w+)', views.get_question, name='get_question'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {"next_page":".."}),



]
