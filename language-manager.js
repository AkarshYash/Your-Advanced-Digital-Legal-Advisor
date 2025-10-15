/**
 * Language Manager for LegalEase AI Advanced
 * Handles multi-language support for Indian regional languages
 */

class LanguageManager {
    constructor() {
        this.languages = {
            'en': { name: 'English', flag: '🇮🇳', nativeName: 'English' },
            'hi': { name: 'Hindi', flag: '🇮🇳', nativeName: 'हिंदी' },
            'ta': { name: 'Tamil', flag: '🇮🇳', nativeName: 'தமிழ்' },
            'te': { name: 'Telugu', flag: '🇮🇳', nativeName: 'తెలుగు' },
            'bn': { name: 'Bengali', flag: '🇮🇳', nativeName: 'বাংলা' },
            'mr': { name: 'Marathi', flag: '🇮🇳', nativeName: 'मराठी' },
            'gu': { name: 'Gujarati', flag: '🇮🇳', nativeName: 'ગુજરાતી' },
            'pa': { name: 'Punjabi', flag: '🇮🇳', nativeName: 'ਪੰਜਾਬੀ' },
            'kn': { name: 'Kannada', flag: '🇮🇳', nativeName: 'ಕನ್ನಡ' },
            'ml': { name: 'Malayalam', flag: '🇮🇳', nativeName: 'മലയാളം' },
            'or': { name: 'Odia', flag: '🇮🇳', nativeName: 'ଓଡ଼ିଆ' },
            'as': { name: 'Assamese', flag: '🇮🇳', nativeName: 'অসমীয়া' },
            'ur': { name: 'Urdu', flag: '🇮🇳', nativeName: 'اردو' },
            'sa': { name: 'Sanskrit', flag: '🇮🇳', nativeName: 'संस्कृत' }
        };
        
        this.translations = {};
        this.currentLanguage = this.loadLanguage();
        this.loadTranslations();
    }
    
    async loadTranslations() {
        try {
            const response = await fetch(`/static/translations/${this.currentLanguage}.json`);
            if (response.ok) {
                this.translations = await response.json();
                this.applyTranslations();
            }
        } catch (error) {
            console.warn('Translation file not found, using default language');
        }
    }
    
    setLanguage(langCode, displayName) {
        if (this.languages[langCode]) {
            this.currentLanguage = langCode;
            this.saveLanguage(langCode);
            this.updateLanguageIndicator(displayName);
            this.loadTranslations();
            this.showLanguageChangeNotification(displayName);
            
            // Reload page to apply language changes
            setTimeout(() => {
                window.location.reload();
            }, 1000);
        }
    }
    
    applyTranslations() {
        document.querySelectorAll('[data-translate]').forEach(element => {
            const key = element.getAttribute('data-translate');
            if (this.translations[key]) {
                if (element.tagName === 'INPUT' && element.type === 'text') {
                    element.placeholder = this.translations[key];
                } else {
                    element.textContent = this.translations[key];
                }
            }
        });
    }
    
    updateLanguageIndicator(displayName) {
        const langIndicator = document.getElementById('currentLang');
        if (langIndicator) {
            langIndicator.textContent = displayName;
        }
    }
    
    loadLanguage() {
        return localStorage.getItem('legalease-language') || 'en';
    }
    
    saveLanguage(langCode) {
        localStorage.setItem('legalease-language', langCode);
    }
    
    showLanguageChangeNotification(displayName) {
        this.showNotification(`Language changed to ${displayName}`, 'success');
    }
    
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        notification.style.cssText = 'top: 100px; right: 20px; z-index: 9999; min-width: 300px;';
        notification.innerHTML = `
            <i class="fas fa-language me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 3000);
    }
    
    translate(key, fallback = '') {
        return this.translations[key] || fallback || key;
    }
    
    getCurrentLanguage() {
        return this.currentLanguage;
    }
    
    getLanguageInfo(langCode) {
        return this.languages[langCode] || this.languages['en'];
    }
}

// Global language functions
function setLanguage(langCode, displayName) {
    if (window.languageManager) {
        window.languageManager.setLanguage(langCode, displayName);
    }
}

// Voice synthesis for multi-language support
class VoiceManager {
    constructor() {
        this.synthesis = window.speechSynthesis;
        this.voices = [];
        this.loadVoices();
    }
    
    loadVoices() {
        this.voices = this.synthesis.getVoices();
        if (this.voices.length === 0) {
            this.synthesis.addEventListener('voiceschanged', () => {
                this.voices = this.synthesis.getVoices();
            });
        }
    }
    
    speak(text, langCode = 'en-IN') {
        if (!this.synthesis) return;
        
        const utterance = new SpeechSynthesisUtterance(text);
        
        // Find appropriate voice for the language
        const voice = this.voices.find(v => 
            v.lang.startsWith(langCode) || 
            v.lang.startsWith(langCode.split('-')[0])
        );
        
        if (voice) {
            utterance.voice = voice;
        }
        
        utterance.rate = 0.9;
        utterance.pitch = 1;
        utterance.volume = 0.8;
        
        this.synthesis.speak(utterance);
    }
    
    stop() {
        if (this.synthesis) {
            this.synthesis.cancel();
        }
    }
    
    getAvailableVoices(langCode) {
        return this.voices.filter(voice => 
            voice.lang.startsWith(langCode) || 
            voice.lang.startsWith(langCode.split('-')[0])
        );
    }
}

// Initialize language and voice managers
document.addEventListener('DOMContentLoaded', function() {
    window.languageManager = new LanguageManager();
    window.voiceManager = new VoiceManager();
});