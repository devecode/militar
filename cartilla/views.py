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
    report = generarPDF(pk)
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                        pagesize=A6,
                        rightMargin=40,
                        leftMargin=40,
                        topMargin=30,
                        bottomMargin=18,
                        )
    doc.build(report)
    response.write(buff.getvalue())
    buff.close()
    return response

def texto(texto, tamanio):
    styles = getSampleStyleSheet()
    style = 'Heading{}'.format(tamanio)
    return Paragraph(texto, styles[style])


def generarPDF(pk):


    body = ParagraphStyle('parrafos',
                           fontSize = 9,
                           fontName="Times-Roman",
                           leftIndent=36,
                           spaceAfter = 1,
                           spaceBefore = 0
                           )
    clase = ParagraphStyle('parrafos',
                            alignment = TA_CENTER,
                           fontSize = 9,
                           fontName="Times-Roman",
                           spaceAfter = 0
                           )



    info = []
   

    cartilla = Cartilla.objects.filter(id=pk)

    for c in cartilla:
        info.append(Paragraph("{}".format(c.clase),clase))
        info.append(Paragraph("{}".format(c.nombre),body))
        info.append(Paragraph("{}".format(c.fecha_nacimiento),body))
        info.append(Paragraph("{}".format(c.nacio),body))
        info.append(Paragraph("{}".format(c.papa),body))
        info.append(Paragraph("{}".format(c.mama),body))
        info.append(Paragraph("{}".format(c.estado),body))
        info.append(Paragraph("{}".format(c.ocupacion),body))
        info.append(Paragraph("{}".format(c.leer_escribir),body))
        info.append(Paragraph("{}".format(c.curp),body))
        info.append(Paragraph("{}".format(c.grado_maximo),body))
        info.append(Paragraph("{}".format(c.domicilio),body))
        info.append(Paragraph("{}".format(c.presidente),body))
        info.append(Paragraph("{}".format(c.lugar),body))
        info.append(Paragraph("{}".format(c.fecha),body))

    return info