from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import *


class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer


class GradyearViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Gradyear.objects.all()
    serializer_class = GradyearSerializer


class TpositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tposition.objects.all()
    serializer_class = TpositionSerializer


class TrankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Trank.objects.all()
    serializer_class = TrankSerializer


class TlengthViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tlength.objects.all()
    serializer_class = TlengthSerializer


class TcatagoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tcategory.objects.all()
    serializer_class = TcategorySerializer


class ThonorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Thonor.objects.all()
    serializer_class = ThonorSerializer


class DanceTypeViewSet(viewsets.ModelViewSet):
    """
    APIz endpoint that allows groups to be viewed or edited.
    """
    queryset = DanceType.objects.all()
    serializer_class = DanceTypeSerializer


class SpecialSkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SpecialSkill.objects.all()
    serializer_class = SpecialSkillSerializer


class VocalTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = VocalType.objects.all()
    serializer_class = VocalTypeSerializer


class ShowlistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Showlist.objects.all()
    serializer_class = ShowlistSerializer


class TechrolelistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Techrolelist.objects.all()
    serializer_class = TechrolelistSerializer


class RolelistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Rolelist.objects.all()
    serializer_class = RolelistSerializer


class ConflictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Conflict.objects.all()
    serializer_class = ConflictSerializer


class ConflictReasonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ConflictReason.objects.all()
    serializer_class = ConflictReasonSerializer


class AudtionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Audtion.objects.all()
    serializer_class = AudtionSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class VenueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class DirectorsnoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Directorsnote.objects.all()
    serializer_class = DirectorsnoteSerializer
