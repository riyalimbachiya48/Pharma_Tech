from django.shortcuts import redirect , render
from django.contrib import messages
from home.forms import CustomUserForm
from django. contrib.auth import authenticate , login ,logout



def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration sucessful")
            return redirect("/register")    
    context = {'form':form }
    return render(request,"auth/register.html",context)


def loginpage(request):   
    if request.user.is_authenticated:
            messages.warning(request,"you are already logged in")
            return redirect( "/register")
    else:
        if request.method == 'POST':
            name  = request.POST.get('username')
            passwd  = request.POST.get('password')
            user = authenticate(request,username = name , password=passwd)
          
            if user is not None:
                 login(request, user)
                 messages.success(request,"logged in sucess")
                 print("sucess")
                 return redirect ("/register")  
            else:
                messages.error(request,"Invalid username and password")
                return  redirect('/')
        else:
             messages.error(request,"no post method")
             return redirect("/")
                
    
def logoutpage(request):
        if request.user.is_authenticated:
             logout( request)
             messages.success(request,"logged out sucessfully")
        return redirect( "/register")