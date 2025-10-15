#!/usr/bin/env python3
"""
LegalEase AI Advanced - Deployment Helper Script
Developed by Akarsh Chaturvedi
"""

import os
import sys
import subprocess
import shutil

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Output: {e.output}")
        return False

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'run.py',
        'requirements-deploy.txt',
        'Procfile',
        'runtime.txt',
        '.env.example'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False

    print("✅ All required deployment files found!")
    return True

def setup_git():
    """Initialize git repository if not exists"""
    if not os.path.exists('.git'):
        print("🔄 Initializing Git repository...")
        commands = [
            "git init",
            "git add .",
            "git commit -m 'Initial commit - LegalEase AI Advanced'"
        ]

        for cmd in commands:
            if not run_command(cmd, f"Running: {cmd}"):
                return False
    else:
        print("✅ Git repository already exists!")
        # Add and commit current changes
        run_command("git add .", "Adding current changes")
        run_command("git commit -m 'Update for deployment'", "Committing changes")

    return True

def create_env_file():
    """Create .env file from example if it doesn't exist"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            print("✅ Created .env file from .env.example")
            print("⚠️  Please edit .env file with your actual API keys!")
        else:
            print("❌ .env.example file not found!")
            return False
    else:
        print("✅ .env file already exists!")

    return True

def main():
    """Main deployment preparation function"""
    print("🚀 LegalEase AI Advanced - Deployment Preparation")
    print("=" * 60)

    # Check requirements
    if not check_requirements():
        print("❌ Please ensure all required files are present!")
        sys.exit(1)

    # Create .env file
    if not create_env_file():
        print("❌ Failed to create .env file!")
        sys.exit(1)

    # Setup git
    if not setup_git():
        print("❌ Failed to setup Git repository!")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("🎉 Deployment preparation completed successfully!")
    print("\n📋 Next Steps:")
    print("1. Edit .env file with your actual API keys")
    print("2. Create a GitHub repository and push your code:")
    print("   git remote add origin https://github.com/yourusername/legalease-ai.git")
    print("   git push -u origin main")
    print("3. Choose a deployment platform:")
    print("   • Render.com (Recommended)")
    print("   • Railway.app")
    print("   • Heroku")
    print("   • Vercel")
    print("4. Follow the deployment guide in FREE_DEPLOYMENT_GUIDE.md")
    print("\n🌟 Your LegalEase AI Advanced will be live soon!")
    print("=" * 60)

if __name__ == '__main__':
    main()