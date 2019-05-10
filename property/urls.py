from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="property-index"),
    path('<int:id>', views.get_property_by_id, name="property_details"),
    path('create_property', views.create_property, name="create_property"),
    path('delete_property/<int:id>', views.delete_property, name="delete_property"),
    path('update_property/<int:id>', views.update_property, name="update_property"),
]
