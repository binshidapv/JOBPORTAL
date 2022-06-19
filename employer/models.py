from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_title_name=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    salary=models.PositiveIntegerField(null=True)
    experiance=models.PositiveIntegerField(default=0)




     # overriding string method
    def __str__(self):
        return self.job_title_name  #display only job titles
# for filtering
# qs=Jobs.objects.filter(experiance=6)
# print all experiance above1 (in orm query greater lessrhan nottake so check in documention equal to working
#SO


#python manage.py makemigrations
#python manage.py migrate
# object  crud operation
# create retrive,update,delete
# job,mobile,
#list
# create
# update
# detail
# remove/delete eg: website amazon list create update delete in every this  is done
# modelname.objects.create(field:value)
# Jobs.objects.create(job_title_name="frontend  developer",company_name="abc",)
# \in shell

# # 1.create
# # 2.listfetching all records using orm query
# # Jobs.objects.all()
# qs=Jobs.objects.all()assign in to a variable query search user provide variableqs
#specific object
#

#print qs
# qs.company_name
# 3.update
# qs=Jobs.objects.get(id=3)
#  qs=Jobs.objects.get(id=3)
# >>> qs
# <Jobs: software enginear>
# >>> qs.experiance=3
# >>> qs.save()
# 4.delete
# qs=Jobs.objects.get(id=2)
# qs.delete()
# #create=modelname.objects.create(field:value)
# #all=nameof.objects.all()
# specific object=mn.objec.get(uf=value)
# qs=jobs.objects.filter(company_name"ey")
# create
# listdetail
# update
#delete
