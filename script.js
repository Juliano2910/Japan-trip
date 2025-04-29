// Apparition en scroll
window.addEventListener('scroll', function() {
    const reveals = document.querySelectorAll('.reveal');
    for (let i = 0; i < reveals.length; i++) {
        const windowHeight = window.innerHeight;
        const elementTop = reveals[i].getBoundingClientRect().top;
        const elementVisible = 150;
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add('active');
        }
    }
});

// Carousel automatique
let carouselIndex = 0;
const items = document.querySelectorAll('.carousel-item');
function showCarousel() {
    for (let i = 0; i < items.length; i++) {
        items[i].classList.remove('active');
    }
    carouselIndex++;
    if (carouselIndex > items.length) {carouselIndex = 1}
    items[carouselIndex-1].classList.add('active');
    setTimeout(showCarousel, 3000);
}
showCarousel();

// Sons au clic
const buttons = document.querySelectorAll('.btn');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const audio = new Audio('click.mp3'); // mets un petit son "click.mp3"
        audio.play();
    });
});

// Popup à la fin
window.addEventListener('load', function() {
    setTimeout(() => {
        document.getElementById('popup').style.display = 'flex';
        confetti();
    }, 7000); // après 7 secondes
});

// Confettis simples
function confetti() {
    const count = 200;
    for (let i = 0; i < count; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.width = '10px';
        confetti.style.height = '10px';
        confetti.style.backgroundColor = ['#e60012', '#ffcc00', '#66ccff'][Math.floor(Math.random()*3)];
        confetti.style.position = 'absolute';
        confetti.style.top = Math.random() * window.innerHeight + 'px';
        confetti.style.left = Math.random() * window.innerWidth + 'px';
        confetti.style.opacity = 0.7;
        confetti.style.zIndex = 1000;
        confetti.style.animation = `fall ${2 + Math.random()*3}s linear infinite`;
        document.body.appendChild(confetti);
    }
}

/* Ajoute dans style.css si tu veux aussi des confettis qui tombent */
