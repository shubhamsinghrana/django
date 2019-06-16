from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from . import forms
def index(request):
    # webpages_list=AccessRecord.objects.order_by('date')
    # date_dict ={'access_records':webpages_list}
    #return render(request,'first_app/index.html',context=date_dict)
    return render(request,'first_app/index.html')
# Create your views here.
def form_name_view(request):
    form =forms.FormName()

    if request.method == 'POST':
        
            form=forms.FormName(request.POST)

            if form.is_valid():
                print("validation success")
                form.cleaned_data['name']
                print("name:"+form.cleaned_data['name'])
                print("name:"+form.cleaned_data['email'])
                print("name:"+form.cleaned_data['text'])  
    else:
        print("validation fail")
    return render(request,'first_app/form_page.html',{'form':form})