from flask import render_template, request, jsonify, session, redirect, url_for
from app.student import bp
from app.models import db
import json
import time
from config import Config

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    genai = None

# Configure Gemini AI for student features
if GENAI_AVAILABLE:
    try:
        genai.configure(api_key=Config.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Gemini AI initialized for student features")
    except Exception as e:
        print(f"❌ Gemini AI initialization failed: {e}")
        model = None
else:
    model = None
    print("❌ Gemini AI not available for student features")

@bp.route('/dashboard')
def student_dashboard():
    """Student-specific dashboard with academic tools"""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    conn = db.get_connection()
    cursor = conn.cursor()
    
    # Get student statistics
    user_id = session['user_id']
    stats = {}
    
    # Case studies analyzed
    cursor.execute('SELECT COUNT(*) as count FROM case_study_analysis WHERE user_id = ?', (user_id,))
    stats['case_studies_analyzed'] = cursor.fetchone()['count']
    
    # Subjects studied
    cursor.execute('SELECT COUNT(DISTINCT subject) as count FROM study_sessions WHERE user_id = ?', (user_id,))
    stats['subjects_studied'] = cursor.fetchone()['count']
    
    # Study hours
    cursor.execute('SELECT SUM(duration_minutes) as total FROM study_sessions WHERE user_id = ?', (user_id,))
    total_minutes = cursor.fetchone()['total'] or 0
    stats['study_hours'] = round(total_minutes / 60, 1)
    
    # Recent activities
    cursor.execute('''
        SELECT activity_type, activity_description, created_at 
        FROM user_activity 
        WHERE user_id = ? AND activity_type IN ('case_study', 'subject_study', 'quiz_attempt')
        ORDER BY created_at DESC 
        LIMIT 5
    ''', (user_id,))
    recent_activities = cursor.fetchall()
    
    conn.close()
    
    return render_template('student/dashboard.html', stats=stats, recent_activities=recent_activities)

@bp.route('/case-study-analyzer')
def case_study_analyzer():
    """Case study analysis tool for students"""
    return render_template('student/case_study_analyzer.html')

@bp.route('/api/analyze-case-study', methods=['POST'])
def analyze_case_study():
    """AI-powered case study analysis"""
    try:
        data = request.get_json()
        case_text = data.get('case_text', '').strip()
        analysis_type = data.get('analysis_type', 'comprehensive')
        
        if not case_text:
            return jsonify({'error': 'Case study text is required'}), 400
        
        if len(case_text) < 100:
            return jsonify({'error': 'Case study text is too short. Please provide more details.'}), 400
        
        start_time = time.time()
        
        # Generate AI analysis
        if model:
            try:
                prompt = generate_case_study_prompt(case_text, analysis_type)
                response = model.generate_content(prompt)
                analysis_result = parse_case_study_response(response.text)
            except Exception as e:
                print(f"AI Error: {e}")
                analysis_result = generate_fallback_case_analysis(case_text)
        else:
            analysis_result = generate_fallback_case_analysis(case_text)
        
        processing_time = time.time() - start_time
        
        # Save analysis if user is logged in
        if session.get('user_id'):
            conn = db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO case_study_analysis (
                    user_id, case_text, analysis_result, analysis_type, processing_time
                ) VALUES (?, ?, ?, ?, ?)
            ''', (session['user_id'], case_text[:1000], json.dumps(analysis_result), 
                  analysis_type, processing_time))
            
            # Log activity
            cursor.execute('''
                INSERT INTO user_activity (user_id, activity_type, activity_description)
                VALUES (?, ?, ?)
            ''', (session['user_id'], 'case_study', f'Analyzed case study: {analysis_type} analysis'))
            
            conn.commit()
            conn.close()
        
        return jsonify({
            'success': True,
            'analysis': analysis_result,
            'processing_time': round(processing_time, 2)
        })
        
    except Exception as e:
        return jsonify({'error': f'Error analyzing case study: {str(e)}'}), 500

@bp.route('/subject-tutor')
def subject_tutor():
    """Interactive law subject tutor"""
    return render_template('student/subject_tutor.html')

@bp.route('/api/subject-tutor', methods=['POST'])
def subject_tutor_api():
    """AI-powered subject tutoring"""
    try:
        data = request.get_json()
        subject = data.get('subject', '')
        topic = data.get('topic', '')
        question = data.get('question', '')
        difficulty_level = data.get('difficulty_level', 'intermediate')
        
        if not subject or not topic:
            return jsonify({'error': 'Subject and topic are required'}), 400
        
        start_time = time.time()
        
        # Generate tutoring response
        if model:
            try:
                prompt = generate_tutor_prompt(subject, topic, question, difficulty_level)
                response = model.generate_content(prompt)
                tutor_response = parse_tutor_response(response.text)
            except Exception as e:
                print(f"AI Error: {e}")
                tutor_response = generate_fallback_tutor_response(subject, topic, question)
        else:
            tutor_response = generate_fallback_tutor_response(subject, topic, question)
        
        processing_time = time.time() - start_time
        
        # Save study session if user is logged in
        if session.get('user_id'):
            conn = db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO study_sessions (
                    user_id, subject, topic, question, response, difficulty_level, duration_minutes
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (session['user_id'], subject, topic, question, 
                  json.dumps(tutor_response), difficulty_level, round(processing_time / 60, 2)))
            
            # Log activity
            cursor.execute('''
                INSERT INTO user_activity (user_id, activity_type, activity_description)
                VALUES (?, ?, ?)
            ''', (session['user_id'], 'subject_study', f'Studied {subject}: {topic}'))
            
            conn.commit()
            conn.close()
        
        return jsonify({
            'success': True,
            'response': tutor_response,
            'processing_time': round(processing_time, 2)
        })
        
    except Exception as e:
        return jsonify({'error': f'Error in tutoring session: {str(e)}'}), 500

@bp.route('/quiz-generator')
def quiz_generator():
    """Generate practice quizzes for law subjects"""
    return render_template('student/quiz_generator.html')

@bp.route('/api/generate-quiz', methods=['POST'])
def generate_quiz():
    """Generate AI-powered quiz questions"""
    try:
        data = request.get_json()
        subject = data.get('subject', '')
        topic = data.get('topic', '')
        num_questions = min(int(data.get('num_questions', 5)), 20)  # Max 20 questions
        difficulty = data.get('difficulty', 'intermediate')
        
        if not subject or not topic:
            return jsonify({'error': 'Subject and topic are required'}), 400
        
        # Generate quiz questions
        if model:
            try:
                prompt = generate_quiz_prompt(subject, topic, num_questions, difficulty)
                response = model.generate_content(prompt)
                quiz_data = parse_quiz_response(response.text, num_questions)
            except Exception as e:
                print(f"AI Error: {e}")
                quiz_data = generate_fallback_quiz(subject, topic, num_questions)
        else:
            quiz_data = generate_fallback_quiz(subject, topic, num_questions)
        
        # Save quiz if user is logged in
        if session.get('user_id'):
            conn = db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO generated_quizzes (
                    user_id, subject, topic, questions, difficulty, num_questions
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (session['user_id'], subject, topic, json.dumps(quiz_data), difficulty, num_questions))
            
            conn.commit()
            conn.close()
        
        return jsonify({
            'success': True,
            'quiz': quiz_data
        })
        
    except Exception as e:
        return jsonify({'error': f'Error generating quiz: {str(e)}'}), 500

@bp.route('/study-planner')
def study_planner():
    """AI-powered study planner for LLB students"""
    return render_template('student/study_planner.html')

@bp.route('/api/create-study-plan', methods=['POST'])
def create_study_plan():
    """Generate personalized study plan"""
    try:
        data = request.get_json()
        semester = data.get('semester', '')
        subjects = data.get('subjects', [])
        exam_date = data.get('exam_date', '')
        study_hours_per_day = int(data.get('study_hours_per_day', 4))
        weak_subjects = data.get('weak_subjects', [])
        
        if not semester or not subjects:
            return jsonify({'error': 'Semester and subjects are required'}), 400
        
        # Generate study plan
        if model:
            try:
                prompt = generate_study_plan_prompt(semester, subjects, exam_date, 
                                                 study_hours_per_day, weak_subjects)
                response = model.generate_content(prompt)
                study_plan = parse_study_plan_response(response.text)
            except Exception as e:
                print(f"AI Error: {e}")
                study_plan = generate_fallback_study_plan(semester, subjects, study_hours_per_day)
        else:
            study_plan = generate_fallback_study_plan(semester, subjects, study_hours_per_day)
        
        # Save study plan if user is logged in
        if session.get('user_id'):
            conn = db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO study_plans (
                    user_id, semester, subjects, exam_date, study_hours_per_day, 
                    weak_subjects, plan_data
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (session['user_id'], semester, json.dumps(subjects), exam_date,
                  study_hours_per_day, json.dumps(weak_subjects), json.dumps(study_plan)))
            
            conn.commit()
            conn.close()
        
        return jsonify({
            'success': True,
            'study_plan': study_plan
        })
        
    except Exception as e:
        return jsonify({'error': f'Error creating study plan: {str(e)}'}), 500

@bp.route('/legal-research')
def legal_research():
    """Legal research assistant for students"""
    return render_template('student/legal_research.html')

@bp.route('/api/legal-research', methods=['POST'])
def legal_research_api():
    """AI-powered legal research assistant"""
    try:
        data = request.get_json()
        research_query = data.get('query', '').strip()
        research_type = data.get('type', 'general')  # general, case_law, statute, article
        
        if not research_query:
            return jsonify({'error': 'Research query is required'}), 400
        
        # Generate research response
        if model:
            try:
                prompt = generate_research_prompt(research_query, research_type)
                response = model.generate_content(prompt)
                research_result = parse_research_response(response.text)
            except Exception as e:
                print(f"AI Error: {e}")
                research_result = generate_fallback_research(research_query, research_type)
        else:
            research_result = generate_fallback_research(research_query, research_type)
        
        # Save research if user is logged in
        if session.get('user_id'):
            conn = db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO legal_research (
                    user_id, query, research_type, result
                ) VALUES (?, ?, ?, ?)
            ''', (session['user_id'], research_query, research_type, json.dumps(research_result)))
            
            conn.commit()
            conn.close()
        
        return jsonify({
            'success': True,
            'research': research_result
        })
        
    except Exception as e:
        return jsonify({'error': f'Error in legal research: {str(e)}'}), 500

