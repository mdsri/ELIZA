import streamlit as st

# Team Members Data
team_members = [
    {
        "name": "Rawan Alghamdi",
        "intro": "Computer Science graduate from KAU with a bachelor's degree, passionate about artificial intelligence and Data analysis.",
        "linkedin": "https://www.linkedin.com/in/rawan-alghamdi-460364222/"
    },
    {
        "name": "Najla Alhomaid",
        "intro": "Computer Science graduate from King Saud University, interested in Artificial Intelligence.",
        "linkedin": "https://www.linkedin.com/in/najla-a-154039226"
    },
    {
        "name": "Mohammed Aldawsari",
        "intro": "Computer science student at King Saud University, interested in AI and Data science",
        "linkedin": "https://www.linkedin.com/in/mohammed-aldawsari-8ab71624b/"
    },
    {
        "name": "Mohammad Alkhatim",
        "intro": "Computer Science graduate from Jubail Industrial College with a bachelor's degree, passionate about artificial intelligence.",
        "linkedin": "https://www.linkedin.com/in/mohammad-alkhatim-9b1770266/"
    },
    {
        "name": "Abdulkarim Almalki",
        "intro": "Student at IMAMU, Management Information System, Interested in data analysis and AI",
        "linkedin": "https://www.linkedin.com/in/abdulkarimalmalki/"
    }
]

# CSS for Modern Horizontal Layout
st.markdown(
    """
    <style>
    .team-container {
        display: flex;              /* Flexbox for horizontal alignment */
        flex-direction: row;        /* Align items in a row */
        justify-content: center;    /* Center items horizontally */
        gap: 15px;                  /* Space between team member cards */
        flex-wrap: wrap;            /* Wrap to next line on smaller screens */
        margin-top: 30px;
    }

    .team-member {
        background: linear-gradient(145deg, #e0e0e0, #ffffff); /* Subtle gradient background */
        border-radius: 15px;          /* Rounded corners */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Box shadow for depth */
        padding: 20px;
        text-align: center;
        width: 250px;                /* Set fixed width */
        height: 250px;               /* Set fixed height */
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effects */
    }

    .team-member:hover {
        transform: translateY(-8px);  /* Slightly raise the card on hover */
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2); /* Enhan ced shadow on hover */
    }

    .member-name {
        font-size: 16px;
        font-weight: bold;
        color: #003161;              /* Deep blue color */
        margin-bottom: 12px;
    }

    .member-intro {
        font-size: 13px;
        color: #555555;              /* Subtle gray for intro text */
        margin-bottom: 20px;
        line-height: 1.4;
    }

    .linkedin-link {
        font-size: 14px;
        color: #0073b1;              /* LinkedIn blue */
        text-decoration: none;
        font-weight: bold;
    }

    .linkedin-link:hover {
        text-decoration: underline;  /* Underline effect on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Team Members</h2>", unsafe_allow_html=True)

# Display Team Members in a Horizontal Layout
columns = st.columns(5)  # Create 5 columns for the members
for i, member in enumerate(team_members):
    with columns[i]:  # Access each column
        # Create a styled box for each member
        st.markdown(
            f"""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; display: flex; flex-direction: column; justify-content: start; align-items: center; width: 100%; height: 100%;">
                <a href="{member['linkedin']}" target="_blank" style="text-decoration: none; color: #003161;">
                    <h4 style="margin-bottom: 10px; font-size: 16px;">{member['name']}</h4>
                </a>
                <p style="color: #555; font-size: 12px; margin-bottom: 0;">{member['intro']}</p>
                <a href="{member['linkedin']}" target="_blank" class="linkedin-link" style="margin-top: 10px;">LinkedIn</a>
            </div>
            """,
            unsafe_allow_html=True
        )
