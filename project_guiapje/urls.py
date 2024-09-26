from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('project_guiapje.app_core.urls'), namespace='app_core')),
    path('', include(('project_guiapje.app_guiapje.urls'), namespace='app_guiapje')),
    path('', include(('project_guiapje.app_accounts.urls'), namespace='app_accounts')),
]

# if settings.DEBUG == True:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# if settings.DEBUG == False:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)