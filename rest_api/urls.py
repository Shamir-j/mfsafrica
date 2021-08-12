from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PointAPIView, PointDetailAPIView, PointViewSet
from rest_framework.routers import DefaultRouter
from .views import loginPage,register

router = DefaultRouter()
router.register('point/v1', PointViewSet, basename='point')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('points/', PointAPIView.as_view()),
    path('pointdetail/<int:pk>/', PointDetailAPIView.as_view()),
    # path('login/', loginPage, name="login"),
    # path('register/', register, name="sign_up"),
]

