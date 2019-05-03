mapboxgl.accessToken =
  "pk.eyJ1IjoiaXNhYWMxNjM3IiwiYSI6ImNqdXN0ZWp0ZTAwdnk0M3BmcDk2c203eHEifQ.HaZxXmd388S6TRWuKaqADg";
var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/dark-v10",
  center: [-103.59179687498357, 40.66995747013945],
  zoom: 3
});
map.on('load', function () {
 
  map.addLayer({
  "id": "points",
  "type": "symbol",
  "source": {
  "type": "geojson",
  "data": {
  "type": "FeatureCollection",
  "features": [{
  "type": "Feature",
  "geometry": {
  "type": "Point",
  "coordinates": [-77.03238901390978, 38.913188059745586]
  },
  "properties": {
  "title": "Point 2",
  "icon": "monument"
  }
  }, {
  "type": "Feature",
  "geometry": {
  "type": "Point",
  "coordinates": [-122.414, 37.776]
  },
  "properties": {
  "title": "Point 1",
  "icon": "harbor"
  }
  }]
  }
  },
  "layout": {
  "icon-image": "{icon}-15",
  "text-field": "{title}",
  "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
  "text-offset": [0, 0.6],
  "text-anchor": "top"
  }
  });


  });
map.on("load", function() {
  // Add a new source from our GeoJSON data and set the
  // 'cluster' option to true. GL-JS will add the point_count property to your source data.
  map.addSource("earthquakes", {
    type: "geojson",
    // Point to GeoJSON data. This example visualizes all M1.0+ earthquakes
    // from 12/22/15 to 1/21/16 as logged by USGS' Earthquake hazards program.
    data: "http://localhost:3000/data.geojson",
    cluster: true,
    clusterMaxZoom: 14, // Max zoom to cluster points on
    clusterRadius: 50 // Radius of each cluster when clustering points (defaults to 50)
  });

  map.addLayer({
    id: "clusters",
    type: "circle",
    source: "earthquakes",
    filter: ["has", "point_count"],
    paint: {
      // Use step expressions (https://docs.mapbox.com/mapbox-gl-js/style-spec/#expressions-step)
      // with three steps to implement three types of circles:
      //   * Blue, 20px circles when point count is less than 100
      //   * Yellow, 30px circles when point count is between 100 and 750
      //   * Pink, 40px circles when point count is greater than or equal to 750
      "circle-color": [
        "step",
        ["get", "point_count"],
        "#51bbd6",
        5,
        "#f1f075",
        10,
        "#f28cb1"
      ],
      "circle-radius": ["step", ["get", "point_count"], 20, 5, 30, 10, 40]
    }
  });

  map.addLayer({
    id: "cluster-count",
    type: "symbol",
    source: "earthquakes",
    filter: ["has", "point_count"],
    layout: {
      "text-field": "{point_count_abbreviated}",
      "text-font": ["DIN Offc Pro Medium", "Arial Unicode MS Bold"],
      "text-size": 12
    }
  });

  map.addLayer({
    id: "unclustered-point",
    type: "circle",
    source: "earthquakes",
    filter: ["!", ["has", "point_count"]],
    paint: {
      "circle-color": "#11b4da",
      "circle-radius": 4,
      "circle-stroke-width": 1,
      "circle-stroke-color": "#fff"
    }
  });

  // inspect a cluster on click
  map.on("click", "clusters", function(e) {
    var features = map.queryRenderedFeatures(e.point, { layers: ["clusters"] });
    var clusterId = features[0].properties.cluster_id;
    map
      .getSource("earthquakes")
      .getClusterExpansionZoom(clusterId, function(err, zoom) {
        if (err) return;

        map.easeTo({
          center: features[0].geometry.coordinates,
          zoom: zoom
        });
      });
  });

  map.on("mouseenter", "clusters", function(d) {
    console.log(d);
    map.getCanvas().style.cursor = "pointer";
  });
  map.on("mouseleave", "clusters", function() {
    map.getCanvas().style.cursor = "";
  });
});
