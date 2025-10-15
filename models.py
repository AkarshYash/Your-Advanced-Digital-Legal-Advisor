import sqlite3

class Database:
    def __init__(self, db_path='legalease_advanced.db'):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Enhanced Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                user_type VARCHAR(20) NOT NULL,
                full_name VARCHAR(100) NOT NULL,
                phone VARCHAR(15),
                address TEXT,
                profile_image VARCHAR(500),
                date_of_birth DATE,
                gender VARCHAR(10),
                preferred_language VARCHAR(10) DEFAULT 'en',
                is_verified BOOLEAN DEFAULT 0,
                is_active BOOLEAN DEFAULT 1,
                email_verified BOOLEAN DEFAULT 0,
                phone_verified BOOLEAN DEFAULT 0,
                two_factor_enabled BOOLEAN DEFAULT 0,
                last_login TIMESTAMP,
                login_count INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Enhanced Advocate profiles
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS advocate_profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                bar_council_id VARCHAR(50),
                license_number VARCHAR(100),
                years_experience INTEGER,
                specializations TEXT,
                practice_areas TEXT,
                languages TEXT,
                court_locations TEXT,
                consultation_fee DECIMAL(10,2),
                hourly_rate DECIMAL(10,2),
                rating DECIMAL(3,2) DEFAULT 0.0,
                total_cases INTEGER DEFAULT 0,
                cases_won INTEGER DEFAULT 0,
                cases_pending INTEGER DEFAULT 0,
                bio TEXT,
                education TEXT,
                certifications TEXT,
                achievements TEXT,
                office_address TEXT,
                office_timing VARCHAR(100),
                availability_status VARCHAR(20) DEFAULT 'available',
                consultation_modes TEXT,
                social_links TEXT,
                verification_status VARCHAR(20) DEFAULT 'pending',
                verification_documents TEXT,
                subscription_plan VARCHAR(20) DEFAULT 'basic',
                subscription_expires DATE,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Enhanced Client profiles
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS client_profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                occupation VARCHAR(100),
                company VARCHAR(100),
                annual_income VARCHAR(50),
                emergency_contact VARCHAR(15),
                emergency_contact_name VARCHAR(100),
                legal_history TEXT,
                case_preferences TEXT,
                communication_preferences TEXT,
                notification_settings TEXT,
                privacy_settings TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Enhanced Chat sessions
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                session_title VARCHAR(200),
                session_type VARCHAR(50) DEFAULT 'general',
                language VARCHAR(10) DEFAULT 'en',
                total_messages INTEGER DEFAULT 0,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Enhanced Chat messages
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                message TEXT NOT NULL,
                message_type VARCHAR(20) DEFAULT 'text',
                sender_type VARCHAR(20) DEFAULT 'user',
                ai_model VARCHAR(50),
                response_time DECIMAL(5,3),
                tokens_used INTEGER,
                language VARCHAR(10) DEFAULT 'en',
                sentiment_score DECIMAL(3,2),
                legal_categories TEXT,
                confidence_score DECIMAL(3,2),
                attachments TEXT,
                is_flagged BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES chat_sessions (id),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # Document analysis
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS document_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                filename VARCHAR(255) NOT NULL,
                file_path VARCHAR(500),
                file_type VARCHAR(20),
                file_size INTEGER,
                analysis_type VARCHAR(50),
                analysis_result TEXT,
                key_points TEXT,
                legal_issues TEXT,
                recommendations TEXT,
                confidence_score DECIMAL(3,2),
                processing_time DECIMAL(5,3),
                status VARCHAR(20) DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Legal templates
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS legal_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(200) NOT NULL,
                category VARCHAR(100) NOT NULL,
                subcategory VARCHAR(100),
                description TEXT,
                template_content TEXT NOT NULL,
                fields_required TEXT,
                language VARCHAR(10) DEFAULT 'en',
                complexity_level VARCHAR(20) DEFAULT 'basic',
                usage_count INTEGER DEFAULT 0,
                rating DECIMAL(3,2) DEFAULT 0.0,
                tags TEXT,
                created_by INTEGER,
                is_premium BOOLEAN DEFAULT 0,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (created_by) REFERENCES users (id)
            )
        ''')
        
        # Appointments system
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                advocate_id INTEGER NOT NULL,
                appointment_date DATETIME NOT NULL,
                duration_minutes INTEGER DEFAULT 60,
                appointment_type VARCHAR(50) DEFAULT 'consultation',
                meeting_mode VARCHAR(20) DEFAULT 'online',
                meeting_link VARCHAR(500),
                case_type VARCHAR(100),
                case_description TEXT,
                urgency_level VARCHAR(20) DEFAULT 'normal',
                consultation_fee DECIMAL(10,2),
                payment_status VARCHAR(20) DEFAULT 'pending',
                payment_id VARCHAR(100),
                status VARCHAR(20) DEFAULT 'scheduled',
                notes TEXT,
                reminder_sent BOOLEAN DEFAULT 0,
                feedback_rating INTEGER,
                feedback_comment TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (client_id) REFERENCES users (id),
                FOREIGN KEY (advocate_id) REFERENCES users (id)
            )
        ''')
        
        # Legal resources
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS legal_resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(200) NOT NULL,
                category VARCHAR(100) NOT NULL,
                subcategory VARCHAR(100),
                content_type VARCHAR(50),
                description TEXT,
                content TEXT,
                file_path VARCHAR(500),
                external_url VARCHAR(500),
                language VARCHAR(10) DEFAULT 'en',
                difficulty_level VARCHAR(20) DEFAULT 'beginner',
                tags TEXT,
                view_count INTEGER DEFAULT 0,
                like_count INTEGER DEFAULT 0,
                is_featured BOOLEAN DEFAULT 0,
                is_premium BOOLEAN DEFAULT 0,
                created_by INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (created_by) REFERENCES users (id)
            )
        ''')
        
        # User activity logs
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_activity (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                activity_type VARCHAR(50) NOT NULL,
                activity_description TEXT,
                ip_address VARCHAR(45),
                user_agent TEXT,
                session_id VARCHAR(100),
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Notifications
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title VARCHAR(200) NOT NULL,
                message TEXT NOT NULL,
                notification_type VARCHAR(50) DEFAULT 'info',
                priority VARCHAR(20) DEFAULT 'normal',
                is_read BOOLEAN DEFAULT 0,
                action_url VARCHAR(500),
                expires_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # System settings
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                setting_key VARCHAR(100) UNIQUE NOT NULL,
                setting_value TEXT,
                setting_type VARCHAR(50) DEFAULT 'string',
                description TEXT,
                is_public BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert default legal templates
        self._insert_default_templates(cursor)
        
        # Insert default legal resources
        self._insert_default_resources(cursor)
        
        # Student-specific tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS case_study_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                case_text TEXT NOT NULL,
                analysis_result TEXT,
                analysis_type VARCHAR(50) DEFAULT 'comprehensive',
                processing_time DECIMAL(5,3),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS study_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                subject VARCHAR(100) NOT NULL,
                topic VARCHAR(200) NOT NULL,
                question TEXT,
                response TEXT,
                difficulty_level VARCHAR(20) DEFAULT 'intermediate',
                duration_minutes DECIMAL(5,2),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS generated_quizzes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                subject VARCHAR(100) NOT NULL,
                topic VARCHAR(200) NOT NULL,
                questions TEXT NOT NULL,
                difficulty VARCHAR(20) DEFAULT 'intermediate',
                num_questions INTEGER DEFAULT 5,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quiz_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                quiz_id INTEGER NOT NULL,
                answers TEXT NOT NULL,
                score INTEGER,
                total_questions INTEGER,
                time_taken INTEGER,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (quiz_id) REFERENCES generated_quizzes (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS study_plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                semester VARCHAR(50),
                subjects TEXT NOT NULL,
                exam_date DATE,
                study_hours_per_day INTEGER,
                weak_subjects TEXT,
                plan_data TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS legal_research (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                query TEXT NOT NULL,
                research_type VARCHAR(50) DEFAULT 'general',
                result TEXT,
                sources TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS study_materials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(200) NOT NULL,
                subject VARCHAR(100) NOT NULL,
                semester VARCHAR(50),
                material_type VARCHAR(50) NOT NULL,
                content TEXT,
                file_path VARCHAR(500),
                difficulty_level VARCHAR(20) DEFAULT 'intermediate',
                tags TEXT,
                view_count INTEGER DEFAULT 0,
                rating DECIMAL(3,2) DEFAULT 0.0,
                uploaded_by INTEGER,
                is_verified BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (uploaded_by) REFERENCES users (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                subject VARCHAR(100) NOT NULL,
                topic VARCHAR(200),
                progress_percentage DECIMAL(5,2) DEFAULT 0.0,
                last_studied TIMESTAMP,
                study_streak INTEGER DEFAULT 0,
                total_study_time INTEGER DEFAULT 0,
                quiz_scores TEXT,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Insert system settings
        self._insert_system_settings(cursor)
        
        # Insert default study materials
        self._insert_default_study_materials(cursor)
        
        # Insert sample lawyers
        self._insert_sample_lawyers(cursor)
        
        conn.commit()
        conn.close()
        print("✅ Advanced database with student features initialized successfully")
    
    def _insert_default_templates(self, cursor):
        templates = [
            {
                'title': 'Consumer Complaint Format',
                'category': 'Consumer Law',
                'subcategory': 'Complaints',
                'description': 'Standard format for filing consumer complaints',
                'content': '''BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL FORUM
