from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^', views.index,name='index'),
    url(r'^view/(?P<book_id>\d+)$',views.view,name='view')
]