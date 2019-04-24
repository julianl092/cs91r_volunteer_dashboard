var chartDiv = document.getElementById("mapChart");
var margin = { top: 10, right: 10, bottom: 10, left: 500 },
  width = chartDiv.clientWidth,
  height = chartDiv.clientHeight;

print("height");
print(height);

//MAP
var active = d3.select(null);
var svg = d3
  .select(".mapChart")
  .append("svg")
  .attr("class", "center-container")
  .attr("width", width / 2.2 + margin.left + margin.right)
  .attr("height", height / 2 + margin.top + margin.bottom);

svg
  .append("rect")
  .attr("class", "background-center-container")
  .attr("width", width / 2.2 + margin.left + margin.right)
  .attr("height", height / 2 + margin.top + margin.bottom)
  .on("click", clicked);

//var clickStore;
//var scaleStore;
d3.json("https://d3js.org/us-10m.v1.json")
  .then(ready)
  .catch(function(error) {
    console.log(error);
  });

var projection = d3
  .geoAlbers()
  .translate([width / 2.5, height / 2.5])
  .scale(width / 5);

var path = d3.geoPath().projection(projection);

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
    .attr("width", width / 2.2)
    .attr("height", width / 2)
    .attr("class", "county-boundary")
    .on("click", reset);

  g.append("g")
    .attr("id", "states")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.states).features)
    .enter()
    .append("path")
    .attr("d", path)
    .attr("width", width / 2.2)
    .attr("height", height / 2)
    .attr("class", "state")
    .on("mouseover", clicked);

  g.append("path")
    .datum(
      topojson.mesh(us, us.objects.states, function(a, b) {
        return a !== b;
      })
    )
    .attr("id", "state-borders")
    .attr("d", path);

  var marks = [];
  for (i = 0; i < 20; i++) {
    var lon = Math.random() * (600 - 130) + 130; //max=min
    var la = Math.random() * (400 - 95) + 95;
    var sz = Math.random() > 0.5;

    var tup = { long: lon, lat: la, gender: sz };
    marks.push(tup);
  }

  g.selectAll(".mark")
    .data(marks)
    .enter()
    .append("image")
    .attr("class", "mark")
    .attr("width", 50)
    .attr("height", 50)
    .attr("xlink:href", function(d) {
      console.log(d);
      if (d.gender) {
        return "https://image.flaticon.com/icons/svg/10/10522.svg";
      } else {
        return "https://image.flaticon.com/icons/svg/264/264735.svg";
      }
    })
    .attr("transform", d => "translate(" + d.long + "," + d.lat + ")")
    .on("click", function(d) {
      alert("Location: " + d.lat + "," + d.long);
    });
}

function clicked(d) {
  if (d3.select(".background").node() === this) return reset();

  if (active.node() === this) return reset();

  active.classed("active", false);
  active = d3.select(this).classed("active", true);

  /* var bounds = path.bounds(d),
            dx = bounds[1][0] - bounds[0][0],
            dy = bounds[1][1] - bounds[0][1],
            x = (bounds[0][0] + bounds[1][0]) / 2,
            y = (bounds[0][1] + bounds[1][1]) / 2,
            scale = .9 / Math.max(dx / (width), dy / (height)),
            translate = [(width) / 2 - scale * x, (height) / 2 - scale * y];

        g//.transition()
           // .delay(100)
            //.duration(750)
            .style("stroke-width", 1.5 / scale + "px")
            .attr("transform", "translate(" + translate + ")scale(" + scale + ")");
        
      svg.selectAll(".mark").attr("transform", "translate(" + translate + ")scale(" + scale + ")") */
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
// graph

// // The number of datapoints
// var n = 21;

// // 5. X scale will use the index of our data
// var xScale = d3
//   .scaleLinear()
//   .domain([0, n + 4]) // input
//   .range([0, width / 2]); // output

// // 6. Y scale will use the randomly generate number
// var yScale = d3
//   .scaleLinear()
//   .domain([0, 1000]) // input
//   .range([height / 2, 0]); // output

// // 7. d3's line generator
// var line = d3
//   .line()
//   .x(function(d, i) {
//     return xScale(i);
//   }) // set the x values for the line generator
//   .y(function(d) {
//     return yScale(d.y);
//   }) // set the y values for the line generator
//   .curve(d3.curveMonotoneX); // apply smoothing to the line

// // 8. An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
// var dataset = d3.range(n).map(function(d) {
//   return { y: d3.randomUniform(1, 900)() };
// });

// // 1. Add the SVG to the page and employ #2
// var svg = d3
//   .select("#myMap")
//   .append("svg")
//   .attr("width", width / 2.5 + margin.left + margin.right)
//   .attr("height", height / 2 + margin.top + margin.bottom)
//   .append("g")
//   .attr("transform", "translate(" + margin.left + "," + 0 + ")");

// // 3. Call the x axis in a group tag
// svg
//   .append("g")
//   .attr("class", "x axis")
//   .attr("transform", "translate(0," + height / 1.965 + ")")
//   .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

// // 4. Call the y axis in a group tag
// svg
//   .append("g")
//   .attr("class", "y axis")
//   .attr("transform", "translate(0," + height / 100 + ")")
//   .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

// // 9. Append the path, bind the data, and call the line generator
// svg
//   .append("path")
//   .datum(dataset) // 10. Binds data to the line
//   .attr("class", "line") // Assign a class for styling
//   .attr("d", line); // 11. Calls the line generator

// // 12. Appends a circle for each datapoint
// svg
//   .selectAll(".dot")
//   .data(dataset)
//   .enter()
//   .append("circle") // Uses the enter().append() method
//   .attr("class", "dot") // Assign a class for styling
//   .attr("cx", function(d, i) {
//     return xScale(i);
//   })
//   .attr("cy", function(d) {
//     return yScale(d.y);
//   })
//   .attr("r", 5)
//   .on("mouseover", function(a, b, c) {
//     console.log(a);
//     this.attr("class", "focus");
//   })
//   .on("mouseout", function() {});
