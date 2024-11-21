import streamlit as st

# Team Members Data
team_members = [
    {
        "name": "Rawan Alghamdi",
        "image": "https://via.placeholder.com/150",  # Replace with actual image URL
        "intro": "AI Specialist",
        "linkedin": "https://www.linkedin.com/in/rawan-alghamdi"  # Replace with actual LinkedIn URL
    },
    {
        "name": "Ahmed Saleh",
        "image": "https://via.placeholder.com/150",  # Replace with actual image URL
        "intro": "Backend Developer",
        "linkedin": "https://www.linkedin.com/in/ahmed-saleh"  # Replace with actual LinkedIn URL
    },
    {
        "name": "Sara Ali",
        "image": "https://via.placeholder.com/150",  # Replace with actual image URL
        "intro": "UI/UX Designer",
        "linkedin": "https://www.linkedin.com/in/sara-ali"  # Replace with actual LinkedIn URL
    },
    {
        "name": "Mohammed Zaid",
        "image": "https://via.placeholder.com/150",  # Replace with actual image URL
        "intro": "ML Engineer",
        "linkedin": "https://www.linkedin.com/in/mohammed-zaid"  # Replace with actual LinkedIn URL
    },
    {
        "name": "Fatimah Khan",
        "image": "https://via.placeholder.com/150",  # Replace with actual image URL
        "intro": "Data Scientist",
        "linkedin": "https://www.linkedin.com/in/fatimah-khan"  # Replace with actual LinkedIn URL
    }
]

# App Header
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Team Members</h2>", unsafe_allow_html=True)

# Display Team Members in a Horizontal Layout
columns = st.columns(5)  # Create 5 columns

for i, member in enumerate(team_members):
    with columns[i]:  # Access each column
        # Create a clickable image linked to LinkedIn profile
        st.markdown(
            f"""
            <a href="{member['linkedin']}" target="_blank">
                <img src="{member['image']}" style="width: 100%; border-radius: 10px;">
            </a>
            """,
            unsafe_allow_html=True
        )
        st.markdown(f"<h4 style='text-align: center; margin-top: 10px;'>{member['name']}</h4>", unsafe_allow_html=True)  # Name
        st.markdown(f"<p style='text-align: center; margin-top: 5px;'>{member['intro']}</p>", unsafe_allow_html=True)  # Intro
