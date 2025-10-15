#!/usr/bin/env python3
"""
LegalEase AI Advanced - Dependency Installer
Installs required and optional packages
"""

import subprocess
import sys

# Core requirements (essential for basic functionality)
CORE_PACKAGES = [
    'Flask>=2.3.0',
    'Werkzeug>=2.3.0'
]

# Optional packages (for enhanced features)
OPTIONAL_PACKAGES = {
    'AI Features': [
        'google-generativeai>=0.3.2'
    ],
    'Real-time Features': [
        'flask-socketio>=5.3.0',
        'flask-cors>=4.0.0'
    ],
    'Document Processing': [
        'pdfplumber>=0.9.0',
        'python-docx>=1.1.0'
    ],
    'Additional Features': [
        'python-dotenv>=1.0.0',
        'Pillow>=10.0.0',
        'requests>=2.31.0'
    ]
}

def install_package(package):
    """Install a single package"""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🚀 LegalEase AI Advanced - Dependency Installer")
    print("=" * 50)
    
    # Install core packages
    print("📦 Installing core packages...")
    failed_core = []
    for package in CORE_PACKAGES:
        print(f"   Installing {package}...")
        if install_package(package):
            print(f"   ✅ {package} installed successfully")
        else:
            print(f"   ❌ Failed to install {package}")
            failed_core.append(package)
    
    if failed_core:
        print(f"\n❌ Failed to install core packages: {', '.join(failed_core)}")
        print("The application may not work properly without these packages.")
        return False
    
    print("\n✅ Core packages installed successfully!")
    
    # Install optional packages
    print("\n📦 Installing optional packages...")
    for category, packages in OPTIONAL_PACKAGES.items():
        print(f"\n   {category}:")
        for package in packages:
            print(f"      Installing {package}...")
            if install_package(package):
                print(f"      ✅ {package} installed successfully")
            else:
                print(f"      ⚠️  Failed to install {package} (optional)")
    
    print("\n🎉 Installation completed!")
    print("\nYou can now run the application with: python run.py")
    
    return True

if __name__ == '__main__':
    success = main()
    if not success:
        sys.exit(1)