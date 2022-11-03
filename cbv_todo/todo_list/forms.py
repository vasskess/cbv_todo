from django.forms import ModelForm

from cbv_todo.todo_list.models import Task


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
