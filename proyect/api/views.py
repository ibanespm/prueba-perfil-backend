from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Element
from django.http import JsonResponse
import json

#imports 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.


class ElementView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)   #metodo cada vez que se envia o se despacha


    def get(self, request, id=0):

        try:
                    if (id > 0) :
                            elements = list(Element.objects.filter(id=id).values())  #filtramos por id
                            if len(elements) > 0:
                                data={'message':"Success", 'element': elements[0]}
                            else:
                                data = {'message':"Item not found...!"}

                    else:        
                    
                            elements =list(Element.objects.values()) # devolvemos un listado de Elements
                            if len(elements) > 0 :
                                data = {'message': "Success", 'elements':elements}
                            else:
                                data = {'message' : "Elements not fount..!"}

        except Exception as e:
                    print(f"Error: {e}")
                    
                    data = {'message':"Error..!", 'error_details':str(e)}
        return JsonResponse(data)       



    def post(self, request):
        
        try:
                        json_data = request.body  #requperar el post 
                        dict_data = json.loads(json_data) #duvuelve un diccionario de python 
                        
                        #insert element to database
                        Element.objects.create(
                                name=dict_data['name'], 
                                country=dict_data['country'], 
                                email = dict_data['email'])
                        
                        print(dict_data)
                        data = {'message':"Sucess"}
                                
                        return JsonResponse(data)
        except Exception as e:
            print(f' error: {e}')


    def put(self, request, id):

        json_data =  list(Element.objects.filter(id=id).values())


    def delete(self, request):
        pass 

























