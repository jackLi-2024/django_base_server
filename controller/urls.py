"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from werkzeug.utils import import_string
from conf import route

urlpatterns = [

]

for route_one in route.url_settings:
    for k in route_one:
        urlpatterns.append(path(k, view=import_string("views.%s" % route_one[k]).as_view()))

urlpatterns.append(re_path(r"/*", view=import_string("views.error_view:ErrorView").as_view()))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
