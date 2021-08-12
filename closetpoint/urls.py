from rest_api.views import loginPage, register,logout_view
from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from pages.views import home_view, contact_view, about_view, login_view, points_view, register_view
from django.views.generic import TemplateView 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="CLOSET POINT PAIR API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="gideonochiengokwach@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_api.urls')),
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('login/', loginPage, name="login"),
    path('register/', register, name="sign_up"),
    path('points/', points_view, name="points"),
    path('logout/',logout_view, name="logout"),
    path('store/', include('store.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('apiv2/', include('accounts.urls')),
    # path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),




    path('documentation/', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

]
