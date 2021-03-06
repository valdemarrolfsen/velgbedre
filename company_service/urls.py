from django.conf.urls import url

from company_service import views

viewpatterns = [
	url(r'^company/frontpage', views.frontpage_view, name='company_frontpage'),
	url(r'^company/wishlist', views.wishlist_view, name='wishlist'),
	url(r'^company/intro/(?P<code>\w+)/$', views.intro_view, name='intro'),
	url(r'^gavekort/', views.giftcard_view, name='giftcard'),
	url(r'^login', views.login_view, name='login'),

]

urlpatterns = viewpatterns