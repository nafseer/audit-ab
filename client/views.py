from django.shortcuts import render
from .models import ClientsProfile,ClientsTeam,ClientsContact
from company.models import CompanyList
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
class ClientsListView(TemplateView):

    model = ClientsProfile
    template_name = 'clients.html'
    context_object_name = 'clientslist'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ClientsListView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        clientslist = ClientsProfile.objects.filter(company_name = pk)
        print('hhhhhh')
        print(pk)
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
        return context


class ClientsProfileListCreateView(CreateView):
    model = ClientsProfile
    template_name = 'clientsprofilecreate.html'
    fields = ('company_name','client_company','client_cin','client_address','client_doi')
    success_url = reverse_lazy('companylist')
    context_object_name = 'clientslist'

    def get_context_data(self,*args, **kwargs):
        context = super(ClientsProfileListCreateView, self).get_context_data(**kwargs)
        # i=context['form']
        # print(context)
        # print(i)


        s=context['form']
        # print(f.fields)
        pk = self.kwargs['pk']
        devices = CompanyList.objects.filter(pk=pk)
        s.fields['company_name'].queryset = devices
        a=CompanyList.objects.get(id=pk)
        # print(t.id)
        s.fields['company_name'].initial = a
        context['form']=s
        # print(context['form'].fields['lead_id'].initial)
        context['test'] = 'dkjghrke'
        # print(context, 'piiiiiiiiiiiiiiiiiiiiiiiii')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('company_new', css_class='form-group col-md-6 mb-0'),
                Column('client_company', css_class='form-group col-md-6 mb-0'),
                Column('client_cin', css_class='form-group col-md-6 mb-0'),
                Column('client_address', css_class='form-group col-md-6 mb-0'),
                Column('client_doi', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            

        )
        
        return context

class ClientsTeamListCreateView(CreateView):
    model = ClientsTeam
    template_name = 'clientsteamcreate.html'
    fields = ('company_name','client_teamname','client_designation','client_role',)
    success_url = reverse_lazy('companylist')
    context_object_name = 'clientsteamlist'

    def get_context_data(self,*args, **kwargs):
        context = super(ClientsTeamListCreateView, self).get_context_data(**kwargs)
        s=context['form']
        # print(f.fields)
        pk = self.kwargs['pk']
        devices = CompanyList.objects.filter(pk=pk)
        s.fields['company_name'].queryset = devices
        a=CompanyList.objects.get(id=pk)
        # print(t.id)
        s.fields['company_name'].initial = a
        context['form']=s
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('client_teamname', css_class='form-group col-md-6 mb-0'),
                Column('client_designation', css_class='form-group col-md-6 mb-0'),
                Column('client_role', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            

        )
        

        return context

class ClientsContactCreateView(CreateView):
    model = ClientsContact
    template_name = 'clientscontactcreate.html'
    fields = ('company_name','client_name','client_position','client_email','client_phone')
    success_url = reverse_lazy('companylist')
    context_object_name = 'clientcontacts'

    def get_context_data(self,*args, **kwargs):
        context = super(ClientsContactCreateView, self).get_context_data(**kwargs)
        s=context['form']
        # print(f.fields)
        pk = self.kwargs['pk']
        devices = CompanyList.objects.filter(pk=pk)
        s.fields['company_name'].queryset = devices
        a=CompanyList.objects.get(id=pk)
        # print(t.id)
        s.fields['company_name'].initial = a
        context['form']=s
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('client_name', css_class='form-group col-md-6 mb-0'),
                Column('client_position', css_class='form-group col-md-6 mb-0'),
                Column('client_email', css_class='form-group col-md-6 mb-0'),
                Column('client_phone', css_class='form-group col-md-6 mb-0'),


                css_class='form-row'
            ),
            

        )
        

        return context

