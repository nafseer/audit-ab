from django.shortcuts import render
from .models import ProcedureMaster,ProcedureComments,ProcedureFile
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
# class ProcedureListView(TemplateView):

#     model = ProcedureMaster
#     template_name = 'procedures.html'
#     context_object_name = 'procedures'
#     # paginate_by = 5

#     def get_context_data(self, **kwargs):
#         context = super(ProcedureListView, self).get_context_data(**kwargs)
        
#         companylist = CompanyList.objects.filter(id = pk).values()

#         curr_comp = companylist[0]['company_name']
#         procedures = ProcedureMaster.objects.filter(company_name = curr_comp)
#         print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
#         print(procedures)
#         print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
#         page = self.request.GET.get('page')
#         context['procedures'] = procedures
#         return context


class ProcedureCreateView(CreateView):
    model = ProcedureMaster
    template_name = 'procedurecreate.html'
    fields = ('company_name','auditee_name','started_on','completed_on','reviewer','reviewed_on','time_taken')
    success_url = reverse_lazy('procedurescomment')
    context_object_name = 'procedures'

    def get_context_data(self,*args, **kwargs):
        procedures = ProcedureMaster.objects.all()
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print(procedures)
        context = super(ProcedureCreateView, self).get_context_data(**kwargs)
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
                Column('auditee_name', css_class='form-group col-md-6 mb-0'),
                Column('started_on', css_class='form-group col-md-6 mb-0'),
                Column('completed_on', css_class='form-group col-md-6 mb-0'),
                Column('reviewer', css_class='form-group col-md-6 mb-0'),
                Column('reviewed_on', css_class='form-group col-md-6 mb-0'),
                Column('time_taken', css_class='form-group col-md-6 mb-0'),
               

                css_class='form-row'
            ),
            

        )
        

        return context

class CommentCreateView(CreateView):
    model = ProcedureComments
    template_name = 'procedures.html'
    fields = ('comments','company_name',)
    success_url = reverse_lazy('companylist')
    context_object_name = 'comments'

    def get_context_data(self,*args, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        comments = ProcedureComments.objects.all()
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
                Column('comments', css_class='form-group col-md-6 mb-0'),
                Column('notesfile', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            

        )
        page = self.request.GET.get('page')
        context['comments'] = comments
        return context


class FileCreateView(CreateView):
    model = ProcedureFile
    template_name = 'procedures.html'
    fields = ('notesfile','company_name',)
    success_url = reverse_lazy('companylist')
    context_object_name = 'files'

    def get_context_data(self,*args, **kwargs):
        context = super(FileCreateView, self).get_context_data(**kwargs)
        files = ProcedureFile.objects.all()
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
                Column('comments', css_class='form-group col-md-6 mb-0'),
                Column('notesfile', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            

        )
        page = self.request.GET.get('page')
        context['files'] = files
        return context

class ProceduresListView(TemplateView):

    template_name = 'procedures.html'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProceduresListView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        companylist = CompanyList.objects.filter(id = pk).values()

        curr_comp = companylist[0]['company_name']
        procedures = ProcedureMaster.objects.filter(company_name = curr_comp)
        comments = ProcedureComments.objects.filter(company_name = curr_comp)
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print(procedures)
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        page = self.request.GET.get('page')
        context['procedures'] = procedures
        context['comments'] = comments
        return context


