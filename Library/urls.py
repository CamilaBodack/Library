"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from bravo_library import views
from bravo_library.views import (ClientViewSet, BookViewSet)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r"client", ClientViewSet)
router.register(r"books", BookViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Bravo Library API",
        default_version='v1',
        description="Wellcome to Bravo Library API",
        terms_of_service="",
        contact=openapi.Contact(email="camila.bodack@gmail.com"),
        license=openapi.License(name="Bravo Library"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('books/<int:pk>/reserve/', views.BookViewSet.reserve, name="reserve"),
    path('client/<int:pk>/books/', views.ClientViewSet.book_tax, name="book_tax"),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),
]
