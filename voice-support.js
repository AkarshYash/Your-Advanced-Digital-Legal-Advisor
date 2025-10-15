/**
 * Voice Support for LegalEase AI Advanced
 * Handles speech recognition and text-to-speech functionality
 */

class VoiceSupport {
    constructor() {
        this.recognition = null;
        this.synthesis = window.speechSynthesis;
        this.isListening = false;
        this.isSupported = this.checkSupport();
        this.currentLanguage = 'en-IN';
        this.voices = [];
        
        this.initializeRecognition();
        this.loadVoices();
        
        // Language mapping for speech recognition
        this.languageMap = {
            'en': 'en-IN',
            'hi': 'hi-IN',
            'ta': 'ta-IN',
            'te': 'te-IN',
            'bn': 'bn-IN',
            'mr': 'mr-IN',
            'gu': 'gu-IN',
            'pa': 'pa-IN',
            'kn': 'kn-IN',
            'ml': 'ml-IN',
            'or': 'or-IN',
            'as': 'as-IN',
            'ur': 'ur-IN'
        };
    }
    
    checkSupport() {
        const hasRecognition = 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window;
        const hasSynthesis = 'speechSynthesis' in window;
        
        if (!hasRecognition) {
            console.warn('Speech recognition not supported in this browser');
        }
        
        if (!hasSynthesis) {
            console.warn('Speech synthesis not supported in this browser');
        }
        
        return hasRecognition && hasSynthesis;
    }
    
    initializeRecognition() {
        if (!this.isSupported) return;
        
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        this.recognition = new SpeechRecognition();
        
        this.recognition.continuous = false;
        this.recognition.interimResults = true;
        this.recognition.lang = this.currentLanguage;
        
        this.recognition.onstart = () => {
            this.isListening = true;
            this.updateVoiceButton(true);
            this.showVoiceStatus('Listening...', 'info');
        };
        
        this.recognition.onresult = (event) => {
            let finalTranscript = '';
            let interimTranscript = '';
            
            for (let i = event.resultIndex; i < event.results.length; i++) {
                const transcript = event.results[i][0].transcript;
                
                if (event.results[i].isFinal) {
                    finalTranscript += transcript;
                } else {
                    interimTranscript += transcript;
                }
            }
            
            if (finalTranscript) {
                this.onSpeechResult(finalTranscript);
            }
            
            // Show interim results
            if (interimTranscript) {
                this.showInterimResult(interimTranscript);
            }
        };
        
        this.recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            this.isListening = false;
            this.updateVoiceButton(false);
            
            let errorMessage = 'Voice recognition error';
            switch (event.error) {
                case 'no-speech':
                    errorMessage = 'No speech detected. Please try again.';
                    break;
                case 'audio-capture':
                    errorMessage = 'Microphone not accessible. Please check permissions.';
                    break;
                case 'not-allowed':
                    errorMessage = 'Microphone access denied. Please allow microphone access.';
                    break;
                case 'network':
                    errorMessage = 'Network error. Please check your connection.';
                    break;
            }
            
            this.showVoiceStatus(errorMessage, 'error');
        };
        
