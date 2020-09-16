from  django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('skills/',views.skills,name="skills"),
    path('certi/',views.certi,name="certi"),
    path('projects/',views.projects,name="projects"),
    path('contact/',views.contact,name="contact"),
    path('contact',views.contact,name="contact")

]
