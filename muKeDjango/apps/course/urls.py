import django

from .views import CourseListView,CourseDetailView

from django.urls import path,re_path



app_name = 'course'

urlpatterns =[
    path('list/',CourseListView.as_view(),name='course_list'),
    re_path('course/(?P<course_id>\d+)/',CourseDetailView.as_view(),name='course_detail'),
]