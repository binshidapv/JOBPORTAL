from django.urls import path
from employer import views

urlpatterns = [
    path('home',views.EmployerHomeView.as_view(),name="emp-home"),
    path('jobs/add',views.AddJobView.as_view(), name="emp-addjob"),
    path('jobs/all',views.ListJobView.as_view(),name="emp-alljobs"),
    path('jobs/details/<int:id>',views.JobDetailView.as_view(),name="emp-jobdetail"),
    # ( soecific id int pass)
    path("jobs/change/<int:id>",views.JobEditView.as_view(),name="emp-editjob"),
    path("jobs/remove/<int:id>",views.JobDeleteView.as_view(),name="emp-deletejob"),
    path("users/account/signup",views.SignUpView.as_view(),name="signup"),
    path("users/account/signin",views.SignInView.as_view(),name="signin"),
    path("users/accounts/signout",views.signout_view,name="signout"), #asview no cause class method
    path("users/password/change",views.ChangePasswordView.as_view(),name="password-change"),
    path("users/password/reset",views.PasswordResetView.as_view(),name="password-reset"),
]
