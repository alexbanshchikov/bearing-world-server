from django.shortcuts import render

from rest_framework import viewsets

from .models import ArticulatedBearingTypeDetails, BallRadialAndBallRollerBearingTypeDetails, \
    BallAngularContactBearingTypeDetails, BallPersistentAndPersistentRadialBearingTypeDetails, \
    BallRadialSphericalBearingTypeDetails, Bearing, BearingInnerType, BearingOuterType, \
    RadialNeedleRollerWithLongCylindricalRollersBearingType, RollerConicBearingTypeDetails, \
    RollerPersistentAndPersistentRadialBearingTypeDetails, ShortCylindricalRollerBearingTypeDetails, \
    SphericalRollerBearingsAndAngularContactSphericalBearing

from .serializers import ArticulatedBearingTypeDetailsSerializer, BallRadialAndBallRollerBearingTypeDetailsSerializer, \
    BallAngularContactBearingTypeDetailsSerializer, BallPersistentAndPersistentRadialBearingTypeDetailsSerializer, \
    BallRadialSphericalBearingTypeDetailsSerializer, BearingSerializer, BearingInnerTypeSerializer, BearingOuterTypeSerializer, \
    RadialNeedleRollerWithLongCylindricalRollersBearingTypeSerializer, RollerConicBearingTypeDetailsSerializer, \
    RollerPersistentAndPersistentRadialBearingTypeDetailsSerializer, ShortCylindricalRollerBearingTypeDetailsSerializer, \
    SphericalRollerBearingsAndAngularContactSphericalBearingSerializer


class ArticulatedBearingTypeDetailsSet(viewsets.ModelViewSet):
    serializer_class    = ArticulatedBearingTypeDetailsSerializer
    queryset            = ArticulatedBearingTypeDetails.objects.all()


class BallRadialAndBallRollerBearingTypeDetailsSet(viewsets.ModelViewSet):
    serializer_class    = BallRadialAndBallRollerBearingTypeDetailsSerializer
    queryset            = BallRadialAndBallRollerBearingTypeDetails.objects.all()


class BallAngularContactBearingTypeDetailsSet(viewsets.ModelViewSet):
    serializer_class    = BallAngularContactBearingTypeDetailsSerializer
    queryset            = BallAngularContactBearingTypeDetails.objects.all()


class BallPersistentAndPersistentRadialBearingTypeDetailsSet(viewsets.ModelViewSet):
    serializer_class    = BallPersistentAndPersistentRadialBearingTypeDetailsSerializer
    queryset            = BallPersistentAndPersistentRadialBearingTypeDetails.objects.all()


class BearingSet(viewsets.ModelViewSet):
    serializer_class    = BearingSerializer
    queryset            = Bearing.objects.all()


class BallRadialSphericalBearingTypeDetailsSet(viewsets.ModelViewSet):
    serializer_class    = BallRadialSphericalBearingTypeDetailsSerializer
    queryset            = BallRadialSphericalBearingTypeDetails.objects.all()


class BearingInnerTypeSet(viewsets.ModelViewSet):
    serializer_class    = BearingInnerTypeSerializer
    queryset            = BearingInnerType.objects.all()


class BearingOuterTypeSet(viewsets.ModelViewSet):
    serializer_class    = BearingOuterTypeSerializer
    queryset            = BearingOuterType.objects.all()


class RadialNeedleRollerWithLongCylindricalRollersBearingTypeSet(viewsets.ModelViewSet):
    serializer_class    = RadialNeedleRollerWithLongCylindricalRollersBearingTypeSerializer
    queryset            = RadialNeedleRollerWithLongCylindricalRollersBearingType.objects.all()


class RollerConicBearingTypeDetailsSet(viewsets.ModelViewSet):
    serializer_class    = RollerConicBearingTypeDetailsSerializer
    queryset            = RollerConicBearingTypeDetails.objects.all()


class RollerPersistentAndPersistentRadialBearingTypeDetailsSet(viewsets.ModelViewSet):
    serializer_class    = RollerPersistentAndPersistentRadialBearingTypeDetailsSerializer
    queryset            = RollerPersistentAndPersistentRadialBearingTypeDetails.objects.all()


class ShortCylindricalRollerBearingTypeDetailsSet(viewsets.ModelViewSet):
    serializer_class    = ShortCylindricalRollerBearingTypeDetailsSerializer
    queryset            = ShortCylindricalRollerBearingTypeDetails.objects.all()


class SphericalRollerBearingsAndAngularContactSphericalBearingSet(viewsets.ModelViewSet):
    serializer_class    = SphericalRollerBearingsAndAngularContactSphericalBearingSerializer
    queryset            = SphericalRollerBearingsAndAngularContactSphericalBearing.objects.all()