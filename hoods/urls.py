from hoods import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
  url(r'^logout/$', auth_views.logout, {"next_page": '/'}, name='logout'),
  url(r'^$', views.home_page, name='home'),
  url(r'^profile/$',views.profile, name='profile'),
  url(r'^hood/(?P<pk>[\d]+)/$',views.PostHood.as_view(),name='myhood'),
  url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  url(r'^signup/$',views.registration, name='signup'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)