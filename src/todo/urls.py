from django.urls import path


from . import views

urlpatterns = [
    path('add/', views.add_task, name='add'),
    path('done/<int:pk>', views.mark_as_done, name='done'),
    path('undo/<int:pk>', views.mark_as_incomplete, name='undo'),
    path('edit/<int:pk>', views.edit_task, name='edit'),
    path('delete/<int:pk>', views.delete_task, name='delete')
]