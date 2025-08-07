from django.urls import path
from courses.views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, jsondata, datavalue

urlpatterns = [
    path('', CourseListView, name='course-list'),
    path('<courseName>/', CourseDetailView, name='course-detail'),
    path('create/', CourseCreateView, name='course-create'),
    path('update/<int:pk>/', CourseUpdateView, name='course-update'),
    path('delete/<int:pk>/', CourseDeleteView, name='course-delete'),
    path('jsondata/', jsondata, name='json-data'),
    path('slugexp/<slug:courseName>/', CourseDetailView, name='course-detail-slug'),
    path('datavalue/<str:name>/<int:age>/', datavalue, name='data-value'),
]
