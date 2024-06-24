from django.urls import path
from . import views
from .feeds import LatestPostsFeed
from django.conf import settings
from django.conf.urls.static import static

#define an application namespace with the app_name variable. This allows you to organize URLs by application and use the name when referring to them.
app_name = 'blog'

urlpatterns = [
    #post views
    # path('', views.PostListView.as_view(), name='post_list'),  
    path('', views.post_list, name='post_list'), 
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/',views.post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)