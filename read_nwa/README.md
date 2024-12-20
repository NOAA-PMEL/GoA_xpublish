## Reading a CEFI MOM6 NW Atlantic netCDF file via kerchunk on S3

If you don't have a python environment already, you can use the [environment.yml](environment.yml) file to create everything you need to run the notebook, read and plot the data. If you already have a environment set up, you can compare your module list to the one provided to see what you might be missing. I tested this using Python 3.13.0. The Python version is not specified here, but you can a specific verion to the environment file if needed. 

## Examples for each type of output

### northwest_atlantic/full_domain/seasonal_reforecast/monthly/regrid/r20240213

There is a JSON Kerchunk index which aggregates this collection into a single index which you can use to access the entire data set. This example notebook uses that index (called all.json) and plots one initialization, lead and ensember member over the entire region).

[Example reading and plotting SST.](read_nwa_seasonal_reforecast_monthly_regird_s3.ipynb)

This directory contains 205 files of seasonal (March, June, September and December) which you can access indivdually if you'd like by downloading the appropriate .json index and accessing it as we did the combined file in the example notebook.
