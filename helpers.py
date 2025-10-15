"""
Helper functions for API routes
"""
from app.models import db
from app.legal_cases_db import enhance_response_with_cases


def get_recommended_advocates(message):
    """Get recommended advocates based on the user's query."""
    message_lower = message.lower()

    # Connect to database to get real advocates
    conn = db.get_connection()
    cursor = conn.cursor()

    # Determine specialization based on query
    specialization_keywords = {
        'criminal': ['fir', 'police', 'theft', 'fraud', 'crime', 'arrest', 'bail',
                     'ipc', 'murder', 'assault'],
        'family': ['divorce', 'marriage', 'custody', 'maintenance', 'domestic',
                   'dowry', 'alimony'],
        'consumer': ['consumer', 'defective', 'product', 'service', 'refund',
                     'warranty', 'complaint'],
        'property': ['property', 'land', 'registration', 'sale', 'purchase',
                     'mutation', 'title'],
        'corporate': ['company', 'business', 'contract', 'agreement',
                      'partnership', 'gst', 'tax']
    }

    detected_specialization = 'general'
    for spec, keywords in specialization_keywords.items():
        if any(keyword in message_lower for keyword in keywords):
            detected_specialization = spec
            break

    # Query advocates based on specialization
    if detected_specialization != 'general':
        cursor.execute('''
            SELECT u.full_name, u.phone, u.email, ap.specializations, ap.years_experience,
                   ap.rating, ap.consultation_fee, ap.court_locations, ap.office_address,
                   ap.consultation_modes, u.id
            FROM users u
            JOIN advocate_profiles ap ON u.id = ap.user_id
            WHERE u.user_type = "advocate" AND u.is_active = 1
            AND ap.verification_status = "verified" AND ap.is_active = 1
            AND ap.specializations LIKE ?
            ORDER BY ap.rating DESC, ap.years_experience DESC
            LIMIT 3
        ''', (f'%{detected_specialization}%',))
    else:
        # Get top-rated general advocates
        cursor.execute('''
            SELECT u.full_name, u.phone, u.email, ap.specializations, ap.years_experience,
                   ap.rating, ap.consultation_fee, ap.court_locations, ap.office_address,
                   ap.consultation_modes, u.id
            FROM users u
            JOIN advocate_profiles ap ON u.id = ap.user_id
            WHERE u.user_type = "advocate" AND u.is_active = 1
            AND ap.verification_status = "verified" AND ap.is_active = 1
            ORDER BY ap.rating DESC, ap.years_experience DESC
            LIMIT 3
        ''')

    advocates = cursor.fetchall()
    conn.close()

    # Format advocate data for frontend
    recommended = []
    for advocate in advocates:
        recommended.append({
            'id': advocate['id'],
            'name': advocate['full_name'],
            'specialization': advocate['specializations'],
            'experience': advocate['years_experience'],
            'rating': advocate['rating'],
            'consultation_fee': advocate['consultation_fee'],
            'phone': advocate['phone'],
            'email': advocate['email'],
            'location': advocate['court_locations'],
            'office_address': advocate['office_address'],
            'consultation_modes': advocate['consultation_modes'],
            'specialization_match': detected_specialization
        })

    return recommended


