
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("ToDoList_app.urls")),
    path('add/', include("ToDoList_app.urls")),
    path('update/', include('ToDoList_app.urls')),
    path('admin/', admin.site.urls),
]
