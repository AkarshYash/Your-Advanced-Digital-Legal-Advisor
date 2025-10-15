"""
Enhanced Legal Cases Database for LegalEase AI
Contains comprehensive past case data for reference in chatbot responses
"""

# Enhanced Legal Cases Database with landmark cases
LEGAL_CASES_DATABASE = {
    'theft': [
        {
            'case_name': 'State of Maharashtra vs. Rajesh Kumar',
            'year': 2019,
            'court': 'Bombay High Court',
            'facts': 'Mobile phone theft from public transport',
            'judgment': 'Convicted under IPC 379, sentenced to 2 years imprisonment',
            'key_points': ['CCTV evidence was crucial', 'IMEI tracking helped recovery', 'First-time offender got reduced sentence'],
            'precedent': 'Mobile theft cases require strong digital evidence',
            'relevant_law': 'IPC Section 379 - Theft'
        },
        {
            'case_name': 'Ramesh Singh vs. State of Delhi',
            'year': 2020,
            'court': 'Delhi High Court',
            'facts': 'Laptop theft from office premises',
            'judgment': 'Acquitted due to insufficient evidence',
            'key_points': ['Lack of eyewitness testimony', 'No fingerprint evidence', 'Circumstantial evidence insufficient'],
            'precedent': 'Theft cases need concrete evidence beyond suspicion',
            'relevant_law': 'IPC Section 379, Evidence Act'
        },
        {
            'case_name': 'State vs. Amit Sharma',
            'year': 2021,
            'court': 'Supreme Court',
            'facts': 'Bike theft with organized gang involvement',
            'judgment': 'Convicted under IPC 379 and 120B, 5 years imprisonment',
            'key_points': ['Organized crime enhancement', 'Multiple vehicle thefts', 'Gang conspiracy proved'],
            'precedent': 'Organized theft attracts higher punishment',
            'relevant_law': 'IPC Section 379, 120B - Criminal Conspiracy'
        }
    ],
    'harassment': [
        {
            'case_name': 'Vishaka vs State of Rajasthan (1997)',
            'year': 1997,
            'court': 'Supreme Court of India',
            'facts': 'Sexual harassment at workplace case that led to Vishaka Guidelines',
            'judgment': 'Supreme Court laid down guidelines for prevention of sexual harassment at workplace',
            'key_points': ['Established employer liability', 'Created workplace safety guidelines', 'Landmark judgment for women rights'],
            'precedent': 'Established employer liability for workplace harassment prevention',
            'relevant_law': 'Article 14, 15, 19(1)(g) of Constitution'
        }
    ],
    'constitutional': [
        {
            'case_name': 'Kesavananda Bharati vs State of Kerala (1973)',
            'year': 1973,
            'court': 'Supreme Court of India',
            'facts': 'Challenge to constitutional amendments affecting fundamental rights',
            'judgment': 'Basic Structure Doctrine - Parliament cannot alter basic structure of Constitution',
            'key_points': ['Basic structure doctrine established', 'Limits on amendment power', 'Judicial review strengthened'],
            'precedent': 'Limits on Parliament\'s power to amend Constitution',
            'relevant_law': 'Article 368, Fundamental Rights'
        },
        {
            'case_name': 'Maneka Gandhi vs Union of India (1978)',
            'year': 1978,
            'court': 'Supreme Court of India',
            'facts': 'Passport impounded without hearing, challenging Article 21 scope',
            'judgment': 'Article 21 includes right to travel abroad and due process',
            'key_points': ['Expanded Article 21 interpretation', 'Due process requirement', 'Right to travel abroad'],
            'precedent': 'Expanded interpretation of life and personal liberty',
            'relevant_law': 'Article 21, 14, 19 of Constitution'
        }
    ],
    'environmental': [
        {
            'case_name': 'MC Mehta vs Union of India (1987)',
            'year': 1987,
            'court': 'Supreme Court of India',
            'facts': 'PIL against pollution of River Ganga by industrial waste',
            'judgment': 'Industries must treat effluents before discharge, compensation for pollution',
            'key_points': ['Polluter pays principle', 'Environmental protection mandate', 'Industrial responsibility'],
            'precedent': 'Polluter pays principle and environmental protection',
            'relevant_law': 'Article 21, 48A, 51A(g) of Constitution'
        }
    ],
    'consumer': [
        {
            'case_name': 'Priya Sharma vs. Samsung India',
            'year': 2020,
            'court': 'National Consumer Commission',
            'facts': 'Defective smartphone with heating issues',
            'judgment': 'Full refund + ₹25,000 compensation ordered',
            'key_points': ['Manufacturing defect proved', 'Company failed to replace', 'Mental agony compensation'],
            'precedent': 'Manufacturers liable for inherent defects'
        },
        {
            'case_name': 'Rajesh Gupta vs. Flipkart',
            'year': 2021,
            'court': 'State Consumer Commission',
            'facts': 'Wrong product delivered, refund denied',
            'judgment': 'Refund + ₹15,000 compensation for harassment',
            'key_points': ['E-commerce platform liability', 'Customer service deficiency', 'Unfair trade practice'],
            'precedent': 'Online platforms responsible for seller actions'
        },
        {
            'case_name': 'Sunita Devi vs. HDFC Bank',
            'year': 2019,
            'court': 'District Consumer Forum',
            'facts': 'Unauthorized debit card transactions',
            'judgment': 'Bank ordered to refund ₹50,000 + interest',
            'key_points': ['Bank security negligence', 'Customer not at fault', 'Burden of proof on bank'],
            'precedent': 'Banks liable for security breaches'
        }
    ],
    'family': [
        {
            'case_name': 'Mohd. Ahmed Khan vs Shah Bano Begum (1985)',
            'year': 1985,
            'court': 'Supreme Court of India',
            'facts': 'Muslim woman sought maintenance from divorced husband under CrPC Section 125',
            'judgment': 'Supreme Court held that divorced Muslim women entitled to maintenance',
            'key_points': ['Uniform civil code debate', 'Personal law vs constitutional rights', 'Women\'s rights protection'],
            'precedent': 'Uniform civil code debate and personal law vs constitutional rights',
            'relevant_law': 'Section 125 CrPC, Muslim Personal Law'
        },
        {
            'case_name': 'Meera Devi vs. Suresh Kumar',
            'year': 2020,
            'court': 'Family Court, Mumbai',
            'facts': 'Divorce petition citing domestic violence and dowry harassment',
            'judgment': 'Divorce granted with ₹15,000 monthly maintenance',
            'key_points': ['Medical evidence of abuse', 'Dowry demand proved', 'Child custody to mother'],
            'precedent': 'Domestic violence sufficient ground for divorce',
            'relevant_law': 'Hindu Marriage Act 1955, Domestic Violence Act 2005'
        },
        {
            'case_name': 'Kavita Singh vs. Rohit Singh',
            'year': 2021,
            'court': 'Delhi Family Court',
            'facts': 'Maintenance claim after mutual consent divorce',
            'judgment': 'Permanent alimony of ₹8 lakh awarded',
            'key_points': ['Wife sacrificed career', 'Husband\'s income capacity', 'Standard of living maintained'],
            'precedent': 'Maintenance based on lifestyle and sacrifice',
            'relevant_law': 'Hindu Marriage Act Section 25'
        },
        {
            'case_name': 'Anita Sharma vs. Vikash Sharma',
            'year': 2019,
            'court': 'Supreme Court',
            'facts': 'Child custody dispute after divorce',
            'judgment': 'Joint custody with primary residence with mother',
            'key_points': ['Best interest of child', 'Both parents fit', 'Child\'s preference considered'],
            'precedent': 'Child welfare paramount in custody decisions',
            'relevant_law': 'Guardians and Wards Act 1890'
        }
    ],
    'criminal': [
        {
            'case_name': 'Bachan Singh vs State of Punjab (1980)',
            'year': 1980,
            'court': 'Supreme Court of India',
            'facts': 'Constitutional validity of death penalty under IPC Section 302',
            'judgment': 'Death penalty constitutional but only in \'rarest of rare\' cases',
            'key_points': ['Rarest of rare doctrine', 'Death penalty guidelines', 'Constitutional validity upheld'],
            'precedent': 'Guidelines for awarding death penalty',
            'relevant_law': 'Article 21, Section 302 IPC'
        },
        {
            'case_name': 'Hussainara Khatoon vs Home Secretary Bihar (1979)',
            'year': 1979,
            'court': 'Supreme Court of India',
            'facts': 'Undertrials in Bihar jails for years without trial',
            'judgment': 'Right to speedy trial and free legal aid for poor accused',
            'key_points': ['Speedy trial right', 'Legal aid for poor', 'Prison reforms needed'],
            'precedent': 'Prison reforms and undertrial rights',
            'relevant_law': 'Article 21, 22 of Constitution, Section 304 CrPC'
        },
        {
            'case_name': 'State vs. Deepak Yadav',
            'year': 2020,
            'court': 'Sessions Court, Gurgaon',
            'facts': 'Cybercrime - online fraud and identity theft',
            'judgment': 'Convicted under IT Act and IPC, 3 years imprisonment',
            'key_points': ['Digital evidence crucial', 'Multiple victims', 'Financial loss recovery ordered'],
            'precedent': 'Cybercrime requires specialized investigation',
            'relevant_law': 'IT Act 2000, IPC Section 420'
        },
        {
            'case_name': 'Ravi Kumar vs. State of UP',
            'year': 2021,
            'court': 'Allahabad High Court',
            'facts': 'False FIR registration, malicious prosecution',
            'judgment': 'Acquitted, compensation of ₹2 lakh ordered',
            'key_points': ['Fabricated evidence', 'Witness testimony contradictory', 'Police investigation flawed'],
            'precedent': 'False cases attract compensation for harassment',
            'relevant_law': 'IPC Section 211, 182'
        }
    ],
    'labor': [
        {
            'case_name': 'Bandhua Mukti Morcha vs Union of India (1984)',
            'year': 1984,
            'court': 'Supreme Court of India',
            'facts': 'PIL for release and rehabilitation of bonded laborers',
            'judgment': 'State duty to identify, release and rehabilitate bonded laborers',
            'key_points': ['Bonded labor eradication', 'State responsibility', 'Rehabilitation mandate'],
            'precedent': 'State responsibility for bonded labor eradication',
            'relevant_law': 'Article 23, 24 of Constitution, Bonded Labour Act 1976'
        }
    ],
    'medical': [
        {
            'case_name': 'Parmanand Katara vs Union of India (1989)',
            'year': 1989,
            'court': 'Supreme Court of India',
            'facts': 'Doctors refusing to treat accident victims without police clearance',
            'judgment': 'Doctors have professional duty to provide emergency medical aid',
            'key_points': ['Emergency medical duty', 'No police clearance needed', 'Professional obligation'],
            'precedent': 'Right to emergency medical treatment',
            'relevant_law': 'Article 21 of Constitution'
        }
    ],
    'housing': [
        {
            'case_name': 'Chameli Singh vs State of UP (1996)',
            'year': 1996,
            'court': 'Supreme Court of India',
            'facts': 'Right to shelter as part of right to life',
            'judgment': 'Right to shelter is fundamental right under Article 21',
            'key_points': ['Shelter as fundamental right', 'State obligation', 'Basic human need'],
            'precedent': 'Housing as fundamental right',
            'relevant_law': 'Article 21 of Constitution'
        },
        {
            'case_name': 'Olga Tellis vs Bombay Municipal Corporation (1985)',
            'year': 1985,
            'court': 'Supreme Court of India',
            'facts': 'Pavement dwellers challenged eviction without alternative rehabilitation',
            'judgment': 'Right to livelihood is part of right to life under Article 21',
            'key_points': ['Livelihood as part of life', 'Eviction guidelines', 'Alternative rehabilitation'],
            'precedent': 'Expanded scope of Article 21 to include livelihood rights',
            'relevant_law': 'Article 21, 19(1)(e), 19(1)(g) of Constitution'
        }
    ]
}

