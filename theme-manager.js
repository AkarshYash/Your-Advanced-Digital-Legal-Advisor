/**
 * Theme Manager for LegalEase AI Advanced
 * Handles theme switching and persistence
 */

class ThemeManager {
    constructor() {
        this.themes = {
            normal: {
                name: 'Normal Theme',
                icon: 'fas fa-circle text-primary',
                colors: {
                    '--bg-primary': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                    '--bg-secondary': 'rgba(255, 255, 255, 0.1)',
                    '--text-primary': '#ffffff',
                    '--text-secondary': 'rgba(255, 255, 255, 0.8)',
                    '--border-color': 'rgba(255, 255, 255, 0.2)'
                }
            },
            dark: {
                name: 'Dark Theme',
                icon: 'fas fa-moon text-dark',
                colors: {
                    '--bg-primary': 'linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%)',
                    '--bg-secondary': 'rgba(255, 255, 255, 0.05)',
                    '--text-primary': '#ffffff',
                    '--text-secondary': 'rgba(255, 255, 255, 0.7)',
                    '--border-color': 'rgba(255, 255, 255, 0.1)'
                }
            },
            light: {
                name: 'Light Theme',
                icon: 'fas fa-sun text-warning',
                colors: {
                    '--bg-primary': 'linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%)',
                    '--bg-secondary': 'rgba(0, 0, 0, 0.05)',
                    '--text-primary': '#1f2937',
                    '--text-secondary': '#4b5563',
                    '--border-color': 'rgba(0, 0, 0, 0.1)'
                }
            }
        };
        
        this.currentTheme = this.loadTheme();
        this.applyTheme(this.currentTheme);
    }
    
    setTheme(themeName) {
        if (this.themes[themeName]) {
            this.currentTheme = themeName;
            this.applyTheme(themeName);
            this.saveTheme(themeName);
            this.showThemeChangeNotification(themeName);
        }
    }
    
    applyTheme(themeName) {
        const theme = this.themes[themeName];
        if (!theme) return;
        
        document.documentElement.setAttribute('data-theme', themeName);
        
        // Apply CSS custom properties
        Object.entries(theme.colors).forEach(([property, value]) => {
            document.documentElement.style.setProperty(property, value);
        });
        
        // Update theme indicator in navbar
        this.updateThemeIndicator(themeName);
    }
    
    updateThemeIndicator(themeName) {
        const themeButton = document.querySelector('[data-theme-toggle]');
        if (themeButton) {
            const theme = this.themes[themeName];
            themeButton.innerHTML = `<i class="${theme.icon} me-1"></i>${theme.name}`;
        }
    }
    
    loadTheme() {
        return localStorage.getItem('legalease-theme') || 'normal';
    }
    
    saveTheme(themeName) {
        localStorage.setItem('legalease-theme', themeName);
    }
    
    showThemeChangeNotification(themeName) {
        const theme = this.themes[themeName];
        this.showNotification(`Theme changed to ${theme.name}`, 'success');
    }
    
    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        notification.style.cssText = 'top: 100px; right: 20px; z-index: 9999; min-width: 300px;';
        notification.innerHTML = `
            <i class="fas fa-palette me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 3000);
    }
    
    getAvailableThemes() {
        return Object.keys(this.themes);
    }
    
    getCurrentTheme() {
        return this.currentTheme;
    }
}

// Global theme functions
function setTheme(themeName) {
    if (window.themeManager) {
        window.themeManager.setTheme(themeName);
    }
}

function toggleTheme() {
    if (window.themeManager) {
        const themes = window.themeManager.getAvailableThemes();
        const currentIndex = themes.indexOf(window.themeManager.getCurrentTheme());
        const nextIndex = (currentIndex + 1) % themes.length;
        window.themeManager.setTheme(themes[nextIndex]);
    }
}

// Initialize theme manager when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.themeManager = new ThemeManager();
});