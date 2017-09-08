from django.shortcuts import render
from forms.forms import SurveyForms

from .models import Survey,ChoiceFieldOptions
from .serializers import FormSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.

def survey_create(request):
    #




    if request.method == 'POST':
        # print(request.POST.getlist('send[]'))
        print(request.POST.getlist('choice_1[]'))




        dic = request.POST

        sur = Survey(user=request.user)

        print(sur,request.user)

        sur.save()

        for i,u in dic.items():
            print(i,u)

            if i.count('text')==1:
                sur.textfield_set.create(identifier=i,name=u) # identifier follows this pattern text_1, date_1, etc...
            elif i.count('date')==1:
                sur.datefield_set.create(identifier=i,name=u)
            elif i.count('check')==1:
                sur.checkfield_set.create(identifier=i,name=u)

            elif i.count('choice')==1 and i.count('[]')!=1:
                print('passed')

                choice_options = sur.choicefield_set.create(identifier=i,name=u)

                options = request.POST.getlist(i+'[]')

                for k in options:

                    choice_options.choicefieldoptions_set.create(name=k)







    form = SurveyForms()

    # print(form.as_p())
    # form['date'].__setattr__('form','meme')



    return render(request, 'forms/survey_create.html', {'form': form})





@csrf_exempt
def form_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = ChoiceFieldOptions.objects.all()
        serializer = FormSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)









def survey_view(request):
    return render(request,'forms/survey_view.html')