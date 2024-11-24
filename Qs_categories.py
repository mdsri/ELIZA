import re
import time
import random

print("Phantom: Hello! I'm Phantom. Please introduce yourself by telling me your name.")
    
asked_patterns = set()
name = input("You: ").strip()
time.sleep(random.uniform(3, 7))

# # Check if user doesn't want to share their name
# if any(phrase in name.lower() for phrase in ["don't", "dont", "not", "won't", "wont", "prefer not", "rather not", "private", "personal", "no", "nope", "nah", "pass"]):
#     print("Phantom: I understand if you prefer to remain anonymous. How old are you?")
# elif name.isdigit():  # Check if the input is numeric
#     print("Phantom: That's an unusual name! No problem though. How old are you?")
# else:
#     print("Phantom: It's nice to meet you! How old are you?")
    
    # Check if user doesn't want to share their name
if any(phrase in name.lower() for phrase in ["don't", "dont", "not", "won't", "wont", "prefer not", "rather not", "private", "personal", "no", "nope", "nah", "pass"]):
    print("Phantom: I understand if you prefer to remain anonymous. How old are you?")
elif any(char.isdigit() for char in name):  # Check if any number is in the input
    print("Phantom: That's an unusual name! No problem though. How old are you?")
else:
    print("Phantom: It's nice to meet you! How old are you?")


age = input("You: ").strip()
time.sleep(random.uniform(3, 7))

#if user doesn't want to share age
if any(phrase in age.lower() for phrase in ["don't", "dont", "not", "won't", "wont", "prefer not", "rather not", "private", "personal", "no", "nope", "nah", "pass"]):
    print("Phantom: I understand if you prefer not to share your age. From which university did you graduate?")
elif re.match(r".*(?:\d+|twenty|\byears\b).*", age): 
     print(f"Phantom: From which university did you graduate?")
else: # it prints a natural response if the user input a number as "five" or "thirty" or undefined
    print("Phantom: Hmm, just to let you know, the position we're discussing is generally suited for individuals in their twenties. From which university did you graduate?")

graduation = input("You: ").strip()
time.sleep(random.uniform(3, 7))

# Check if user doesn't want to share graduation info
if any(phrase in graduation.lower() for phrase in ["don't", "dont", "not", "won't", "wont", "prefer not", "rather not", "private", "personal", "no", "nope", "nah", "pass"]):
    print("Phantom: That's perfectly fine. Let's move on. Phantom: Can you tell mehow proficient are you in Python, and what libraries do you use most often?")
else:
    print("Phantom: Can you tell me how proficient are you in Python, and what libraries do you use most often?")
    
