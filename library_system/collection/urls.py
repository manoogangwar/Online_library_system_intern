from django.urls import path
from collection.views import exportExelView,exportView
from .import views 

urlpatterns = [
    path('add-author/', views.addingAuthorView.as_view(), name='add_author'),
    path('add-book/', views.addBookView.as_view(), name='add_book'),
    path('add-borrow/', views.addborrowRecordView.as_view(), name='add_borrow'),
    path('author/', views.authorListView.as_view(), name='author_list'),
    path('book/', views.bookListView.as_view(), name='book_list'),
    path('borrow/', views.borrowRecordListView.as_view(), name='borrow_list'),
    path('export-excel/', exportExelView.as_view(), name='export-excel'),
    path('export/', exportView, name='export'),
]

