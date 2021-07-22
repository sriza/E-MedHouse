
from django.urls import path
from . import views

urlpatterns = [ 
    path('add/microbiology/', views.createMicrobiology, name="createMicrobiology"), 
    path('add/chemistry/', views.createChemistry, name="createChemistry"), 
    path('add/hematology/', views.createHematology, name="createHematology"),
    path('add/bank/', views.createBloodBank, name="createBloodBank"), 
    path('add/diagnotics/', views.createMolecularDiagnotics, name="createMolecularDiagnotics"), 
    path('add/reproductive/', views.createReproductiveBiology, name="createReproductiveBiology"), 
    path('list/', views.listServices, name="listServices"), 
    path('detail/<int:id>', views.detailService, name="detailService"), 
    path('book/', views.bookService, name="bookService"), 
    path('book/detail/<int:id>', views.bookServiceDetail, name="bookServiceDetail"), 

]
