document.addEventListener('DOMContentLoaded', () => {
    // Sticky Navigation
    const navbar = document.getElementById('navbar');
    const sticky = navbar.offsetTop;

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > sticky) {
            navbar.classList.add('sticky');
        } else {
            navbar.classList.remove('sticky');
        }
    });

    // Scroll Reveal Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');

                // If it's a stat number, trigger counter animation
                if (entry.target.classList.contains('stat-card')) {
                    const numberEl = entry.target.querySelector('.stat-number');
                    if (numberEl && !numberEl.classList.contains('counted')) {
                        animateValue(numberEl, 0, parseInt(numberEl.getAttribute('data-target')), 2000);
                        numberEl.classList.add('counted');
                    }
                }

                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-up, .fade-in, .slide-in-right');
    animatedElements.forEach(el => observer.observe(el));

    // Number Counter Animation
    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            // Easing
            const easeOutQuart = 1 - Math.pow(1 - progress, 4);
            obj.innerHTML = Math.floor(easeOutQuart * (end - start) + start);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                obj.innerHTML = end; // Ensure exact final value
            }
        };
        window.requestAnimationFrame(step);
    }
});
