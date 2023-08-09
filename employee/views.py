from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from employee.forms import EmployeeForm, EmployeeUpdateForm
from employee.models import Employee


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'employee/create_employee.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('homepage')
    permission_required = 'employee.add_employee'


class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'employee/list_of_employees.html'
    model = Employee
    context_object_name = 'all_employees'
    permission_required = 'employee.view_list_of_employees'

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'employee/update_employee.html'
    model = Employee
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('lista-angajati')
    permission_required = 'employee.change_employee'


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'employee/delete_employee.html'
    model = Employee
    success_url = reverse_lazy('lista-angajati')
    permission_required = 'employee.delete_employee'


class EmployeeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'employee/details_employee.html'
    model = Employee
    success_url = reverse_lazy('lista-angajati')
    permission_required = 'employee.view_employee'




