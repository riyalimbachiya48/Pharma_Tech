from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.conf import settings
from django.http.response import JsonResponse,HttpResponse
from django.views import View
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.core.mail import EmailMessage, message,send_mail
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template


def index(request):
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            email = EmailMessage(
                subject= f"{name} from  PharmaTech.",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email]
            )
            email.send()
            messages.error(request,"You Feedback has been sent sucessfully !")
    
        else:
            print("error")
        return render(request,'index.html')
    
class AppointmentTemplateView(TemplateView):
    template_name = "appointment/appointment.html"
    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP! select next for date")
        return HttpResponseRedirect(request.path)

class ManageAppointmentTemplateView(ListView):
    template_name = "appointment/manage.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('appointment/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"Your appointment accepted !! Check your Email {appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context

def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name',flat=True)
    productsList = list(products)

    return JsonResponse(productsList, safe=False)

def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()
            
            if product:
                return redirect('collection/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request,"No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
            
    return redirect(request.META.get('HTTP_REFERER'))
    
def collection(request):
    category = Category.objects.filter(status=0)
    trending_products = Product.objects.filter(trending=1)
    context = {'category':category , 'trending_products':trending_products}
    return render(request,'Collection.html', context)
 
def collectionview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category =  Category.objects.filter(slug=slug).first()
        context = {'products' : products , 'category': category}
        return render(request, 'products.html', context)
    else:
        messages.warning(request,"No such category found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products = Product.objects.filter(slug=prod_slug,status=0).first
            context = {'products' : products}
        else:
            messages.error(request,"No such product found")
            return redirect('collection')
    else:
        messages.error(request,"no such category found")
        return redirect('collection')
    return render(request,'view.html', context)

def cart(request):
    return render(request,'cart.html')
   
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')
   
def profile(request):
     return render(request, 'profile/profile.html')

def login(request):
     return render(request, 'user/login.html')

