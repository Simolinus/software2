function dice_roll_total() {
  const paragraph1 = document.getElementById("paragraph1");
  let dice_amount = prompt("Enter number of dice to roll");
  dice_amount = parseInt(dice_amount);

  let total = 0;
  for (let i = 1; i <= dice_amount; i++) {
    let dice_roll = Math.floor(Math.random() * 6) + 1;
    total += dice_roll;
  }
  paragraph1.textContent = "Task 7: total amount = " + total;
}

function leap_year() {
  start_year = prompt("Enter start year");
  end_year = prompt("Enter end year");

  list1 = document.getElementById("list1");

  for (let i = start_year; i <= end_year; i++) {
    let element = document.createElement("li");
    if (i % 400 === 0) {
      element.textContent = i;
      list1.appendChild(element);
    } else if (i % 100 === 0) {
      continue;
    } else if (i % 4 === 0) {
      element.textContent = i;
      list1.appendChild(element);
    } else {
      continue;
    }
  }
}

function dice_probability() {
  const paragraph2 = document.getElementById("paragraph2");
  let dice_amount = prompt("Enter number of dice to roll");
  let total_sum = prompt("Enter desired sum for dice");
  dice_amount = parseInt(dice_amount);
  total_sum = parseInt(total_sum);

  let successful_rolls = 0;
  for (let i = 0; i < 10000; i++) {
    let total = 0;
    for (let x = 0; x < dice_amount; x++) {
      let dice_roll = Math.floor(Math.random() * 6) + 1;
      total += dice_roll;
    }
    if (total === total_sum) successful_rolls++;
  }
  const probability = (successful_rolls / 10000) * 100;
  paragraph2.textContent =
    "Task 10: Probability to get sum of " +
    total_sum +
    " with " +
    dice_amount +
    " dice " +
    " is " +
    probability.toFixed(2) +
    "%";
}
