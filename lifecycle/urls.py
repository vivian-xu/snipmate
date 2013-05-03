from django.conf.urls import patterns, url  # include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# url(r'^admin/', include(admin.site.urls)),
urlpatterns = patterns('',
                       url(r'^$', 'views.home', name='home'),
                       )
