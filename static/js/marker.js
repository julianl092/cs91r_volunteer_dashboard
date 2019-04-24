mapboxgl.accessToken =
  "pk.eyJ1IjoiaXNhYWMxNjM3IiwiYSI6ImNqdXN0ZWp0ZTAwdnk0M3BmcDk2c203eHEifQ.HaZxXmd388S6TRWuKaqADg";

var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11"
});
L.marker([50.5, 30.5]).addTo(map);
// map.on("load", function() {
//   map.loadImage(
//     "https://upload.wikimedia.org/wikipedia/commons/1/14/Map_Icon_-_Dining.png",
//     function(error, image) {
//       if (error) throw error;
//       map.addImage("cat", image);
//       map.addLayer({
//         id: "points",
//         type: "symbol",
//         source: {
//           type: "geojson",
//           data: {
//             type: "FeatureCollection",
//             features: [
//               {
//                 type: "Feature",
//                 geometry: {
//                   type: "Point",
//                   coordinates: [1, 0]
//                 }
//               }
//             ]
//           }
//         },
//         layout: {
//           "icon-image": "cat",
//           "icon-size": 0.0001
//         }
//       });
//     }
//   );
// });
