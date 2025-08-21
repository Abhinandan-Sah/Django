from django.urls import path, re_path
from courses.views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, jsondata, datavalue, site
from courses import views
urlpatterns = [
    path('', CourseListView, name='course-list'),
    path('<courseName>/', CourseDetailView, name='course-detail'),
    path('create/', CourseCreateView, name='course-create'),
    path('update/<int:pk>/', CourseUpdateView, name='course-update'),
    path('delete/<int:pk>/', CourseDeleteView, name='course-delete'),
    path('jsondata/', jsondata, name='json-data'),
    path('slugexp/<slug:courseName>/', CourseDetailView, name='course-detail-slug'),
    path('datavalue/<str:name>/<int:age>/', datavalue, name='data-value'),
    path('add/<n1>/<n2>', site, name='add'),
    path('home/<name>', views.name, name='home-name'),

    # validation of url using Regular Expression
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.article_year, name='article-year'),
    re_path(r'^userid/(?P<userid>[0-9]+)/$', views.user_id, name='user-id')
]

handler404= "courses.views.handler404"
