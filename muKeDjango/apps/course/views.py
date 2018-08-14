from django.shortcuts import render

from django.views.generic.base import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course


class CourseListView(View):
    """

    """
    def get(self,request):
        all_course = Course.objects.all()
        hot_courses = Course.objects.all().order_by("-students")[:3]
        search_keywords = request.GET.get('keywords', '')
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course,5, request=request)
        courses = p.page(page)

        # 进行排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_course = all_course.order_by("-students")
            elif sort == "hot":
                all_course = all_course.order_by("-click_nums")

        return render(request,'course/course-list.html',{
            "all_course":courses,
            "sort":sort,
            "hot_courses":hot_courses,
            "search_keywords":search_keywords
        })


class CourseDetailView(View):
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False


        return render(request,'course/course-detail.html',{
            "course":course

        })