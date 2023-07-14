from django.urls import path

from services import views
from services.views import rezerva_servicii, selecteaza_data_ora, appointments_view

urlpatterns = [
    path('creare_serviciu/', views.ServiceCreateView.as_view(), name='creare-serviciu'),
    path('lista_servicii/', views.ServiceListView.as_view(), name='lista-servicii'),
    path('update_serviciu/<int:pk>', views.ServiceUpdateView.as_view(), name='update-serviciu'),
    path('sterge_serviciu/<int:pk>', views.ServiceDeleteView.as_view(), name='sterge-serviciu'),
    path('detalii_serviciu/<int:pk>', views.ServiceDetailView.as_view(), name='detalii-serviciu'),
    path('rezervare/', views.Rezervare.as_view(), name='rezervare'),
    path('rezervare/programare/', rezerva_servicii, name='rezervare-programare'),
    path('rezervare/selecteaza_data_ora/', selecteaza_data_ora, name='selecteaza-data-ora'),
    path('rezervare/programare/succes/', selecteaza_data_ora, name='rezervare-programare-succes'),
    path('programari/', appointments_view, name='programarile-mele')
]