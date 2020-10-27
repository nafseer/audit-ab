from django.shortcuts import render
from .models import TrailList
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
class TrailListView(TemplateView):

    model = TrailList
    template_name = 'traillist.html'
    context_object_name = 'traillist'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TrailListView, self).get_context_data(**kwargs)
        traillist = TrailList.objects.all()
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print(traillist)
        print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        page = self.request.GET.get('page')
        # paginator = Paginator(users, self.paginate_by)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users= paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        context['traillist'] = traillist
        return context


class TrailListCreateView(CreateView):
    model = TrailList
    template_name = 'traillistcreate.html'
    fields = ('trail_id','trail_account','trail_sheets',)
    success_url = reverse_lazy('userroles')
    context_object_name = 'traillist'

    def get_context_data(self,*args, **kwargs):
        context = super(TrailListCreateView, self).get_context_data(**kwargs)
        i=context['form']
        print(context)
        print(i)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('trail_account', css_class='form-group col-md-6 mb-0'),
                Column('trail_sheets', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            

        )
        

        return context