/* ==========================================================================
   MY ANIME BOOK - INTELLIGENT THEME MANAGER
   Modes:
     1. 'dark'  -> Dark Mode (Locked)
     2. 'light' -> Light Mode (Locked)
     3. 'auto'  -> Scheduled Mode (8 PM to 6 AM = Dark, 6 AM to 8 PM = Light)
   ========================================================================== */

(function() {
    // 1. Determine scheduled theme based on local time
    function getAutoTheme() {
        const hour = new Date().getHours();
        // 8:00 PM (20:00) to 5:59 AM (05:59) -> Dark Mode
        // 6:00 AM (06:00) to 7:59 PM (19:59) -> Light Mode
        const isNight = (hour >= 20 || hour < 6);
        return isNight ? 'dark' : 'light';
    }

    // 2. Apply theme to DOM and update UI buttons
    window.applyAnimeTheme = function(mode) {
        if (!mode) {
            mode = localStorage.getItem('animeThemeMode') || 'auto';
        }

        let effectiveTheme = mode;
        if (mode === 'auto') {
            effectiveTheme = getAutoTheme();
        }

        // Apply attribute to <html> tag
        document.documentElement.setAttribute('data-theme', effectiveTheme);

        // Update Theme Button UI if present
        const icons = document.querySelectorAll('.theme-icon-indicator');
        const labels = document.querySelectorAll('.theme-label-indicator');
        const items = document.querySelectorAll('.theme-opt');

        labels.forEach(lbl => {
            if (mode === 'auto') {
                lbl.textContent = 'Auto (' + (effectiveTheme === 'dark' ? '🌙' : '☀️') + ')';
            } else if (mode === 'dark') {
                lbl.textContent = 'Dark';
            } else {
                lbl.textContent = 'Light';
            }
        });

        icons.forEach(ico => {
            if (mode === 'auto') {
                ico.className = 'fa fa-clock-o me-1 theme-icon-indicator text-info';
            } else if (mode === 'dark') {
                ico.className = 'fa fa-moon-o me-1 theme-icon-indicator text-primary';
            } else {
                ico.className = 'fa fa-sun-o me-1 theme-icon-indicator text-warning';
            }
        });

        items.forEach(item => {
            const optTheme = item.getAttribute('data-theme-set');
            if (optTheme === mode) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    };

    // 3. Set and save selected theme mode (Locks 'dark' or 'light', or enables 'auto')
    window.setAnimeThemeMode = function(mode) {
        localStorage.setItem('animeThemeMode', mode);
        window.applyAnimeTheme(mode);
    };

    // 4. Run immediately on script execution to prevent flickering
    const savedMode = localStorage.getItem('animeThemeMode') || 'auto';
    window.applyAnimeTheme(savedMode);

    // 5. Initialize event listeners once DOM is ready
    document.addEventListener('DOMContentLoaded', function() {
        window.applyAnimeTheme(localStorage.getItem('animeThemeMode') || 'auto');

        document.querySelectorAll('.theme-opt').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const selectedMode = this.getAttribute('data-theme-set');
                if (selectedMode) {
                    window.setAnimeThemeMode(selectedMode);
                }
            });
        });

        // Initialize alert auto-dismiss & timer bars
        initAnimeAlerts();
    });

    // 6. Automatic background interval: checks every 30 seconds for scheduled transition in 'auto' mode
    setInterval(function() {
        const currentMode = localStorage.getItem('animeThemeMode') || 'auto';
        if (currentMode === 'auto') {
            window.applyAnimeTheme('auto');
        }
    }, 30000);

    // 7. Auto-Dismiss Alert Messages with Timer & Contained Close Animation
    function initAnimeAlerts() {
        const alerts = document.querySelectorAll('.myalert');
        alerts.forEach(alert => {
            // Append timer bar if not already present
            if (!alert.querySelector('.alert-timer-bar')) {
                const timerBar = document.createElement('div');
                timerBar.className = 'alert-timer-bar';
                alert.appendChild(timerBar);
            }

            let dismissTimeout;
            const startDismissTimer = () => {
                dismissTimeout = setTimeout(() => {
                    dismissAlert(alert);
                }, 4500);
            };

            const clearDismissTimer = () => {
                if (dismissTimeout) {
                    clearTimeout(dismissTimeout);
                }
            };

            // Start initial timer
            startDismissTimer();

            // Pause on hover
            alert.addEventListener('mouseenter', () => {
                clearDismissTimer();
                const bar = alert.querySelector('.alert-timer-bar');
                if (bar) bar.style.animationPlayState = 'paused';
            });

            // Resume on mouse leave
            alert.addEventListener('mouseleave', () => {
                startDismissTimer();
                const bar = alert.querySelector('.alert-timer-bar');
                if (bar) bar.style.animationPlayState = 'running';
            });

            // Handle close button click
            const closeBtn = alert.querySelector('.btn-close');
            if (closeBtn) {
                closeBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    clearDismissTimer();
                    dismissAlert(alert);
                });
            }
        });
    }

    function dismissAlert(alert) {
        if (!alert || alert.dataset.dismissing === 'true') return;
        alert.dataset.dismissing = 'true';
        alert.style.transition = 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)';
        alert.style.opacity = '0';
        alert.style.transform = 'translateY(-20px) scale(0.95)';
        alert.style.maxHeight = alert.scrollHeight + 'px';
        setTimeout(() => {
            alert.style.maxHeight = '0px';
            alert.style.paddingTop = '0px';
            alert.style.paddingBottom = '0px';
            alert.style.marginTop = '0px';
            alert.style.marginBottom = '0px';
            alert.style.borderWidth = '0px';
        }, 150);
        setTimeout(() => {
            if (alert.parentNode) {
                alert.parentNode.removeChild(alert);
            }
        }, 400);
    }
})();
