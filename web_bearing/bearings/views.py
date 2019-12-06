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


class ArticulatedBearingTypeDetailsViewSet(viewsets.ModelViewSet):
    serializer_class    = ArticulatedBearingTypeDetailsSerializer
    queryset            = ArticulatedBearingTypeDetails.objects.all()


class BallRadialAndBallRollerBearingTypeDetailsViewSet(viewsets.ModelViewSet):
    serializer_class    = BallRadialAndBallRollerBearingTypeDetailsSerializer
    queryset            = BallRadialAndBallRollerBearingTypeDetails.objects.all()


class BallAngularContactBearingTypeDetailsViewSet(viewsets.ModelViewSet):
    serializer_class    = BallAngularContactBearingTypeDetailsSerializer
    queryset            = BallAngularContactBearingTypeDetails.objects.all()


class BallPersistentAndPersistentRadialBearingTypeDetailsViewSet(viewsets.ModelViewSet):
    serializer_class    = BallPersistentAndPersistentRadialBearingTypeDetailsSerializer
    queryset            = BallPersistentAndPersistentRadialBearingTypeDetails.objects.all()


class BearingViewSet(viewsets.ModelViewSet):
    serializer_class    = BearingSerializer
    queryset            = Bearing.objects.all()


class BallRadialSphericalBearingTypeDetailsViewSet(viewsets.ModelViewSet):
    serializer_class    = BallRadialSphericalBearingTypeDetailsSerializer
    queryset            = BallRadialSphericalBearingTypeDetails.objects.all()


class BearingInnerTypeViewSet(viewsets.ModelViewSet):
    serializer_class    = BearingInnerTypeSerializer
    queryset            = BearingInnerType.objects.all()


class BearingOuterTypeViewSet(viewsets.ModelViewSet):
    serializer_class    = BearingOuterTypeSerializer
    queryset            = BearingOuterType.objects.all()


class RadialNeedleRollerWithLongCylindricalRollersBearingTypeViewSet(viewsets.ModelViewSet):
    serializer_class    = RadialNeedleRollerWithLongCylindricalRollersBearingTypeSerializer
    queryset            = RadialNeedleRollerWithLongCylindricalRollersBearingType.objects.all()


class RollerConicBearingTypeDetailsViewSet(viewsets.ModelViewSet):
    serializer_class    = RollerConicBearingTypeDetailsSerializer
    queryset            = RollerConicBearingTypeDetails.objects.all()


class RollerPersistentAndPersistentRadialBearingTypeDetailsViewSet(viewsets.ModelViewSet):
    serializer_class    = RollerPersistentAndPersistentRadialBearingTypeDetailsSerializer
    queryset            = RollerPersistentAndPersistentRadialBearingTypeDetails.objects.all()


class ShortCylindricalRollerBearingTypeDetailsViewSet(viewsets.ModelViewSet):
    serializer_class    = ShortCylindricalRollerBearingTypeDetailsSerializer
    queryset            = ShortCylindricalRollerBearingTypeDetails.objects.all()


class SphericalRollerBearingsAndAngularContactSphericalBearingViewSet(viewsets.ModelViewSet):
    serializer_class    = SphericalRollerBearingsAndAngularContactSphericalBearingSerializer
    queryset            = SphericalRollerBearingsAndAngularContactSphericalBearing.objects.all()