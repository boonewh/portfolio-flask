// Arrays with the prices, names and images 
var menuPrices = [.99, 1.99, 1.49, .99, 1.99];
var menuNames = ["Dark Roast", "Medium Roast", "Light Roast", "Breakfast Blend", "House Blend"];
var menuImages = [
  '/static/images/blackCoffee.jpg',
  '/static/images/mediumRoast.jpg',
  '/static/images/lightRoast.jpg',
  '/static/images/breakfastBlend.jpg',
  '/static/images/houseBlend.jpg'
];

function createMenu() {
    // create variable that holds the section that will hold the menu
    var createTable = document.getElementById('menuTable')

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

createMenu();

/*
window.addEventListener("load", function() {
    var menuPlacement = document.getElementById("menuTable");

    menuPlacement.innerHTML = "Hello World";

    var table = document.createElement("table");
    menuPlacement.appendChild(table);

    var tableRows = document.createElement('tr');
    table.appendChild(tableRows);

    var tableColumns = document.createElement('td');
    tableRows.appendChild(tableColumns);

    tableColumns.innerHTML = "Hello World";
});
*/
