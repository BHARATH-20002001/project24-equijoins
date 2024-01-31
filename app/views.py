from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename='king')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2023)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=3000)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr=7839)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='research')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='dallas')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='new york')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='dallas')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=20)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[1:5:]

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)



def selfjoins(request):
    eop = Emp.objects.select_related('mgr').all()
    eop = Emp.objects.select_related('mgr').filter(sal__gte=2500)
    eop = Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    eop = Emp.objects.select_related('mgr').filter(ename='king')
    eop = Emp.objects.select_related('mgr').filter(sal__lt=2000)
    eop = Emp.objects.select_related('mgr').filter(comm__gte=500)
    eop = Emp.objects.select_related('mgr').filter(comm__isnull=False)
    eop = Emp.objects.select_related('mgr').filter(sal__lte=2000)
    eop = Emp.objects.select_related('mgr').filter(deptno=20)
    eop = Emp.objects.select_related('mgr').filter(sal__gte=500)
    eop = Emp.objects.select_related('mgr').all()[1:5:]
    eop = Emp.objects.select_related('mgr').filter(mgr=7839)
    eop = Emp.objects.select_related('mgr').filter(ename='king')
    eop = Emp.objects.select_related('mgr').all()[:2:]
    

    d = {'eop':eop}
    return render(request,'selfjoins.html',d)

