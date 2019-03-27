var margin = { top: 10, right: 10, bottom: 10, left: 500 },
  width = window.innerWidth - margin.left - margin.right, // Use the window's width
  height = window.innerHeight - margin.top - margin.bottom; // Use the window's height

//MAP
var active = d3.select(null);
var svg = d3
  .select(".hero-body")
  .append("svg")
  .attr("class", "center-container")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom);

svg
  .append("rect")
  .attr("class", "background-center-container")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .on("click", clicked);

d3.json("https://d3js.org/us-10m.v1.json")
  .then(ready)
  .catch(function(error) {
    console.log(error);
  });

var projection = d3
  .geoAlbers()
  .translate([width / 2.5, height / 2.5])
  .scale(width / 5);

var path = d3.geoPath();
// .projection(projection);

var g = svg
  .append("g")
  .attr("class", "center-container center-items us-state")
  //.attr('transform', 'translate('+margin.left+','+margin.top+')')
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom);

function ready(us) {
  g.append("g")
    .attr("id", "counties")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.counties).features)
    .enter()
    .append("path")
    .attr("d", path)
    .attr("class", "county-boundary")
    .on("click", reset);

  g.append("g")
    .attr("id", "states")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.states).features)
    .enter()
    .append("path")
    .attr("d", path)
    .attr("class", "state")
    .on("click", clicked);

  g.append("path")
    .datum(
      topojson.mesh(us, us.objects.states, function(a, b) {
        return a !== b;
      })
    )
    .attr("id", "state-borders")
    .attr("d", path);

  var marks = [
    { long: 120, lat: 90 },
    { long: 160, lat: 115 },
    { long: 200, lat: 150 }
  ];

  svg
    .selectAll(".mark")
    .data(marks)
    .enter()
    .append("image")
    .attr("class", "mark")
    .attr("width", 20)
    .attr("height", 20)
    .attr(
      "xlink:href",
      "https://cdn3.iconfinder.com/data/icons/softwaredemo/PNG/24x24/DrawingPin1_Blue.png"
    )
    .attr("transform", d => "translate(" + d.long + "," + d.lat + ")");
}

function clicked(d) {
  if (d3.select(".background").node() === this) return reset();

  if (active.node() === this) return reset();

  active.classed("active", false);
  active = d3.select(this).classed("active", true);

  var bounds = path.bounds(d),
    dx = bounds[1][0] - bounds[0][0],
    dy = bounds[1][1] - bounds[0][1],
    x = (bounds[0][0] + bounds[1][0]) / 2,
    y = (bounds[0][1] + bounds[1][1]) / 2,
    scale = 0.9 / Math.max(dx / width, dy / height),
    translate = [width / 2 - scale * x, height / 2 - scale * y];

  g //.transition()
    // .delay(100)
    //.duration(750)
    .style("stroke-width", 1.5 / scale + "px")
    .attr("transform", "translate(" + translate + ")scale(" + scale + ")");

  svg
    .selectAll(".mark")
    .attr("transform", "translate(" + translate + ")scale(" + scale + ")");
}
function reset() {
  active.classed("active", false);
  d3.active = d3.select(null);

  g //.transition()
    //  .delay(100)
    //  .duration(1000)
    .style("stroke-width", "1.5px")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
}
