from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="seller-index"),
    path('update_seller/<int:id>', views.update_seller, name="update_seller"),
    path('<int:id>', views.get_seller_by_id, name="seller_details"),
]
