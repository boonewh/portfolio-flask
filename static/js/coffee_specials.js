// Arrays with the prices, names and images 
var menuPrices = [1.99, 1.99, 2.49, 1.00, 1.00];
var menuNames = [
  "Banana Muffin", 
  "Chocolate Muffin", 
  "Cinnamon Roll", 
  "Croissant", 
  "Cookie"];
var menuImages = [
  '/static/images/bananaMuffin.jpg',
  '/static/images/chocMuffin.jpg',
  '/static/images/cinnRoll.jpg',
  '/static/images/croissant.jpg',
  '/static/images/cookie.jpg'
];

function createMenu() {
    // create variable that holds the section that will hold the menu
    var createTable = document.getElementById('specialsTable')

    // crate the table tag and put it in the holding section
    var coffeeTable = document.createElement('table');
    createTable.appendChild(coffeeTable);

    // create the cells for images, names and prices
    for(var i = 0; i < menuPrices.length; i++) {
        var menuRow = document.createElement('tr');
        coffeeTable.appendChild(menuRow);

        // Image
        var imgCell = document.createElement('td');
        menuRow.appendChild(imgCell);

        var image = document.createElement('img');
        imgCell.appendChild(image);
        image.src = menuImages[i];
        image.alt = menuNames[i];
        
        // Name
        var nameCell = document.createElement('td');
        menuRow.appendChild(nameCell);

        nameCell.textContent = menuNames[i];

        // Price
        var priceCell = document.createElement('td');
        menuRow.appendChild(priceCell);

        priceCell.textContent = '$' + menuPrices[i];
    }
}

document.addEventListener('DOMContentLoaded', function() {
  // link to the button with the id "specialsButton"
  const specialsButton = document.getElementById('specialsButton');

  // Add a click event listener to the button
  specialsButton.addEventListener('click', function() {
    // Open the "specialsPage.html" in a new window
    window.open('/coffee_specials', '_blank');
  });
});

createMenu();


