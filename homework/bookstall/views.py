from django.views.generic.list import ListView
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from el_pagination.views import AjaxListView


# import json
# from django.http import HttpResponseBadRequest, HttpResponse
# from braces.views import JSONResponseMixin, AjaxResponseMixin


class FrontPage(TemplateView):
    template_name = "front.html"


class SignUp(CreateView):
    template_name = 'sign_up.html'
    form_class = UserCreateForm
    success_url = '/store/'

    # def form_valid(self, form):
    #     return super(SignUp, self).form_valid(form)


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


@method_decorator(login_required, name='dispatch')
class Store(AjaxListView):
    model = Book
    template_name = 'store.html'
    page_template = 'store_page.html'

    def get_context_data(self, **kwargs):
        context = super(Store, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        if self.request.GET.get('stock') is not None:
            return Book.objects.filter(count__gt=0)
        else:
            return Book.objects.all()


class BookView(TemplateView):
    template_name = "book.html"
    form_class = Order

    def get(self, request, *args, **kwargs):
        id = int(args[0])
        form = self.form_class()
        form.fields['book_id'].initial = id
        return render(request, self.template_name, {'book': Book.objects.get(id=id),
                                                    'form': form})


class AddBook(CreateView):
    template_name = "add_book.html"
    form_class = BookForm
    success_url = '/store/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('{0}id{1}'.format(self.success_url, obj.id))
        return render(request, self.template_name, {'form': form,
                                                    'author_form': AuthorForm()})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class(),
                                                    'author_form': AuthorForm()})


@csrf_exempt
def add_author(request):
    form = AuthorForm(data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse(status=201)
    return HttpResponse(status=400)


@csrf_exempt
def order(request):
    user = request.user
    order = Order(data=request.POST)
    if order.is_valid():
        id = int(order.data['book_id'])
        book = Book.objects.get(id=id)
        book.order.add(user)
        return HttpResponse(status=201)
    return HttpResponse(status=400)


def logout_view(request):
    logout(request)
    request.session.clear()
    return redirect('front')
