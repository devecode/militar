from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from cartilla.models import Cartilla

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):

    login_url = "bases:login"
    raise_exception=False
    redirect_field_name="redirect_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class HomeView(SinPrivilegios, generic.ListView):
    model = Cartilla
    queryset = Cartilla.objects.latest('pk')
    context_object_name = "obj"
    template_name = 'bases/home.html'
    login_url='bases:login'
    permission_required="cartilla.view_cartilla"

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/sin_privilegios.html"