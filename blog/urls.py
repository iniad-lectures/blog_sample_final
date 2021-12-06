from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('hello', views.hello, name='hello'),
	path('redirect', views.redirect_test, name='redirect_test'),
	path('<int:article_id>/', views.detail, name='detail'),
	path('<int:article_id>/delete', views.delete, name='delete'),
	path('<int:article_id>/update', views.update, name='update'),
	path('<int:article_id>/like', views.like, name='like'),
	path('api/articles/<int:article_id>/like', views.api_like),
]