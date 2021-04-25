const chart = require("electron-chartjs");

function result_function(x) {
  return Math.exp(-Math.sin(x)) + Math.sin(x) - 1;
}

function f(x, y) {
  return (1 / 2) * Math.sin(2 * x) - y * Math.cos(x);
}

let adams_errors = [];
let runge_errors = [];
let result_array = [[0, 0]];
let runge_array = [[0, 0]];
let adams_array = [[0, 0]];
for (let h = 0.5; h > 0.00001; h /= 2) {
  let counter = 0;
  let result_arr = [[0, 0]];
  let runge_arr = [[0, 0]];
  let adams_arr = [[0, 0]];
  let runge_err_arr = [[0, 0]];
  let adams_err_arr = [[0, 0]];
  for (let x = 0; x < 1; x += h) {
    //runge-kutta
    let y = runge_arr[runge_arr.length - 1][1];
    let k1 = f(x, y);
    let k2 = f(x + h / 2, y + (h * k1) / 2);
    let k3 = f(x + h / 2, y + (h * k2) / 2);
    let k4 = f(x + h, y + h * k3);
    let dy = (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
    runge_arr.push([x + h, y + dy]);
    result_arr.push([x + h, result_function(x + h)]);
    let err = Math.abs(
      runge_arr[runge_arr.length - 1][1] - result_arr[result_arr.length - 1][1]
    );
    runge_err_arr.push([x + h, err]);

    //Adams
    if (counter < 4) {
      ++counter;
      adams_arr.push([x + h, y + dy]);
      adams_err_arr.push([x + h, err]);
    } else {
      const last = adams_arr.length - 1;
      let yk =
        adams_arr[last][1] +
        (h / 24) *
          (55 * f(adams_arr[last][0], adams_arr[last][1]) -
            59 * f(adams_arr[last - 1][0], adams_arr[last - 1][1]) +
            37 * f(adams_arr[last - 2][0], adams_arr[last - 2][1]) -
            9 * f(adams_arr[last - 3][0], adams_arr[last - 3][1]));
      adams_arr.push([x + h, yk]);
      let adams_err = Math.abs(
        adams_arr[adams_arr.length - 1][1] -
          result_arr[result_arr.length - 1][1]
      );
      adams_err_arr.push([x + h, adams_err]);
    }
  }
  const max_adams = Math.max(...adams_err_arr.map((value) => value[1]));
  console.log(max_adams);
  adams_errors.push([h, max_adams]);
  runge_errors.push([h, Math.max(...runge_err_arr.map((value) => value[1]))]);

  if (h > 0.01) {
    result_array = result_arr;
    runge_array = runge_arr;
    adams_array = adams_arr;
  }
}

console.table(result_array);
console.table(runge_array);
console.table(adams_array);
console.table(adams_errors);
console.table(runge_errors);


//plotting
const datapoints = {
  labels: result_array.map((value) => value[0]),
  datasets: [
    {
      data: result_array.map((value) => value[1]),
      fill: false,
      label: "original function",
      borderColor: "#00ffff",
    },
    {
      data: runge_array.map((value) => value[1]),
      fill: false,
      label: "Runge Kutta method",
      borderColor: "#ff0000",
    },
    {
      data: adams_array.map((value) => value[1]),
      fill: false,
      label: "Adams method",
      borderColor: "#ff5500",
    },
  ],
};

chart({
  type: "line",
  data: datapoints,
});

chart({
  type: "line",
  data: {
    labels: runge_errors.map((value) => value[0]),
    datasets: [
      {
        data: runge_errors.map((value) => value[1]),
        fill: false,
        label: "Runge-Kutta error",
        borderColor: "#0000ff",
      },
      {
        data: adams_errors.map((value) => value[1]),
        fill: false,
        label: "Adams error",
        borderColor: "#32a852",
      },
    ],
  },
});
