from django.shortcuts import render,redirect
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages

from django.contrib.auth import authenticate

from bases.views import SinPrivilegios

from .models import Cartilla
from .forms import CartillaForm

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A6, inch, elevenSeventeen
from reportlab.platypus import Table
from io import BytesIO
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

from militar import settings

class VistaBaseCreate(SuccessMessageMixin,SinPrivilegios, \
    generic.CreateView):
    context_object_name = 'obj'
    success_message="Registro Agregado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CartillaView(SinPrivilegios, generic.ListView):
    model = Cartilla
    template_name = "cartilla/cartilla_list.html"
    context_object_name = "obj"
    permission_required="cartilla.view_cartilla"

class CartillaNew(VistaBaseCreate):
    model=Cartilla
    template_name="cartilla/cartilla_form.html"
    form_class=CartillaForm
    success_url= reverse_lazy("cartilla:cartilla_list")
    permission_required="cartilla.add_cartilla"

class CartillaEdit(SuccessMessageMixin,SinPrivilegios,\
                   generic.UpdateView):
    model=Cartilla
    template_name="cartilla/cartilla_form.html"
    context_object_name = 'obj'
    form_class=CartillaForm
    success_url= reverse_lazy("cartilla:cartilla_list")
    success_message="Cartilla Editada"
    permission_required="cartilla.change_cartilla"

class CartillaDelete(SinPrivilegios, generic.DeleteView):
    permission_required = "cartilla.delete_cartilla"
    model = Cartilla
    template_name = "cartilla/cartilla_del.html"
    context_object_name = 'obj'
    success_url= reverse_lazy("cartilla:cartilla_list")
    success_message="Cartilla Borrada"

def reporte(request,pk):
    response = HttpResponse(content_type='application/pdf')
    cartilla = Cartilla.objects.get(pk=pk)

    canva = canvas.Canvas(response, pagesize=A6)
    canva.setFont("Times-Roman", 9)
    canva.drawString(158, 355, "" + str(cartilla.clase))
    canva.drawString(65.7, 342.7, "" + cartilla.nombre)
    canva.drawString(139.2, 331, "" + str(cartilla.fecha_nacimiento))
    canva.drawString(78.6, 318, "" + cartilla.nacio)
    canva.drawString(71.7, 305.5, "" + cartilla.papa)
    canva.drawString(55, 293.2, "" + cartilla.mama)
    canva.drawString(99.6, 280.6, "" + cartilla.estado)
    canva.drawString(81.3, 267.8, "" + cartilla.ocupacion)
    canva.drawString(150.3, 254.8, "" + cartilla.leer_escribir)
    canva.drawString(191, 254.8, "" + cartilla.curp)
    canva.drawString(170.7, 243.2, "" + cartilla.grado_maximo)
    canva.drawString(84.2, 230.9, "" + cartilla.domicilio)
    canva.drawString(19.7, 137.2, "" + cartilla.presidente)
    canva.drawString(42.2, 119.3, "" + cartilla.lugar)
    canva.drawString(201.9, 119.3, "" + str(cartilla.fecha))
    canva.save()

    return response