AT [DISTRICT NAME]

COMPLAINT UNDER SECTION 35 OF THE CONSUMER PROTECTION ACT, 2019

Complaint No: ___________
Date: ___________

[COMPLAINANT NAME]
S/o [FATHER'S NAME]
R/o [ADDRESS]
[PHONE NUMBER]
[EMAIL]
                                                    ...Complainant

VERSUS

[OPPOSITE PARTY NAME]
[ADDRESS]
                                                    ...Opposite Party

COMPLAINT UNDER SECTION 35 OF THE CONSUMER PROTECTION ACT, 2019

MOST RESPECTFULLY SHOWETH:

1. That the complainant is a consumer within the meaning of Section 2(7) of the Consumer Protection Act, 2019.

2. That on [DATE], the complainant purchased [PRODUCT/SERVICE] from the opposite party for Rs. [AMOUNT].

3. That the product/service was found to be defective/deficient in the following manner:
   [DESCRIBE DEFECT/DEFICIENCY]

4. That the complainant approached the opposite party on [DATE] but no satisfactory response was received.

5. That the opposite party has committed unfair trade practice and deficiency in service.

PRAYER:
It is therefore prayed that this Hon'ble Forum may be pleased to:
a) Direct the opposite party to replace/repair the defective product
b) Direct the opposite party to refund the amount of Rs. [AMOUNT]
c) Award compensation of Rs. [AMOUNT] for mental agony and harassment
d) Award costs of litigation