# Helper functions for AI prompts and responses

def generate_case_study_prompt(case_text, analysis_type):
    """Generate prompt for case study analysis"""
    base_prompt = f"""
You are an expert law professor analyzing a case study for LLB students. Provide a comprehensive analysis of the following case:

CASE STUDY:
{case_text}

ANALYSIS TYPE: {analysis_type}

Please provide a detailed analysis including:

1. **Case Summary**: Brief overview of the case
2. **Key Facts**: Important factual elements
3. **Legal Issues**: Main legal questions raised
4. **Applicable Laws**: Relevant statutes, sections, and legal principles
5. **Court's Reasoning**: Analysis of judicial reasoning (if available)
6. **Judgment/Decision**: Outcome and its implications
7. **Legal Principles**: Key legal principles established or applied
8. **Precedent Value**: Importance as precedent for future cases
9. **Critical Analysis**: Strengths and weaknesses of the decision
10. **Student Learning Points**: Key takeaways for law students

Format your response in clear sections with proper headings. Make it educational and suitable for LLB students.
"""
    return base_prompt

def parse_case_study_response(response_text):
    """Parse AI response for case study analysis"""
    return {
        'analysis': response_text,
        'summary': extract_section(response_text, 'Case Summary'),
        'key_facts': extract_section(response_text, 'Key Facts'),
        'legal_issues': extract_section(response_text, 'Legal Issues'),
        'applicable_laws': extract_section(response_text, 'Applicable Laws'),
        'judgment': extract_section(response_text, 'Judgment'),
        'learning_points': extract_section(response_text, 'Student Learning Points')
    }

