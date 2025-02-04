from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BasicNoteViewSet, GenericNoteViewSet, ModelNoteViewSet

router = DefaultRouter()
router.register(r'basic-notes', BasicNoteViewSet, basename='basicnote')
router.register(r'generic-notes', GenericNoteViewSet, basename='genericnote')
router.register(r'model-notes', ModelNoteViewSet, basename='modelnote')

urlpatterns = [
    path('', include(router.urls)),
]