Place: [PLACE]                                    [COMPLAINANT SIGNATURE]
Date: [DATE]                                      [COMPLAINANT NAME]''',
                'fields_required': '["complainant_name", "father_name", "address", "phone", "email", "opposite_party", "date_of_purchase", "amount", "defect_description"]',
                'language': 'en',
                'complexity_level': 'intermediate'
            },
            {
                'title': 'Rent Agreement Format',
                'category': 'Property Law',
                'subcategory': 'Agreements',
                'description': 'Standard rental agreement format',
                'content': '''RENT AGREEMENT

This Rent Agreement is made on [DATE] between:

LANDLORD:
Name: [LANDLORD_NAME]
Address: [LANDLORD_ADDRESS]
Phone: [LANDLORD_PHONE]

TENANT:
Name: [TENANT_NAME]
Address: [TENANT_ADDRESS]
Phone: [TENANT_PHONE]

PROPERTY DETAILS:
Address: [PROPERTY_ADDRESS]
Type: [PROPERTY_TYPE]
Area: [PROPERTY_AREA]

TERMS AND CONDITIONS:

1. RENT: The monthly rent is Rs. [MONTHLY_RENT] payable on or before [DUE_DATE] of each month.

2. SECURITY DEPOSIT: The tenant has paid Rs. [SECURITY_DEPOSIT] as security deposit.

3. DURATION: This agreement is for [DURATION] starting from [START_DATE] to [END_DATE].

4. MAINTENANCE: [MAINTENANCE_TERMS]

5. UTILITIES: [UTILITY_TERMS]

6. TERMINATION: Either party can terminate this agreement by giving [NOTICE_PERIOD] notice.

IN WITNESS WHEREOF, both parties have signed this agreement.

LANDLORD SIGNATURE: _______________    TENANT SIGNATURE: _______________
DATE: _______________              DATE: _______________