def generate_tutor_prompt(subject, topic, question, difficulty_level):
    """Generate prompt for subject tutoring"""
    return f"""
You are an expert law tutor helping LLB students understand legal concepts. 

SUBJECT: {subject}
TOPIC: {topic}
STUDENT QUESTION: {question if question else 'Explain this topic comprehensively'}
DIFFICULTY LEVEL: {difficulty_level}

Please provide a comprehensive explanation that includes:

1. **Concept Overview**: Clear explanation of the main concept
2. **Key Definitions**: Important legal terms and definitions
3. **Legal Framework**: Relevant laws, sections, and regulations
4. **Practical Examples**: Real-world examples and case illustrations
5. **Important Cases**: Landmark cases related to this topic
6. **Exam Tips**: What students should focus on for exams
7. **Common Mistakes**: Typical errors students make
8. **Further Reading**: Suggested resources for deeper study

Make your explanation clear, engaging, and appropriate for the {difficulty_level} level.
Use simple language while maintaining legal accuracy.
"""

def parse_tutor_response(response_text):
    """Parse AI response for tutoring"""
    return {
        'explanation': response_text,
        'key_points': extract_bullet_points(response_text),
        'examples': extract_section(response_text, 'Practical Examples'),
        'cases': extract_section(response_text, 'Important Cases'),
        'exam_tips': extract_section(response_text, 'Exam Tips')
    }

