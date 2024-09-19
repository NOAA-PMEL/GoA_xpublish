# Reading S3 from EC2 instance and extenal server.

## Summary:

The goal is to test providing access to large model outputs via S3 and Kurchunk. Eventually we hope the data will be hosted as part of NODD so the access will be unrestricted for all users. However, we don't know the access time will be good enough for use by CEFI scientists and the data portal.

To test this we want to make a sample available to a variety of users (currently all within NOAA).

## Results:

By setting the bucket to "publically readable" I can read it when [running a notebook](https://github.com/NOAA-PMEL/GoA_xpublish/blob/main/read_s3/read_goa_kerchunk-s3.ipynb) on an EC2 instance at AWS without as far as I can tell providing credentials.

However, when I try the [same notebook](https://github.com/NOAA-PMEL/GoA_xpublish/blob/main/read_s3/read_goa_kerchunk-s3_from_pmel.ipynb) form pmel.noaa.gov I get an error:

NoCredentialsError: Unable to locate credentials
