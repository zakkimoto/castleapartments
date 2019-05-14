from django.urls import path
from . import views
#from buyer.views import payment_review, payment_property, buy_property



urlpatterns = [
    path('', views.index, name="property-index"),
    path('<int:id>', views.get_property_by_id, name="property_details"),
    path('create_property', views.create_property, name="create_property"),
    path('delete_property/<int:id>', views.delete_property, name="delete_property"),
    path('update_property/<int:id>', views.update_property, name="update_property"),
    path('buy_property/<int:id>', views.buy_property, name="buy_property"),
    path('payment_property/<int:id>', views.payment_property, name="payment_property"),
    path('payment_review', views.payment_review, name="payment_review")
]