def generate_quiz_prompt(subject, topic, num_questions, difficulty):
    """Generate prompt for quiz creation"""
    return f"""
Create a quiz for LLB students on the following:

SUBJECT: {subject}
TOPIC: {topic}
NUMBER OF QUESTIONS: {num_questions}
DIFFICULTY: {difficulty}

Generate {num_questions} multiple-choice questions with the following format for each question:

Question X: [Question text]
A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]
Correct Answer: [Letter]
Explanation: [Brief explanation of why this is correct]

Make sure questions cover different aspects of the topic and are appropriate for the {difficulty} level.
Include questions about definitions, applications, case law, and practical scenarios.
"""

def parse_quiz_response(response_text, num_questions):
    """Parse AI response for quiz questions"""
    questions = []
    lines = response_text.split('\n')
    current_question = {}
    
    for line in lines:
        line = line.strip()
        if line.startswith('Question'):
            if current_question:
                questions.append(current_question)
            current_question = {'question': line.split(':', 1)[1].strip(), 'options': []}
        elif line.startswith(('A)', 'B)', 'C)', 'D)')):
            current_question['options'].append(line[3:].strip())
        elif line.startswith('Correct Answer:'):
            current_question['correct'] = line.split(':', 1)[1].strip()
        elif line.startswith('Explanation:'):
            current_question['explanation'] = line.split(':', 1)[1].strip()
    
    if current_question:
        questions.append(current_question)
    
    return {'questions': questions[:num_questions]}

def generate_study_plan_prompt(semester, subjects, exam_date, study_hours, weak_subjects):
    """Generate prompt for study plan creation"""
    return f"""
Create a comprehensive study plan for an LLB student with the following details:

SEMESTER: {semester}
SUBJECTS: {', '.join(subjects)}
EXAM DATE: {exam_date}
DAILY STUDY HOURS: {study_hours}
WEAK SUBJECTS: {', '.join(weak_subjects)}

Create a detailed study plan that includes:

1. **Weekly Schedule**: Day-wise breakdown of subjects to study
2. **Subject Allocation**: Time distribution among subjects
3. **Priority Areas**: Focus areas for weak subjects
4. **Revision Schedule**: When and how to revise each subject
5. **Practice Tests**: When to take mock tests and practice papers
6. **Study Techniques**: Recommended study methods for each subject
7. **Milestones**: Weekly goals and checkpoints
8. **Flexibility**: Buffer time for unexpected delays

Make the plan realistic, achievable, and focused on exam success.
Give extra attention to the weak subjects: {', '.join(weak_subjects)}
"""

def parse_study_plan_response(response_text):
    """Parse AI response for study plan"""
    return {
        'plan': response_text,
        'weekly_schedule': extract_section(response_text, 'Weekly Schedule'),
        'subject_allocation': extract_section(response_text, 'Subject Allocation'),
        'revision_schedule': extract_section(response_text, 'Revision Schedule'),
        'study_techniques': extract_section(response_text, 'Study Techniques')
    }

def generate_research_prompt(query, research_type):
    """Generate prompt for legal research"""
    return f"""
You are a legal research assistant helping LLB students with their research.

RESEARCH QUERY: {query}
RESEARCH TYPE: {research_type}

Provide comprehensive research assistance including:

1. **Research Overview**: Understanding of the research question
2. **Relevant Laws**: Applicable statutes, acts, and regulations
3. **Case Law**: Important cases related to the query
4. **Legal Principles**: Key legal principles and doctrines
5. **Comparative Analysis**: How different jurisdictions handle this issue
6. **Recent Developments**: Latest changes or updates in this area
7. **Research Sources**: Where to find more information
8. **Citation Format**: How to properly cite the sources
9. **Research Tips**: How to conduct further research on this topic

Make your response detailed, accurate, and helpful for academic research purposes.
Include proper legal citations where applicable.
"""

def parse_research_response(response_text):
    """Parse AI response for legal research"""
    return {
        'research': response_text,
        'relevant_laws': extract_section(response_text, 'Relevant Laws'),
        'case_law': extract_section(response_text, 'Case Law'),
        'principles': extract_section(response_text, 'Legal Principles'),
        'sources': extract_section(response_text, 'Research Sources')
    }

