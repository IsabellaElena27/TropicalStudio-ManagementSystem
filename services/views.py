from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView

import employee
from employee.models import Employee
from services.forms import ServiceForm, ServiceUpdateForm, SelectareDataOraForm
from services.models import Service, RezervareServicii


class ServiceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'services/create_service.html'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('homepage')
    permission_required = 'services.add_service'


class ServiceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'services/list_of_services.html'
    model = Service
    context_object_name = 'all_services'
    permission_required = 'services.view_list_of_services'

    def get_queryset(self):
        return Service.objects.all()


class ServiceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'services/update_service.html'
    model = Service
    form_class = ServiceUpdateForm
    success_url = reverse_lazy('lista-servicii')
    permission_required = 'services.change_service'


class ServiceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'services/delete_service.html'
    model = Service
    success_url = reverse_lazy('lista-servicii')
    permission_required = 'services.delete_service'


class ServiceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'services/details_service.html'
    model = Service
    success_url = reverse_lazy('lista-servicii')
    permission_required = 'services.view_service'


class Rezervare(ListView):
    template_name = 'services/rezervare.html'
    model = Service
    context_object_name = 'all_services'
    success_url = reverse_lazy('homepage')


def rezervare(request):
    all_services = Service.objects.all()
    return render(request, 'services/rezervare.html', {'all_services': all_services})


def rezerva_servicii(request):
    if request.POST and request.user.is_authenticated:
        current_user_id = request.user.id
        services_ids = [int(item) for item in dict(request.POST) if
                        item != 'csrfmiddlewaretoken' and item != 'data_ora']
        date = request.POST.get('data_ora')
        for service_id in services_ids:
            service = Service.objects.get(id=service_id)
            serviciu = RezervareServicii(
                id_service=service,
                id_user=current_user_id,
                date=date
            )
            serviciu.save()
        all_employees = Employee.objects.all()
        return render(request, 'services/rezervare_programare.html', {'employees': all_employees})
    return HttpResponseRedirect(reverse("login"))


class RezervareProgramareView(CreateView):
    template_name = 'services/rezervare_programare.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context



# def selecteaza_data_ora(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("login"))
#
#     if request.POST:
#         form = SelectareDataOraForm(request.POST)
#         if form.is_valid():
#             date = form.cleaned_data.get('data_ora')
#             selected_services = RezervareServicii.objects.filter(id_user=request.user.id, status='draft')
#             for service in selected_services:
#                 service.date = date
#                 service.status = 'completed'
#                 service.save()
#         return render(request, 'services/rezervare_programare_succes.html', {'form': form})
#     else:
#         all_employees = Employee.objects.all()
#         return render(request, 'services/rezervare_programare.html', {'employees': all_employees})



from django.shortcuts import redirect

def selecteaza_data_ora(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.POST:
        form = SelectareDataOraForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('data_ora')
            selected_services = RezervareServicii.objects.filter(id_user=request.user.id, status='draft')
            for service in selected_services:
                service.date = date
                service.status = 'completed'
                service.save()

            if selected_services:
                service = selected_services[0].id_service
                employee = service.employee
                return render(request, 'services/rezervare_programare_succes.html',
                              {'form': form, 'date': date, 'service': service, 'employee': employee})
            else:
                return redirect('rezervare')

    else:
        all_employees = Employee.objects.all()
        return render(request, 'services/rezervare_programare.html', {'employees': all_employees})





def appointments_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    programari = RezervareServicii.objects.filter(id_user=request.user.id).select_related('id_service', 'id_service__employee')
    return render(request, 'services/appointments.html', {'programari': programari})
