from django.urls import path

from employee import views

urlpatterns = [
    path('creare_angajat/', views.EmployeeCreateView.as_view(), name='creare-angajat'),
    path('lista_angajati/', views.EmployeeListView.as_view(), name='lista-angajati'),
    path('update_angajat/<int:pk>', views.EmployeeUpdateView.as_view(), name='update-angajat'),
    path('stergere_angajat/<int:pk>', views.EmployeeDeleteView.as_view(), name='stergere-angajat'),
    path('detalii_angajat/<int:pk>', views.EmployeeDetailView.as_view(), name='detalii-angajat')
]