# Fallback functions for when AI is not available

def generate_fallback_case_analysis(case_text):
    """Generate basic case analysis when AI is unavailable"""
    return {
        'analysis': f"Case Analysis for: {case_text[:100]}...\n\nThis case requires detailed analysis of facts, legal issues, and applicable laws. Please consult legal databases and textbooks for comprehensive analysis.",
        'summary': "AI analysis temporarily unavailable. Please use manual analysis methods.",
        'key_facts': "Extract key facts from the case text manually.",
        'legal_issues': "Identify main legal questions raised in the case.",
        'applicable_laws': "Research relevant statutes and legal provisions.",
        'judgment': "Analyze the court's decision and reasoning.",
        'learning_points': "Focus on legal principles and precedent value."
    }

def generate_fallback_tutor_response(subject, topic, question=None):
    """Generate basic tutoring response when AI is unavailable"""
    question_text = f" for question: {question}" if question else ""
    return {
        'explanation': f"Study Guide for {subject} - {topic}{question_text}\n\nPlease refer to your textbooks and class notes for detailed explanation of this topic. Consider consulting legal databases and academic resources for comprehensive understanding.",
        'key_points': [f"Study {topic} thoroughly", "Review relevant case law", "Practice with examples"],
        'examples': "Consult textbooks for practical examples",
        'cases': "Research landmark cases in legal databases",
        'exam_tips': "Focus on definitions, applications, and case analysis"
    }

def generate_fallback_quiz(subject, topic, num_questions):
    """Generate basic quiz when AI is unavailable"""
    questions = []
    for i in range(min(num_questions, 3)):
        questions.append({
            'question': f"Sample question {i+1} for {topic}",
            'options': ["Option A", "Option B", "Option C", "Option D"],
            'correct': "A",
            'explanation': "Please create custom questions based on your study material."
        })
    return {'questions': questions}

def generate_fallback_study_plan(semester, subjects, study_hours):
    """Generate basic study plan when AI is unavailable"""
    subjects_count = len(subjects) if subjects else 1
    hours_per_subject = study_hours / subjects_count if subjects_count > 0 else study_hours
    subject_list = ", ".join(subjects) if subjects else "your subjects"
    
    return {
        'plan': f"Basic Study Plan for {semester}\n\nAllocate {study_hours} hours daily among {subjects_count} subjects ({subject_list}). Create a balanced schedule with regular revision periods.",
        'weekly_schedule': "Distribute subjects evenly across the week",
        'subject_allocation': f"Spend approximately {hours_per_subject:.1f} hours per subject daily",
        'revision_schedule': "Dedicate weekends for revision and practice tests",
        'study_techniques': "Use active reading, note-taking, and case analysis methods"
    }

def generate_fallback_research(query, research_type):
    """Generate basic research response when AI is unavailable"""
    research_focus = {
        'case_law': 'Focus on landmark cases and judicial precedents',
        'statute': 'Focus on relevant acts, sections, and regulations',
        'academic': 'Focus on scholarly articles and academic papers',
        'comparative': 'Focus on comparative legal analysis',
        'general': 'Focus on comprehensive legal research'
    }.get(research_type, 'Focus on comprehensive legal research')
    
    return {
        'research': f"Research Guide for: {query}\n\n{research_focus}. Consult legal databases, textbooks, and academic journals for comprehensive research on this topic.",
        'relevant_laws': "Search legal databases for applicable statutes",
        'case_law': "Use case law databases to find relevant precedents",
        'principles': "Review legal textbooks for fundamental principles",
        'sources': "Use law libraries, online databases, and academic resources"
    }

# Utility functions

def extract_section(text, section_name):
    """Extract a specific section from formatted text"""
    lines = text.split('\n')
    section_content = []
    in_section = False
    
    for line in lines:
        if section_name.lower() in line.lower() and ('**' in line or '#' in line):
            in_section = True
            continue
        elif in_section and ('**' in line or '#' in line) and section_name.lower() not in line.lower():
            break
        elif in_section:
            section_content.append(line.strip())
    
    return '\n'.join(section_content).strip()

def extract_bullet_points(text):
    """Extract bullet points from text"""
    lines = text.split('\n')
    bullet_points = []
    
    for line in lines:
        line = line.strip()
        if line.startswith(('•', '-', '*', '1.', '2.', '3.', '4.', '5.')):
            bullet_points.append(line)
    
    return bullet_points[:5]  # Return top 5 points