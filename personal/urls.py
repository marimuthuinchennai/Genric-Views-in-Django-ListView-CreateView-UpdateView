#from django.conf.urls import url,include
from django.urls import path
from . import views
from .views import EmployeeListView,CreateView,EmpUpdateView
urlpatterns = [
    #path('', views.index,name='index'),
    path('', EmployeeListView.as_view(), name='article-list'),
    path('create/', CreateView.as_view(), name='create-list'),
    path('update/<int:id>/', EmpUpdateView.as_view(), name='update-list'),
    path('page1/', views.page1,name='index'),
    path('page2/', views.page2,name='index'),
    path('post_new/', views.post_new,name='posted'),
    path('page1/', views.page1,name='index'),
    path('page2/', views.page2,name='index'),
    path('post_new/', views.post_new,name='posted')
]
