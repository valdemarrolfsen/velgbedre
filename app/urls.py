from django.conf.urls import url

from app import views

viewpatterns = [
	url(r'^$', views.frontpage_view, name='frontpage'),
	url(r'^about/', views.about_view, name='about'),
	url(r'^contact/', views.contact_view, name='contact'),
	url(r'^packages/', views.package_view, name='packages'),
	url(r'^product/(?P<pId>\d+)/$', views.product_view, name='product'),
]

urlpatterns = viewpatterns