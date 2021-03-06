from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'school', views.SchoolViewSet)
router.register(r'district', views.DistrictViewSet)
router.register(r'state', views.StateViewSet)
router.register(r'gradyear', views.GradyearViewSet)
router.register(r'tposition', views.TpositionViewSet)
router.register(r'trank', views.TrankViewSet)
router.register(r'tlength', views.TlengthViewSet)
router.register(r'tcatagory', views.TcatagoryViewSet)
router.register(r'thonor', views.ThonorViewSet)
router.register(r'dancetype', views.DanceTypeViewSet)
router.register(r'specialskill', views.SpecialSkillViewSet)
router.register(r'vocaltype', views.VocalTypeViewSet)
router.register(r'showlist', views.ShowlistViewSet)
router.register(r'techrolelist', views.TechrolelistViewSet)
router.register(r'rolelist', views.RolelistViewSet)
router.register(r'conflict', views.ConflictViewSet)
router.register(r'conflictreason', views.ConflictReasonViewSet)
router.register(r'audition', views.AudtionViewSet)
router.register(r'publisher', views.PublisherViewSet)
router.register(r'venue', views.VenueViewSet)
router.register(r'directorsnote', views.DirectorsnoteViewSet)
router.register(r'donor', views.DonorViewSet)
router.register(r'donortype', views.DonortypeViewSet)
router.register(r'budgetcatagory', views.BudgetcatagoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
