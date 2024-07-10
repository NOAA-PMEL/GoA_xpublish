import xarray as xr
import xpublish
from xpublish import Dependencies, Plugin, SingleDatasetRest, hookimpl

d = xr.open_dataset("/home/users/rhs/notebooks/GoA/ne_pacific_10km/json/combined.json")
grid = xr.open_dataset("/home/users/rhs/notebooks/GoA/ne_pacific_10km/json/roms_grd_nep.json")

rest_collection = xpublish.Rest({"ne_pacific_10km_data": d, "ne_pacific_10km_grid": grid})

rest_collection.serve(port=8970)
