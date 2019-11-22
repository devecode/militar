from django.urls import path, include
from cartilla import views as vistas

from .views import CartillaView, CartillaNew, CartillaEdit, CartillaDelete

urlpatterns = [
    path('cartillas/',CartillaView.as_view(), name="cartilla_list"),
    path('cartillas/new',CartillaNew.as_view(), name="cartilla_new"),
    path('cartillas/edit/<int:pk>',CartillaEdit.as_view(), name="cartilla_edit"),
    path('cartillas/delete/<int:pk>', CartillaDelete.as_view(), name='cartilla_delete'),

    path('reporte/<int:pk>', vistas.reporte, name='reporte')

]