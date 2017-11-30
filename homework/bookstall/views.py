from django.views.generic.list import ListView
from django.utils import timezone
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.base import TemplateView


class FrontPage(TemplateView):

    template_name = "front.html"

    def get_context_data(self, **kwargs):
        context = super(FrontPage, self).get_context_data(**kwargs)
        return context


class SignUp(FormView):
    template_name = 'sign_up.html'
    form_class = UserCreateForm
    success_url = '/store/'

    def form_valid(self, form):
        return super(SignUp, self).form_valid(form)


class LogIn(FormView):

    template_name = 'log_in.html'
    form_class = AuthenticateForm
    success_url = '/store/'

    def post(self, request, *args, **kwargs):
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return super(LogIn, self).form_valid(form)


class Store(ListView):

    model = Book
    template_name = 'store.html'
    paginate_by = 6

    # @login_required
    def get(self, request):
        return super(Store, self).get(self, request)

    def get_context_data(self, **kwargs):
        context = super(Store, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BookView(TemplateView):

    template_name = "book.html"

    def get(self, request, id):
        return render(request, self.template_name, {'book': Book.objects.get(id=id)})


@login_required
def logout_view(request):
    logout(request)
    request.session.clear()
    return redirect('front')