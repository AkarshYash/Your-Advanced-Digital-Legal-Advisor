# 🚀 LegalEase AI Advanced - Startup Guide

## Quick Start (3 Steps)

### 1. Test the Application
```bash
python test_app.py
```
This will check if everything is working correctly.

### 2. Install Dependencies (if needed)
```bash
python install_dependencies.py
```
This will install all required and optional packages.

### 3. Run the Application
```bash
python run.py
```
Then open your browser to `http://localhost:5000`

---

## Detailed Setup Instructions

### Prerequisites
- **Python 3.8+** (Check with: `python --version`)
- **Internet connection** (for AI features)
- **Modern web browser** (Chrome, Firefox, Edge, Safari)

### Installation Options

#### Option A: Automatic Setup (Recommended)
```bash
# 1. Test everything first
python test_app.py

# 2. Install what's needed
python install_dependencies.py

# 3. Start the application
python run.py
```

#### Option B: Manual Setup
```bash
# Install core packages
pip install Flask Werkzeug

# Install optional packages (for full features)
pip install google-generativeai flask-socketio flask-cors
pip install pdfplumber python-docx requests python-dotenv

# Run the application
python run.py
```

#### Option C: Simple Start (Minimal Features)
```bash
# Just install the basics
pip install Flask Werkzeug

# Run with basic features only
python run.py
```

---

## What Works Without Optional Packages

### ✅ Always Available (Core Features)
- **Web Interface**: All pages and navigation
- **User System**: Registration, login, profiles
- **Basic AI Chat**: Fallback responses when Gemini AI unavailable
- **Legal Resources**: Browse constitutional articles and legal information
- **Student Tools**: All student features with fallback content
- **Lawyer Directory**: Browse and search lawyers
- **Templates**: View and use legal document templates

### 🔧 Enhanced with Optional Packages
- **Advanced AI Chat**: Google Gemini AI responses (`google-generativeai`)
- **Real-time Features**: Live chat updates (`flask-socketio`)
- **Document Analysis**: PDF/DOC file processing (`pdfplumber`, `python-docx`)
- **File Uploads**: Enhanced file handling capabilities

---

## Troubleshooting

### Common Issues & Solutions

#### 1. Import Errors
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Install Flask
```bash
pip install Flask
```

#### 2. Port Already in Use
```
Address already in use: Port 5000
```
**Solutions**:
- Kill existing process: `taskkill /f /im python.exe` (Windows)
- Or change port in `run.py`: Change `port=5000` to `port=5001`

#### 3. AI Features Not Working
```
Gemini AI initialization failed
```
**Solutions**:
- Check internet connection
- Install AI package: `pip install google-generativeai`
- App will work with fallback responses if AI unavailable

#### 4. Template Errors
```
TemplateNotFound: template.html
```
**Solution**: All templates are included, restart the application

#### 5. Database Errors
```
Database is locked
```
**Solution**: Restart the application (database auto-creates)

### Getting Help

1. **Run the test script**: `python test_app.py`
2. **Check the console output** for specific error messages
3. **Try minimal installation** first, then add features
4. **Restart the application** if you encounter issues

---

## Application Features

### 🏠 **Main Features**
- **Home Page**: Modern landing page with feature showcase
- **AI Chat**: Legal consultation with AI assistant
- **Document Analysis**: Upload and analyze legal documents
- **Lawyer Network**: Find and connect with verified lawyers
- **Legal Resources**: Constitution, IPC sections, case studies

### 🎓 **Student Features**
- **Student Dashboard**: Comprehensive learning hub
- **Case Study Analyzer**: AI-powered case analysis
- **Subject Tutor**: Interactive learning for all LLB subjects
- **Quiz Generator**: Custom practice quizzes
- **Study Planner**: AI-generated study schedules
- **Legal Research**: Advanced research assistant

### 👥 **User Management**
- **Dual Accounts**: Client and Advocate registration
- **Profile Management**: Detailed user profiles
- **Authentication**: Secure login/logout system
- **Dashboard**: Personalized user dashboards

---

## File Structure

```
LegalEase AI Advanced/
├── 📄 run.py                 # Main application runner
├── 📄 start.py               # Simple startup script
├── 📄 test_app.py            # Application tester
├── 📄 install_dependencies.py # Dependency installer
├── 📄 config.py              # Configuration settings
├── 📄 requirements.txt       # Package requirements
├── 📁 app/                   # Main application
│   ├── 📄 __init__.py        # App factory
│   ├── 📄 models.py          # Database models
│   ├── 📁 main/              # Main routes
│   ├── 📁 auth/              # Authentication
│   ├── 📁 chat/              # AI chat system
│   ├── 📁 api/               # REST APIs
│   ├── 📁 student/           # Student features
│   └── 📁 templates/         # HTML templates
└── 📁 uploads/               # File uploads (auto-created)
```

---

## Next Steps After Installation

### 1. **Explore the Application**
- Visit the home page and browse features
- Try the AI chat assistant
- Register user accounts (both client and advocate)
- Test student tools and features

### 2. **Customize Configuration**
- Edit `config.py` for custom settings
- Add your own Gemini AI API key for enhanced features
- Configure email settings (optional)

### 3. **Add Content**
- Upload legal documents for analysis
- Create custom legal templates
- Add more legal resources and case studies

### 4. **Deploy (Optional)**
- The application is ready for deployment
- Works on local networks and cloud platforms
- Supports multiple users simultaneously

---

## Performance Tips

### For Best Experience:
1. **Use Chrome or Firefox** for optimal performance
2. **Stable internet connection** for AI features
3. **Close unnecessary browser tabs** to free memory
4. **Keep the application updated** with latest features

### For Development:
1. **Enable debug mode** in `config.py`
2. **Use virtual environment** for package isolation
3. **Monitor console output** for debugging
4. **Test with different user types** (client/advocate)

---

## Support & Updates

### Getting Support:
- **Test Script**: Run `python test_app.py` for diagnostics
- **Documentation**: Check README.md for detailed information
- **Error Messages**: Console output provides helpful debugging info

### Future Updates:
- **Automatic Updates**: Check for new versions periodically
- **Feature Requests**: Suggest new features for future releases
- **Bug Reports**: Report issues for quick resolution

---

## Success! 🎉

If you've followed this guide, you should now have:
- ✅ A fully functional legal AI application
- ✅ Modern web interface with 3D effects
- ✅ AI-powered legal assistance
- ✅ Comprehensive student learning tools
- ✅ Professional lawyer network
- ✅ Document analysis capabilities

**Enjoy using LegalEase AI Advanced!**

*Making legal assistance accessible to every Indian citizen* ⚖️🤖