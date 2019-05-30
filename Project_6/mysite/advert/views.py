from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from advert.models import Advert


# Create your views here.
class AdvertList(ListView):
    template_name = 'advert/advert_list.html'
    context_object_name = 'adverts'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Advert.objects.all()
        else:
            return Advert.objects.filter(is_public=True)


class AdvertCreate(LoginRequiredMixin, CreateView):
    template_name = 'advert/advert_create.html'
    model = Advert
    fields = ('name', 'content','is_public')

    def form_valid(self, form):
        advert = form.save(commit=False)
        advert.user = self.request.user
        advert.save()
        return super(AdvertCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('adverts:view')


class AdvertUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'advert/advert_create.html'
    model = Advert
    fields = ('name', 'content')

    def dispatch(self, request, *args, **kwargs):
        advert = get_object_or_404(Advert, pk=kwargs.get('pk'))
        if advert.user == request.user:
            return super(AdvertUpdate, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()

    def get_success_url(self):
        return reverse_lazy('adverts:view')


class AdvertDelete(LoginRequiredMixin, DeleteView):
    template_name = 'advert/advert_delete.html'
    model = Advert
    success_url = reverse_lazy('adverts:view')

    def dispatch(self, request, *args, **kwargs):
        advert = get_object_or_404(Advert, pk=kwargs.get('pk'))
        if advert.user == request.user:
            return super(AdvertDelete, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()
