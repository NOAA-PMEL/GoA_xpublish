# Issue using xpublish with kerchunk file.

## The issue
When serving any (an individual time step file or the file that combines the time steps) of the kerchunk files the server throws an error:

```
ValueError: Encoding chunks do not match inferred chunks
```

However, when reading the .json kerchunk files directly everything works fine.

## The details

The kerchunk files were made with [this notebook](mk_kerchunk_goa.ipynb) using dachunks = NetCDF3ToZarr(u). I tried various max_chunksize values, but here it is with nothing.

I can read the kerchunk files directly and make a CF data set. [This notebook reads the data and shows a plot](read_json.ipynb) of the second time step to demonstate the reading kerchunk files directly works fine.

I serve the files with xpublish using [this code](server.py). I've tried serving both the merged data set (how I'd like to serve the data) and the data and the grid separately (as shown in the example).
All attempts (setting the chunks parameter to one time step, to 'auto' and leaveing it off) to serve the data give the same error.
