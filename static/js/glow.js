window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY || window.pageYOffset;
    var maxHeight = document.body.scrollHeight - window.innerHeight;
    var scrollRatio = scrollPosition / maxHeight;
  
    // Adjust the glow intensity based on the scroll position
    var glowIntensity = scrollRatio * 10; // Adjust the multiplier as needed
  
    // Update the glow color from white to yellow based on the scroll
    var red = 255; // Red stays 255 for yellow
    var green = 255 * scrollRatio; // Green goes from 255 to 0
    var blue = 255 * (1 - scrollRatio); // Blue goes from 255 to 0
  
    // Apply the glow effect to the ::before element
    document.querySelector('.resume::before').style.boxShadow = `0 0 ${glowIntensity}px rgba(${red}, ${green}, ${blue}, 1)`;
  });