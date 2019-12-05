from rest_framework import serializers
from .models import ArticulatedBearingTypeDetails, BallRadialAndBallRollerBearingTypeDetails, \
    BallAngularContactBearingTypeDetails, BallPersistentAndPersistentRadialBearingTypeDetails, \
    BallRadialSphericalBearingTypeDetails, Bearing, BearingInnerType, BearingOuterType, \
    RadialNeedleRollerWithLongCylindricalRollersBearingType, RollerConicBearingTypeDetails, \
    RollerPersistentAndPersistentRadialBearingTypeDetails, ShortCylindricalRollerBearingTypeDetails, SphericalRollerBearingsAndAngularContactSphericalBearing


class ArticulatedBearingTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticulatedBearingTypeDetails
        fields = ('id', 'diameter_of_spheres_of_bearing_rings', 'radius_of_mounting_bevel_of_bearing',
                  'diameter_of_intersection_of_sphere_with_end_face_of_bearing_rin',
                  'width_of_outer_ring_of_bearing', 'width_of_inner_ring_of_bearing',
                  'bearing')


class BallRadialAndBallRollerBearingTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BallRadialAndBallRollerBearingTypeDetails
        fields = ('id', 'width_of_inner_ring_of_bearing_together_with_eccentric_ring',
                  'dynamic_load_capacity', 'diameter_of_groove_under_snap_ring',
                  'width_of_groove_under_snap_ring', 'nominal_bushing_inner_diameter',
                  'distance_from_edge_of_inner_ring_of_bearing_to_middle_of_racewa',
                  'distance_between_outer_ring_of_bearing_and_axis_of_roller_bore',
                  'distance_from_axis_of_lubrication_hole_to_middle_of_raceway',
                  'diameter_of_roller_hole', 'outer_diameter_of_thrust_side',
                  'axis_of_axis_of_locking_groove_of_shaft', 'width_of_inner_ring_of_bearing',
                  'width_of_outer_ring_of_bearing', 'length_of_roller_field', 'bearing_width',
                  'bearing')


class BallAngularContactBearingTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BallAngularContactBearingTypeDetails
        fields = ('id', 'radius_of_mounting_chamfer_bearing',
                  'dynamic_payload', 'static_payload',
                  'bearing_width', 'bearing')


class BallPersistentAndPersistentRadialBearingTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BallPersistentAndPersistentRadialBearingTypeDetails
        fields = ('id', 'diameter_of_hole_in_washer',
                  'nominal_height_of_washer', 'static_payload',
                  'width_of_tight_bearing_ring', 'outer_diameter_of_free_ring',
                  'radius_of_mounting_bevel_of_bearing', 'diameter_of_hole_tight_ring',
                  'nominal_bearing_height_with_washer', 'height_of_center_of_radius_of_spherical_support_ring',
                  'outer_diameter_of_tight_ring_of_double_bearing', 'dynamic_payload', 'diameter_of_holes_of_free_ring',
                  'diameter_of_hole_tight_ring_double_bearing', 'outer_diameter_of_washer', 'bearing_height',
                  'bearing_width', 'outer_diameter_of_tight_ring', 'nominal_height_of_tight_double_bearing_ring',
                  'radius_of_spherical_bearing_face_of_free_bearing_ring_and_spher', 'width_of_free_ring_of_bearing',
                  'bearing')


class BallRadialSphericalBearingTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BallRadialSphericalBearingTypeDetails
        fields = ('id', 'radius_of_mounting_bevel_of_bearing',
                  'static_payload', 'width_of_inner_ring_of_bearing',
                  'size_of_balls_protruding_symmetrically_beyond_width_of_bearing', 'dynamic_payload',
                  'nominal_diameter_of_sleeve', 'width_of_outer_ring_of_bearing',
                  'bearing_width', 'bearing')


class BearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bearing
        fields = ('id', 'gost_name', 'international_name', 'gost_type', 'sub_type',
                  'weight', 'inner_diameter', 'outer_diameter', 'bearing_inner_type')


class BearingInnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BearingInnerType
        fields = ('id', 'name', 'image', 'bearing_outer_type')


class BearingOuterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BearingOuterType
        fields = ('id', 'name')


class RadialNeedleRollerWithLongCylindricalRollersBearingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadialNeedleRollerWithLongCylindricalRollersBearingType
        fields = ('id', 'static_payload', 'dynamic_carrying_capacity', 'bearing_width',
                  'nominal_thickness_of_flat_bottom_of_outer_ring', 'radius_of_mounting_bevel_of_bearing',
                  'nominal_diameter_of_circle_inscribed_in_set_of_rolling_elements', 'nominal_diameter_of_circle_described_around_set_of_rolling_bodi',
                  'nominal_width_of_profiled_bottom_of_outer_ring', 'bearing')


class RollerConicBearingTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollerConicBearingTypeDetails
        fields = ('id', 'static_payload', 'dynamic_payload', 'width_of_outer_distance_ring',
                  'outer_diameter_of_thrust_side', 'distance_from_end_to_axis_of_lubrication_holes',
                  'thrust_side_height', 'width_of_outer_ring_of_bearing', 'width_of_thrust_side',
                  'width_of_inner_distance_ring', 'width_of_inner_ring_of_bearing', 'bearing_height', 'radius_of_mounting_bevel_of_bearing',
                  'diameter_of_grease_hole', 'bearing')


class RollerPersistentAndPersistentRadialBearingTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollerPersistentAndPersistentRadialBearingTypeDetails
        fields = ('id', 'outer_diameter_of_tight_ring', 'dynamic_payload', 'height_of_free_ring',
                  'distance_from_end_of_tight_ring_to_center_of_radius_of_sphere', 'roller_diameter',
                  'outer_diameter_of_free_ring', 'bearing_height', 'diameter_of_hole_tight_ring',
                  'outer_diameter_of_separator', 'static_payload', 'radius_of_mounting_bevel_of_bearing',
                  'diameter_of_holes_of_separator', 'diameter_of_holes_of_free_ring_field', 'bearing')


class ShortCylindricalRollerBearingTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortCylindricalRollerBearingTypeDetails
        fields = ('id', 'nominal_width_of_side', 'bearing_width', 'static_payload',
                  'nominal_value_of_protrusion_of_distance_ring_beyond_end_of_inne', 'nominal_value_of_protrusion_of_shaped_thrust_ring_beyond_end_of',
                  'dynamic_payload', 'radius_of_mounting_bevel_of_bearing', 'nominal_diameter_of_circle_inscribed_in_set_of_rolling_elements', 'bearing')



class SphericalRollerBearingsAndAngularContactSphericalBearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SphericalRollerBearingsAndAngularContactSphericalBearing
        fields = ('id', 'radius_of_mounting_bevel_of_bearing_field', 'static_payload', 'dynamic_payload',
                  'nominal_bushing_inner_diameter', 'bearing_width', 'bearing')
