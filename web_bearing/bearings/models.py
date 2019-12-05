# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArticulatedBearingTypeDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    diameter_of_spheres_of_bearing_rings = models.TextField(blank=True, null=True)
    radius_of_mounting_bevel_of_bearing = models.TextField(blank=True, null=True)
    diameter_of_intersection_of_sphere_with_end_face_of_bearing_rin = models.TextField(blank=True, null=True)
    width_of_outer_ring_of_bearing = models.TextField(blank=True, null=True)
    width_of_inner_ring_of_bearing = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey('Bearing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'articulated_bearing_type_details'


class BallRadialAndBallRollerBearingTypeDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    width_of_inner_ring_of_bearing_together_with_eccentric_ring = models.TextField(blank=True, null=True)
    dynamic_load_capacity = models.TextField(blank=True, null=True)
    diameter_of_groove_under_snap_ring = models.TextField(blank=True, null=True)
    width_of_groove_under_snap_ring = models.TextField(blank=True, null=True)
    nominal_bushing_inner_diameter = models.TextField(blank=True, null=True)
    distance_from_edge_of_inner_ring_of_bearing_to_middle_of_racewa = models.TextField(blank=True, null=True)
    distance_between_outer_ring_of_bearing_and_axis_of_roller_bore = models.TextField(blank=True, null=True)
    distance_from_axis_of_lubrication_hole_to_middle_of_raceway = models.TextField(blank=True, null=True)
    diameter_of_roller_hole = models.TextField(blank=True, null=True)
    outer_diameter_of_thrust_side = models.TextField(blank=True, null=True)
    axis_of_axis_of_locking_groove_of_shaft = models.TextField(blank=True, null=True)
    width_of_inner_ring_of_bearing = models.TextField(blank=True, null=True)
    width_of_outer_ring_of_bearing = models.TextField(blank=True, null=True)
    length_of_roller_field = models.TextField(db_column='length_of_roller ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bearing_width = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey('Bearing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ball_ radial_ and_ball-roller_bearing_type_details'


class BallAngularContactBearingTypeDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    radius_of_mounting_chamfer_bearing = models.TextField(blank=True, null=True)
    dynamic_payload = models.TextField(blank=True, null=True)
    static_payload = models.TextField(blank=True, null=True)
    bearing_width = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey('Bearing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ball_angular_contact_bearing_type_details'


class BallPersistentAndPersistentRadialBearingTypeDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    diameter_of_hole_in_washer = models.TextField(blank=True, null=True)
    nominal_height_of_washer = models.TextField(blank=True, null=True)
    static_payload = models.TextField(blank=True, null=True)
    width_of_tight_bearing_ring = models.TextField(blank=True, null=True)
    outer_diameter_of_free_ring = models.TextField(blank=True, null=True)
    radius_of_mounting_bevel_of_bearing = models.TextField(blank=True, null=True)
    diameter_of_hole_tight_ring = models.TextField(blank=True, null=True)
    nominal_bearing_height_with_washer = models.TextField(blank=True, null=True)
    height_of_center_of_radius_of_spherical_support_ring = models.TextField(blank=True, null=True)
    outer_diameter_of_tight_ring_of_double_bearing = models.TextField(blank=True, null=True)
    dynamic_payload = models.TextField(blank=True, null=True)
    diameter_of_holes_of_free_ring = models.TextField(blank=True, null=True)
    diameter_of_hole_tight_ring_double_bearing = models.TextField(blank=True, null=True)
    outer_diameter_of_washer = models.TextField(blank=True, null=True)
    bearing_height = models.TextField(blank=True, null=True)
    bearing_width = models.TextField(blank=True, null=True)
    outer_diameter_of_tight_ring = models.TextField(blank=True, null=True)
    nominal_height_of_tight_double_bearing_ring = models.TextField(blank=True, null=True)
    radius_of_spherical_bearing_face_of_free_bearing_ring_and_spher = models.TextField(blank=True, null=True)
    width_of_free_ring_of_bearing = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey('Bearing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ball_persistent_and_persistent_radial_bearing_type_details'


class BallRadialSphericalBearingTypeDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    radius_of_mounting_bevel_of_bearing = models.TextField(blank=True, null=True)
    static_payload = models.TextField(blank=True, null=True)
    width_of_inner_ring_of_bearing = models.TextField(blank=True, null=True)
    size_of_balls_protruding_symmetrically_beyond_width_of_bearing = models.TextField(blank=True, null=True)
    dynamic_payload = models.TextField(blank=True, null=True)
    nominal_diameter_of_sleeve = models.TextField(blank=True, null=True)
    width_of_outer_ring_of_bearing = models.TextField(blank=True, null=True)
    bearing_width = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey('Bearing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ball_radial_spherical_bearing_type_details'


class Bearing(models.Model):
    id = models.BigAutoField(primary_key=True)
    gost_name = models.TextField()
    international_name = models.TextField(blank=True, null=True)
    gost_type = models.TextField(blank=True, null=True)
    sub_type = models.TextField(blank=True, null=True)
    weight = models.TextField()
    inner_diameter = models.TextField(blank=True, null=True)
    outer_diameter = models.TextField(blank=True, null=True)
    bearing_inner_type = models.ForeignKey('BearingInnerType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bearing'


class BearingInnerType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    image = models.TextField()
    bearing_outer_type = models.ForeignKey('BearingOuterType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bearing_inner_type'


class BearingOuterType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'bearing_outer_type'


class RadialNeedleRollerWithLongCylindricalRollersBearingType(models.Model):
    id = models.BigAutoField(primary_key=True)
    static_payload = models.TextField(blank=True, null=True)
    dynamic_carrying_capacity = models.TextField(blank=True, null=True)
    bearing_width = models.TextField(blank=True, null=True)
    nominal_thickness_of_flat_bottom_of_outer_ring = models.TextField(blank=True, null=True)
    radius_of_mounting_bevel_of_bearing = models.TextField(blank=True, null=True)
    nominal_diameter_of_circle_inscribed_in_set_of_rolling_elements = models.TextField(blank=True, null=True)
    nominal_diameter_of_circle_described_around_set_of_rolling_bodi = models.TextField(blank=True, null=True)
    nominal_width_of_profiled_bottom_of_outer_ring = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey(Bearing, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'radial_needle_roller_with_long_cylindrical_rollers_bearing_type'


class RollerConicBearingTypeDetails(models.Model):
    static_payload = models.TextField(blank=True, null=True)
    dynamic_payload = models.TextField(blank=True, null=True)
    width_of_outer_distance_ring = models.TextField(blank=True, null=True)
    outer_diameter_of_thrust_side = models.TextField(blank=True, null=True)
    distance_from_end_to_axis_of_lubrication_holes = models.TextField(blank=True, null=True)
    thrust_side_height = models.TextField(blank=True, null=True)
    width_of_outer_ring_of_bearing = models.TextField(blank=True, null=True)
    width_of_thrust_side = models.TextField(blank=True, null=True)
    width_of_inner_distance_ring = models.TextField(blank=True, null=True)
    width_of_inner_ring_of_bearing = models.TextField(blank=True, null=True)
    bearing_height = models.TextField(blank=True, null=True)
    radius_of_mounting_bevel_of_bearing = models.TextField(blank=True, null=True)
    diameter_of_grease_hole = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey(Bearing, models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'roller_conic_bearing_type_details'


class RollerPersistentAndPersistentRadialBearingTypeDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    outer_diameter_of_tight_ring = models.TextField(blank=True, null=True)
    dynamic_payload = models.TextField(blank=True, null=True)
    height_of_free_ring = models.TextField(blank=True, null=True)
    distance_from_end_of_tight_ring_to_center_of_radius_of_sphere = models.TextField(blank=True, null=True)
    roller_diameter = models.TextField(blank=True, null=True)
    outer_diameter_of_free_ring = models.TextField(blank=True, null=True)
    bearing_height = models.TextField(blank=True, null=True)
    diameter_of_hole_tight_ring = models.TextField(blank=True, null=True)
    outer_diameter_of_separator = models.TextField(blank=True, null=True)
    static_payload = models.TextField(blank=True, null=True)
    radius_of_mounting_bevel_of_bearing = models.TextField(blank=True, null=True)
    diameter_of_holes_of_separator = models.TextField(blank=True, null=True)
    diameter_of_holes_of_free_ring_field = models.TextField(db_column='diameter_of_holes_of_free_ring ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bearing = models.ForeignKey(Bearing, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'roller_persistent_and_persistent_radial_bearing_type_details'


class ShortCylindricalRollerBearingTypeDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    nominal_width_of_side = models.TextField(blank=True, null=True)
    bearing_width = models.TextField(blank=True, null=True)
    static_payload = models.TextField(blank=True, null=True)
    nominal_value_of_protrusion_of_distance_ring_beyond_end_of_inne = models.TextField(blank=True, null=True)
    nominal_value_of_protrusion_of_shaped_thrust_ring_beyond_end_of = models.TextField(blank=True, null=True)
    dynamic_payload = models.TextField(blank=True, null=True)
    radius_of_mounting_bevel_of_bearing = models.TextField(blank=True, null=True)
    nominal_diameter_of_circle_inscribed_in_set_of_rolling_elements = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey(Bearing, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'short_cylindrical_roller_bearing_type_details'


class SphericalRollerBearingsAndAngularContactSphericalBearing(models.Model):
    id = models.BigAutoField(primary_key=True)
    radius_of_mounting_bevel_of_bearing_field = models.TextField(db_column='radius_of_mounting_bevel_of_bearing ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    static_payload = models.TextField(blank=True, null=True)
    dynamic_payload = models.TextField(blank=True, null=True)
    nominal_bushing_inner_diameter = models.TextField(blank=True, null=True)
    bearing_width = models.TextField(blank=True, null=True)
    bearing = models.ForeignKey(Bearing, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spherical_roller_bearings_and_angular_contact_spherical_bearing'
