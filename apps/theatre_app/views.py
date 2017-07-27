from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = School.objects.all().order_by('-date_joined')
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


class DanceViewSet(viewsets.ModelViewSet):
    """
    APIz endpoint that allows groups to be viewed or edited.
    """
    queryset = Dance.objects.all()
    serializer_class = DanceSerializer


class SpecialSkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SpecialSkill.objects.all()
    serializer_class = SpecialSkillSerializer
