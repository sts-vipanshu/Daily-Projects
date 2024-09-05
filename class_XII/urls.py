from django.urls import path

from .views import *

urlpatterns = [
    path(route="", view=listView, name="listView"),
    path(route="create/", view=createView, name="createView"),
    path(route="update/<int:student_id>", view=updateView, name="updateView"),
    path(route="delete/<int:student_id>", view=deleteView, name="deleteView"),
]
