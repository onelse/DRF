from django.contrib import admin
from django.urls import path, include
from storage import urls
# �α����� ���ؼ�
from rest_framework import urls
# media static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('storage.urls')),
	# api �α���
	path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)