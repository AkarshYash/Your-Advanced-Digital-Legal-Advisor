#!/usr/bin/env python3
"""
LegalEase AI Advanced - Simple Startup Script
Quick way to start the application
"""

import subprocess
import sys
import os

def check_requirements():
    """Check if core packages are installed"""
    core_packages = ['flask', 'werkzeug']
    optional_packages = [
        'google-generativeai', 'flask-socketio', 'flask-cors', 
        'pdfplumber', 'python-docx', 'requests'
    ]
    
    missing_core = []
    missing_optional = []
    
    # Check core packages
    for package in core_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_core.append(package)
    
    # Check optional packages
    for package in optional_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_optional.append(package)
    
    if missing_core:
        print("❌ Missing core packages (required):")
        for package in missing_core:
            print(f"   - {package}")
        print("\n📦 Installing core packages...")
        
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_core)
            print("✅ Core packages installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install core packages. Please install manually:")
            print(f"   pip install {' '.join(missing_core)}")
            return False
    
    if missing_optional:
        print("⚠️  Missing optional packages (some features may be limited):")
        for package in missing_optional:
            print(f"   - {package}")
        print("\n💡 To install optional packages, run: python install_dependencies.py")
        print("   Or install manually: pip install " + " ".join(missing_optional))
    
    return True

def main():
    print("🚀 LegalEase AI Advanced - Startup Script")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('run.py'):
        print("❌ Error: run.py not found!")
        print("Please make sure you're in the correct directory.")
        return
    
    # Check requirements
    if not check_requirements():
        return
    
    print("🎯 Starting LegalEase AI Advanced...")
    print("🔗 The application will be available at: http://localhost:5000")
    print("=" * 50)
    
    try:
        # Run the main application
        subprocess.run([sys.executable, 'run.py'])
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()