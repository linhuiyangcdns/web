from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from django.views.generic.base import View

from .models import CourseOrg,CityDict,Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserAskform
from operation.models import UserFavorite




class OrgListView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        all_citys = CityDict.objects.all()
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs,5, request=request)
        orgs = p.page(page)
        org_nums = all_orgs.count()

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # 在name字段进行操作,做like语句的操作。i代表不区分大小写
            # or操作使用Q
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords) | Q(
                address__icontains=search_keywords))

        city_id = request.GET.get('city', "")
        if city_id:
            # 外键city在数据中叫city_id
            # 我们就在机构中作进一步筛选
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            # 我们就在机构中作进一步筛选类别
            all_orgs = all_orgs.filter(category=category)

        # 进行排序
        sort = request.GET.get('sort',"")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

        return render(request,'org/org-list.html',{
            "all_orgs":orgs,
            "all_citys":all_citys,
            "org_nums": org_nums,
            "hot_orgs":hot_orgs,
            "sort":sort,
            "city_id": city_id,
            "search_keywords":search_keywords,
            "category":category,

        })


class AddUserAskView(View):
    def post(self,request):
        userask_form = UserAskform(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit= True)

            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status': 'fail', 'msg':{0}}".format(userask_form.errors),  content_type='application/json')


class OrgHomeView(View):
    def get(self,request,org_id):
        current_page = "home"

        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums +=1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()[:4]
        all_teacher = course_org.teacher_set.all()[:2]

        return render(request,'org/org-detail-homepage.html',{
            'all_courses': all_courses,
            'all_teacher': all_teacher,
            'course_org': course_org,
            "has_fav":has_fav,
            "current_page":current_page,
        })


class OrgCourseView(View):
    """
    机构课程
    """
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()
        return render(request,'org/org-detail-course.html',{
            "course_org":course_org,
            "all_course":all_courses,
        })


class OrgDescView(View):
    """
    机构介绍
    """
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))

        return render(request,'org/org-detail-desc.html',{
            "course_org":course_org,

        })


class OrgTeacherView(View):
    """
    教师介绍
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org/org-detail-desc.html', {
            "course_org": course_org,
            "all_teachers":all_teachers,


        })


class AddFavView(View):
    """
    用户收藏与取消收藏功能
    """
    def post(self,request):
        id = request.POST.get('fav_id', 0)
        pass


class TeacherListView(View):
    def get(self,request):
        all_teacher = Teacher.objects.all()
        teacher_nums = all_teacher.count()
        sort = request.GET.get("sort,")
        if sort:
            if sort =="hot":
                all_teacher = all_teacher.order_by("-click_nums")

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_teacher = all_teacher.filter(
                Q(name__icontains=search_keywords) | Q(work_company__icontains=search_keywords))

        rank_teacher = Teacher.objects.all().order_by("-fav_nums")[:5]

        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_teacher,4,request=request)
        teachers = p.page(page)
        return render(request,'teachers/teachers-list.html',{
            "all_teacher":teachers,
            "teacher_nums":teacher_nums,
            "sort":sort,
            "rank_teachers":rank_teacher,
            "search_kyewords":search_keywords
        })

class TeacherDetailView(View):
    def get(self,request):
        return render(request,'teachers/teachers-detail.html',{

        })