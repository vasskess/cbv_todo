from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as view
from django.views.decorators.cache import never_cache

from cbv_todo.todo_list.forms import TaskCreateForm
from cbv_todo.todo_list.models import Task


# THIS WORKS, BUT DON`T DO IT - OK ?   o_0
# class IndexListView(view.View):
#     form_class = TaskCreateForm
#     # context_object_name = "tasks"
#     model = Task.objects.all()
#     # template_name = "html_todo.html"
#     # extra_context = {"form": TaskCreateForm}
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, template_name="html_todo.html", context={"form": form, "tasks": self.model})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#
#         return render(request, template_name="html_todo.html", context={"form": form, "tasks": self.model})


class CreateTaskView(view.CreateView):
    template_name = 'html_todo.html'
    model = Task
    fields = '__all__'
    success_url = '/'


class TasksListView(view.ListView):
    context_object_name = "tasks"
    model = Task
    template_name = "html_view.html"


class TaskUpdateView(view.UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'html_update.html'
    success_url = reverse_lazy('view-tasks')


class TaskDeleteView(view.DeleteView):
    model = Task
    fields = '__all__'
    template_name = 'html_delete.html'
    success_url = reverse_lazy('view-tasks')


# @method_decorator(login_required, name='dispatch')  --- > Read bout that shit !
class TaskDetailsView(view.DetailView):
    context_object_name = "task"
    model = Task
    fields = "__all__"
    template_name = 'html_view_task.html'
    success_url = reverse_lazy('view-tasks')
