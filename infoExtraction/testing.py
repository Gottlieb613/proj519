import geopandas as gpd
import numpy as np

def create_grid_from_shapefile(shapefile_path, lat_step, lon_step):
    """
    Create a latitude and longitude grid within the bounding box of a shapefile.
    
    Parameters:
        shapefile_path (str): Path to the shapefile.
        lat_step (float): Step size for latitude.
        lon_step (float): Step size for longitude.
    
    Returns:
        list of tuples: List of (latitude, longitude) tuples representing the grid.
    """
    # Load the shapefile
    gdf = gpd.read_file(shapefile_path)

    # If the CRS is not in geographic (latitude-longitude), convert it
    if gdf.crs.to_string() != 'EPSG:4326':
        gdf = gdf.to_crs(epsg=4326)

    
    # Get the total bounding box of all geometries in the shapefile
    bounds = gdf.total_bounds  # returns (minx, miny, maxx, maxy)
    west, south, east, north = bounds
    
    # Generate grid coordinates
    latitudes = np.arange(south, north + lat_step, lat_step)
    longitudes = np.arange(west, east + lon_step, lon_step)
    
    grid = []
    for lat in latitudes:
        for lon in longitudes:
            grid.append((lat, lon))
    
    return grid

# Path to your shapefile
shapefile_path = 'gbShapeFile/gb_10km.shp'

# Define the size of each grid cell (e.g., 0.1 degrees)
lat_step = 1
lon_step = 1

# Generate the grid from the shapefile
grid = create_grid_from_shapefile(shapefile_path, lat_step, lon_step)

# Optionally, print the grid
for point in grid:
    print(point)
