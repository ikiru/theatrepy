from django.contrib.auth.models import User, Group
from rest_framework import serializers


class SchoolSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = School
        fields = ('id', 'name', 'address', 'zip', 'phone',
                  'logo', 'prim_color', 'sec_color', 'updated_at', 'created_at')


class DistrictSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = District
        fields = ('id', 'name', 'updated_at', 'created_at')


class StateSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = State
        fields = ('id', 'name', 'updated_at', 'created_at')


class GradyearSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Gradyear
        fields = ('id', 'year', 'updated_at', 'created_at')


class ProfileSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Profile
        fields = ('id', 'address', 'city', 'state', 'zip', 'email', 'phone', 'district',
                  'school', 'gradyear', 'is_active', 'image', 'updated_at', 'created_at')


class TpositionSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Tposition
        fields = ('id', 'name', 'updated_at', 'created_at')


class TrankSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Trank
        fields = ('id', 'name', 'updated_at', 'created_at')


class TlengthSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Tlength
        fields = ('id', 'name', 'updated_at', 'created_at')


class TcategorySerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Tcategory
        fields = ('id', 'name', 'updated_at', 'created_at')


class ThonorSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Thonor
        fields = ('id', 'points_earned', 'rank',
                  'desrciption', 'updated_at', 'created_at')


class DanceTypeSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = DanceType
        fields = ('id', 'name', 'updated_at', 'created_at')


class SpecialSkillSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = SpecialSkill
        fields = ('id', 'name', 'updated_at', 'created_at')


class VocalTypeSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = VocalType
        fields = ('id', 'name', 'updated_at', 'created_at')


class ShowlistSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Showlist
        fields = ('id', 'user', 'name', 'updated_at', 'created_at')


class TechrolelistSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Techrolelist
        fields = ('id', 'user', 'name', 'updated_at', 'created_at')


class RolelistSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Rolelist
        fields = ('id', 'user', 'name', 'age', 'gender',
                  'descriptoon', 'updated_at', 'created_at')


class ContflictSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Conflict
        fields = ('id', 'user', 'date', 'note', 'conflicteason', 'is_approved')


class ConflictReasonSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = ConflictReason
        fields = ('id', 'user', 'name', 'updated_at', 'created_at')


class AudtionSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Audtion
        fields = ('id', 'user', 'name', 'age', 'height', 'weight', 'eye', 'hair', 'sex', 'character_one', 'character_two', 'character_three', 'other_role',
                  'ensemble_role', 'understudy', 'read_music', 'dancetype', 'danceexp', 'vocaltype', 'vocalexp', 'note', 'physical_limitation')


class PublisherSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Publisher
        fields = ('id', 'user', 'name', 'updated_at', 'created_at')


class VenueSerializer(serializers.HyperlinkedModelSerializer)
    class Meta
        model = Venue
        fields = ('id', 'user', 'name', 'address', 'city', 'state', 'zip', 'phone', 'website', 'in_district', 'notes', "}
