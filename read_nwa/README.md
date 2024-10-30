## Reading a CEFI MOM6 NE Atlantic netCDF file via kerchunk on S3

To read the file, I configured an intake catalog which points to the Kerchunk index on S3 and sets up the necessary paraemeters to allow anonymous access to the S3 bucket. The intake catalog points to the Kerchunk JSON file (not directly to the netCDF file). Both files are stored on S3.

This is the [intake catalog](nwa_catalog.yml).

Reading the file is done by passing the intake catalog to xarray and returning a Dask data set. From there you can access data in the file using xarray, slicing via .sel and so on.

Here is an example [notebook](read_mom6_nea_thetao_intake.ipynb) that makes a plot of a particular time at a particular level which I selected at random.
Here is another [example notebook]() using the same intake catalog, but plotting SST.