        this.recognition.onend = () => {
            this.isListening = false;
            this.updateVoiceButton(false);
            this.hideVoiceStatus();
        };
    }
    
    loadVoices() {
        this.voices = this.synthesis.getVoices();
        
        if (this.voices.length === 0) {
            this.synthesis.addEventListener('voiceschanged', () => {
                this.voices = this.synthesis.getVoices();
            });
        }
    }
    
    setLanguage(langCode) {
        this.currentLanguage = this.languageMap[langCode] || 'en-IN';
        
        if (this.recognition) {
            this.recognition.lang = this.currentLanguage;
        }
    }
    
    startListening() {
        if (!this.isSupported || this.isListening) return;
        
        try {
            this.recognition.start();
        } catch (error) {
            console.error('Error starting speech recognition:', error);
            this.showVoiceStatus('Could not start voice recognition', 'error');
        }
    }
    
    stopListening() {
        if (!this.isSupported || !this.isListening) return;
        
        this.recognition.stop();
    }
    
    speak(text, langCode = 'en') {
        if (!this.isSupported) return;
        
        // Stop any ongoing speech
        this.synthesis.cancel();
        
        const utterance = new SpeechSynthesisUtterance(text);
        
        // Find appropriate voice for the language
        const voiceLang = this.languageMap[langCode] || 'en-IN';
        const voice = this.voices.find(v => 
            v.lang === voiceLang || 
            v.lang.startsWith(voiceLang.split('-')[0])
        );
        
        if (voice) {
            utterance.voice = voice;
        }
        
        utterance.rate = 0.9;
        utterance.pitch = 1;
        utterance.volume = 0.8;
        
        utterance.onstart = () => {
            this.showVoiceStatus('Speaking...', 'info');
            this.updateSpeakButton(true);
        };
        
        utterance.onend = () => {
            this.hideVoiceStatus();
            this.updateSpeakButton(false);
        };
        
        utterance.onerror = (event) => {
            console.error('Speech synthesis error:', event.error);
            this.showVoiceStatus('Speech error occurred', 'error');
            this.updateSpeakButton(false);
        };
        
        this.synthesis.speak(utterance);
    }
    
    stopSpeaking() {
        if (this.synthesis) {
            this.synthesis.cancel();
            this.updateSpeakButton(false);
            this.hideVoiceStatus();
        }
    }
    
    onSpeechResult(transcript) {
        // This method should be overridden by the implementing class
        console.log('Speech result:', transcript);
        
        // Try to find chat input and set the value
        const chatInput = document.querySelector('#messageInput, .chat-input, input[type="text"]');
        if (chatInput) {
            chatInput.value = transcript;
            chatInput.focus();
            
            // Trigger input event
            const event = new Event('input', { bubbles: true });
            chatInput.dispatchEvent(event);
        }
    }
    
    showInterimResult(transcript) {
        // Show interim speech recognition results
        const interimElement = document.getElementById('interimResult');
        if (interimElement) {
            interimElement.textContent = transcript;
            interimElement.style.display = 'block';
        }
    }
    
    updateVoiceButton(isActive) {
        const voiceBtn = document.querySelector('.voice-btn, #voiceBtn');
        if (voiceBtn) {
            if (isActive) {
                voiceBtn.classList.add('active', 'btn-danger');
                voiceBtn.classList.remove('btn-primary');
                voiceBtn.innerHTML = '<i class="fas fa-stop"></i>';
                voiceBtn.title = 'Stop listening';
            } else {
                voiceBtn.classList.remove('active', 'btn-danger');
                voiceBtn.classList.add('btn-primary');
                voiceBtn.innerHTML = '<i class="fas fa-microphone"></i>';
                voiceBtn.title = 'Start voice input';
            }
        }
    }
    
    updateSpeakButton(isActive) {
        const speakBtn = document.querySelector('.speak-btn, #speakBtn');
        if (speakBtn) {
            if (isActive) {
                speakBtn.classList.add('active', 'btn-warning');
                speakBtn.classList.remove('btn-success');
                speakBtn.innerHTML = '<i class="fas fa-stop"></i>';
                speakBtn.title = 'Stop speaking';
            } else {
                speakBtn.classList.remove('active', 'btn-warning');
                speakBtn.classList.add('btn-success');
                speakBtn.innerHTML = '<i class="fas fa-volume-up"></i>';
                speakBtn.title = 'Read aloud';
            }
        }
    }
    
    showVoiceStatus(message, type = 'info') {
        let statusElement = document.getElementById('voiceStatus');
        
        if (!statusElement) {
            statusElement = document.createElement('div');
            statusElement.id = 'voiceStatus';
            statusElement.className = 'voice-status position-fixed';
            statusElement.style.cssText = `
                top: 20px;
                right: 20px;
                z-index: 9999;
                padding: 10px 15px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: 500;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                backdrop-filter: blur(10px);
                transition: all 0.3s ease;
            `;
            document.body.appendChild(statusElement);
        }
        
        statusElement.textContent = message;
        statusElement.className = `voice-status position-fixed alert alert-${type}`;
        statusElement.style.display = 'block';
        statusElement.style.opacity = '1';
    }
    
    hideVoiceStatus() {
        const statusElement = document.getElementById('voiceStatus');
        if (statusElement) {
            statusElement.style.opacity = '0';
            setTimeout(() => {
                statusElement.style.display = 'none';
            }, 300);
        }
    }
    
    // Utility methods
    isRecognitionSupported() {
        return 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window;
    }
    
    isSynthesisSupported() {
        return 'speechSynthesis' in window;
    }
    
    getAvailableVoices(langCode) {
        const voiceLang = this.languageMap[langCode] || 'en-IN';
        return this.voices.filter(voice => 
            voice.lang === voiceLang || 
            voice.lang.startsWith(voiceLang.split('-')[0])
        );
    }
}

// Global voice support functions
function initializeVoiceSupport() {
    if (!window.voiceSupport) {
        window.voiceSupport = new VoiceSupport();
    }
    return window.voiceSupport;
}

function startVoiceInput() {
    if (window.voiceSupport) {
        if (window.voiceSupport.isListening) {
            window.voiceSupport.stopListening();
        } else {
            window.voiceSupport.startListening();
        }
    }
}

function speakText(text, langCode = 'en') {
    if (window.voiceSupport) {
        window.voiceSupport.speak(text, langCode);
    }
}

function stopSpeaking() {
    if (window.voiceSupport) {
        window.voiceSupport.stopSpeaking();
    }
}

// Initialize voice support when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeVoiceSupport();
    
    // Update language when language manager changes language
    if (window.languageManager) {
        const originalSetLanguage = window.languageManager.setLanguage;
        window.languageManager.setLanguage = function(langCode, displayName) {
            originalSetLanguage.call(this, langCode, displayName);
            if (window.voiceSupport) {
                window.voiceSupport.setLanguage(langCode);
            }
        };
    }
});