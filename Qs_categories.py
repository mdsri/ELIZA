import re
import time
import random

def interviewer_chat():
    
    print("Interviewer: Hello! I'm Interviewer. Please introduce yourself by telling me your name. (type 'quit' to exit)")
    
    user_name = None
    asked_patterns = set()
    
    # Fallback responses to handle undefined input
    fallback_responses = [ 
        "Interesting, {user_name}. Could you elaborate on that?",
        "I see. {user_name}, can you tell me more?",
        "That's fascinating, {user_name}. Could you expand on that?",
        "Hmm, {user_name}. Can you share more details?",
        "I'm curious, {user_name}. What do you think about this further?"
    ]
    
    used_fallbacks = []  # Track fallback responses already used
    consecutive_fallbacks = 0  # Counter for consecutive fallback responses

    while True:
        user_input = input("You: ").strip()

        # Exit condition
        if user_input.lower() == "quit":
            print(f"Interviewer: Goodbye! Take care, {user_name or 'guest'}.")
            break

        if user_name is None:
                # Extract the user's name
                match = re.search(r"(my name is|i'm|i am)\s+(.+)", user_input, re.IGNORECASE) 
                if match:
                    user_name = match.group(2).capitalize() # ex : I am Najla
                else:
                    user_name = user_input.capitalize() # ex : Najla 
                    
                print(f"Interviewer: Nice to meet you, {user_name}!")
                print(f"Interviewer: How old are you?")
                asked_patterns.add("How old are you?")
                
                continue

        # Generate response or fallback
        response = generate_response(user_input, asked_patterns)
        
        if response is None:
            consecutive_fallbacks += 1
            if consecutive_fallbacks > 2:  # Transition to next question after two fallbacks
                response = get_next_question(asked_patterns, user_name)
                consecutive_fallbacks = 0
            else:
                response = get_fallback_response(user_name, fallback_responses, used_fallbacks)
        else:
            consecutive_fallbacks = 0  # Reset fallback counter on valid response

        time.sleep(2)  # Simulate typing delay
        print(f"Interviewer: {response}")


# Categories of questions
categories = {
    "Personal": [
        (r"^\d+$|.*old.*", "From which university did you graduate?"),
        (r"(.*)university(.*)", "What’s your current job or role?"),
    ],
    "Behavioral": [
        (r"(.*)motivation(.*)", "What motivates you to excel in your field?"),
        (r"(.*)failure(.*)", "Can you share a failure you’ve experienced and how you handled it?"),
    ],
    "Technical": [
        (r"(.*)(Python)(.*)", "What is Python, and why is it popular?"),
        (r"(.*)(machine learning|ML)(.*)", "Can you describe what machine learning is?"),
    ]
}

def generate_response(user_input, asked_patterns):
    """
    Matches the user's input to a predefined pattern and returns the corresponding question.
    """
    for category_name, question_list in categories.items():
        for pattern, question in question_list:
            if re.search(pattern, user_input, re.IGNORECASE) and question not in asked_patterns:
                asked_patterns.add(question)
                return question
    # Return None to indicate fallback should handle the response
    return None


def get_fallback_response(user_name, fallback_responses, used_fallbacks):
    """
    Generates a fallback response if the user's input doesn't match any patterns.
    Ensures variety by tracking used fallback responses.
    """
    available_responses = [resp for resp in fallback_responses if resp not in used_fallbacks]
    if not available_responses:
        used_fallbacks.clear()
        available_responses = fallback_responses

    response = random.choice(available_responses)
    used_fallbacks.append(response)
    return response.format(user_name=user_name if user_name else "there")


def get_next_question_from_category(category_name, asked_patterns):
    """
    Get the next unanswered question from a specific category.
    """
    for pattern, question in categories[category_name]:
        if question not in asked_patterns:
            asked_patterns.add(question)
            return question
    return None  # All questions in this category have been asked


def get_next_question(asked_patterns, user_name):
    """
    Sequentially go through categories to find the next question.
    """
    for category_name in categories:
        question = get_next_question_from_category(category_name, asked_patterns)
        if question:
            return f"Let's move on to {category_name.lower()} questions: {question}"
    return f"I think we've covered a lot, {user_name}! Is there anything else you'd like to discuss?"


# Start the Interviewer
interviewer_chat()
