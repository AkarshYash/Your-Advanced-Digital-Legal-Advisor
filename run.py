#!/usr/bin/env python3
"""
LegalEase AI Advanced - Main Application Runner
Developed by Akarsh Chaturvedi
"""

import os
import sys
from app import create_app, socketio
from app.models import db

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main application entry point"""
    print("🚀 Starting LegalEase AI Advanced...")
    print("=" * 50)
    
    # Create Flask app
    app = create_app()
    
    # Initialize database
    with app.app_context():
        db.init_database()
        
        print("✅ Application initialized successfully!")
        print("📊 Database tables created/verified")
        print("🤖 AI Assistant ready")
        print("🌐 Multi-language support enabled")
        print("=" * 50)
        print("🎯 Features Available:")
        print("   • AI-Powered Legal Assistant")
        print("   • Document Analysis & Generation")
        print("   • Expert Lawyer Network")
        print("   • Legal Resources & Templates")
        print("   • Multi-language Support (12+ languages)")
        print("   • Real-time Chat with Voice Input")
        print("   • Advanced User Management")
        print("   • Student Tools & Case Study Analyzer")
        print("   • AI Subject Tutor & Quiz Generator")
        print("   • Study Planner & Legal Research Assistant")
        print("=" * 50)
    
    # Run the application
    try:
        print("🌟 LegalEase AI Advanced is running!")
        print("🔗 Access the application at: http://localhost:5000")
        print("👨‍💻 Developed by: Akarsh Chaturvedi")
        print("=" * 50)
        
        # Use SocketIO for real-time features if available
        if socketio:
            socketio.run(
                app, 
                host='0.0.0.0', 
                port=5000, 
                debug=True,
                allow_unsafe_werkzeug=True
            )
        else:
            # Fallback to regular Flask
            app.run(
                host='0.0.0.0',
                port=5000,
                debug=True
            )
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()