#urls.py
from django.urls import path  
from .import views  
urlpatterns = [  
    path('', views.index),  
    path('addnew',views.addnew),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  

    path('responsive', views.responsive),  

]  