"use strict";

/*
   validateSummary()
      Validates the data entry in the summary field.
   
   calcClass(sumClass)
      Sums up all of the data values for elements of the sumClass class.
      
   calcExp()
      Calculates the travel expenses from all categories and dates.
      
   formatNumber(val, decimals)
      Formats the value, "val" to the number of decimals indicated 
      by "decimals", adding thousands separators.
      
   formatUSCurrency(val)
      Formats the value, "val", as U.S. currency.
      
*/


// Event listener for the load event
window.addEventListener('load', function() {
  // Declare a variable named changingCells that matches all input elements in the travelExp table that belong to the sum class.
  var changingCells = document.querySelectorAll('table#travelExp .sum');

  // Add onchange event handler to each item in changingCells collection
  for (var i = 0; i < changingCells.length; i++) {
    changingCells[i].onchange = calcExp;
  }

  // Event handler for the submitButton click event
  var submitButton = document.getElementById('submitButton');
  submitButton.onclick = validateSummary;
});

function validateSummary() {
  var validSummary = document.getElementById("summary");
  if(validSummary.validity.valueMissing) {
   validSummary.setCustomValidity("You must include a summary of the trip in your report.")
  } else {
   validSummary.setCustomValidity("");
  }
}

function calcClass(sumClass) {
  var sumFields = document.getElementsByClassName(sumClass);
  var totalSum = 0;

  for (var i = 0; i < sumFields.length; i++) {
    var itemValue = parseFloat(sumFields[i].value);
    if (!isNaN(itemValue)) {
      totalSum += itemValue;
    }
  }

  return totalSum;
}

function calcExp() {
  var expTable = document.querySelectorAll("#travelExp tbody > tr");
  for (var i = 0; i < expTable.length; ++i) {
    document.getElementById("subtotal" + i).value = formatNumber(calcClass("date" + i), 2);
  }
  
  // Column totals
  document.getElementById("transTotal").value = formatNumber(calcClass("trans"), 2);
  document.getElementById("lodgeTotal").value = formatNumber(calcClass("lodge"), 2);
  document.getElementById("mealTotal").value = formatNumber(calcClass("meal"), 2);
  document.getElementById("otherTotal").value = formatNumber(calcClass("other"), 2);

  // Grand total
  document.getElementById("expTotal").value = formatUSCurrency(calcClass("sum"));
}

function formatNumber(val, decimals) {
   return val.toLocaleString(undefined, {minimumFractionDigits: decimals, 
                                         maximumFractionDigits: decimals});
}

function formatUSCurrency(val) {
   return val.toLocaleString('en-US', {style: "currency", currency: "USD"} );
}


