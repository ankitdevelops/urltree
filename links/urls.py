from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home,name='home'),
    path('', views.dashboard, name='dashboard'),
    path('link_edit/<int:id>',views.link_edit,name='link_edit'),
    path('delete_link/<int:id>', views.delete_link, name='delete_link'),
    path('<str:username>/',views.user_link,name='user_link'),
    # path('change_image/', views.change_image, name='change_image'),
   
]