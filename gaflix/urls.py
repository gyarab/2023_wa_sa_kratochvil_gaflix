from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="filmy/home.html")),
    path('druhy/', TemplateView.as_view(template_name="filmy/druhy.html")),
    path('set_language/', set_language, name='set_language'),
)
