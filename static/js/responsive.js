// ============================================
// RESPONSIVE DESIGN JAVASCRIPT
// Mobile Navigation and Responsive Utilities
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize responsive features
    initHamburgerMenu();
    initResponsiveImages();
    initTouchOptimization();
    initViewportDetection();
});

// ============================================
// HAMBURGER MENU FOR MOBILE
// ============================================

function initHamburgerMenu() {
    const hamburger = document.getElementById('hamburger');
    const navbar = document.getElementById('navbar');

    if (!hamburger || !navbar) return;

    hamburger.addEventListener('click', function(e) {
        e.stopPropagation();
        hamburger.classList.toggle('active');
        navbar.classList.toggle('active');
    });

    // Close menu when clicking on a link
    const navLinks = navbar.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            hamburger.classList.remove('active');
            navbar.classList.remove('active');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('header')) {
            hamburger.classList.remove('active');
            navbar.classList.remove('active');
        }
    });
}

// ============================================
// RESPONSIVE IMAGE HANDLING
// ============================================

function initResponsiveImages() {
    const images = document.querySelectorAll('img');
    
    images.forEach(img => {
        // Add lazy loading
        if ('loading' in HTMLImageElement.prototype) {
            img.loading = 'lazy';
        }
        
        // Ensure images are responsive
        if (!img.style.maxWidth) {
            img.style.maxWidth = '100%';
            img.style.height = 'auto';
        }
    });
}

// ============================================
// TOUCH OPTIMIZATION FOR TABLETS & PHONES
// ============================================

function initTouchOptimization() {
    const isTouchDevice = () => {
        return (('ontouchstart' in window) ||
                (navigator.maxTouchPoints > 0) ||
                (navigator.msMaxTouchPoints > 0));
    };

    if (isTouchDevice()) {
        document.body.classList.add('touch-device');
        
        // Increase touch target sizes
        const buttons = document.querySelectorAll('button, a, input[type="button"]');
        buttons.forEach(btn => {
            const currentHeight = btn.offsetHeight;
            if (currentHeight < 48) {
                btn.style.minHeight = '48px';
            }
            const currentWidth = btn.offsetWidth;
            if (currentWidth < 48) {
                btn.style.minWidth = '48px';
            }
        });
    }
}

// ============================================
// VIEWPORT & DEVICE DETECTION
// ============================================

function initViewportDetection() {
    const updateViewportClass = () => {
        const width = window.innerWidth;
        const html = document.documentElement;
        
        // Remove previous classes
        html.classList.remove('mobile', 'tablet', 'laptop', 'desktop', 'tv');
        
        // Add appropriate class
        if (width < 577) {
            html.classList.add('mobile');
            console.log('Device: Mobile (' + width + 'px)');
        } else if (width < 993) {
            html.classList.add('tablet');
            console.log('Device: Tablet (' + width + 'px)');
        } else if (width < 1921) {
            html.classList.add('laptop');
            console.log('Device: Laptop (' + width + 'px)');
        } else if (width < 3840) {
            html.classList.add('desktop');
            console.log('Device: Desktop (' + width + 'px)');
        } else {
            html.classList.add('tv');
            console.log('Device: TV (' + width + 'px)');
        }
    };

    // Initial check
    updateViewportClass();

    // Update on window resize with debouncing
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(updateViewportClass, 250);
    });
}

// ============================================
// RESPONSIVE VIDEO EMBEDDING
// ============================================

function makeVideosResponsive() {
    const videos = document.querySelectorAll('iframe[src*="youtube"], iframe[src*="vimeo"]');
    
    videos.forEach(video => {
        const container = document.createElement('div');
        container.style.position = 'relative';
        container.style.width = '100%';
        container.style.paddingBottom = '56.25%'; // 16:9 aspect ratio
        container.style.height = '0';
        container.style.overflow = 'hidden';
        
        video.style.position = 'absolute';
        video.style.top = '0';
        video.style.left = '0';
        video.style.width = '100%';
        video.style.height = '100%';
        
        video.parentNode.insertBefore(container, video);
        container.appendChild(video);
    });
}

// ============================================
// PRINT STYLES OPTIMIZATION
// ============================================

window.addEventListener('beforeprint', function() {
    // Hide navigation on print
    const header = document.querySelector('header');
    const footer = document.querySelector('footer');
    if (header) header.style.display = 'none';
    if (footer) footer.style.display = 'none';
});

window.addEventListener('afterprint', function() {
    // Restore navigation after print
    const header = document.querySelector('header');
    const footer = document.querySelector('footer');
    if (header) header.style.display = 'block';
    if (footer) footer.style.display = 'block';
});

// ============================================
// VIEWPORT META TAG MANAGEMENT
// ============================================

function ensureViewportMeta() {
    let viewportMeta = document.querySelector('meta[name="viewport"]');
    if (!viewportMeta) {
        viewportMeta = document.createElement('meta');
        viewportMeta.name = 'viewport';
        viewportMeta.content = 'width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes';
        document.head.appendChild(viewportMeta);
    }
}

ensureViewportMeta();

// ============================================
// PERFORMANCE OPTIMIZATION
// ============================================

// Lazy load images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => imageObserver.observe(img));
}

// ============================================
// UTILITY FUNCTIONS
// ============================================

// Get current device type
window.getDeviceType = function() {
    const width = window.innerWidth;
    if (width < 577) return 'mobile';
    if (width < 993) return 'tablet';
    if (width < 1921) return 'laptop';
    if (width < 3840) return 'desktop';
    return 'tv';
};

// Get viewport dimensions
window.getViewport = function() {
    return {
        width: Math.max(document.documentElement.clientWidth, window.innerWidth || 0),
        height: Math.max(document.documentElement.clientHeight, window.innerHeight || 0)
    };
};

console.log('Responsive Design Framework Loaded');
console.log('Current Device:', window.getDeviceType());
console.log('Viewport:', window.getViewport());
