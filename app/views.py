from django.shortcuts import render
from django.db.models import Q

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
    eop = Emp.objects.select_related('mgr').all()
    

    d = {'eop':eop}
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    emd = Emp.objects.select_related('deptno','mgr').all()
    emd = Emp.objects.select_related('deptno','mgr').filter(ename='king')
    emd = Emp.objects.select_related('deptno','mgr').filter(mgr__empno=7839)
    emd = Emp.objects.select_related('deptno','mgr').filter(empno=7839)
    emd = Emp.objects.select_related('deptno','mgr').filter(sal__gte=4999)
    emd = Emp.objects.select_related('deptno','mgr').filter(mgr=7839 , deptno__dlocation='dallas')
    emd = Emp.objects.select_related('deptno','mgr').filter(ename__startswith='j')
    emd = Emp.objects.select_related('deptno','mgr').filter(ename__startswith='j' , deptno__dname='research')
    emd = Emp.objects.select_related('deptno','mgr').all()
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(ename='allen') | Q(sal=1600))
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(ename='bbbbb') | Q(sal__gte=2000))
    emd = Emp.objects.select_related('deptno','mgr').filter(mgr__gt=7700)
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(comm=None) | Q(sal__gte=2000))
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(sal__gte=2000) | Q(comm=None))
    emd = Emp.objects.select_related('deptno','mgr').filter(deptno__dname='research' , deptno__dlocation='dallas')
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(comm=None) | Q(sal__gt=2000))
    emd = Emp.objects.select_related('deptno','mgr').filter(comm=None , sal__gt=3000)
    emd = Emp.objects.select_related('deptno','mgr').filter(deptno__dname='sales')
    emd = Emp.objects.select_related('deptno','mgr').filter(comm__gte=500 , sal__gt=1000)
    emd = Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='r')
    emd = Emp.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='s',sal__lte=1600)
    emd = Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2023 , sal=1600)
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(empno__gt=7700) | Q(job='clerk'))
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(ename='ford') | Q(deptno=20))
    emd = Emp.objects.select_related('deptno','mgr').filter(ename='jones' , job='manager')
    emd = Emp.objects.select_related('deptno','mgr').filter(hiredate__year__gte=2023 , sal=1600)
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(sal__gte=2000) | Q(hiredate__year__gte=2024))
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year__lte=2023) | Q(sal__gte=2000))

    d = {'emd':emd}
    return render(request,'emp_mgr_dept.html',d)



def emp_salgrade(request):

    # EO = Emp.objects.all()
    # SO = SalGrade.objects.all()
    # d = {'EO':EO ,'SO':SO}

    SO = SalGrade.objects.filter(grade__in=(1,2,3,4))
    EO = Emp.objects.none()

    SO = SalGrade.objects.filter(grade__in=(1,2))
    EO = Emp.objects.none()

    
    for sgo in SO:
        # EO = EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))
        # EO = EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal),ename='smith')
        # EO = EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal),ename='smith')
        EO = EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal),ename='smith')
        
    

    d = {'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)
    