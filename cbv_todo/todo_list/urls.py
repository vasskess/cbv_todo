from django.urls import path

from cbv_todo.todo_list.views import *

urlpatterns = (
    path("", CreateTaskView.as_view(), name="show-index"),
    path("tasks/view/", TasksListView.as_view(), name="view-tasks"),
    path("tasks/update/<int:pk>", TaskUpdateView.as_view(), name="update-task"),
    path("tasks/delete/<int:pk>", TaskDeleteView.as_view(), name="delete-task"),
    path("task/details/<int:pk>", TaskDetailsView.as_view(), name="details-task"),
)
