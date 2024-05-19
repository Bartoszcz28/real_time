import math

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculates the distance between two points on the Earth's surface
    using the Haversine formula.

    Parameters:
    lon1, lat1 -- longitude and latitude of the first point
    lon2, lat2 -- longitude and latitude of the second point

    Returns:
    The distance between the two points in kilometers
    """
    # Convert degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Difference in longitude and latitude
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula components
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Earth's radius in kilometers (average)
    r = 6371.0

    # Calculate the distance
    distance = c * r

    return distance