def extract_legal_categories_from_message(message):
    """Extract legal categories from user message for better classification."""
    message_lower = message.lower()
    categories = []

    category_keywords = {
        'Criminal Law': ['fir', 'police', 'theft', 'fraud', 'crime', 'arrest',
                         'bail', 'ipc', 'murder', 'assault', 'cybercrime'],
        'Family Law': ['divorce', 'marriage', 'custody', 'maintenance', 'domestic',
                       'dowry', 'alimony', 'adoption'],
        'Consumer Protection': ['consumer', 'defective', 'product', 'service',
                               'refund', 'warranty', 'complaint', 'bank'],
        'Property Law': ['property', 'land', 'registration', 'sale', 'purchase',
                        'mutation', 'title', 'rent'],
        'Corporate Law': ['company', 'business', 'contract', 'agreement',
                         'partnership', 'gst', 'tax'],
        'Constitutional Law': ['fundamental rights', 'article', 'constitution',
                              'pil', 'writ', 'habeas corpus'],
        'Labor Law': ['employment', 'salary', 'termination', 'pf', 'esi',
                      'bonus', 'overtime'],
        'Civil Law': ['civil suit', 'damages', 'injunction',
                     'specific performance', 'tort']
    }

    for category, keywords in category_keywords.items():
        if any(keyword in message_lower for keyword in keywords):
            categories.append(category)

    return categories if categories else ['General Legal']


