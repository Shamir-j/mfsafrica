from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from pages.views import home_view, contact_view, about_view
from django.views.generic import TemplateView


# Swagger documentation setup
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_api.urls')),
#     path('', home_view, name='home'),
#     path('about/', about_view),
#     path('contact/', contact_view),
#     path('store/', include('store.urls')),
#     url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_api.urls')),
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('store/', include('store.urls')),
    path('openapi/', get_schema_view(
        title="School Service",
        description="API developers hpoing to use our service"
        ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        # template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),
]
