#!/usr/bin/env python3
"""
Add Sample Data to LegalEase AI Advanced
Adds sample Q&A and advocate profiles
"""

import sqlite3
import json
from datetime import datetime, timedelta
import random

def add_sample_data():
    """Add sample Q&A and advocate data to the database"""
    conn = sqlite3.connect('legalease_advanced.db')
    cursor = conn.cursor()
    
    # Sample Q&A Data
    sample_qna = [
        {
            "question": "What are my rights as a consumer in India?",
            "answer": "**Consumer Rights in India:**\n\n**Under Consumer Protection Act 2019:**\n• Right to Safety - Protection from hazardous goods\n• Right to Information - Complete product details\n• Right to Choose - Access to variety of goods\n• Right to be Heard - Voice complaints\n• Right to Redressal - Compensation for defects\n• Right to Consumer Education\n\n**How to File Complaint:**\n1. District Forum (up to ₹1 Crore)\n2. State Commission (₹1-10 Crore)\n3. National Commission (above ₹10 Crore)\n\n**Helpline:** 1915",
            "category": "consumer",
            "tags": "consumer rights, protection act, complaint"
        },
        {
            "question": "How to file an FIR in India?",
            "answer": "**Filing FIR (First Information Report):**\n\n**Steps to File FIR:**\n1. Visit nearest police station\n2. Provide written complaint or oral statement\n3. Police must register FIR for cognizable offenses\n4. Get FIR copy with number\n5. Keep receipt for future reference\n\n**Important Points:**\n• FIR can be filed 24/7\n• No fee required\n• Can be filed online in many states\n• Police cannot refuse cognizable offense FIR\n\n**Online FIR:** Available in most states through state police websites\n\n**Emergency:** Call 100",
            "category": "criminal",
            "tags": "FIR, police, complaint, criminal"
        },
        {
            "question": "What is Section 420 of IPC?",
            "answer": "**IPC Section 420 - Cheating and Dishonestly Inducing Delivery of Property:**\n\n**Definition:**\nWhoever cheats and thereby dishonestly induces the person deceived to deliver any property or to make, alter or destroy any valuable security shall be punished.\n\n**Punishment:**\n• Imprisonment up to 7 years\n• Fine or both\n\n**Key Elements:**\n1. Cheating (Section 415)\n2. Dishonest inducement\n3. Delivery of property\n4. Deception of victim\n\n**Common Cases:**\n• Online fraud\n• Investment scams\n• Fake documents\n• Identity theft\n\n**Legal Remedy:** File FIR, civil suit for recovery",
            "category": "criminal",
            "tags": "IPC 420, cheating, fraud, criminal law"
        },
        {
            "question": "Property registration process in India",
            "answer": "**Property Registration Process:**\n\n**Required Documents:**\n• Sale deed\n• Title documents\n• NOC from society/builder\n• Property tax receipts\n• Identity & address proof\n• PAN cards of both parties\n\n**Steps:**\n1. Draft sale deed\n2. Pay stamp duty\n3. Visit Sub-Registrar office\n4. Biometric verification\n5. Document registration\n6. Get registered deed\n\n**Fees:**\n• Stamp duty: 3-10% (varies by state)\n• Registration fee: 1-3%\n• Legal fees: 0.5-1%\n\n**Timeline:** 1-7 days\n\n**Online:** Available in most states",
            "category": "property",
            "tags": "property, registration, sale deed, stamp duty"
        },
        {
            "question": "Divorce procedure in India",
            "answer": "**Divorce Procedure in India:**\n\n**Types of Divorce:**\n1. **Mutual Consent** (Section 13B Hindu Marriage Act)\n2. **Contested Divorce** (Section 13)\n\n**Grounds for Divorce:**\n• Cruelty (mental/physical)\n• Adultery\n• Desertion (1+ years)\n• Conversion to another religion\n• Mental disorder\n• Communicable disease\n\n**Process:**\n1. File petition in family court\n2. Serve notice to spouse\n3. Court proceedings\n4. Evidence and arguments\n5. Final decree\n\n**Documents Required:**\n• Marriage certificate\n• Address proof\n• Income proof\n• Evidence of grounds\n\n**Timeline:** 6 months to 2+ years",
            "category": "family",
            "tags": "divorce, marriage, family law, mutual consent"
        },
        {
            "question": "What are fundamental rights under Indian Constitution?",
            "answer": "**Fundamental Rights (Articles 12-35):**\n\n**Six Fundamental Rights:**\n\n**1. Right to Equality (Articles 14-18)**\n• Equality before law\n• No discrimination\n• Equal opportunity in employment\n• Abolition of untouchability\n• Abolition of titles\n\n**2. Right to Freedom (Articles 19-22)**\n• Freedom of speech and expression\n• Freedom of assembly\n• Freedom of movement\n• Freedom of residence\n• Freedom of profession\n• Protection of life and liberty\n\n**3. Right against Exploitation (Articles 23-24)**\n• Prohibition of trafficking\n• Prohibition of child labor\n\n**4. Right to Freedom of Religion (Articles 25-28)**\n• Freedom of conscience\n• Freedom to practice religion\n\n**5. Cultural and Educational Rights (Articles 29-30)**\n• Protection of minorities\n• Right to education\n\n**6. Right to Constitutional Remedies (Article 32)**\n• Right to approach Supreme Court\n• Writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo-warranto",
            "category": "constitutional",
            "tags": "fundamental rights, constitution, articles, equality, freedom"
        },
        {
            "question": "How to start a company in India?",
            "answer": "**Company Registration Process:**\n\n**Types of Companies:**\n• Private Limited Company\n• Public Limited Company\n• One Person Company (OPC)\n• Limited Liability Partnership (LLP)\n\n**Steps for Private Limited:**\n1. **Digital Signature Certificate (DSC)**\n2. **Director Identification Number (DIN)**\n3. **Name Reservation (RUN)**\n4. **Incorporation (SPICe+)**\n5. **PAN & TAN Application**\n6. **Bank Account Opening**\n\n**Required Documents:**\n• Identity & address proof of directors\n• Registered office proof\n• MOA & AOA\n• Form DIR-2 & INC-9\n\n**Fees:**\n• Government fees: ₹4,000-10,000\n• Professional fees: ₹5,000-15,000\n\n**Timeline:** 10-15 days\n\n**Online Portal:** MCA website",
            "category": "corporate",
            "tags": "company registration, incorporation, MCA, business"
        },
        {
            "question": "What is cyber crime and how to report it?",
            "answer": "**Cyber Crime in India:**\n\n**Common Cyber Crimes:**\n• Online fraud & phishing\n• Identity theft\n• Cyberbullying & harassment\n• Data theft\n• Ransomware attacks\n• Social media crimes\n• Online defamation\n\n**Relevant Laws:**\n• **IT Act 2000** - Sections 43, 43A, 66, 66A, 66B, 66C, 66D, 66E, 66F\n• **IPC Sections** - 419, 420, 463, 465, 468, 471, 500, 503, 506\n\n**How to Report:**\n1. **Online:** cybercrime.gov.in\n2. **Helpline:** 1930\n3. **Local Police:** Cyber crime cell\n4. **Email:** complaints@cybercrime.gov.in\n\n**Evidence to Preserve:**\n• Screenshots\n• Transaction details\n• Communication records\n• Device logs\n\n**Quick Action Required:** Report within 24-48 hours",
            "category": "cyber",
            "tags": "cyber crime, IT Act, online fraud, reporting"
        },
        {
            "question": "Employee rights and labor laws in India",
            "answer": "**Employee Rights in India:**\n\n**Key Labor Laws:**\n• **Industrial Relations Code 2020**\n• **Wage Code 2019**\n• **Social Security Code 2020**\n• **Occupational Safety Code 2020**\n\n**Basic Rights:**\n• Minimum wages\n• 8-hour working day\n• Weekly rest day\n• Annual leave\n• Maternity/paternity leave\n• Provident Fund (PF)\n• Employee State Insurance (ESI)\n• Gratuity (after 5 years)\n\n**Termination Rights:**\n• 30 days notice or pay in lieu\n• Retrenchment compensation\n• No termination during illness/injury\n\n**Complaint Mechanisms:**\n• Labor Commissioner\n• Industrial Tribunal\n• Labor Court\n• Grievance Committee\n\n**Helplines:**\n• Labor Helpline: 1800-11-1000\n• Women Helpline: 1091",
            "category": "labor",
            "tags": "employee rights, labor laws, wages, termination"
        },
        {
            "question": "How to get legal aid in India?",
            "answer": "**Legal Aid in India:**\n\n**National Legal Services Authority (NALSA):**\n• Free legal services to eligible persons\n• Legal advice and representation\n• Lok Adalats for dispute resolution\n\n**Eligibility for Free Legal Aid:**\n• Annual income below ₹9,000 (rural) / ₹12,000 (urban)\n• SC/ST members\n• Women and children\n• Persons with disabilities\n• Industrial workers\n• Victims of trafficking\n• Prisoners\n\n**Services Provided:**\n• Legal advice\n• Court representation\n• Document drafting\n• Lok Adalat services\n\n**How to Apply:**\n1. Visit District Legal Services Authority\n2. Submit application with income certificate\n3. Get legal aid card\n4. Avail services\n\n**Contact:**\n• Website: nalsa.gov.in\n• Helpline: 15100\n• Toll-free: 1800-110-001",
            "category": "legal_aid",
            "tags": "legal aid, NALSA, free legal services, eligibility"
        },
        {
            "question": "What is bail and how to get it?",
            "answer": "**Bail in Indian Criminal Law:**\n\n**Types of Bail:**\n1. **Regular Bail** - Applied in Magistrate/Sessions Court\n2. **Interim Bail** - Temporary bail\n3. **Anticipatory Bail** - Before arrest (Section 438 CrPC)\n4. **Default Bail** - Automatic after 60/90 days\n\n**Bail Conditions:**\n• Personal bond with/without surety\n• Surrender passport\n• Regular reporting to police\n• No tampering with evidence\n• No contact with witnesses\n\n**Non-Bailable Offenses:**\n• Murder, rape, terrorism\n• Dowry death, kidnapping\n• POCSO Act offenses\n• Narcotic drugs cases\n\n**Bail Application Process:**\n1. File bail application\n2. Attach supporting documents\n3. Court hearing\n4. Furnish bail bond\n5. Release from custody\n\n**Documents Required:**\n• Bail application\n• Case details\n• Surety documents\n• Character certificate\n\n**Legal Maxim:** 'Bail is rule, jail is exception'",
            "category": "criminal",
            "tags": "bail, criminal law, CrPC, anticipatory bail"
        },
        {
            "question": "Domestic violence laws in India",
            "answer": "**Protection of Women from Domestic Violence Act 2005:**\n\n**What Constitutes Domestic Violence:**\n• Physical abuse\n• Sexual abuse\n• Verbal and emotional abuse\n• Economic abuse\n\n**Who Can File Complaint:**\n• Wife or female live-in partner\n• Sister, mother, daughter\n• Any woman in domestic relationship\n\n**Legal Remedies:**\n1. **Protection Order** - Stop violence\n2. **Residence Order** - Right to stay\n3. **Monetary Relief** - Maintenance, compensation\n4. **Custody Order** - Child custody\n5. **Compensation Order** - For injuries/damages\n\n**How to File Complaint:**\n1. Approach Protection Officer\n2. File complaint with Magistrate\n3. Submit medical reports, evidence\n4. Court proceedings\n5. Get protection order\n\n**Support Services:**\n• Women Helpline: 1091\n• Domestic Violence Helpline: 181\n• Service Providers for counseling\n• Shelter homes\n\n**Emergency:** Call 100 or 1091",
            "category": "family",
            "tags": "domestic violence, women protection, DV Act, legal remedies"
        },
        {
            "question": "How to file RTI application?",
            "answer": "**Right to Information (RTI) Act 2005:**\n\n**Who Can File RTI:**\n• Any Indian citizen\n• No need to give reason\n• Can seek any information from public authorities\n\n**How to File RTI:**\n1. **Offline:** Submit application to PIO (Public Information Officer)\n2. **Online:** Through RTI portal (rtionline.gov.in)\n3. **By Post:** Send to concerned department\n\n**Application Format:**\n• Address to PIO\n• Information sought (specific)\n• Contact details\n• Application fee (₹10)\n• Preferred language\n\n**Timeline:**\n• Normal cases: 30 days\n• Life and liberty cases: 48 hours\n• Third party involvement: 40 days\n\n**Appeal Process:**\n• First Appeal: To Appellate Authority (30 days)\n• Second Appeal: To Information Commission (90 days)\n\n**Exempted Information:**\n• National security matters\n• Personal information\n• Cabinet papers\n• Investigation records\n\n**Penalty:** ₹250 per day for delay (max ₹25,000)",
            "category": "constitutional",
            "tags": "RTI, right to information, transparency, public information"
        },
        {
            "question": "What are the rights of arrested person?",
            "answer": "**Rights of Arrested Person (Article 22 & CrPC):**\n\n**Constitutional Rights:**\n1. **Right to be informed** of grounds of arrest\n2. **Right to legal representation**\n3. **Right against self-incrimination**\n4. **Right to be produced before magistrate within 24 hours**\n\n**Rights under CrPC:**\n• Right to know arrest grounds (Section 50)\n• Right to inform family/friends (Section 50A)\n• Right to medical examination (Section 54)\n• Right to legal aid if indigent (Section 304)\n• Right to bail (bailable offenses)\n• Right against torture/custodial violence\n\n**Police Duties:**\n• Inform arrest grounds\n• Allow one phone call\n• Provide medical aid if needed\n• Prepare arrest memo\n• Inform family within 8-12 hours\n\n**Prohibited Actions:**\n• Torture or third-degree methods\n• Detention beyond 24 hours without magistrate order\n• Arrest without warrant (except specific cases)\n• Handcuffing (except in exceptional cases)\n\n**Legal Remedies:**\n• Habeas Corpus petition\n• Complaint to Human Rights Commission\n• Departmental complaint against police\n\n**Emergency Contacts:**\n• Police: 100\n• Legal Aid: 15100",
            "category": "criminal",
            "tags": "arrest rights, police custody, legal aid, habeas corpus"
        },
        {
            "question": "Property inheritance laws in India",
            "answer": "**Property Inheritance Laws:**\n\n**Hindu Succession Act 2005:**\n\n**Class I Heirs (Equal Share):**\n• Son, daughter, widow\n• Mother, son/daughter of predeceased son\n• Son/daughter of predeceased daughter\n• Widow of predeceased son\n\n**Women's Rights:**\n• Equal inheritance rights (2005 Amendment)\n• Coparcenary rights in ancestral property\n• Right in father's self-acquired property\n\n**Muslim Personal Law:**\n• Governed by Shariat Act 1937\n• Fixed shares for heirs\n• Male heirs get double of female heirs\n• No concept of joint family property\n\n**Christian/Parsi Laws:**\n• Indian Succession Act 1925\n• Equal rights to all children\n• Widow gets 1/3rd share\n\n**Will/Testament:**\n• Can override succession laws\n• Must be properly executed\n• Requires witnesses\n• Can be registered\n\n**Legal Process:**\n1. Obtain death certificate\n2. Apply for succession certificate\n3. Mutation of property records\n4. Transfer of assets\n\n**Documents Required:**\n• Death certificate\n• Property documents\n• Family tree/relationship proof\n• Identity proofs of heirs",
            "category": "property",
            "tags": "inheritance, succession, property rights, will, Hindu law"
        },
        {
            "question": "How to register a trademark in India?",
            "answer": "**Trademark Registration in India:**\n\n**What Can Be Trademarked:**\n• Words, logos, symbols\n• Sounds, colors, shapes\n• Combination marks\n• Service marks\n\n**Benefits of Registration:**\n• Exclusive rights for 10 years (renewable)\n• Legal protection against infringement\n• Right to use ® symbol\n• Asset value creation\n\n**Registration Process:**\n1. **Trademark Search** - Check availability\n2. **Application Filing** - Form TM-A\n3. **Examination** - By Trademark Office\n4. **Publication** - In Trademark Journal\n5. **Opposition Period** - 4 months\n6. **Registration** - Certificate issued\n\n**Required Documents:**\n• Trademark application (TM-A)\n• Logo/wordmark representation\n• Power of attorney (if through agent)\n• Priority document (if claiming priority)\n• User affidavit (if using mark)\n\n**Fees:**\n• Individual/Startup: ₹4,500 per class\n• Small Entity: ₹9,000 per class\n• Others: ₹18,000 per class\n\n**Timeline:** 18-24 months\n\n**Classes:** 45 classes (34 goods + 11 services)\n\n**Online Portal:** ipindia.gov.in",
            "category": "intellectual_property",
            "tags": "trademark, registration, IP rights, brand protection"
        },
        {
            "question": "What is GST and how does it work?",
            "answer": "**Goods and Services Tax (GST):**\n\n**GST Structure:**\n• **CGST** - Central GST\n• **SGST** - State GST\n• **IGST** - Integrated GST (inter-state)\n• **UTGST** - Union Territory GST\n\n**GST Rates:**\n• **0%** - Essential items (rice, wheat, milk)\n• **5%** - Daily necessities (sugar, tea, medicines)\n• **12%** - Standard items (computers, processed food)\n• **18%** - Most goods and services\n• **28%** - Luxury items (cars, tobacco, aerated drinks)\n\n**GST Registration:**\n• **Mandatory:** Turnover > ₹40 lakhs (₹20 lakhs for NE states)\n• **Voluntary:** Below threshold\n• **Composition Scheme:** Turnover < ₹1.5 crore\n\n**GST Returns:**\n• **GSTR-1** - Outward supplies (monthly/quarterly)\n• **GSTR-3B** - Summary return (monthly)\n• **GSTR-9** - Annual return\n\n**Input Tax Credit (ITC):**\n• Credit for tax paid on inputs\n• Can be used to pay output tax\n• Conditions: Valid invoice, goods/services received\n\n**Penalties:**\n• Late filing: ₹50 per day per return\n• Non-registration: 100% of tax amount\n• Wrong ITC claim: 100% of credit + interest\n\n**GST Portal:** gst.gov.in\n**Helpline:** 1800-103-4786",
            "category": "tax",
            "tags": "GST, tax, registration, returns, input credit"
        },
        {
            "question": "How to file income tax return in India?",
            "answer": "**Income Tax Return (ITR) Filing:**\n\n**ITR Forms:**\n• **ITR-1 (Sahaj)** - Salary, pension, one house property\n• **ITR-2** - No business income, multiple sources\n• **ITR-3** - Business/professional income\n• **ITR-4 (Sugam)** - Presumptive business income\n• **ITR-5** - Partnership firms, LLP\n• **ITR-6** - Companies\n• **ITR-7** - Trusts, political parties\n\n**Due Dates:**\n• **Individual/HUF:** July 31\n• **Companies:** October 31\n• **Audit cases:** October 31\n• **Belated return:** December 31 (with penalty)\n\n**Documents Required:**\n• Form 16 (salary)\n• Bank statements\n• Investment proofs\n• Property documents\n• Business books (if applicable)\n• Previous year ITR\n\n**Filing Process:**\n1. **Register** on incometax.gov.in\n2. **Download** pre-filled ITR\n3. **Fill details** and verify\n4. **Upload** supporting documents\n5. **Submit** and e-verify\n\n**E-Verification Methods:**\n• Aadhaar OTP\n• Net banking\n• Bank account number\n• Demat account\n• EVC through bank ATM\n\n**Penalties:**\n• Late filing: ₹5,000 (₹1,000 if income < ₹5 lakhs)\n• Non-filing: ₹10,000\n\n**Refund:** Processed within 45 days",
            "category": "tax",
            "tags": "income tax, ITR filing, tax return, refund"
        },
        {
            "question": "What are the laws related to online privacy in India?",
            "answer": "**Online Privacy Laws in India:**\n\n**Information Technology Act 2000:**\n• **Section 43A** - Data protection and compensation\n• **Section 72** - Breach of confidentiality and privacy\n• **Section 72A** - Disclosure of information in breach of lawful contract\n\n**IT Rules 2011 (Privacy Rules):**\n• Consent for data collection\n• Purpose limitation\n• Data retention policies\n• Security safeguards\n• Grievance redressal\n\n**Personal Data Protection Bill 2019 (Proposed):**\n• Comprehensive data protection framework\n• Data localization requirements\n• Rights of data principals\n• Penalties for violations\n\n**Digital Personal Data Protection Act 2023:**\n• **Consent-based processing**\n• **Right to erasure**\n• **Data portability**\n• **Breach notification**\n• **Penalties up to ₹500 crore**\n\n**Key Rights:**\n• Right to information about data processing\n• Right to correction and erasure\n• Right to data portability\n• Right to grievance redressal\n\n**Violations & Penalties:**\n• Unauthorized data processing\n• Data breach without notification\n• Non-compliance with data subject rights\n• Transfer of data outside India without permission\n\n**Complaint Mechanism:**\n• Data Protection Board\n• Cyber crime cells\n• Consumer forums\n\n**Best Practices:**\n• Read privacy policies\n• Use strong passwords\n• Enable two-factor authentication\n• Regular privacy settings review",
            "category": "cyber",
            "tags": "data protection, privacy, IT Act, DPDP Act, cyber security"
        },
        {
            "question": "How to start an NGO in India?",
            "answer": "**Starting an NGO in India:**\n\n**Types of NGO Registration:**\n1. **Society** - Societies Registration Act 1860\n2. **Trust** - Indian Trusts Act 1882\n3. **Section 8 Company** - Companies Act 2013\n\n**Society Registration:**\n• Minimum 7 members\n• Memorandum of Association\n• Rules and Regulations\n• State Registrar of Societies\n\n**Trust Registration:**\n• Minimum 2 trustees\n• Trust Deed\n• Registration with Sub-Registrar\n• Stamp duty payment\n\n**Section 8 Company:**\n• Minimum 2 directors\n• MOA & AOA\n• License from Central Government\n• ROC registration\n\n**Required Documents:**\n• Identity & address proof of members\n• Registered office proof\n• Affidavit of members\n• NOC from landlord\n• Bank account details\n\n**Post-Registration Compliances:**\n• **12A Registration** - Income tax exemption\n• **80G Registration** - Donation tax benefit\n• **FCRA Registration** - Foreign funding\n• **CSR Registration** - Corporate funding\n\n**Annual Compliances:**\n• Annual returns filing\n• Income tax returns\n• Audit (if income > ₹1 crore)\n• FCRA returns (if applicable)\n\n**Funding Sources:**\n• Individual donations\n• Corporate CSR funds\n• Government grants\n• Foreign contributions (with FCRA)\n• Crowdfunding platforms\n\n**Timeline:** 15-30 days\n**Cost:** ₹5,000-25,000",
            "category": "corporate",
            "tags": "NGO, society, trust, registration, 12A, 80G, FCRA"
        }
    ]
    
    # Insert sample Q&A
    for qna in sample_qna:
        cursor.execute('''
            INSERT OR IGNORE INTO legal_resources (
                title, description, content, category, resource_type, 
                is_featured, is_active, view_count, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            qna['question'], 
            qna['question'][:200] + '...' if len(qna['question']) > 200 else qna['question'],
            qna['answer'], 
            qna['category'], 
            'qna',
            1 if random.choice([True, False]) else 0,
            1,
            random.randint(50, 500),
            datetime.now().isoformat()
        ))
    
    # Sample Advocate Data
    sample_advocates = [
        {
            "full_name": "Adv. Rajesh Kumar Sharma",
            "email": "rajesh.sharma@legalease.com",
            "phone": "+91 9876543210",
            "address": "Chamber No. 45, District Court Complex, Delhi",
            "specializations": "Criminal Law, Consumer Protection, Cyber Crime",
            "court_locations": "Delhi High Court, Tis Hazari Court, Rohini Court",
            "years_experience": 15,
            "consultation_fee": 2000,
            "rating": 4.8,
            "total_cases": 450,
            "bio": "Experienced criminal lawyer with expertise in cyber crimes and consumer protection cases. Successfully handled 450+ cases with 95% success rate."
        },
        {
            "full_name": "Adv. Priya Mehta",
            "email": "priya.mehta@legalease.com",
            "phone": "+91 9876543211",
            "address": "Law Chamber, High Court Complex, Mumbai",
            "specializations": "Family Law, Divorce, Child Custody, Domestic Violence",
            "court_locations": "Bombay High Court, Family Court Mumbai, Magistrate Court",
            "years_experience": 12,
            "consultation_fee": 1800,
            "rating": 4.9,
            "total_cases": 380,
            "bio": "Specialized family law advocate with focus on women's rights and child welfare. Known for compassionate approach and successful mediation."
        },
        {
            "full_name": "Adv. Suresh Patel",
            "email": "suresh.patel@legalease.com",
            "phone": "+91 9876543212",
            "address": "Legal Associates, Commercial Complex, Ahmedabad",
            "specializations": "Corporate Law, Company Registration, GST, Taxation",
            "court_locations": "Gujarat High Court, Commercial Court, Tribunal",
            "years_experience": 18,
            "consultation_fee": 2500,
            "rating": 4.7,
            "total_cases": 520,
            "bio": "Corporate law expert with extensive experience in company formations, mergers, and tax matters. Advisor to 100+ companies."
        },
        {
            "full_name": "Adv. Kavitha Reddy",
            "email": "kavitha.reddy@legalease.com",
            "phone": "+91 9876543213",
            "address": "Advocate Chamber, High Court, Hyderabad",
            "specializations": "Property Law, Real Estate, Land Disputes, Registration",
            "court_locations": "Telangana High Court, Civil Court, Revenue Court",
            "years_experience": 14,
            "consultation_fee": 1500,
            "rating": 4.6,
            "total_cases": 320,
            "bio": "Property law specialist with deep knowledge of land laws and real estate regulations. Expert in property disputes and documentation."
        },
        {
            "full_name": "Adv. Amit Singh",
            "email": "amit.singh@legalease.com",
            "phone": "+91 9876543214",
            "address": "Legal Clinic, Civil Lines, Lucknow",
            "specializations": "Labor Law, Employment Disputes, Industrial Relations",
            "court_locations": "Allahabad High Court, Labor Court, Industrial Tribunal",
            "years_experience": 16,
            "consultation_fee": 1200,
            "rating": 4.5,
            "total_cases": 410,
            "bio": "Labor law expert representing both employees and employers. Specialized in industrial disputes and employment contract matters."
        },
        {
            "full_name": "Adv. Meera Joshi",
            "email": "meera.joshi@legalease.com",
            "phone": "+91 9876543215",
            "address": "Supreme Court Bar Association, New Delhi",
            "specializations": "Constitutional Law, Public Interest Litigation, Human Rights",
            "court_locations": "Supreme Court of India, Delhi High Court",
            "years_experience": 22,
            "consultation_fee": 5000,
            "rating": 4.9,
            "total_cases": 180,
            "bio": "Senior advocate practicing in Supreme Court with expertise in constitutional matters and human rights cases. Argued landmark cases."
        },
        {
            "full_name": "Adv. Ravi Krishnan",
            "email": "ravi.krishnan@legalease.com",
            "phone": "+91 9876543216",
            "address": "Advocate Office, High Court Complex, Chennai",
            "specializations": "Intellectual Property, Patent, Trademark, Copyright",
            "court_locations": "Madras High Court, IP Appellate Board, Commercial Court",
            "years_experience": 13,
            "consultation_fee": 3000,
            "rating": 4.8,
            "total_cases": 290,
            "bio": "IP law specialist with expertise in patent prosecution and trademark registration. Handles complex IP litigation and licensing."
        },
        {
            "full_name": "Adv. Sunita Agarwal",
            "email": "sunita.agarwal@legalease.com",
            "phone": "+91 9876543217",
            "address": "Legal Chamber, District Court, Jaipur",
            "specializations": "Consumer Law, Banking Law, Recovery, Cheque Bounce",
            "court_locations": "Rajasthan High Court, Consumer Forum, Banking Tribunal",
            "years_experience": 11,
            "consultation_fee": 1000,
            "rating": 4.4,
            "total_cases": 350,
            "bio": "Consumer protection advocate with focus on banking disputes and recovery matters. Known for quick resolution of cases."
        },
        {
            "full_name": "Adv. Deepak Gupta",
            "email": "deepak.gupta@legalease.com",
            "phone": "+91 9876543218",
            "address": "Law Office, High Court, Chandigarh",
            "specializations": "Service Law, Government Employment, Pension Disputes",
            "court_locations": "Punjab & Haryana High Court, Central Administrative Tribunal",
            "years_experience": 19,
            "consultation_fee": 1800,
            "rating": 4.6,
            "total_cases": 480,
            "bio": "Service law expert representing government employees in service matters, promotions, and pension disputes."
        },
        {
            "full_name": "Adv. Anita Sharma",
            "email": "anita.sharma@legalease.com",
            "phone": "+91 9876543219",
            "address": "Advocate Chamber, District Court, Pune",
            "specializations": "Immigration Law, Visa Issues, Citizenship, NRI Matters",
            "court_locations": "Bombay High Court, Foreigners Tribunal, Immigration Court",
            "years_experience": 10,
            "consultation_fee": 2200,
            "rating": 4.7,
            "total_cases": 220,
            "bio": "Immigration law specialist helping clients with visa applications, citizenship matters, and NRI legal issues."
        },
        {
            "full_name": "Adv. Vikram Malhotra",
            "email": "vikram.malhotra@legalease.com",
            "phone": "+91 9876543220",
            "address": "Senior Advocate Chamber, High Court, Kolkata",
            "specializations": "Commercial Law, Contract Disputes, Arbitration, Mediation",
            "court_locations": "Calcutta High Court, Commercial Court, Arbitration Tribunal",
            "years_experience": 20,
            "consultation_fee": 3500,
            "rating": 4.8,
            "total_cases": 390,
            "bio": "Commercial law expert with extensive experience in contract disputes and alternative dispute resolution mechanisms."
        },
        {
            "full_name": "Adv. Pooja Nair",
            "email": "pooja.nair@legalease.com",
            "phone": "+91 9876543221",
            "address": "Law Associates, High Court, Kochi",
            "specializations": "Maritime Law, Shipping, Admiralty, International Trade",
            "court_locations": "Kerala High Court, Admiralty Court, Commercial Court",
            "years_experience": 8,
            "consultation_fee": 2800,
            "rating": 4.5,
            "total_cases": 150,
            "bio": "Maritime law specialist with expertise in shipping disputes, admiralty matters, and international trade law."
        },
        {
            "full_name": "Adv. Harish Chandra",
            "email": "harish.chandra@legalease.com",
            "phone": "+91 9876543222",
            "address": "Legal Consultant, High Court, Patna",
            "specializations": "Land Revenue, Agricultural Law, Cooperative Law",
            "court_locations": "Patna High Court, Revenue Court, Cooperative Tribunal",
            "years_experience": 17,
            "consultation_fee": 800,
            "rating": 4.3,
            "total_cases": 420,
            "bio": "Agricultural and revenue law expert with deep understanding of land records and cooperative society matters."
        },
        {
            "full_name": "Adv. Neha Kapoor",
            "email": "neha.kapoor@legalease.com",
            "phone": "+91 9876543223",
            "address": "Women Legal Aid Center, District Court, Gurgaon",
            "specializations": "Women Rights, Sexual Harassment, POCSO, Dowry Cases",
            "court_locations": "Punjab & Haryana High Court, Fast Track Court, Women Court",
            "years_experience": 9,
            "consultation_fee": 1500,
            "rating": 4.9,
            "total_cases": 280,
            "bio": "Women rights advocate specializing in cases of harassment, domestic violence, and crimes against women."
        },
        {
            "full_name": "Adv. Sanjay Verma",
            "email": "sanjay.verma@legalease.com",
            "phone": "+91 9876543224",
            "address": "Tax Consultant Chamber, High Court, Indore",
            "specializations": "Tax Law, GST, Income Tax, Customs, Excise",
            "court_locations": "Madhya Pradesh High Court, Tax Tribunal, Customs Court",
            "years_experience": 21,
            "consultation_fee": 2000,
            "rating": 4.7,
            "total_cases": 510,
            "bio": "Tax law expert with comprehensive knowledge of direct and indirect taxes. Regular speaker at tax seminars."
        },
        {
            "full_name": "Adv. Rashmi Pandey",
            "email": "rashmi.pandey@legalease.com",
            "phone": "+91 9876543225",
            "address": "Legal Aid Society, District Court, Varanasi",
            "specializations": "Environmental Law, Pollution Control, Green Tribunal",
            "court_locations": "Allahabad High Court, National Green Tribunal, Environmental Court",
            "years_experience": 7,
            "consultation_fee": 1200,
            "rating": 4.4,
            "total_cases": 130,
            "bio": "Environmental law advocate working on pollution control and green initiatives. Active in public interest litigation."
        },
        {
            "full_name": "Adv. Manoj Kumar",
            "email": "manoj.kumar@legalease.com",
            "phone": "+91 9876543226",
            "address": "Criminal Law Chamber, Sessions Court, Kanpur",
            "specializations": "Criminal Defense, White Collar Crime, Economic Offenses",
            "court_locations": "Allahabad High Court, Sessions Court, Economic Offenses Court",
            "years_experience": 14,
            "consultation_fee": 1800,
            "rating": 4.6,
            "total_cases": 380,
            "bio": "Criminal defense lawyer with expertise in white-collar crimes and economic offenses. Known for thorough case preparation."
        },
        {
            "full_name": "Adv. Shweta Jain",
            "email": "shweta.jain@legalease.com",
            "phone": "+91 9876543227",
            "address": "Corporate Law Firm, Business District, Bangalore",
            "specializations": "Startup Law, Venture Capital, SEBI Compliance, IPO",
            "court_locations": "Karnataka High Court, SEBI, Company Law Tribunal",
            "years_experience": 6,
            "consultation_fee": 4000,
            "rating": 4.8,
            "total_cases": 95,
            "bio": "Startup and securities law expert helping companies with funding, compliance, and public offerings."
        },
        {
            "full_name": "Adv. Ramesh Babu",
            "email": "ramesh.babu@legalease.com",
            "phone": "+91 9876543228",
            "address": "Advocate Office, High Court, Visakhapatnam",
            "specializations": "Insurance Law, Motor Accident Claims, Compensation",
            "court_locations": "Andhra Pradesh High Court, Motor Accident Tribunal, Insurance Court",
            "years_experience": 12,
            "consultation_fee": 1000,
            "rating": 4.5,
            "total_cases": 340,
            "bio": "Insurance and motor accident claims specialist with excellent track record in securing maximum compensation for clients."
        },
        {
            "full_name": "Adv. Geeta Rani",
            "email": "geeta.rani@legalease.com",
            "phone": "+91 9876543229",
            "address": "Legal Clinic, Civil Court, Bhopal",
            "specializations": "Medical Negligence, Consumer Protection, Health Law",
            "court_locations": "Madhya Pradesh High Court, Consumer Forum, Medical Tribunal",
            "years_experience": 11,
            "consultation_fee": 1500,
            "rating": 4.7,
            "total_cases": 250,
            "bio": "Medical negligence and health law expert with medical background. Specializes in complex medical malpractice cases."
        }
    ]
    
    # Insert sample advocates
    for i, advocate in enumerate(sample_advocates, 1):
        # Create user account
        cursor.execute('''
            INSERT OR IGNORE INTO users (
                username, email, full_name, phone, address, user_type, 
                password_hash, is_active, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            f"advocate{i:02d}",
            advocate['email'],
            advocate['full_name'],
            advocate['phone'],
            advocate['address'],
            'advocate',
            'hashed_password_placeholder',  # In real app, this would be properly hashed
            1,
            datetime.now().isoformat()
        ))
        
        user_id = cursor.lastrowid
        
        # Create advocate profile
        cursor.execute('''
            INSERT OR IGNORE INTO advocate_profiles (
                user_id, bar_council_id, specializations, court_locations,
                years_experience, consultation_fee, office_timing, bio,
                rating, total_cases, verification_status, is_available
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id,
            f"BAR/{random.randint(1000, 9999)}/{random.randint(2010, 2020)}",
            advocate['specializations'],
            advocate['court_locations'],
            advocate['years_experience'],
            advocate['consultation_fee'],
            "9:00 AM - 6:00 PM",
            advocate['bio'],
            advocate['rating'],
            advocate['total_cases'],
            'verified',
            1
        ))
    
    conn.commit()
    conn.close()
    print("✅ Sample Q&A and advocate data added successfully!")

if __name__ == '__main__':
    add_sample_data()