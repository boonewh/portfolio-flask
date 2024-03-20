var calcPrices = [0.99, 1.99, 1.49, 0.99, 1.99];
var calcTotal = 0;
const tax = 0.0825;

function calculate() {
  for (var i = 0; i < calcPrices.length; i++) {
    var countId = "count" + (i + 1); 

    var quantity = document.getElementById(countId);
    var calcValue = parseInt(quantity.value);

    var calcSubtotal = calcValue * calcPrices[i];

    calcTotal += calcSubtotal;
  }

  calcTotal += (calcTotal * tax);

  window.alert(`Thank you for your order!\nYour total is: \$${calcTotal.toFixed(2)}`);
}