def interviewer_chat():
 
    
    # Fallback responses to handle undefined input
    fallback_responses = [
    "Alright, let's explore something else.",
    "Let's change the subject a bit.",
    "How about we switch gears?",
    "Let’s move on to another topic.",
    "Let’s change direction a little.",
    "How about we talk about something different?",
    "Alright, let's dive into another topic.",
    "Let’s shift the conversation.",
    "Let’s explore a new subject.",
    "How about we move to a different area?",
    "Let’s turn to a new topic.",
    "Alright, let’s talk about something else.",
    "Let’s move on and talk about something fresh.",
    "How about we change focus?",
    "Let’s take a new direction.",
    "Let’s talk about something different now.",
    "Alright, let’s dive into something else.",
    "How about we shift topics?",
    "Let’s switch it up a bit.",
    "Let’s move on and discuss something new.",
    "Let’s change it up and talk about something else.",
    "Alright, let's discuss something else.",
    "Let’s talk about something fresh.",
    "How about we explore a different topic?",
    "Let’s take this conversation in a new direction.",
    "Alright, let’s move on to a different discussion.",
    "Let’s shift focus to something else.",
    "How about we talk about something else for a change?",
    "Let’s take the conversation elsewhere.",
    "Alright, let’s head in a new direction.",
    "Let’s switch things around a bit.",
    "Let’s move on and try something new.",
    "Alright, let’s dive into another area of discussion.",
    "How about we explore a different perspective?",
    "Let’s change topics and talk about something new.",
    "Alright, let’s move forward with a new subject.",
    "Let’s jump into something else.",
    "How about we explore a different angle?",
    "Let’s change the conversation a bit.",
    "Alright, let’s talk about something else for a while.",
    "Let’s shift to a new subject.",
    "How about we turn to something else?",
    "Let’s change the conversation a bit.",
    "Alright, let’s dive into a new area.",
    "Let’s move to a fresh topic.",
    "Let’s explore something new and different.",
    "How about we talk about something fresh?",
    "Let’s switch to something else.",
    "Alright, let’s explore a different direction.",
    "Let’s change the focus of the conversation.",
    "How about we jump to a new subject?",
    "Let’s talk about something different.",
    "Alright, let’s move on and explore something new.",
    "Let’s change the topic for a bit.",
    "How about we turn to something else now?",
    "Let’s talk about something else for a moment.",
    "Alright, let’s shift to a new topic.",
    "Let’s try a different conversation.",
    "Let’s explore another area.",
    "Alright, let’s switch up the conversation.",
    "Let’s head in a new direction.",
    "Let’s change the focus a bit.",
    "How about we talk about something fresh?",
    "Let’s dive into something different now.",
    "Let’s move to a different topic now.",
    "Alright, let’s explore something fresh.",
    "Let’s shift the focus to something else.",
    "How about we jump into a new subject?",
    "Let’s take a different approach and talk about something else.",
    "Alright, let’s change gears.",
    "Let’s move ahead with a new topic.",
    "How about we shift to another area?",
    "Let’s talk about something fresh now.",
    "Alright, let’s explore a different subject.",
    "Let’s dive into something else entirely.",
    "How about we try a new direction?",
    "Let’s shift focus to something different.",
    "Alright, let’s discuss something else for now.",
    "Let’s talk about something else briefly.",
    "How about we explore a new topic?",
    "Let’s talk about something fresh for a bit.",
    "Alright, let’s dive into a different topic.",
    "Let’s change things up and talk about something new.",
    "Let’s shift to a fresh subject.",
    "How about we move on and try something else?",
    "Let’s talk about something else now.",
    "Alright, let’s move on and switch topics.",
    "Let’s change the focus and explore something else."
]

    
    used_fallbacks = []  # Track fallback responses already used
    consecutive_fallbacks = 0  # Counter for consecutive fallback responses

    while True:
        user_input = input("You: ").strip()

        # Generate response or fallback
        response = generate_response(user_input, asked_patterns)
        
        if response is None:
            consecutive_fallbacks += 1
            if consecutive_fallbacks > 2:
                response = get_next_question(asked_patterns)
                consecutive_fallbacks = 0
            else:
                response = get_fallback_response(fallback_responses, used_fallbacks)
        else:
            consecutive_fallbacks = 0  # Reset fallback counter on valid response

        time.sleep(random.uniform(3, 7))  # Simulate typing delay
        print(f"Phantom: {response}")


