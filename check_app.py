#!/usr/bin/env python3
"""
LegalEase AI Advanced - Simple App Checker
Quick check if the application can start
"""

def main():
    print("🚀 LegalEase AI Advanced - Quick Check")
    print("=" * 40)
    
    try:
        print("📦 Checking Flask...")
        import flask
        print("   ✅ Flask available")
        
        print("📦 Checking app creation...")
        from app import create_app
        test_app = create_app()
        print("   ✅ App created successfully")
        
        print("📦 Checking database...")
        from app.models import db
        conn = db.get_connection()
        conn.close()
        print("   ✅ Database accessible")
        
        print("\n🎉 All checks passed! Ready to run.")
        print("💡 Run with: python run.py")
        return True
        
    except ImportError as e:
        print(f"   ❌ Missing package: {e}")
        print("💡 Install with: pip install Flask Werkzeug")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

if __name__ == '__main__':
    main()