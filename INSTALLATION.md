# 🚀 LegalEase AI Advanced - Installation Guide

## Quick Start (Recommended)

### Option 1: Using the Startup Script
```bash
python start.py
```
This will automatically check and install dependencies, then start the application.

### Option 2: Manual Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python run.py
   ```

3. **Access the Application**
   - Open your browser and go to: `http://localhost:5000`

## Detailed Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for AI features)

### Step-by-Step Installation

1. **Download/Clone the Project**
   ```bash
   # If using git
   git clone <repository-url>
   cd legalease-ai-advanced
   
   # Or download and extract the ZIP file
   ```

2. **Create Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration (Optional)**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env file with your settings (optional)
   # The application will work with default settings
   ```

5. **Run the Application**
   ```bash
   python run.py
   ```

6. **Access the Application**
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - Start using LegalEase AI!

## Troubleshooting

### Common Issues

#### 1. Import Errors
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Install the missing package
```bash
pip install flask
```

#### 2. Port Already in Use
```
Address already in use
```
**Solution**: Either:
- Kill the process using port 5000
- Or modify the port in `run.py` (change port=5000 to another port)

#### 3. AI Features Not Working
```
Gemini AI initialization failed
```
**Solution**: 
- Check your internet connection
- The application will work in fallback mode without AI

#### 4. Permission Errors
**Solution**: 
- Run with administrator/sudo privileges
- Or install packages in user mode: `pip install --user -r requirements.txt`

### System Requirements

#### Minimum Requirements
- **OS**: Windows 7+, macOS 10.12+, or Linux
- **Python**: 3.8+
- **RAM**: 2GB
- **Storage**: 500MB free space
- **Internet**: Required for AI features

#### Recommended Requirements
- **OS**: Windows 10+, macOS 11+, or Ubuntu 20.04+
- **Python**: 3.9+
- **RAM**: 4GB+
- **Storage**: 1GB free space
- **Internet**: Stable broadband connection

### Browser Compatibility

#### Fully Supported
- Google Chrome 90+
- Mozilla Firefox 88+
- Microsoft Edge 90+
- Safari 14+

#### Partially Supported
- Internet Explorer 11 (limited features)
- Older browser versions (basic functionality only)

## Features Available After Installation

### ✅ Immediately Available
- AI Legal Assistant (with internet)
- Multi-language interface
- Legal resources and templates
- User registration and profiles
- Document analysis
- Lawyer search and booking

### 🔧 Requires Configuration
- Email notifications (requires SMTP settings)
- Advanced analytics (requires database setup)
- Custom AI models (requires API keys)

## Getting Help

### If Installation Fails
1. Check Python version: `python --version`
2. Update pip: `pip install --upgrade pip`
3. Try installing packages individually:
   ```bash
   pip install flask
   pip install google-generativeai
   pip install werkzeug
   ```

### If Application Won't Start
1. Check for error messages in the terminal
2. Ensure all files are in the correct location
3. Try running with verbose output: `python run.py --debug`

### For Other Issues
- Check the console output for error messages
- Ensure your firewall isn't blocking the application
- Try accessing via `http://127.0.0.1:5000` instead of localhost

## Next Steps

After successful installation:

1. **Explore the Features**
   - Try the AI chat assistant
   - Browse legal resources
   - Test document analysis
   - Create user accounts

2. **Customize Settings**
   - Edit `.env` file for custom configuration
   - Set up email notifications
   - Configure database settings

3. **Start Using**
   - Register as a client or advocate
   - Start chatting with the AI assistant
   - Upload documents for analysis
   - Connect with legal professionals

## Support

For technical support or questions:
- Check the README.md for detailed information
- Review the troubleshooting section above
- Contact the developer: Akarsh Chaturvedi

---

**Enjoy using LegalEase AI Advanced!** 🎉

*Making legal assistance accessible to every Indian citizen* ⚖️