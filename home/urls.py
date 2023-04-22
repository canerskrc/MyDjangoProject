from django.urls import path
from . import views

# uniform resource locator (URL açılımı -- bir vweb sitesinin adresi)

urlpatterns = [
      path("",views.index, name='home'),
      path('<int:detailNumber>/', views.detail, name='detail'),
      path('<int:archiveNumber>/archive/', views.archive, name='archive'),
      path('comment/<int:commentNumber>/', views.comment, name= 'comment')
]
# path('<int:archiveNumber>/archive/') bu kod detail number ile archive number sayısını ayırt etmek için sonuna /archive/ eklendi.
# <int:detailNumber>/ kodundan önce 'detail/' kodu vardı. detail sayfasına yönlendirmek yerine bir değişken tanımladık.

