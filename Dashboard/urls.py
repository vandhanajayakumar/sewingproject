from django.urls import path
from . import views

# urlpatterns = [
#     path('machinedata/', views.MachineDataListCreate.as_view()),
#     path('machinedata/<int:pk>/', views.MachineDataRetrieveUpdateDestroy.as_view()),
# ]



urlpatterns = [
    path('machinedata/', views.machine_data_list_create),
    path('machinedata/<int:pk>/', views.machine_data_detail),
]