def generate_comprehensive_fallback_response(message, language='en'):
    """Generate comprehensive legal responses with past case integration."""
    message_lower = message.lower()

    # Language-specific responses could be added here in future
    _ = language  # Acknowledge parameter for future use

    # Detect specific legal issues and provide tailored responses
    if any(word in message_lower for word in ['stolen', 'theft', 'mobile', 'phone', 'laptop', 'bike']):
        base_response = """**🤝 Personal Acknowledgment**
I understand your concern about the theft of your property. This is indeed a serious criminal matter that requires immediate legal action, and I'm here to guide you through the entire process step by step.

**⚖️ Legal Viability Assessment**
YES, legal action CAN definitely be taken in this case. Theft is a cognizable offense under Indian law, which means police are legally bound to register your complaint immediately and begin investigation.

**📋 Applicable Legal Framework**
- **Primary Act**: Indian Penal Code (IPC) 1860
- **Specific Sections**: Section 378 (Definition of Theft), Section 379 (Punishment for theft - up to 3 years imprisonment)
- **Constitutional Articles**: Article 21 (Right to life and personal liberty)
- **Relevant Case Laws**: Lalita Kumari vs. Govt. of UP (2013) - Mandatory FIR registration for cognizable offenses

**🏛️ Legal Action Process**
1. **Where to File**: Police station having jurisdiction where the theft occurred
2. **Required Documents**: IMEI number (for phones), purchase receipt, identity proof, any witness details
3. **Filing Procedure**: 
   - Visit police station immediately
   - Provide oral/written complaint with all details
   - Police must register FIR with a number
   - Demand free copy of FIR (your legal right)
   - Note down investigating officer's details
4. **Timeline**: FIR registration is immediate, investigation typically takes 60-90 days

**⚖️ Punishment/Consequences for Offender**
- **Criminal Punishment**: Imprisonment up to 3 years, or fine, or both (Section 379 IPC)
- **Civil Remedies**: Recovery of stolen property or its market value
- **Other Consequences**: Criminal record affecting future employment, travel restrictions

**💰 Your Potential Recovery/Relief**
- **Property Recovery**: Police investigation may lead to recovery of stolen items
- **Monetary Compensation**: Market value of stolen property through court order
- **Victim Compensation**: State victim compensation scheme (₹1 lakh to ₹10 lakh depending on case)
- **Legal Costs**: FIR filing is completely FREE, court proceedings have minimal fees

**📚 Learn More Resources**
- **Related Legal Topics**: Cybercrime (if online fraud involved), Insurance claims, Consumer protection
- **Government Portals**: ecourts.gov.in for case status, cctns.gov.in for FIR status
- **Legal Aid Resources**: NALSA (nalsa.gov.in), District Legal Services Authority for free legal aid

**👨‍💼 Recommended Legal Experts**
Based on your theft case, I recommend consulting:
- **Specialist Required**: Criminal Defense Lawyer with experience in theft cases
- **Experience Level**: Advocate with 3+ years criminal law practice
- **Location Preference**: Local court jurisdiction where FIR is filed"""

        # Enhance response with relevant past cases
        return enhance_response_with_cases(base_response, message)

    elif any(word in message_lower for word in ['consumer', 'defective', 'product', 'refund', 'warranty', 'online shopping']):
        base_response = """**🤝 Personal Acknowledgment**
I understand your frustration with the defective product purchase. This is indeed a common consumer issue that affects millions of Indians, and you have strong legal rights under consumer protection laws.

**⚖️ Legal Viability Assessment**
YES, legal action CAN definitely be taken in this case. The Consumer Protection Act 2019 provides robust remedies for defective products and deficient services, with consumer-friendly procedures.

**📋 Applicable Legal Framework**
- **Primary Act**: Consumer Protection Act 2019
- **Specific Sections**: Section 2(7) - Definition of consumer, Section 35 - Complaint filing procedure
- **Constitutional Articles**: Article 19(1)(g) - Right to practice profession and carry on business
- **Relevant Case Laws**: Numerous consumer forum decisions favoring consumers in defective product cases

**🏛️ Legal Action Process**
1. **Where to File**: 
   - District Consumer Forum (claims up to ₹1 crore)
   - State Consumer Commission (₹1 crore to ₹10 crore)
   - National Consumer Commission (above ₹10 crore)
2. **Required Documents**: Purchase receipt, warranty card, product photos, correspondence with seller
3. **Filing Procedure**:
   - File complaint in prescribed format
   - Pay nominal filing fee (₹100-200)
   - Attach all supporting documents
   - Forum issues notice to opposite party
   - Attend hearings (usually 3-5 hearings)
4. **Timeline**: Consumer forums must decide within 3-5 months

**⚖️ Punishment/Consequences for Seller**
- **Compensation Orders**: Full refund plus compensation for harassment
- **Replacement/Repair**: Free replacement or repair of defective product
- **Penalty**: Additional compensation for mental agony (typically 10-25% of product value)
- **Other Consequences**: Directions to improve service quality, public apology

**💰 Your Potential Recovery/Relief**
- **Full Refund**: Complete purchase amount with interest
- **Replacement**: Brand new product of same or better specifications
- **Compensation**: Additional amount for harassment, mental agony, and expenses
- **Legal Costs**: Minimal filing fees, no advocate required (can represent yourself)

**📚 Learn More Resources**
- **Related Legal Topics**: E-commerce disputes, Banking complaints, Insurance claims
- **Government Portals**: consumerhelpline.gov.in (National Consumer Helpline), edaakhil.nic.in (online filing)
- **Legal Aid Resources**: National Consumer Helpline: 1915 (toll-free)

**👨‍💼 Recommended Legal Experts**
Based on your consumer case, I recommend consulting:
- **Specialist Required**: Consumer Law Advocate familiar with consumer forums
- **Experience Level**: Lawyer with consumer forum experience (2+ years)
- **Location Preference**: Advocate practicing in your district consumer forum"""

        # Enhance response with relevant past cases
        return enhance_response_with_cases(base_response, message)

    elif any(word in message_lower for word in ['divorce', 'marriage', 'husband', 'wife', 'custody', 'maintenance']):
        base_response = """**🤝 Personal Acknowledgment**
I understand you're going through a difficult time with your marriage. Family disputes are emotionally challenging, and I want to provide you with clear legal guidance to help you make informed decisions about your situation.

**⚖️ Legal Viability Assessment**
YES, legal remedies ARE available for your situation. Indian family laws provide multiple options including divorce, judicial separation, maintenance, and child custody, depending on your specific circumstances and religion.

**📋 Applicable Legal Framework**
- **Primary Acts**: Hindu Marriage Act 1955 (for Hindus/Buddhists/Sikhs/Jains), Muslim Personal Law, Indian Christian Marriage Act 1872, Special Marriage Act 1954
- **Specific Sections**: Section 13 (Grounds for divorce), Section 24 (Interim maintenance), Section 25 (Permanent alimony)
- **Constitutional Articles**: Article 14 (Equality before law), Article 15 (Non-discrimination)
- **Relevant Case Laws**: Vishaka vs. State of Rajasthan (workplace harassment), Shah Bano case (maintenance rights)

**🏛️ Legal Action Process**
1. **Where to File**: Family Court or District Court having jurisdiction where you last resided together
2. **Required Documents**: Marriage certificate, income proof, property documents, evidence of cruelty/desertion
3. **Filing Procedure**:
   - File petition with grounds for divorce
   - Pay court fees (₹500-2000)
   - Court issues summons to spouse
   - Mandatory counseling session
   - Evidence recording and arguments
   - Final decree
4. **Timeline**: Mutual consent divorce: 6-18 months, Contested divorce: 2-5 years

**⚖️ Punishment/Consequences for Spouse**
- **Maintenance Obligation**: Monthly maintenance for wife and children
- **Property Division**: Equal share in matrimonial property
- **Child Custody**: Best interest of child principle applies
- **Other Consequences**: Social and family implications

**💰 Your Potential Recovery/Relief**
- **Maintenance**: Monthly amount based on husband's income (typically 25-30%)
- **Lump Sum Alimony**: One-time settlement amount
- **Property Rights**: Share in matrimonial home and other assets
- **Child Support**: Separate maintenance for children's education and welfare
- **Legal Costs**: Court fees range from ₹500-5000, lawyer fees ₹25,000-2,00,000

**📚 Learn More Resources**
- **Related Legal Topics**: Domestic violence protection, Child custody laws, Property rights
- **Government Portals**: ecourts.gov.in, wcd.nic.in (Women and Child Development)
- **Legal Aid Resources**: Women Helpline: 181, Legal Services Authority for free legal aid

**👨‍💼 Recommended Legal Experts**
Based on your family law matter, I recommend consulting:
- **Specialist Required**: Family Law Specialist with matrimonial dispute experience
- **Experience Level**: Senior advocate with 5+ years family court 
  practice
- **Location Preference**: Lawyer practicing in your local family court"""

        # Enhance response with relevant past cases
        return enhance_response_with_cases(base_response, message)

    elif any(word in message_lower for word in ['fir', 'police', 'complaint', 'crime']):
        base_response = """**🤝 Personal Acknowledgment**
I understand your concern about filing an FIR or dealing with a criminal matter. This is indeed a serious legal situation that requires immediate attention, and I'm here to guide you through the process step by step.

**⚖️ Legal Viability Assessment**
YES, legal action CAN definitely be taken in this case. Filing an FIR is your fundamental right under Indian law, and police are legally bound to register it for cognizable offenses without any delay or excuse.

**📋 Applicable Legal Framework**
- **Primary Act**: Code of Criminal Procedure (CrPC) 1973
- **Specific Sections**: Section 154 (FIR registration), Section 156 (Police investigation powers), Section 173 (Police report)
- **Constitutional Articles**: Article 21 (Right to life and personal liberty)
- **Relevant Case Laws**: Lalita Kumari vs. Govt. of UP (2013) - Mandatory FIR registration for cognizable offenses

**🏛️ Legal Action Process**
1. **Where to File**: Police station having jurisdiction over the place where crime occurred
2. **Required Documents**: Identity proof, any evidence (photos, medical reports, witness details)
3. **Filing Procedure**:
   - Visit police station immediately
   - Give oral or written complaint with complete details
   - Police must register FIR with unique number
   - Demand free copy of FIR (your legal right)
   - Note investigating officer's name and contact
   - Follow up on investigation progress
4. **Timeline**: FIR registration is immediate, investigation typically 60-90 days, chargesheet within 90 days

**⚖️ Punishment/Consequences for Offender**
- **Criminal Punishment**: Varies by offense - imprisonment from 6 months 
  to life, fines as per IPC sections
- **Civil Remedies**: Compensation for damages, medical expenses, loss of income
- **Other Consequences**: Criminal record, bail restrictions, employment difficulties

**💰 Your Potential Recovery/Relief**
- **Victim Compensation**: State compensation scheme (₹1 lakh to ₹10 lakh based on offense severity)
- **Medical Expenses**: Reimbursement for treatment costs
- **Loss of Income**: Compensation for earning loss during recovery
- **Legal Costs**: FIR filing is completely FREE, court proceedings have minimal fees

**📚 Learn More Resources**
- **Related Legal Topics**: Bail procedures, Victim rights, Police complaint procedures
- **Government Portals**: ecourts.gov.in, cctns.gov.in (Crime and Criminal Tracking Network)
- **Legal Aid Resources**: NALSA (nalsa.gov.in), District Legal Services Authority

**👨‍💼 Recommended Legal Experts**
Based on your criminal law case, I recommend consulting:
- **Specialist Required**: Criminal Defense Lawyer with police station experience
- **Experience Level**: Senior advocate with 5+ years criminal law practice
- **Location Preference**: Local court jurisdiction where case will be tried"""

        # Enhance response with relevant past cases
        return enhance_response_with_cases(base_response, message)

    else:
        # General comprehensive legal guidance
        base_response = f"""**🤝 Personal Acknowledgment**
Thank you for reaching out to LegalEase AI. I understand you're seeking legal guidance, and I'm here to provide you with comprehensive information to help address your legal concerns effectively.

**⚖️ Legal Viability Assessment**
Based on your query about "{message}", legal remedies MAY be available depending on the specific facts and circumstances of your situation. Indian law provides various avenues for legal redress across different areas.

**📋 General Legal Framework**
- **Constitutional Foundation**: Constitution of India - Supreme law 
  providing fundamental rights and legal framework
- **Civil Laws**: Contract Act, Property laws, Tort law for civil disputes
- **Criminal Laws**: Indian Penal Code, CrPC for criminal matters
- **Special Laws**: Consumer Protection, Family laws, Labor laws, Tax laws

**🏛️ General Legal Process**
1. **Identify Legal Issue**: Determine which area of law applies to your situation
2. **Gather Evidence**: Collect all relevant documents, correspondence, and proof
3. **Legal Consultation**: Consult appropriate legal expert for specific advice
4. **Choose Remedy**: Select most suitable legal remedy (civil suit, criminal complaint, etc.)
5. **File Case**: Approach appropriate court or authority with proper documentation

**⚖️ Potential Outcomes**
- **Civil Remedies**: Monetary compensation, specific performance, injunctions
- **Criminal Remedies**: Punishment for offender, victim compensation
- **Administrative Remedies**: Regulatory action, license cancellation, penalties

**💰 Legal Costs and Timeline**
- **Court Fees**: Vary by case type and claim value (₹500 to several thousands)
- **Lawyer Fees**: Depend on complexity and lawyer's experience (₹10,000 to several lakhs)
- **Timeline**: Ranges from few months to several years depending on case complexity
- **Legal Aid**: Available for economically weaker sections through Legal Services Authority

**📚 Learn More Resources**
- **Related Legal Topics**: Constitutional rights, Civil procedure, Criminal procedure, Alternative dispute resolution
- **Government Portals**: ecourts.gov.in, lawmin.gov.in, nalsa.gov.in
- **Legal Aid Resources**: National Legal Services Authority: 15100, Tele-Law: 9711078888

**👨‍💼 Professional Consultation Recommended**
For your specific legal matter, I recommend consulting:
- **Legal Expert**: Advocate specializing in relevant area of law
- **Experience Level**: Lawyer with appropriate experience for your case complexity
- **Location**: Local court jurisdiction for convenience and cost-effectiveness

**💡 Next Steps**
Please provide more specific details about your legal issue so I can give 
you more targeted guidance with exact laws, procedures, and remedies 
applicable to your situation."""

        # Enhance response with relevant past cases
        return enhance_response_with_cases(base_response, message)