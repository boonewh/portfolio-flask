document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Set a timeout to delay the start of the animation
                setTimeout(() => {
                    entry.target.style.animationName = 'flicker';
                }, 1000); // Delay of 1000 milliseconds (1 second)

                // Optional: stop observing after animation is set to start
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.9 }); // Adjust threshold as needed, at 90% 

    const headings = document.querySelectorAll('h2.neon-effect');
    headings.forEach(h2 => observer.observe(h2));
});