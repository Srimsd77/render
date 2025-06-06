from django.urls import path
from . import views
from . import collector_import


app_name = "collectors"

urlpatterns = [
    path("dashboard/", views.collector_dashboard_view, name="waste_collector_dashboard"),
    path("add/", views.collector_form_view, name="add"),
    path("create/", views.create_collector_view, name="create"),
    path("edit/<int:collector_id>/", views.edit_collector_view, name="edit"),
    path("update/<int:collector_id>/", views.update_collector_view, name="update"),

    # Collector Type 
    path("collector_type_form_add/", views.collector_type_form_add, name="collector_type_form_add"),
    path("assign_collector_type_ajax/", views.assign_collector_type_ajax, name="assign_collector_type_ajax"),


    # Import 
    path('waste_collector_import/', collector_import.waste_collector_import, name='waste_collector_import'),
    path('waste_collector_download_template/', collector_import.waste_collector_download_template, name='waste_collector_download_template'),
    path('delete/', views.delete_waste_collector, name='delete_waste_collector'),

    # Import and download template 
    path('download-template/', collector_import.download_template, name='download_template'),
    path('upload_excel', collector_import.upload_excel, name='upload_excel'),
    path('save_mapped_data', collector_import.save_mapped_data, name='save_mapped_data'),
    
]
