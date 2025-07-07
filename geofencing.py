import geopy.distance

from geopy.distance import great_circle

class Geofencing:
    def __init__(self, campus_center, radius):
        self.campus_center = campus_center
        self.radius = radius
    
    def is_within_geofence(self, current_location):
        distance = great_circle(self.campus_center, current_location).meters
        return distance <= self.radius

# Define your college campus center coordinates and radius (in meters)
campus_center = (17.438188, 78.716631)  # Actual coordinates
radius = 500  # Example radius in meters

# Create geofencing object
geofence = Geofencing(campus_center, radius)
