from django.urls import path
from .views import *

# 패스랑 뷰를 임포트 한다.
urlpatterns = [
    path('', BookmarkList.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('_update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]