# Categories of questions
categories = {
    "Personal": [
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
    ],
    "Behavioral": [
        (r"(.*)motivation(.*)", "What motivates you to excel in your field?"),
        (r"(.*)failure(.*)", "Can you share a failure you've experienced and how you handled it?"),
        (r"(.*)challenge(.*)", "Could you tell me about a challenging situation you've faced?"),
        (r"(.*)teamwork(.*)", "Tell me about a time when you had to work closely with someone whose personality was very different from yours."),
        (r"(.*)deadline(.*)", "Describe a situation where you had to meet a tight deadline. How did you manage it?"),
        (r"(.*)conflict(.*)", "Share an experience where you had to resolve a conflict between team members."),
        (r"(.*)initiative(.*)", "Tell me about a time you saw a problem and took the initiative to correct it."),
        (r"(.*)pressure(.*)", "Describe a time when you worked under intense pressure. How did you handle it?"),
        (r"(.*)mistake(.*)", "Tell me about a time you made a mistake. How did you handle it?"),
        (r"(.*)feedback(.*)", "Share an instance when you received negative feedback. How did you respond?"),
        (r"(.*)goal(.*)", "Describe a goal you set and how you achieved it."),
        (r"(.*)disagreement(.*)", "Tell me about a time you disagreed with a supervisor's decision. How did you handle it?"),
        (r"(.*)change(.*)", "Share an experience where you had to adapt to a significant change."),
        (r"(.*)priority(.*)", "Describe a situation where you had to juggle multiple priorities. How did you organize your time?"),
        (r"(.*)difficult decision(.*)", "Tell me about a difficult decision you had to make at work."),
        (r"(.*)leadership(.*)", "Share an experience where you had to lead a team through a challenging situation."),
        (r"(.*)innovation(.*)", "Describe a time when you came up with an innovative solution to a problem."),
        (r"(.*)failure(.*)", "Tell me about a project that failed. What did you learn from it?"),
        (r"(.*)communication(.*)", "Share an example of how you handled a communication breakdown."),
        (r"(.*)motivation(.*)", "Describe a situation where you had to motivate a demoralized team."),
        (r"(.*)budget(.*)", "Tell me about a time you had to work with a tight budget."),
        (r"(.*)ethical(.*)", "Share an experience where you faced an ethical dilemma at work."),
        (r"(.*)diversity(.*)", "Describe a situation where you worked with a diverse team."),
        (r"(.*)overworked(.*)", "Tell me about a time you felt overworked. How did you handle it?"),
        (r"(.*)mentor(.*)", "Share an experience where you had to mentor someone."),
        (r"(.*)criticism(.*)", "Describe how you handled constructive criticism."),
        (r"(.*)risk(.*)", "Tell me about a calculated risk you took at work."),
        (r"(.*)quality(.*)", "Share a situation where you had to sacrifice quality for speed, or vice versa."),
    ],
    "Technical": [

        (r"(.*)(machine learning|ML)(.*)", "Can you describe what machine learning is?"),
        (r"(.*)(programming|coding)(.*)", "What programming languages are you most comfortable with?"),
        (r"(.*)machine learning(.*)", "Can you explain your experience with machine learning models?"),
        (r"(.*)deep learning(.*)", "What’s the most complex deep learning project you’ve worked on?"),
        (r"(.*)framework(.*)", "Which AI frameworks are you most comfortable working with?"),
        (r"(.*)data preprocessing(.*)", "How do you approach preprocessing data for machine learning models?"),
        (r"(.*)dataset(.*)", "Can you describe a challenging dataset you worked with and how you handled it?"),
        (r"(.*)NLP(.*)", "What experience do you have with natural language processing?"),
        (r"(.*)computer vision(.*)", "Can you discuss your experience with computer vision applications?"),
        (r"(.*)TensorFlow(.*)", "What’s your experience with TensorFlow?"),
        (r"(.*)PyTorch(.*)", "How have you used PyTorch in your projects?"),
        (r"(.*)deployment(.*)", "Can you explain how you deploy machine learning models in production?"),
        (r"(.*)cloud(.*)", "What cloud platforms have you used for AI projects?"),
        (r"(.*)AWS(.*)", "What services in AWS have you used for machine learning or AI?"),
        (r"(.*)Google Cloud(.*)", "How have you utilized Google Cloud for AI development?"),
        (r"(.*)Azure(.*)", "What’s your experience with Azure’s AI offerings?"),
        (r"(.*)scikit-learn(.*)", "How do you use scikit-learn in your work?"),
        (r"(.*)pandas(.*)", "How do you use pandas for data analysis in your projects?"),
        (r"(.*)model optimization(.*)", "Can you describe your approach to optimizing machine learning models?"),
        (r"(.*)hyperparameter(.*)", "How do you tune hyperparameters for your models?"),
        (r"(.*)GPU(.*)", "What experience do you have with GPU acceleration for training models?"),
        (r"(.*)edge AI(.*)", "Have you worked on deploying AI models on edge devices?"),
        (r"(.*)big data(.*)", "How do you handle large datasets in your projects?"),
        (r"(.*)SQL(.*)", "What’s your experience with databases and SQL for AI development?"),
        (r"(.*)API(.*)", "How do you integrate AI models with APIs?"),
        (r"(.*)REST(.*)", "Can you discuss how you’ve worked with REST APIs in AI applications?"),
        (r"(.*)CI/CD(.*)", "How do you incorporate CI/CD practices in AI model development?"),
        (r"(.*)git(.*)", "How do you use version control systems like Git in your projects?"),
        (r"(.*)testing(.*)", "How do you test machine learning models before deployment?"),
        (r"(.*)debugging(.*)", "What’s your approach to debugging a machine learning model?"),
        (r"(.*)ethics(.*)", "How do you approach ethical considerations in AI development?"),
        (r"(.*)bias(.*)", "How do you detect and mitigate bias in AI models?"),
        (r"(.*)explainability(.*)", "What tools or methods do you use for AI model explainability?"),
        (r"(.*)evaluation(.*)", "How do you evaluate the performance of an AI model?"),
        (r"(.*)metrics(.*)", "What metrics do you typically use to assess machine learning models?"),
        (r"(.*)classification(.*)", "How do you handle imbalanced classes in a classification problem?"),
        (r"(.*)regression(.*)", "What’s your approach to solving regression problems?"),
        (r"(.*)clustering(.*)", "Can you describe your experience with clustering algorithms?"),
        (r"(.*)anomaly detection(.*)", "What techniques do you use for anomaly detection?"),
        (r"(.*)transfer learning(.*)", "How have you applied transfer learning in your projects?"),
        (r"(.*)reinforcement learning(.*)", "What’s your experience with reinforcement learning?"),
        (r"(.*)GAN(.*)", "Have you worked with generative adversarial networks (GANs)?"),
        (r"(.*)LSTM(.*)", "How have you used LSTMs in sequence modeling tasks?"),
        (r"(.*)transformer(.*)", "Can you explain your experience with transformer models?"),
        (r"(.*)BERT(.*)", "Have you implemented or fine-tuned BERT in your projects?"),
        (r"(.*)chatbot(.*)", "What experience do you have in developing chatbots?"),
        (r"(.*)recommendation system(.*)", "How have you developed or optimized recommendation systems?"),
        (r"(.*)speech recognition(.*)", "What experience do you have with speech recognition technologies?"),
        (r"(.*)image processing(.*)", "Can you describe your work with image processing techniques?"),
        (r"(.*)data pipeline(.*)", "How do you design and maintain data pipelines for AI projects?"),
        (r"(.*)scalability(.*)", "What’s your approach to ensuring scalability in AI applications?"),
        (r"(.*)cross-validation(.*)", "How do you use cross-validation in model development?"),
        (r"(.*)regularization(.*)", "What techniques do you use for regularization?"),
        (r"(.*)dimensionality reduction(.*)", "Can you discuss your experience with dimensionality reduction techniques?"),
        (r"(.*)PCA(.*)", "Have you used Principal Component Analysis (PCA)? For what purpose?"),
        (r"(.*)ensemble(.*)", "What’s your approach to building ensemble models?"),
        (r"(.*)time series(.*)", "How do you handle time series data in your projects?"),
        (r"(.*)EDA(.*)", "What’s your process for exploratory data analysis (EDA)?"),
        (r"(.*)automation(.*)", "How have you automated repetitive tasks in AI workflows?"),
        (r"(.*)open source(.*)", "What open-source projects or libraries have you contributed to?"),
        (r"(.*)documentation(.*)", "How do you document your AI projects for reproducibility?"),
        (r"(.*)project management(.*)", "How do you manage timelines and deliverables for AI projects?"),
        (r"(.*)team(.*)", "How do you collaborate effectively with cross-functional teams?"),
        (r"(.*)leadership(.*)", "What leadership roles have you taken on in AI projects?"),
        (r"(.*)mentorship(.*)", "Have you mentored junior AI developers? What was your approach?"),
        (r"(.*)continuous learning(.*)", "How do you stay updated with the latest advancements in AI?"),
        (r"(.*)papers(.*)", "What recent AI research papers have you found particularly interesting?"),
        (r"(.*)innovation(.*)", "Can you describe an innovative AI solution you developed?"),
        (r"(.*)hackathon(.*)", "Have you participated in AI hackathons? What was your experience?"),
        (r"(.*)tools(.*)", "What tools do you find most useful in your AI development work?"),
        (r"(.*)DevOps(.*)", "How have you worked with DevOps teams for AI deployments?"),
        (r"(.*)version control(.*)", "How do you use version control for managing AI projects?"),
        (r"(.*)security(.*)", "How do you ensure security and privacy in AI systems?"),
        (r"(.*)integration(.*)", "Can you discuss how you’ve integrated AI solutions into existing systems?"),
        (r"(.*)risk(.*)", "What risks do you consider when deploying AI solutions?"),
        (r"(.*)optimization(.*)", "How do you optimize AI systems for cost and performance?"),
        (r"(.*)visualization(.*)", "What tools do you use for visualizing AI model performance?"),
        (r"(.*)versioning(.*)", "How do you handle versioning for machine learning models?"),
        (r"(.*)AB testing(.*)", "What’s your experience with A/B testing in AI projects?"),
        (r"(.*)scaling(.*)", "How have you scaled AI solutions for large user bases?"),
        (r"(.*)object detection(.*)", "What techniques have you used for object detection tasks?"),
        (r"(.*)image segmentation(.*)", "How have you handled image segmentation projects?"),
        (r"(.*)data augmentation(.*)", "What methods do you use for data augmentation?"),
        (r"(.*)transferable skills(.*)", "What skills from your previous roles have been most transferable to AI development?"),
        (r"(.*)prototyping(.*)", "How do you approach prototyping AI solutions?"),
        (r"(.*)scalability(.*)", "Can you discuss an example where you ensured scalability in an AI solution?"),
        (r"(.*)career(.*)", "What are your long-term career goals in AI development?"),
        (r"(.*)NumPy(.*)", "How do you use NumPy in your AI projects?"),
        (r"(.*)Pandas(.*)", "What advanced data manipulation techniques do you use with Pandas?"),
        (r"(.*)Matplotlib(.*)", "How do you visualize data using Matplotlib?"),
        (r"(.*)Seaborn(.*)", "Can you discuss how you create detailed visualizations using Seaborn?"),
        (r"(.*)Scikit-learn(.*)", "How do you leverage Scikit-learn for machine learning tasks?"),
        (r"(.*)XGBoost(.*)", "What’s your experience with XGBoost for model development?"),
        (r"(.*)LightGBM(.*)", "When do you prefer LightGBM over other gradient boosting frameworks?"),
        (r"(.*)CatBoost(.*)", "Can you describe how you’ve used CatBoost in your projects?"),
        (r"(.*)statsmodels(.*)", "How do you use statsmodels for statistical analysis?"),
        (r"(.*)Plotly(.*)", "What’s your experience with interactive data visualization in Plotly?"),
        (r"(.*)Altair(.*)", "How do you create declarative visualizations using Altair?"),
        (r"(.*)Dask(.*)", "What’s your approach to handling large datasets with Dask?"),
        (r"(.*)Hugging Face(.*)", "How have you used Hugging Face transformers in NLP tasks?"),
        (r"(.*)Keras(.*)", "What advantages do you find in using Keras for deep learning projects?"),
        (r"(.*)OpenCV(.*)", "How have you used OpenCV for image processing tasks?"),
        (r"(.*)PyCaret(.*)", "What’s your experience with PyCaret for automating machine learning workflows?"),
        (r"(.*)Bokeh(.*)", "How do you create interactive visualizations using Bokeh?"),
        (r"(.*)Dash(.*)", "Can you describe a dashboard you built using Dash?"),
        (r"(.*)NetworkX(.*)", "What’s your experience with graph-based data analysis using NetworkX?"),
        (r"(.*)PySpark(.*)", "How have you used PySpark for distributed data processing?"),
        (r"(.*)pytorch-lightning(.*)", "What’s your experience with PyTorch Lightning for structured deep learning?"),
        (r"(.*)fastai(.*)", "How have you used fastai to simplify model training?"),
        (r"(.*)SpaCy(.*)", "What’s your approach to NLP using SpaCy?"),
        (r"(.*)NLTK(.*)", "How do you use NLTK for natural language processing?"),
        (r"(.*)Gensim(.*)", "What’s your experience with Gensim for topic modeling?"),
        (r"(.*)geopandas(.*)", "How do you work with spatial data using GeoPandas?"),
        (r"(.*)imbalanced-learn(.*)", "What techniques do you use from imbalanced-learn to address class imbalance?"),
        (r"(.*)mlflow(.*)", "How do you use MLflow for managing the machine learning lifecycle?"),
        (r"(.*)Optuna(.*)", "What’s your approach to hyperparameter tuning with Optuna?"),
        (r"(.*)Shap(.*)", "How do you use SHAP for interpreting machine learning models?"),
        (r"(.*)Eli5(.*)", "What’s your experience with ELI5 for model explainability?"),
        (r"(.*)Bayesian(.*)", "How do you use Bayesian optimization in model tuning?"),
        (r"(.*)LIME(.*)", "How do you use LIME to interpret predictions from complex models?"),
        (r"(.*)Feature engineering(.*)", "What techniques do you use for feature engineering?"),
        (r"(.*)EDA(.*)", "How do you perform exploratory data analysis for AI projects?"),
        (r"(.*)missing data(.*)", "How do you handle missing data in datasets?"),
        (r"(.*)outliers(.*)", "What’s your approach to detecting and handling outliers?"),
        (r"(.*)scaling(.*)", "When do you prefer normalization versus standardization in preprocessing?"),
        (r"(.*)categorical variables(.*)", "How do you encode categorical variables for machine learning models?"),
        (r"(.*)correlation(.*)", "What techniques do you use to analyze feature correlations?"),
        (r"(.*)imbalanced data(.*)", "How do you address imbalanced data in classification tasks?"),
        (r"(.*)sampling(.*)", "What’s your experience with oversampling and undersampling methods?"),
        (r"(.*)dimensionality(.*)", "What dimensionality reduction techniques do you use, and when?"),
        (r"(.*)clustering(.*)", "Can you describe your experience with clustering algorithms such as K-Means or DBSCAN?"),
        (r"(.*)time series(.*)", "How do you handle feature engineering for time-series data?"),
        (r"(.*)cross-validation(.*)", "What strategies do you use for cross-validation in AI projects?"),
        (r"(.*)regularization(.*)", "How do you apply regularization techniques in model training?"),
        (r"(.*)bootstrap(.*)", "What’s your understanding of bootstrapping in statistical analysis?"),
        (r"(.*)probability(.*)", "How do you use probability distributions in AI models?"),
        (r"(.*)confidence interval(.*)", "What’s your approach to calculating and interpreting confidence intervals?"),
        (r"(.*)unsupervised learning(.*)", "What unsupervised learning techniques have you applied?"),
        (r"(.*)semi-supervised learning(.*)", "Have you worked with semi-supervised learning models?"),
        (r"(.*)data visualization(.*)", "How do you use data visualization to convey insights effectively?"),
        (r"(.*)bias variance tradeoff(.*)", "Can you explain the bias-variance tradeoff and how you address it?"),
        (r"(.*)random forest(.*)", "What’s your experience with random forests for classification or regression?"),
        (r"(.*)decision trees(.*)", "How do you optimize decision trees for performance?"),
        (r"(.*)gradient boosting(.*)", "What’s your approach to tuning gradient boosting algorithms?"),
        (r"(.*)k-NN(.*)", "Can you discuss a project where you used k-Nearest Neighbors (k-NN)?"),
        (r"(.*)SVM(.*)", "What’s your experience with support vector machines for classification tasks?"),
        (r"(.*)logistic regression(.*)", "How do you use logistic regression in classification problems?"),
        (r"(.*)linear regression(.*)", "What’s your approach to applying and interpreting linear regression models?"),
        (r"(.*)data quality(.*)", "How do you ensure data quality in your AI workflows?"),
        (r"(.*)feature selection(.*)", "What methods do you use for feature selection?"),
        (r"(.*)data scaling(.*)", "Can you describe when and why you use data scaling?"),
        (r"(.*)sampling techniques(.*)", "What sampling techniques do you use for creating training datasets?"),
        (r"(.*)synthetic data(.*)", "How do you generate and validate synthetic data for machine learning?"),
        (r"(.*)versioning(.*)", "How do you manage dataset versioning in AI projects?"),
        (r"(.*)data ethics(.*)", "What’s your approach to ensuring ethical use of data in AI?"),
        (r"(.*)real-time(.*)", "How do you design AI models for real-time predictions?"),
        (r"(.*)metadata(.*)", "How do you use metadata in your data science workflows?"),
        (r"(.*)forecasting(.*)", "What techniques do you use for time series forecasting?"),
        (r"(.*)root cause analysis(.*)", "How do you approach root cause analysis in data science projects?"),

    ]
}

