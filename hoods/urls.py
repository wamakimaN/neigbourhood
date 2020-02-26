from hoods import views
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
  url(r'^signup/$',views.registration, name='signup'),
]