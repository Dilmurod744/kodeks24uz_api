from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi, views
from rest_framework import permissions, routers

schema_view = views.get_schema_view(
	openapi.Info(
		title="Kodeks24 API",
		default_version='v1',
		description="Test description",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="contact@snippets.local"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),

	path('', include(router.urls)),

	re_path(r'^accounts/', include('accounts.urls')),
	# re_path(r'^orders/', include('orders.urls')),
	path('', include('products.urls')),

	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
