from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from rest_framework import routers
from apps.users.views import UsersViewSet
from apps.task.views import TaskViewSet


router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'task', TaskViewSet)

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('task/', include('apps.task.urls')),
]

urlpatterns = [
#    path('admin/', admin.site.urls),
   path('api/', include(api_urlpatterns)),
   path('api/', include(router.urls)),
   path('api/drf-auth/', include('rest_framework.urls')),
   path('',RedirectView.as_view(url='/api/')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