def generate_response(user_input, asked_patterns):
    """
    Matches the user's input to a predefined pattern and returns the corresponding question.
    """
    # First check if user wants to skip or is unsure
    skip_pattern = r"(?i)(skip|pass|next|don't know|not sure|can't answer|don't want to answer|unsure|no idea|not comfortable|rather not)"
    if re.search(skip_pattern, user_input):
        return get_next_question(asked_patterns)

    # Regular pattern matching
    for category_name, question_list in categories.items():
        for pattern, question in question_list:
            if re.search(pattern, user_input, re.IGNORECASE) and question not in asked_patterns:
                asked_patterns.add(question)
                return question
    # Return None to indicate fallback should handle the response
    return None

def get_fallback_response(fallback_responses, used_fallbacks):
    """
    Returns both a fallback response and a technical question combined.
    """
    # Get a fallback response that hasn't been used
    available_fallbacks = [resp for resp in fallback_responses if resp not in used_fallbacks]
    if not available_fallbacks:
        used_fallbacks.clear()  # Reset if all have been used
        available_fallbacks = fallback_responses
    
    fallback = random.choice(available_fallbacks)
    used_fallbacks.append(fallback)
    
    # Get a technical question that hasn't been asked
    available_questions = [(pattern, question) for pattern, question in categories["Technical"] 
                         if question not in used_fallbacks]
    
    if not available_questions:
        used_fallbacks.clear()  # Reset if all have been used
        available_questions = categories["Technical"]
    
    _, question = random.choice(available_questions)
    used_fallbacks.append(question)
    
    # Combine both responses
    return f"{fallback} {question}"

def get_next_question_from_category(category_name, asked_patterns):
    """
    Get the next unanswered question from a specific category.
    """
    for pattern, question in categories[category_name]:
        if question not in asked_patterns:
            asked_patterns.add(question)
            return question
    return None  # All questions in this category have been asked

def get_next_question(asked_patterns):
    """
    Sequentially go through categories to find the next question.
    """
    for category_name in categories:
        # Skip personal questions if user showed resistance
        if category_name == "Personal" and any("private" in q or "not share" in q for q in asked_patterns):
            continue
        question = get_next_question_from_category(category_name, asked_patterns)
        if question:
            return f"Let's move on to {category_name.lower()} questions: {question}"
    return "I think we've covered a lot! Is there anything else you'd like to discuss?"

# Start the Interviewer
interviewer_chat()
