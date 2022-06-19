from django.shortcuts import render,redirect
from django.views.generic import View,ListView,TemplateView,CreateView,DetailView,UpdateView,DeleteView,FormView
from django .urls import reverse_lazy
from employer.forms import JobForm
from employer.models import Jobs
from employer.forms import SignUpForm,LoginForm,PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#import jos for creating database

# # Create your views here.
#list,detail,update,delete
class EmployerHomeView(View):
    def get(self,request):
         return render(request,'emp-home.html')

# class EmployerHomeView(TemplateView):
#      template_name = "base.html"    #django predefined
class AddJobView(CreateView):
    model=Jobs
    form_class = JobForm
    template_name = "emp-addjob.html"
    # function return class no return support so use sucess,import reverese lazy,in post activity
    success_url =reverse_lazy ("emp-alljobs")
    # def get(self,request):
    #     form=JobForm()
    #     return render(request,"emp-addjob.html",{"form":form})
    # def post(self,request):
    #     form=JobForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            #object create functionaily form.save
            # jname=form.cleaned_data.get("job_title_name")
            # cname=form.cleaned_data.get("company_name")
            # location=form.cleaned_data.get("location")
            # salary=form.cleaned_data.get("salary")
            # exp=form.cleaned_data.get("experiance")
            # Jobs.objects.create(job_title_name=jname,company_name=cname,location=location,salary=salary,experiance=exp)
        #     return render(request,"emp-home.html")  #form saved go to emphomepage
        # else:
        #     return render(request,"emp-addjob.html",{"form":form})
class ListJobView(ListView):
    model=Jobs
    context_object_name="jobs"
    template_name="emp-listjob.html"
#     def get(self,request):
#         qs=Jobs.objects.all()
#         return render(request,"emp-listjob.html",{"jobs":qs})
#     # create view for particular id
class JobDetailView(DetailView):
    model=Jobs
    context_object_name="jobs"
    template_name="emp-detailjob.html"
    pk_url_kwarg = "id"
    #pk ane built in we write int ,pk_id
    # def get(selfself,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,"emp-detailjob.html",{"job":qs})
class JobEditView(UpdateView):
    model=Jobs
    form_class=JobForm
    template_name = "emp-editjob.html"
    success_url = reverse_lazy("emp-alljobs")
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(instance=qs)
    #     # form edit printed edit
    #     return render(request,"emp-editjob.html",{"form":form})
    # def post(self,request,id):
    #     qs = Jobs.objects.get(id=id)
    #     form=JobForm(request.POST,instance=qs)
    #     #qs instance getb make  take global to addinstance=qs,update qs we must  pass intance
    #     if form.is_valid():
    #         form.save()

    #         return redirect("emp-alljobs")
    #     # urls name empall job hetre we avoid render context,import redirect
    #     else:
    #         return render(request,"emp-editjob.html",{"form":form})
class JobDeleteView(DeleteView):
    template_name="jobconfirmdelete.html"
     # def get(self,request,id):
     #      qs=Jobs.objects.get(id=id)
     #      qs.delete()
     #      return redirect("emp-alljobs")
    success_url = reverse_lazy( "emp-alljobs")
    pk_url_kwarg = "id"
    model=Jobs
class SignUpView(CreateView):
    model=User
    form_class=SignUpForm
    template_name = "usersignup.html"
    success_url=reverse_lazy("emp-alljobs")

class SignInView(FormView):
    form_class = LoginForm
    template_name = "login.html"


    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("emp-alljobs")
            else:
                return render(request,"login.html",{"form":form})
#if you want to create a superuser use this command python manage.py createsuperpython
# manage.py createsuperserpython manage.py createsuperserser
#login session starts here;...
# user  authentication everytime not need it stores
def signout_view(request,*args,**kwargs):
    #function class inside
    logout(request)
    return  redirect("signin")
class ChangePasswordView(TemplateView):
    template_name = "changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user= authenticate(request,username=uname,password=pwd)
        #form valid credentials pass..return object
        if user:
            return redirect("password-reset")

        else:
            return render(request,self.template_name)


class  PasswordResetView(TemplateView):
    template_name = "passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2 = request.POST.get("pwd2")
        if pwd1 != pwd2:
            return render (request,self.template_name,{"msg":"incorrect password"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")

