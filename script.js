// Header scroll change
window.addEventListener('scroll', function() {
  const header = document.getElementById('header');
  header.classList.toggle('scrolled', window.scrollY > 50);
});

// Carousel slider
let carouselIndex = 0;
const items = document.querySelectorAll('.carousel-item');
function showCarousel() {
  items.forEach(item => item.classList.remove('active'));
  carouselIndex = (carouselIndex + 1) % items.length;
  items[carouselIndex].classList.add('active');
}
setInterval(showCarousel, 4000);

// Animation reveal on scroll
window.addEventListener('scroll', function() {
  const reveals = document.querySelectorAll('.reveal');
  reveals.forEach(reveal => {
    const windowHeight = window.innerHeight;
    const elementTop = reveal.getBoundingClientRect().top;
    if (elementTop < windowHeight - 100) {
      reveal.classList.add('active');
    }
  });
});
