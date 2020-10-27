# from django.shortcuts import render
# from .models import ClientsMaster
# # Create your views here.
# from django.views.generic import ListView,CreateView,TemplateView
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.urls import reverse_lazy
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
# from django.views.generic import CreateView
# from django.views.generic.edit import UpdateView,DeleteView
# from django.views.generic.detail import DetailView





# # Create your views here.
# class ClientsListView(TemplateView):

#     model = ClientsMaster
#     template_name = 'clients.html'
#     context_object_name = 'clientslist'
#     # paginate_by = 5

#     def get_context_data(self, **kwargs):
#         context = super(ClientsListView, self).get_context_data(**kwargs)
#         clientslist = ClientsMaster.objects.all()
#         print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
#         print(clientslist)
#         print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
#         page = self.request.GET.get('page')
#         # paginator = Paginator(users, self.paginate_by)
#         # try:
#         #     users = paginator.page(page)
#         # except PageNotAnInteger:
#         #     users= paginator.page(1)
#         # except EmptyPage:
#         #     users = paginator.page(paginator.num_pages)
#         context['clientslist'] = clientslist
#         return context


# class ClientsProfileListCreateView(CreateView):
#     model = ClientsMaster
#     template_name = 'clientsprofilecreate.html'
#     fields = ('client_company','client_cin','client_address','client_doi')
#     success_url = reverse_lazy('companylist')
#     context_object_name = 'clientslist'

#     def get_context_data(self,*args, **kwargs):
#         context = super(ClientsProfileListCreateView, self).get_context_data(**kwargs)
#         i=context['form']
#         print(context)
#         print(i)
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('client_company', css_class='form-group col-md-6 mb-0'),
#                 Column('client_cin', css_class='form-group col-md-6 mb-0'),
#                 Column('client_address', css_class='form-group col-md-6 mb-0'),
#                 Column('client_doi', css_class='form-group col-md-6 mb-0'),

#                 css_class='form-row'
#             ),
            

#         )
        
#         return context

# class ClientsTeamListCreateView(CreateView):
#     model = ClientsMaster
#     template_name = 'clientsteamcreate.html'
#     fields = ('client_teamname','client_designation','client_role',)
#     success_url = reverse_lazy('companylist')
#     context_object_name = 'clientslist'

#     def get_context_data(self,*args, **kwargs):
#         context = super(ClientsTeamListCreateView, self).get_context_data(**kwargs)
#         i=context['form']
#         print(context)
#         print(i)
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('client_teamname', css_class='form-group col-md-6 mb-0'),
#                 Column('client_designation', css_class='form-group col-md-6 mb-0'),
#                 Column('client_role', css_class='form-group col-md-6 mb-0'),

#                 css_class='form-row'
#             ),
            

#         )
        

#         return context

# class ClientsContactCreateView(CreateView):
#     model = ClientsMaster
#     template_name = 'clientscontactcreate.html'
#     fields = ('client_name','client_position','client_email','client_phone')
#     success_url = reverse_lazy('companylist')
#     context_object_name = 'clientslist'

#     def get_context_data(self,*args, **kwargs):
#         context = super(ClientsContactCreateView, self).get_context_data(**kwargs)
#         i=context['form']
#         print(context)
#         print(i)
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('client_name', css_class='form-group col-md-6 mb-0'),
#                 Column('client_position', css_class='form-group col-md-6 mb-0'),
#                 Column('client_email', css_class='form-group col-md-6 mb-0'),
#                 Column('client_phone', css_class='form-group col-md-6 mb-0'),


#                 css_class='form-row'
#             ),
            

#         )
        

#         return context

