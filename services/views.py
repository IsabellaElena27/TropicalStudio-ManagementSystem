from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

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


class Rezervare(ListView):  # afiseaza o lista de obiecte dintr-un model specific
    template_name = 'services/rezervare.html'  # specifică șablonul HTML care va fi folosit pentru a afișa rezultatele.
    model = Service  # Specifică modelul pe care îl va utiliza vizualizarea pentru a obține datele.
    context_object_name = 'all_services'  # Definește numele sub care obiectele din modelul specificat vor fi disponibile în contextul șablonului.
    success_url = reverse_lazy(
        'homepage')  # Specifică URL-ul la care utilizatorul va fi redirecționat după ce a făcut cu succes o rezervare.


def rezervare(request):
    '''
    Primește un obiect request, care conține datele cererii HTTP. Funcția obține toate serviciile din baza de date și
    le afișează utilizând șablonul 'services/rezervare.html'.
    '''
    all_services = Service.objects.all()
    return render(request, 'services/rezervare.html', {'all_services': all_services})


def rezerva_servicii(request):
    if request.POST and request.user.is_authenticated:  # verificam daca cererea este de tip POST ai utilizatorul este autentificat
        current_user_id = request.user.id  # preluam id-ul userului autentificat
        services_ids = [int(item) for item in dict(request.POST) if
                        item != 'csrfmiddlewaretoken' and item != 'data_ora']  # obtinem id-urile serviciilor selectate
        date = request.POST.get('data_ora')
        for service_id in services_ids:  # parcurgem id-urile serviciilor selectate
            service = Service.objects.get(
                id=service_id)  # obținem obiectele Service asociate din baza de date folosind interogări către modelul Service
            ''' pentru fiecare id de serviciu, se creează un obiect RezervareServicii cu informațiile despre serviciu,
             utilizatorul curent și data rezervării. Acest obiect este apoi salvat în baza de date.
            '''
            serviciu = RezervareServicii(
                id_service=service,
                id_user=current_user_id,
                date=date
            )
            serviciu.save()
        return render(request, 'services/rezervare_programare.html')
    return HttpResponseRedirect(reverse("login"))


class RezervareProgramareView(CreateView):
    template_name = 'services/rezervare_programare.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['employees'] = Employee.objects.all()
    #     return context
    #


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


def selecteaza_data_ora(request):
    if not request.user.is_authenticated:  # daca userul nu este autentificat, il redirectionam pe login
        return HttpResponseRedirect(reverse("login"))

    if request.POST:  # daca cererea este de tip POST se obtin datele din formular
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

    programari = RezervareServicii.objects.filter(id_user=request.user.id).select_related('id_service',
                                                                                          'id_service__employee')
    return render(request, 'services/appointments.html', {'programari': programari})
