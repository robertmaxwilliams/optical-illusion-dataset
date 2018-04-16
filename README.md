# optical-illusion-dataset
JSON files with image links and metadata for optical illusions. Stay tuned as it grows and the images are released in gzip format from University host

## Files:
* mo-scraper.py:  final version of web scraping script for moillusions
* moillusions_data.json:  json of image URLs and metadata for moillusions
* mo-downloader.py: downloades images linked in JSON above into data/

* viper-scraper.py: viperlib scraper script
* viperlib_data.json: viperlib image URLs and metadata
* viper-downloader.py: downloades images linked in JSON above into data/

## Sources:

6436 image links and metadata from https://www.moillusions.com/

1454 image links and metadata from http://viperlib.york.ac.uk/

## Download JPEGs:

The full image download can be found here (**6725** images) :

<https://www.floydhub.com/robertmax/datasets/illusions-jpg>

A greatly reduced dataset of only images that have eye-bending patterns is here (**569** images, hand picked):

<https://www.floydhub.com/robertmax/datasets/illusions-filtered>

## My dataset build procese: 
If you want to replicate it, for more latest images, or if some weird bug appears and documentation becomes important:
- run a scraper to make the JSON file of all images
- run a downloader to download images to data/
- make sure `rename`, `mogrify`, and `file` are installed on your system
- run `bash cleanconvert.sh` to convert everything to jpg, and verify all images using `file`
- Investigate lines printed out, but I doubt you'll get anything unless you're unlucky
- look in data/ if it has lots of #####.jpg and nothing else
- rename data/ to something like viper-data/ etc

## Next steps
- come up with a scheme to combine website provided categories (some effort towards this in `combiner.py`)
- train a GAN on the filtered images
- learn a latent space for the images and do dimensionality reduction of some sort on it