WITNESS 1: _______________        WITNESS 2: _______________''',
                'fields_required': '["landlord_name", "landlord_address", "landlord_phone", "tenant_name", "tenant_address", "tenant_phone", "property_address", "monthly_rent", "security_deposit", "duration", "start_date", "end_date"]',
                'language': 'en',
                'complexity_level': 'basic'
            }
        ]
        
        for template in templates:
            cursor.execute('''
                INSERT OR IGNORE INTO legal_templates 
                (title, category, subcategory, description, template_content, fields_required, language, complexity_level)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (template['title'], template['category'], template['subcategory'], 
                  template['description'], template['content'], template['fields_required'],
                  template['language'], template['complexity_level']))
    
    def _insert_default_resources(self, cursor):
        resources = [
            {
                'title': 'Indian Constitution - Fundamental Rights',
                'category': 'Constitution',
                'subcategory': 'Fundamental Rights',
                'content_type': 'article',
                'description': 'Complete guide to fundamental rights under Indian Constitution',
                'content': '''FUNDAMENTAL RIGHTS (Articles 12-35)

The Fundamental Rights are the basic human rights enshrined in the Constitution of India which are guaranteed to all citizens. These rights are essential for the development of the personality of every individual and to preserve human dignity.

ARTICLE 14 - RIGHT TO EQUALITY
The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India.

ARTICLE 15 - PROHIBITION OF DISCRIMINATION
The State shall not discriminate against any citizen on grounds only of religion, race, caste, sex, place of birth or any of them.

ARTICLE 16 - EQUALITY OF OPPORTUNITY IN PUBLIC EMPLOYMENT
There shall be equality of opportunity for all citizens in matters relating to employment or appointment to any office under the State.

ARTICLE 17 - ABOLITION OF UNTOUCHABILITY
"Untouchability" is abolished and its practice in any form is forbidden.

ARTICLE 18 - ABOLITION OF TITLES
No title, not being a military or academic distinction, shall be conferred by the State.

ARTICLE 19 - PROTECTION OF CERTAIN RIGHTS REGARDING FREEDOM OF SPEECH, ETC.
All citizens shall have the right to:
(a) freedom of speech and expression;
(b) assemble peaceably and without arms;
(c) form associations or unions;
(d) move freely throughout the territory of India;
(e) reside and settle in any part of the territory of India;
(f) practice any profession, or to carry on any occupation, trade or business.

ARTICLE 20 - PROTECTION IN RESPECT OF CONVICTION FOR OFFENCES
No person shall be:
(a) convicted of any offence except for violation of a law in force at the time of the commission of the act;
(b) subjected to a penalty greater than that which might have been inflicted under the law in force at the time of the commission of the offence;
(c) compelled to be a witness against himself.

ARTICLE 21 - PROTECTION OF LIFE AND PERSONAL LIBERTY
No person shall be deprived of his life or personal liberty except according to procedure established by law.

ARTICLE 21A - RIGHT TO EDUCATION
The State shall provide free and compulsory education to all children of the age of six to fourteen years.''',
                'language': 'en',
                'difficulty_level': 'intermediate',
                'is_featured': True
            }
        ]
        
        for resource in resources:
            cursor.execute('''
                INSERT OR IGNORE INTO legal_resources 
                (title, category, subcategory, content_type, description, content, language, difficulty_level, is_featured)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (resource['title'], resource['category'], resource['subcategory'],
                  resource['content_type'], resource['description'], resource['content'],
                  resource['language'], resource['difficulty_level'], resource['is_featured']))
    
    def _insert_system_settings(self, cursor):
        settings = [
            ('app_name', 'LegalEase AI Advanced', 'string', 'Application name'),
            ('app_version', '2.0.0', 'string', 'Application version'),
            ('maintenance_mode', 'false', 'boolean', 'Maintenance mode status'),
            ('max_chat_sessions', '10', 'integer', 'Maximum chat sessions per user'),
            ('max_file_size', '16777216', 'integer', 'Maximum file upload size in bytes'),
            ('supported_languages', '["en", "hi", "ta", "te", "bn", "mr", "gu", "pa", "kn", "ml", "or", "as"]', 'json', 'Supported languages'),
            ('default_language', 'en', 'string', 'Default application language'),
            ('ai_model', 'gemini-1.5-flash', 'string', 'Default AI model'),
            ('enable_voice_chat', 'true', 'boolean', 'Enable voice chat feature'),
            ('enable_document_analysis', 'true', 'boolean', 'Enable document analysis feature'),
            ('enable_student_features', 'true', 'boolean', 'Enable student-specific features'),
            ('max_quiz_questions', '20', 'integer', 'Maximum questions per quiz'),
            ('study_session_timeout', '3600', 'integer', 'Study session timeout in seconds')
        ]
        
        for setting in settings:
            cursor.execute('''
                INSERT OR IGNORE INTO system_settings 
                (setting_key, setting_value, setting_type, description)
                VALUES (?, ?, ?, ?)
            ''', setting)
    
    def _insert_default_study_materials(self, cursor):
        """Insert default study materials for students"""
        study_materials = [
            {
                'title': 'Introduction to Indian Constitution',
                'subject': 'Constitutional Law',
                'semester': '1st Semester',
                'material_type': 'notes',
                'content': '''# Introduction to Indian Constitution

## Historical Background
The Indian Constitution was adopted on 26th November 1949 and came into effect on 26th January 1950.

## Key Features
1. **Longest Written Constitution**: The Indian Constitution is the longest written constitution in the world
2. **Federal Structure**: India follows a federal system with a strong center
3. **Parliamentary System**: India adopted the British Parliamentary system
4. **Fundamental Rights**: Guaranteed rights for all citizens
5. **Directive Principles**: Guidelines for state policy

## Important Articles
- **Article 1**: Name and territory of the Union
- **Article 14**: Right to Equality
- **Article 19**: Freedom of Speech and Expression
- **Article 21**: Right to Life and Personal Liberty
- **Article 32**: Right to Constitutional Remedies

## Study Tips for Students
1. Focus on understanding the philosophy behind each article
2. Learn landmark cases that interpret constitutional provisions
3. Understand the relationship between Fundamental Rights and Directive Principles
4. Practice case studies and constitutional amendments

## Important Cases
- **Kesavananda Bharati v. State of Kerala (1973)**: Basic Structure Doctrine
- **Maneka Gandhi v. Union of India (1978)**: Expanded interpretation of Article 21
- **Minerva Mills v. Union of India (1980)**: Limitations on amending power

## Exam Preparation
- Create timeline of constitutional development
- Make comparative charts of different rights
- Practice previous year questions
- Focus on recent constitutional amendments''',
                'difficulty_level': 'beginner',
                'tags': '["constitution", "fundamental rights", "articles", "beginner"]'
            },
            {
                'title': 'Contract Law Fundamentals',
                'subject': 'Contract Law',
                'semester': '1st Semester',
                'material_type': 'notes',
                'content': '''# Contract Law Fundamentals

## Definition of Contract
A contract is an agreement enforceable by law (Section 2(h) of Indian Contract Act, 1872).

## Essential Elements of a Valid Contract
1. **Offer and Acceptance**: Clear proposal and unqualified acceptance
2. **Consideration**: Something in return (quid pro quo)
3. **Capacity to Contract**: Parties must be competent
4. **Free Consent**: Agreement without coercion, fraud, or mistake
5. **Lawful Object**: Purpose must be legal
6. **Legal Formalities**: Writing, registration if required

## Types of Contracts
### Based on Formation
- **Express Contract**: Terms clearly stated
- **Implied Contract**: Terms inferred from conduct
- **Quasi Contract**: Legal fiction to prevent unjust enrichment

### Based on Performance
- **Executed Contract**: Performance completed
- **Executory Contract**: Performance pending

### Based on Validity
- **Valid Contract**: All essentials present
- **Void Contract**: No legal effect
- **Voidable Contract**: One party can avoid
- **Unenforceable Contract**: Cannot be enforced in court

## Important Sections
- **Section 10**: What agreements are contracts
- **Section 23**: Lawful consideration and object
- **Section 25**: Agreement without consideration is void
- **Section 56**: Agreement to do impossible act

## Landmark Cases
- **Balfour v. Balfour**: Social agreements not contracts
- **Carlill v. Carbolic Smoke Ball Co.**: Unilateral contracts
- **Hadley v. Baxendale**: Remoteness of damages

## Study Strategy
1. Understand each essential element with examples
2. Learn exceptions to general rules
3. Practice case law analysis
4. Focus on remedies for breach of contract''',
                'difficulty_level': 'intermediate',
                'tags': '["contract law", "indian contract act", "essentials", "cases"]'
            },
            {
                'title': 'Criminal Law - IPC Overview',
                'subject': 'Criminal Law',
                'semester': '2nd Semester',
                'material_type': 'notes',
                'content': '''# Indian Penal Code (IPC) - Overview

## Introduction
The Indian Penal Code, 1860 is the main criminal code in India. It defines crimes and prescribes punishments.

## Structure of IPC
- **23 Chapters**: Covering different types of offenses
- **511 Sections**: Defining crimes and punishments
- **General Principles**: Chapters I-V
- **Specific Offenses**: Chapters VI-XXIII

## Important Chapters
### Chapter IV: General Exceptions (Sections 76-106)
- **Section 76**: Act done by mistake of fact
- **Section 79**: Act done by mistake of law
- **Section 96-106**: Right of private defense

### Chapter XVI: Offenses Against Human Body (Sections 299-377)
- **Section 299**: Culpable homicide
- **Section 300**: Murder
- **Section 302**: Punishment for murder
- **Section 304**: Culpable homicide not amounting to murder

### Chapter XVII: Offenses Against Property (Sections 378-462)
- **Section 378**: Theft
- **Section 415**: Cheating
- **Section 420**: Cheating and dishonestly inducing delivery of property

## Key Concepts
1. **Mens Rea**: Guilty mind
2. **Actus Reus**: Guilty act
3. **Intention vs. Knowledge**: Different mental states
4. **Preparation vs. Attempt**: Stages of crime

## Important Distinctions
### Murder vs. Culpable Homicide
- **Murder**: Intention to cause death or knowledge that act is likely to cause death
- **Culpable Homicide**: Intention to cause death or knowledge that act is likely to cause death (broader)

### Theft vs. Robbery vs. Dacoity
- **Theft**: Dishonest taking of movable property
- **Robbery**: Theft with violence or threat
- **Dacoity**: Robbery by five or more persons

## Study Tips
1. Focus on definitions and essential ingredients
2. Learn landmark cases for each section
3. Understand exceptions and their rationale
4. Practice problem-solving with fact patterns
5. Create comparison charts for similar offenses

## Recent Amendments
- Bharatiya Nyaya Sanhita (BNS) 2023 - New criminal code
- Changes in definitions and punishments
- New offenses added (cyber crimes, etc.)''',
                'difficulty_level': 'intermediate',
                'tags': '["criminal law", "ipc", "offenses", "punishments"]'
            }
        ]
        
        for material in study_materials:
            cursor.execute('''
                INSERT OR IGNORE INTO study_materials 
                (title, subject, semester, material_type, content, difficulty_level, tags, is_verified)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (material['title'], material['subject'], material['semester'],
                  material['material_type'], material['content'], material['difficulty_level'],
                  material['tags'], True))
    
    def _insert_sample_lawyers(self, cursor):
        """Insert sample lawyer data for demonstration"""
        # First, insert sample advocate users
        sample_advocates = [
            {
                'username': 'ananya_krishnan',
                'email': 'ananya.krishnan@legalease.com',
                'password_hash': 'hashed_password_123',
                'user_type': 'advocate',
                'full_name': 'Adv. Ananya Krishnan',
                'phone': '+91 98765-43210',
                'address': 'Supreme Court Bar Association, New Delhi',
                'is_verified': True,
                'is_active': True
            },
            {
                'username': 'rohit_malhotra',
                'email': 'rohit.malhotra@legalease.com',
                'password_hash': 'hashed_password_456',
                'user_type': 'advocate',
                'full_name': 'Adv. Rohit Malhotra',
                'phone': '+91 98765-43211',
                'address': 'Bombay High Court, Mumbai',
                'is_verified': True,
                'is_active': True
            },
            {
                'username': 'kavitha_nair',
                'email': 'kavitha.nair@legalease.com',
                'password_hash': 'hashed_password_789',
                'user_type': 'advocate',
                'full_name': 'Adv. Kavitha Nair',
                'phone': '+91 98765-43212',
                'address': 'Kerala High Court, Kochi',
                'is_verified': True,
                'is_active': True
            },
            {
                'username': 'arjun_patel',
                'email': 'arjun.patel@legalease.com',
                'password_hash': 'hashed_password_101',
                'user_type': 'advocate',
                'full_name': 'Adv. Arjun Patel',
                'phone': '+91 98765-43213',
                'address': 'Gujarat High Court, Ahmedabad',
                'is_verified': True,
                'is_active': True
            },
            {
                'username': 'meera_bansal',
                'email': 'meera.bansal@legalease.com',
                'password_hash': 'hashed_password_202',
                'user_type': 'advocate',
                'full_name': 'Adv. Meera Bansal',
                'phone': '+91 98765-43214',
                'address': 'Punjab & Haryana High Court, Chandigarh',
                'is_verified': True,
                'is_active': True
            },
            {
                'username': 'deepak_agarwal',
                'email': 'deepak.agarwal@legalease.com',
                'password_hash': 'hashed_password_303',
                'user_type': 'advocate',
                'full_name': 'Adv. Deepak Agarwal',
                'phone': '+91 98765-43215',
                'address': 'Allahabad High Court, Prayagraj',
                'is_verified': True,
                'is_active': True
            },
            {
                'username': 'shalini_reddy',
                'email': 'shalini.reddy@legalease.com',
                'password_hash': 'hashed_password_404',
                'user_type': 'advocate',
                'full_name': 'Adv. Shalini Reddy',
                'phone': '+91 98765-43216',
                'address': 'Telangana High Court, Hyderabad',
                'is_verified': True,
                'is_active': True
            }
        ]
        
        advocate_profiles = [
            {
                'bar_council_id': 'D/789/2009',
                'license_number': 'SC/ADV/2009/789',
                'years_experience': 14,
                'specializations': 'Criminal Law, Cyber Crime, White Collar Crime',
                'practice_areas': 'Criminal Defense, Cyber Crime Investigation, Economic Offenses',
                'languages': 'Hindi, English, Tamil',
                'court_locations': 'Supreme Court of India, Delhi High Court',
                'consultation_fee': 3000.00,
                'hourly_rate': 5500.00,
                'rating': 4.9,
                'total_cases': 312,
                'cases_won': 267,
                'cases_pending': 18,
                'bio': 'Leading criminal law expert specializing in cyber crimes and white-collar offenses. Successfully defended high-profile cases.',
                'education': 'LLM Criminal Law from Jamia Millia Islamia, Cyber Law Certificate',
                'certifications': 'Cyber Crime Specialist, Economic Offense Expert',
                'achievements': 'Landmark cyber crime judgments, Featured in legal journals',
                'office_address': 'Chamber 12, Supreme Court Bar Association, New Delhi',
                'office_timing': '9:30 AM - 6:30 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Video Call, Phone',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'M/892/2012',
                'license_number': 'BHC/ADV/2012/892',
                'years_experience': 11,
                'specializations': 'Corporate Law, Mergers & Acquisitions, Securities Law',
                'practice_areas': 'Corporate Compliance, M&A Transactions, IPO Advisory',
                'languages': 'Hindi, English, Marathi',
                'court_locations': 'Bombay High Court, NCLT Mumbai',
                'consultation_fee': 4500.00,
                'hourly_rate': 8000.00,
                'rating': 4.7,
                'total_cases': 156,
                'cases_won': 142,
                'cases_pending': 14,
                'bio': 'Corporate law expert with extensive experience in mergers, acquisitions, and securities regulations.',
                'education': 'LLM Corporate Law from Mumbai University, CFA Charter',
                'certifications': 'Corporate Law Expert, Securities Law Specialist',
                'achievements': 'Advised on deals worth ₹5000+ crores, Published corporate law articles',
                'office_address': 'Chamber 8, Bombay High Court, Mumbai',
                'office_timing': '9:00 AM - 8:00 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Video Call, Phone',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'KL/345/2014',
                'license_number': 'KHC/ADV/2014/345',
                'years_experience': 9,
                'specializations': 'Family Law, Women Rights, Child Custody',
                'practice_areas': 'Matrimonial Disputes, Domestic Violence, Adoption',
                'languages': 'Hindi, English, Malayalam, Tamil',
                'court_locations': 'Kerala High Court, Family Courts Kochi',
                'consultation_fee': 2000.00,
                'hourly_rate': 3800.00,
                'rating': 4.8,
                'total_cases': 203,
                'cases_won': 178,
                'cases_pending': 11,
                'bio': 'Compassionate family law advocate specializing in women rights and child welfare cases.',
                'education': 'LLB from Cochin University, Family Law Diploma',
                'certifications': 'Family Counselor, Child Rights Advocate',
                'achievements': 'Helped 300+ families resolve disputes amicably',
                'office_address': 'Chamber 15, Kerala High Court, Kochi',
                'office_timing': '10:00 AM - 6:00 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Video Call',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'GJ/567/2015',
                'license_number': 'GHC/ADV/2015/567',
                'years_experience': 8,
                'specializations': 'Consumer Law, Banking Law, Insurance Disputes',
                'practice_areas': 'Consumer Complaints, Banking Disputes, Insurance Claims',
                'languages': 'Hindi, English, Gujarati',
                'court_locations': 'Gujarat High Court, Consumer Forums',
                'consultation_fee': 1600.00,
                'hourly_rate': 3000.00,
                'rating': 4.6,
                'total_cases': 167,
                'cases_won': 145,
                'cases_pending': 9,
                'bio': 'Consumer rights champion with expertise in banking and insurance law disputes.',
                'education': 'LLB from Gujarat University, Banking Law Certificate',
                'certifications': 'Consumer Law Expert, Banking Ombudsman Certified',
                'achievements': 'Won major cases against banks and insurance companies',
                'office_address': 'Chamber 22, Gujarat High Court, Ahmedabad',
                'office_timing': '9:30 AM - 5:30 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Video Call, Phone',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'PH/234/2016',
                'license_number': 'PHC/ADV/2016/234',
                'years_experience': 7,
                'specializations': 'Property Law, Real Estate, Agricultural Law',
                'practice_areas': 'Property Disputes, Real Estate Transactions, Land Records',
                'languages': 'Hindi, English, Punjabi',
                'court_locations': 'Punjab & Haryana High Court, Revenue Courts',
                'consultation_fee': 1800.00,
                'hourly_rate': 3200.00,
                'rating': 4.5,
                'total_cases': 134,
                'cases_won': 118,
                'cases_pending': 7,
                'bio': 'Property law specialist with deep knowledge of agricultural and real estate matters.',
                'education': 'LLB from Panjab University, Real Estate Law Diploma',
                'certifications': 'Property Law Expert, RERA Consultant',
                'achievements': 'Resolved complex land disputes worth hundreds of crores',
                'office_address': 'Chamber 30, Punjab & Haryana High Court, Chandigarh',
                'office_timing': '9:00 AM - 6:00 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Phone',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'UP/678/2017',
                'license_number': 'AHC/ADV/2017/678',
                'years_experience': 6,
                'specializations': 'Constitutional Law, Public Interest Litigation, Human Rights',
                'practice_areas': 'PIL, Writ Petitions, Human Rights Cases',
                'languages': 'Hindi, English, Urdu',
                'court_locations': 'Allahabad High Court, Supreme Court',
                'consultation_fee': 2200.00,
                'hourly_rate': 4000.00,
                'rating': 4.7,
                'total_cases': 89,
                'cases_won': 76,
                'cases_pending': 8,
                'bio': 'Constitutional law expert fighting for public interest and human rights causes.',
                'education': 'LLM Constitutional Law from Allahabad University',
                'certifications': 'Human Rights Advocate, PIL Specialist',
                'achievements': 'Filed successful PILs for environmental protection',
                'office_address': 'Chamber 18, Allahabad High Court, Prayagraj',
                'office_timing': '10:00 AM - 7:00 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Video Call, Phone',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'TS/890/2018',
                'license_number': 'THC/ADV/2018/890',
                'years_experience': 5,
                'specializations': 'Intellectual Property, Technology Law, Startup Legal',
                'practice_areas': 'Patent Law, Trademark, Copyright, Tech Contracts',
                'languages': 'Hindi, English, Telugu',
                'court_locations': 'Telangana High Court, IP Tribunals',
                'consultation_fee': 2800.00,
                'hourly_rate': 5000.00,
                'rating': 4.4,
                'total_cases': 78,
                'cases_won': 67,
                'cases_pending': 6,
                'bio': 'Young and dynamic IP lawyer helping startups and tech companies with legal compliance.',
                'education': 'LLM IP Law from NALSAR, Technology Law Certificate',
                'certifications': 'IP Law Specialist, Startup Legal Advisor',
                'achievements': 'Helped 100+ startups with legal compliance',
                'office_address': 'Chamber 25, Telangana High Court, Hyderabad',
                'office_timing': '9:00 AM - 8:00 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Video Call, Phone',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'WB/789/2013',
                'license_number': 'CHC/ADV/2013/789',
                'years_experience': 10,
                'specializations': 'Corporate Law, Taxation, Commercial Disputes',
                'practice_areas': 'Company Law, Tax Litigation, Commercial Contracts',
                'languages': 'Hindi, English, Bengali',
                'court_locations': 'Calcutta High Court, Commercial Courts',
                'consultation_fee': 2200.00,
                'hourly_rate': 4000.00,
                'rating': 4.6,
                'total_cases': 156,
                'cases_won': 134,
                'cases_pending': 15,
                'bio': 'Corporate law expert with extensive experience in taxation and commercial disputes.',
                'education': 'LLM in Corporate Law from Calcutta University',
                'certifications': 'Corporate Law Specialist, Tax Consultant',
                'achievements': 'Handled major corporate mergers and acquisitions',
                'office_address': 'Chamber 8, Calcutta High Court, Kolkata',
                'office_timing': '9:30 AM - 6:30 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Video Call, Phone',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'KA/101/2015',
                'license_number': 'KHC/ADV/2015/101',
                'years_experience': 8,
                'specializations': 'Property Law, Real Estate, Civil Litigation',
                'practice_areas': 'Property Disputes, Real Estate Transactions, Civil Cases',
                'languages': 'Hindi, English, Kannada, Tamil',
                'court_locations': 'Karnataka High Court, Civil Courts Bangalore',
                'consultation_fee': 1500.00,
                'hourly_rate': 2800.00,
                'rating': 4.7,
                'total_cases': 123,
                'cases_won': 105,
                'cases_pending': 10,
                'bio': 'Property law specialist with focus on real estate transactions and property disputes.',
                'education': 'LLB from Bangalore University',
                'certifications': 'Property Law Expert, Real Estate Consultant',
                'achievements': 'Resolved complex property disputes worth crores',
                'office_address': 'Chamber 25, Karnataka High Court, Bangalore',
                'office_timing': '10:00 AM - 6:00 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Video Call',
                'verification_status': 'verified',
                'is_active': True
            },
            {
                'bar_council_id': 'RJ/202/2016',
                'license_number': 'RHC/ADV/2016/202',
                'years_experience': 7,
                'specializations': 'Consumer Law, Service Matters, Banking Law',
                'practice_areas': 'Consumer Complaints, Banking Disputes, Service Issues',
                'languages': 'Hindi, English, Rajasthani',
                'court_locations': 'Rajasthan High Court, Consumer Forums',
                'consultation_fee': 1200.00,
                'hourly_rate': 2200.00,
                'rating': 4.5,
                'total_cases': 98,
                'cases_won': 82,
                'cases_pending': 6,
                'bio': 'Consumer law expert helping individuals fight against unfair trade practices and service deficiencies.',
                'education': 'LLB from Rajasthan University',
                'certifications': 'Consumer Law Specialist',
                'achievements': 'Won major consumer cases against big corporations',
                'office_address': 'Chamber 18, Rajasthan High Court, Jaipur',
                'office_timing': '9:00 AM - 5:00 PM',
                'availability_status': 'available',
                'consultation_modes': 'In-person, Phone',
                'verification_status': 'verified',
                'is_active': True
            }
        ]
        
        # Insert advocate users
        for i, advocate in enumerate(sample_advocates):
            cursor.execute('''
                INSERT OR IGNORE INTO users 
                (username, email, password_hash, user_type, full_name, phone, address, is_verified, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (advocate['username'], advocate['email'], advocate['password_hash'],
                  advocate['user_type'], advocate['full_name'], advocate['phone'],
                  advocate['address'], advocate['is_verified'], advocate['is_active']))
            
            # Get the user_id
            cursor.execute('SELECT id FROM users WHERE username = ?', (advocate['username'],))
            user_row = cursor.fetchone()
            if user_row:
                user_id = user_row[0]
                
                # Insert advocate profile
                profile = advocate_profiles[i]
                cursor.execute('''
                    INSERT OR IGNORE INTO advocate_profiles 
                    (user_id, bar_council_id, license_number, years_experience, specializations,
                     practice_areas, languages, court_locations, consultation_fee, hourly_rate,
                     rating, total_cases, cases_won, cases_pending, bio, education, certifications,
                     achievements, office_address, office_timing, availability_status,
                     consultation_modes, verification_status, is_active)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (user_id, profile['bar_council_id'], profile['license_number'],
                      profile['years_experience'], profile['specializations'], profile['practice_areas'],
                      profile['languages'], profile['court_locations'], profile['consultation_fee'],
                      profile['hourly_rate'], profile['rating'], profile['total_cases'],
                      profile['cases_won'], profile['cases_pending'], profile['bio'],
                      profile['education'], profile['certifications'], profile['achievements'],
                      profile['office_address'], profile['office_timing'], profile['availability_status'],
                      profile['consultation_modes'], profile['verification_status'], profile['is_active']))

# Database instance
db = Database()