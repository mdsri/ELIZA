import re
import streamlit as st
from streamlit_chat import message

def Interviewer_chat():
    print("Interviewer: Hello! I'm Interviewer. introduce yourself please \n (type 'quit' to exit)")    #beging of the conversation
    
    asked_patterns = set()   #check if the question as already asked

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":        
            print("Interviewer: Goodbye! Take care.")       #to quit the conversation
            break
        
        response = generate_response(user_input, asked_patterns)
        print(f"Interviewer: {response}")

def generate_response(user_input, asked_patterns):
    # Define regex patterns and responses
    patterns = [
        (r"(.*)name(.*)", "How old are you?"),
        (r"(.*)old(.*)", "What are you most passionate about in your work?"),
        (r"(.*)passion(.*)", "What are you most passionate about in your work?"),
        (r"(.*)challenge(.*)", "What is the biggest challenge you have overcome in your career?"),
        (r"(.*)motivation(.*)", "What motivates you to excel in your field?"),
        (r"(.*)failure(.*)", "Can you share a failure you’ve experienced and how you handled it?"),
        (r"(.*)success(.*)", "What does success mean to you in your professional life?"),
        (r"(.*)growth(.*)", "How do you ensure continuous personal and professional growth?"),
        (r"(.*)strength(.*)", "What do you consider to be your greatest strength?"),
        (r"(.*)weakness(.*)", "What is an area where you feel you could improve?"),
        (r"(.*)inspiration(.*)", "Who or what has inspired you most in your career?"),
        (r"(.*)goal(.*)", "What is a personal or professional goal you’re currently working toward?"),
        (r"(.*)decision(.*)", "Can you share an important decision you made and its impact?"),
        (r"(.*)learning(.*)", "What is the most valuable thing you’ve learned recently?"),
        (r"(.*)mentor(.*)", "Have you had a mentor who shaped your career? What did you learn?"),
        (r"(.*)team(.*)", "How do you approach working within a team?"),
        (r"(.*)independence(.*)", "Can you describe a time when you worked independently to achieve a goal?"),
        (r"(.*)leadership(.*)", "What does effective leadership mean to you?"),
        (r"(.*)value(.*)", "What values are most important to you in a workplace?"),
        (r"(.*)adaptability(.*)", "Can you share an instance where you had to adapt quickly to change?"),
        (r"(.*)resilience(.*)", "How do you build resilience when faced with setbacks?"),
        (r"(.*)time(.*)", "How do you prioritize your time when juggling multiple tasks?"),
        (r"(.*)stress(.*)", "How do you handle stressful situations?"),
        (r"(.*)feedback(.*)", "How do you approach giving and receiving feedback?"),
        (r"(.*)collaboration(.*)", "Can you share a time when collaboration led to better results?"),
        (r"(.*)conflict(.*)", "How do you manage conflicts in a professional setting?"),
        (r"(.*)curiosity(.*)", "What’s something new you’ve been curious to learn about?"),
        (r"(.*)failure(.*)", "How do you deal with failure and bounce back?"),
        (r"(.*)decision-making(.*)", "What is your decision-making process?"),
        (r"(.*)communication(.*)", "How do you ensure effective communication in a project?"),
        (r"(.*)initiative(.*)", "Can you provide an example of a time you took the initiative?"),
        (r"(.*)career path(.*)", "What inspired you to choose your career path?"),
        (r"(.*)success(.*)", "Can you describe a success you are particularly proud of?"),
        (r"(.*)motivation(.*)", "What drives you to perform your best?"),
        (r"(.*)learning style(.*)", "How do you approach learning new skills?"),
        (r"(.*)problem-solving(.*)", "Can you share a problem you solved creatively?"),
        (r"(.*)resourcefulness(.*)", "How do you demonstrate resourcefulness in challenging situations?"),
        (r"(.*)ambition(.*)", "What are your ambitions for the next five years?"),
        (r"(.*)vision(.*)", "What is your vision for your future career?"),
        (r"(.*)role model(.*)", "Who is a role model in your life and why?"),
        (r"(.*)habit(.*)", "What habits help you stay productive?"),
        (r"(.*)balance(.*)", "How do you maintain a work-life balance?"),
        (r"(.*)hobby(.*)", "What are your hobbies, and how do they influence your work?"),
        (r"(.*)education(.*)", "How has your education shaped your approach to work?"),
        (r"(.*)decision-making(.*)", "What is the toughest decision you’ve had to make at work?"),
        (r"(.*)priorities(.*)", "How do you determine your priorities?"),
        (r"(.*)dream(.*)", "What is your dream project?"),
        (r"(.*)risk(.*)", "Can you share a time you took a professional risk?"),
        (r"(.*)innovation(.*)", "What’s an innovative idea you’ve brought to a team?"),
        (r"(.*)network(.*)", "How do you build and maintain professional relationships?"),
        (r"(.*)integrity(.*)", "What does integrity mean to you?"),
        (r"(.*)creativity(.*)", "How do you express creativity in your work?"),
        (r"(.*)empathy(.*)", "Can you share a time when empathy helped you in your role?"),
        (r"(.*)efficiency(.*)", "How do you ensure efficiency in your work?"),
        (r"(.*)opportunity(.*)", "What opportunities are you most excited about right now?"),
        (r"(.*)focus(.*)", "How do you maintain focus during complex tasks?"),
        (r"(.*)initiative(.*)", "Can you describe a time you went beyond expectations?"),
        (r"(.*)career(.*)", "What’s been the most defining moment in your career?"),
        (r"(.*)adaptability(.*)", "How do you adjust to new environments?"),
        (r"(.*)vision(.*)", "How do you translate vision into actionable plans?"),
        (r"(.*)conflict(.*)", "How do you navigate disagreements in a professional setting?"),
        (r"(.*)recognition(.*)", "How do you prefer to be recognized for your work?"),
        (r"(.*)networking(.*)", "What role has networking played in your career?"),
        (r"(.*)ambition(.*)", "What’s the most ambitious goal you’ve set for yourself?"),
        (r"(.*)strategy(.*)", "How do you approach creating a strategy?"),
        (r"(.*)failure(.*)", "What’s a failure that taught you an important lesson?"),
        (r"(.*)support(.*)", "How do you support colleagues in challenging situations?"),
        (r"(.*)drive(.*)", "What drives your passion for your field?"),
        (r"(.*)adaptation(.*)", "Can you share an example of a time you adapted to a new role?"),
        (r"(.*)career development(.*)", "How do you approach career development?"),
        (r"(.*)confidence(.*)", "What role does confidence play in your success?"),
        (r"(.*)mistake(.*)", "How do you handle mistakes at work?"),
        (r"(.*)ambition(.*)", "What personal ambition keeps you motivated?"),
        (r"(.*)creativity(.*)", "What’s the most creative solution you’ve proposed?"),
        (r"(.*)feedback(.*)", "What’s the most valuable feedback you’ve received?"),
        (r"(.*)project(.*)", "Can you describe a challenging project and your role in it?"),
        (r"(.*)learning experience(.*)", "What’s been your most significant learning experience?"),
        (r"(.*)mentor(.*)", "What’s a piece of advice from a mentor you’ve found invaluable?"),
        (r"(.*)leadership(.*)", "How do you define leadership in your work?"),
        (r"(.*)confidence(.*)", "What helps you maintain confidence under pressure?"),
        (r"(.*)problem-solving(.*)", "What’s a problem you solved that you’re proud of?"),
        (r"(.*)opportunity(.*)", "How do you recognize and seize opportunities?"),
        (r"(.*)vision(.*)", "What is your long-term vision for your career?"),
        (r"(.*)adaptability(.*)", "Can you share a time you adapted your approach to achieve success?"),
        (r"(.*)teamwork(.*)", "What’s the most valuable lesson you’ve learned about teamwork?"),
        (r"(.*)motivation(.*)", "What keeps you motivated during difficult projects?"),
        (r"(.*)integrity(.*)", "How do you demonstrate integrity in your work?"),
        (r"(.*)initiative(.*)", "What’s an example of you taking initiative at work?"),
        (r"(.*)decision-making(.*)", "What’s a decision you made that had a lasting impact?"),
        (r"(.*)stress(.*)", "How do you stay productive under stress?"),
        (r"(.*)learning style(.*)", "What’s your preferred learning style, and how do you use it?"),
        (r"(.*)balance(.*)", "How do you balance competing priorities?"),
        (r"(.*)feedback(.*)", "How has feedback shaped your career?"),
        (r"(.*)success(.*)", "What do you consider your greatest professional success?"),
        (r"(.*)failure(.*)", "What failure helped you grow the most?"),

    ]
    
    # Match user input to patterns
    for pattern, response in patterns:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            # Check if the pattern is already in asked_patterns
            if pattern not in asked_patterns:
                asked_patterns.add(pattern)  # Mark the pattern as asked
                # Format the response with captured groups
                return response.format(*[group.strip() for group in match.groups()])
    
    # Fallback response if no new patterns are matched
    return "I see. Can you tell me more?"

# Start with ELIDA
Interviewer_chat()

# Function to generate a response
def generate_response(user_input):
    return f"Bot says: You wrote '{user_input}'"

if 'past' not in st.session_state:
    st.session_state['past'] = []  # User messages
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # ELIDA responses

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    bot_response = generate_response(user_input)
    st.session_state.generated.append(bot_response)
    st.session_state.user_input = ""

st.title("ELIDA")

chat_placeholder = st.empty()

with chat_placeholder.container():
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")  # User message
        message(st.session_state['generated'][i], key=f"{i}")  # ELIDA response


# User input field

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")