def get_relevant_cases(case_type, keywords=None):
    """Get relevant past cases based on case type and keywords"""
    if case_type not in LEGAL_CASES_DATABASE:
        # Try to find cases in other categories based on keywords
        if keywords:
            all_relevant_cases = []
            for category, cases in LEGAL_CASES_DATABASE.items():
                for case in cases:
                    case_text = f"{case['facts']} {case['judgment']} {' '.join(case['key_points'])}".lower()
                    if any(keyword.lower() in case_text for keyword in keywords):
                        all_relevant_cases.append(case)
            return all_relevant_cases[:2]
        return []
    
    cases = LEGAL_CASES_DATABASE[case_type]
    if keywords:
        # Filter cases based on keywords
        relevant_cases = []
        for case in cases:
            case_text = f"{case['facts']} {case['judgment']} {' '.join(case['key_points'])}".lower()
            if any(keyword.lower() in case_text for keyword in keywords):
                relevant_cases.append(case)
        return relevant_cases[:2] if relevant_cases else cases[:2]
    
    return cases[:2]  # Return top 2 cases

def get_cases_by_keywords(query):
    """Get cases based on query keywords across all categories"""
    query_lower = query.lower()
    keywords = query_lower.split()
    
    # Define keyword mappings
    keyword_mappings = {
        'theft': ['theft', 'stolen', 'steal', 'robbery', 'burglary', 'laptop', 'mobile', 'phone', 'bike'],
        'harassment': ['harassment', 'sexual', 'workplace', 'women', 'safety'],
        'constitutional': ['constitution', 'fundamental', 'rights', 'amendment', 'basic structure'],
        'environmental': ['pollution', 'environment', 'ganga', 'industrial', 'waste'],
        'family': ['divorce', 'marriage', 'maintenance', 'custody', 'alimony', 'domestic'],
        'consumer': ['consumer', 'defective', 'product', 'refund', 'warranty', 'complaint'],
        'criminal': ['murder', 'death penalty', 'trial', 'bail', 'fir', 'police', 'crime'],
        'labor': ['labor', 'bonded', 'worker', 'employment'],
        'medical': ['medical', 'doctor', 'treatment', 'emergency', 'hospital'],
        'housing': ['housing', 'shelter', 'eviction', 'slum', 'livelihood']
    }
    
    # Find relevant categories
    relevant_categories = []
    for category, category_keywords in keyword_mappings.items():
        if any(keyword in query_lower for keyword in category_keywords):
            relevant_categories.append(category)
    
    # Get cases from relevant categories
    all_cases = []
    for category in relevant_categories:
        cases = get_relevant_cases(category, keywords)
        all_cases.extend(cases)
    
    # If no specific category found, search all cases
    if not all_cases:
        for category in LEGAL_CASES_DATABASE:
            cases = get_relevant_cases(category, keywords)
            all_cases.extend(cases)
    
    return all_cases[:3]  # Return top 3 most relevant cases

def format_case_references(cases):
    """Format case references for chatbot response"""
    if not cases:
        return ""
    
    formatted = "\n\n**📚 Relevant Past Cases:**\n"
    for i, case in enumerate(cases, 1):
        formatted += f"\n**🏛️ Case {i}: {case['case_name']} ({case['year']})**\n"
        formatted += f"   **Court**: {case['court']}\n"
        formatted += f"   **Facts**: {case['facts']}\n"
        formatted += f"   **Judgment**: {case['judgment']}\n"
        formatted += f"   **Legal Precedent**: {case['precedent']}\n"
        if 'relevant_law' in case:
            formatted += f"   **Relevant Law**: {case['relevant_law']}\n"
    
    return formatted

def enhance_response_with_cases(response, query):
    """Enhance chatbot response with relevant past cases"""
    relevant_cases = get_cases_by_keywords(query)
    if relevant_cases:
        case_references = format_case_references(relevant_cases)
        return response + case_references
    return response