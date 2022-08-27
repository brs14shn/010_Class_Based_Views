from django.urls import path
from .views import home, student_list, student_add, student_detail, student_update, student_delete
from .views import HomeView, StudentListView, StudentDetailView, StudentCreateView, Student_Update_View, StudentDelete
urlpatterns = [
    # * FUNCTİON BASED
    # path('', home, name="home"),
    # path('student_list/', student_list, name="list"),
    # path('student_add/', student_add, name="add"),
    # path('detail/<int:id>/', student_detail, name="detail"),
    # path('update/<int:id>/', student_update, name="update"),
    path('delete/<int:id>/', student_delete, name="delete"),

    # * CLASS BASED
    path("", HomeView.as_view(), name="home"),
    path("student_list/", StudentListView.as_view(), name="list"),
    path("detail/<int:id>/", StudentDetailView.as_view(), name="detail"),
    #! detail/<int:pk>/ olarak belirtirsek views tanımlamaya gerek kalmazdı
    path("student_add/", StudentCreateView.as_view(), name="add"),
    path("update/<int:pk>/", Student_Update_View.as_view(), name="update"),
    path("delete/<int:pk>", StudentDelete.as_view(), name="delete")
]
