from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from frontpage.views import sendmail

#this is for django 1.6 - remove for 1.7:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addition_interiors_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')), #grappelli urls
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^$', include('frontpage.urls', namespace='frontpage')),

    # Form URLs
    url(r'^email/send/$', sendmail),
    url(r'^email/thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
    url(r'^email/$', TemplateView.as_view(template_name='email.html'), name='email'),
) 

#SERVE STATIC FILES::NOT RECOMMENDED!
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


#FOR DJANGO-DEBUG-TOOLBAR
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),   
    )
