import django

from .views import OrgListView,AddUserAskView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,TeacherListView,TeacherDetailView


from django.urls import path,re_path


app_name = "organization"

urlpatterns = [
    path('list/',OrgListView.as_view(),name='org_list'),
    path('add_ask/',AddUserAskView.as_view(),name='add_ask'),
    re_path(r'home/(?P<org_id>\d+)/',OrgHomeView.as_view(),name='org_home'),
    re_path(r'course/(?P<org_id>\d+)/',OrgCourseView.as_view(),name='org_course'),
    re_path(r'desc/(?P<org_id>\d+)/',OrgDescView.as_view(),name='org_desc'),
    re_path(r'teacher/(?P<org_id>\d+)/',OrgTeacherView.as_view(),name='org_teacher'),
    path('teacher/list/',TeacherListView.as_view(),name="teacher_list"),
    re_path('teacher/detail/(?P<teacher_id>\d+)/', TeacherDetailView.as_view(), name="teacher_detail"),





]