from django.conf.urls import handler404, handler500, include, url


handler404 = 'selectable.tests.views.test_404'
handler500 = 'selectable.tests.views.test_500'

urlpatterns = [
    re_path(r'^selectable-tests/', include('selectable.urls')),
]
