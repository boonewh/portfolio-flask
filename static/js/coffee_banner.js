var bannerArray = [
    "/static/images/banner1.png",
    "/static/images/banner2.png",
    "/static/images/banner3.png",
    "/static/images/banner4.png"
];

var currentBanner = 0;

function rotate() {
    var bannerPlace = document.getElementById('bannerImages');
    bannerPlace.src = bannerArray[currentBanner];

    currentBanner++;

    if(currentBanner === bannerArray.length) {
        currentBanner = 0;
    }

    setTimeout(rotate, 3000); 
}

rotate();