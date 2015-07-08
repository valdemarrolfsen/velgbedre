from django.conf.urls import url

from company_service import views

viewpatterns = [
	url(r'^company/frontpage', views.frontpage_view, name='frontpage'),
	url(r'^company/wishlist', views.wishlist_view, name='wishlist'),
	url(r'^company/intro', views.intro_view, name='intro'),
]

urlpatterns = viewpatterns