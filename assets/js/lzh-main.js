document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.querySelector('.menu-toggle');
    const overlay = document.createElement('div');
    overlay.className = 'overlay';
    document.body.appendChild(overlay);

    // Toggle Sidebar on Mobile
    function toggleSidebar() {
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
    }

    if (menuToggle) {
        menuToggle.addEventListener('click', toggleSidebar);
    }

    if (overlay) {
        overlay.addEventListener('click', toggleSidebar);
    }

    // Smooth Scrolling for Sidebar Links
    const navLinks = document.querySelectorAll('.sidebar-nav a[href^="#"]');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();

            // Close sidebar on mobile after click
            if (window.innerWidth <= 768 && sidebar.classList.contains('active')) {
                toggleSidebar();
            }

            // Remove the '#' to get the ID string
            const targetId = decodeURIComponent(link.getAttribute('href')).substring(1);
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                // Offset for fixed header on mobile
                const headerOffset = window.innerWidth <= 768 ? 80 : 20;
                const elementPosition = targetSection.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });

                // Update Active State
                // Remove active class from all li elements
                document.querySelectorAll('.sidebar-nav li').forEach(li => li.classList.remove('active'));
                // Add active class to the parent li of the clicked link
                link.parentElement.classList.add('active');
            }
        });
    });

    // Intersection Observer for Active State on Scroll
    const sections = document.querySelectorAll('section[id]');

    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -70% 0px', // Trigger when section is near top
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                // Remove active class from all li elements
                document.querySelectorAll('.sidebar-nav li').forEach(li => li.classList.remove('active'));

                navLinks.forEach(link => {
                    const linkHref = decodeURIComponent(link.getAttribute('href')).substring(1);
                    if (linkHref === id) {
                        link.parentElement.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => observer.observe(section));
});
