from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="index"),
    path('addtask/',views.addtask,name="addtask"),
    path('addtolist/',views.addtolist,name="addtolist"),
    path('updpage/<int:id>/',views.updpage,name="updpage"),
    path('updatelist/<int:id>/',views.updatelist,name="updatelist"),
    path('dellist/<int:id>/',views.dellist,name="dellist")

]