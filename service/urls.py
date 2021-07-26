
from django.urls import path
from . import views

urlpatterns = [ 
    path('add/microbiology/', views.createMicrobiology, name="createMicrobiology"), 
    path('add/chemistry/', views.createChemistry, name="createChemistry"), 
    path('add/hematology/', views.createHematology, name="createHematology"),
    path('add/bank/', views.createBloodBank, name="createBloodBank"), 
    path('add/diagnotics/', views.createMolecularDiagnotics, name="createMolecularDiagnotics"), 
    path('add/reproductive/', views.createReproductiveBiology, name="createReproductiveBiology"), 
    path('update/microbiology/<int:id>', views.updateMicrobiology, name="updateMicrobiology"),
    path('update/chemistry/<int:id>', views.updateChemistry, name="updateChemistry"), 
    path('update/hematology/<int:id>', views.updateHematology, name="updateHematology"),
    path('update/bank/<int:id>', views.updateBloodBank, name="updateBloodBank"), 
    path('update/diagnotics/<int:id>', views.updateMolecularDiagnotics, name="updateMolecularDiagnotics"), 
    path('update/reproductive/<int:id>', views.updateReproductiveBiology, name="updateReproductiveBiology"),
    path('list/', views.listServices, name="listServices"), 
    path('detail/<int:id>', views.detailService, name="detailService"), 
    path('book/', views.bookService, name="bookService"), 
    path('book/detail/<int:id>', views.bookServiceDetail, name="bookServiceDetail"), 
    path('delete/microbiology/<int:id>',views.deleteService),
    path('appointment/<int:id>/', views.bookAppointment, name="bookAppointment"),
    path('upload/report/<int:id>/', views.uploadReport, name="uploadReport"),
    path('reportlist/',views.pdfList)
]
