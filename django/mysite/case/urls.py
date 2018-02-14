from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.case_title, name="case_title")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
