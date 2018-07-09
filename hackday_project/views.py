from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

from hackday_project.models import Grocery, Family


# GET /groceries/all
def get_all_groceries(request):
    if request.method != 'GET':
        return HttpResponseNotFound('Method not supported')
    all_groceries = Grocery.objects.all()
    template = loader.get_template('index.html')
    context = {
        'groceries': all_groceries,
    }
    return HttpResponse(template.render(context, request))
