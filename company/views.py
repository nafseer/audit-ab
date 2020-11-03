from django.shortcuts import render
# from client.models import ClientsMasterNew
from client.models import ClientsProfile,ClientsTeam,ClientsContact
from .models import CompanyList
# Create your views here.
from django.views.generic import ListView,CreateView,TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.detail import DetailView





# Create your views here.
class CompanysListView(TemplateView):

    model = CompanyList
    template_name = 'companylist.html'
    context_object_name = 'companylist'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CompanysListView, self).get_context_data(**kwargs)
        companylist = CompanyList.objects.all()
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print(companylist)
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        page = self.request.GET.get('page')
        # paginator = Paginator(users, self.paginate_by)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users= paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        context['companylist'] = companylist
        return context


class CompanyListCreateView(CreateView):
    model = CompanyList
    template_name = 'companycreate.html'
    fields = ('company_name',)
    success_url = reverse_lazy('companylist')
    context_object_name = 'companylist'

    def get_context_data(self,*args, **kwargs):
        context = super(CompanyListCreateView, self).get_context_data(**kwargs)
        i=context['form']
        print(context)
        print(i)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('company_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            

        )
        

        return context

class CompanysDetailsView(TemplateView):

    # model = ClientsMasterNew
    template_name = 'companydetails.html'
    context_object_name = 'clientslist'

    def get_context_data(self, **kwargs):
        context = super(CompanysDetailsView, self).get_context_data(**kwargs)
        # clientslist = ClientsProfile.objects.all()
        # print(clientslist)
        pk = self.kwargs['pk']
        companylist = CompanyList.objects.filter(id = pk).values()

        curr_comp = companylist[0]['company_name']
        clientslist = ClientsProfile.objects.filter(company_name = curr_comp)
        clientsteams = ClientsTeam.objects.filter(company_name = curr_comp)
        clientcontacts = ClientsContact.objects.filter(company_name = curr_comp)
        print('hhhhhh')
        print(pk)
        print(clientslist)
        print('hhhh')
        page = self.request.GET.get('page')
        # paginator = Paginator(users, self.paginate_by)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users= paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        context['clientslist'] = clientslist
        context['clientsteams'] = clientsteams 
        context['clientcontacts'] = clientcontacts 

        return context