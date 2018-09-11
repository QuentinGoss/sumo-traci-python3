# <a name="top_of_page"></a>modules
[Point of Interest](#poi) , [Vehicle](#vehicle)
>Quentin: This section contains notes about the various python modules we created.
>
>[Sumo + TraCI Home](../Readme.md)

---
<!-- begin poi -->
## <a name="poi"></a>Point of Interest
[Top](#top_of_page)

A class created to manage Point of Interest (POI) nodes featuring coordinates, values, increase/decrease and vehicle hit methods.
Useful code:
```
# Importing the POI library
import poi

# Initializing a POI object
# closest_edge = (edge_ID,x,y)
# poi.poi(id,x,y,value,closest_edge)
o_poi = poi.poi("veh0",30.0,25.0,50,("gneE15",15.4,10.3))
```
<!-- end poi -->
---
<!-- begin vehicle -->
## <a name="vehicle"></a>Vehicle
[Top](#top_of_page)

A class created to manage Vehicles featuring edge/POI memory and capacity.
Useful code:
```
# Importing the Vehicle library
import vehicle

#Initializing a Vehicle object
# vehicle.vehicle(id)
o_veh = vehicle.vehicle("veh0")
```
<!-- end vehicle -->
