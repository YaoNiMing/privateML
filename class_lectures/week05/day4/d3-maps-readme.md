# Maps

In this class we'll equip you to make two very common forms of maps – **Choropleth** and **Bubble**.

## Examples

Just like with charting, mapping is all about what you want to show. There's no such thing as the perfect form, especially with maps. A few examples:
  
  * [Presidential vote](http://elections.nytimes.com/2012/results/president)
  * [Emphasizing change](http://www.nytimes.com/interactive/2012/11/07/us/politics/obamas-diverse-base-of-support.html)
  * [Extremely detailed Senate election maps](http://www.nytimes.com/interactive/2014/11/04/upshot/senate-maps.html)
  * [House districts are hard](http://elections.nytimes.com/2014/results/house), and sometimes [maps shouldn't be maps](http://www.ericson.net/content/2011/10/when-maps-shouldnt-be-maps/)

## Basic principles of GIS

Why use TopoJSON?

1. Let's download some data from the Census. How about a [big shapefile](https://www.census.gov/cgi-bin/geo/shapefiles2010/main) of counties? Download and unzip the 2010 counties file `tl_2010_us_county10` to your local project folder. 

1. If you have a GIS program, like QGis, feel free to inspect your shapefile there. Otherwise...

2. Let's go to Matthew Bloch's amazing [MapShaper.org](http://mapshaper.org/). Drag your `.shp` file to the browser and choose "simplify." See what happens to the file size as you move the slider.

3. Export the map as both TopoJSON and GeoJSON. Notice any difference?

4. Let's [look](http://bost.ocks.org/mike/simplify/) at how that difference in file size happens.

5. In a nutshell, that's all we need to know about TopoJSON: it's really good at reducing file size. It can do hard spatial things too, but for now let's focus on using TopoJSON files someon else has already prepared for us. If you want to do fancier things, [start installing command-line tools](http://bost.ocks.org/mike/map/#installing-tools).


## Helpful links

  * Mike's helpful [tutorial series](http://bost.ocks.org/mike/map/).
  * [Let's make a bubble map](https://bost.ocks.org/mike/bubble-map/) - in d3-maps-bubble folder
  * [When Maps Shouldn't Be Maps](http://www.ericson.net/content/2011/10/when-maps-shouldnt-be-maps/) by Matt Ericson, NYT Big Dog
  * [Sickening examples](https://www.jasondavies.com/maps/) from Jason Davies
  * Mike's [US Atlas](https://github.com/mbostock/us-atlas)
  * Matt Bloch's amazing [Mapshapr](http://mapshaper.org/)
  * [QGIS](http://www.qgis.org/en/site/) is excellent, free GIS software 
  * [Every ColorBrewer scale](http://bl.ocks.org/mbostock/5577023)
