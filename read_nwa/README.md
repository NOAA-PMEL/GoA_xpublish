## Reading a CEFI MOM6 NE Atlantic netCDF file via kerchunk on S3

If you don't have a python environment already, you can use the [environment.yml](environment.yml) file to create everything you need to run the notebook, read and plot the data. If you already have a environment set up, you can compare your module list to the one provided to see what you might be missing. I tested this using Python 3.13.0. The Python version is not specified here, but you can a specific verion to the environment file if needed. 

To read the file, I configured an intake catalog which points to the Kerchunk index on S3 and sets up the necessary paraemeters to allow anonymous access to the S3 bucket. The intake catalog points to the Kerchunk JSON file (not directly to the netCDF file). Both files are stored on S3.

This is the [intake catalog](nwa_catalog.yml).

Reading the file is done by passing the intake catalog to xarray and returning a Dask data set. From there you can access data in the file using xarray, slicing via .sel and so on.

Here is an example [notebook](read_mom6_nea_thetao_intake.ipynb) that makes a plot of a particular time at a particular level which I selected at random.
Here is another [example notebook](read_mom6_nwa_tos.ipynb) using the same intake catalog, but plotting SST.
