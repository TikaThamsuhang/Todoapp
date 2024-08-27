from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home-page'),
    path("delete-task/<int:id>/",views.DeleteTask,name="delete"),
    path("update/<int:id>/", views.Update, name="update"), 
    path("edit-task/<int:id>/", views.EditTask, name="edit"),
]
