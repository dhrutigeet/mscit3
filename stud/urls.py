from django.conf.urls import url
from. import views
urlpatterns = [
   
	#url(r'^$',views.index,name='index'),
	url(r'^$',views.list,name='list'),
	url(r'^about/',views.about),
	url(r'^contact/',views.contact),
	url(r'^courses/',views.courses),
	url(r'^insert/',views.insert),
	url(r'^delete/',views.delete),
	url(r'^event/',views.upload_pic),
	url(r'^login/',views.login),
	url(r'^chklogin/',views.chklogin),
	url(r'^disp/',views.disp),
]