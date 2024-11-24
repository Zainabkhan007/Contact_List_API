from django.urls import path
from . import views


urlpatterns = [

      path("view/",views.Contact_View.as_view(),name='view'),
      path('<int:id>/', views.Contact_Detail.as_view(),name='detail'),
      

]