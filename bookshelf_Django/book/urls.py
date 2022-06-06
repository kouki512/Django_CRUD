from django.urls import path
from . import views
urlpatterns = [
    path('book/', views.ListBookView.as_view()) ,# ClassBasedViewsの呼び出し方

    path('book/<int:pk>/detail/', views.DetailBookView.as_view()) ,
]
