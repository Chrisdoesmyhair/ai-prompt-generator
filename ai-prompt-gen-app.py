import streamlit as st

# Set page configuration
st.set_page_config(page_title="AI Prompt Generator", page_icon="🚀")

# Styling to match your green theme
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stTitle {
        color: #16a34a;
        font-weight: 800;
    }
    .formula-box {
        background-color: #f0fdf4;
        border: 2px solid #22c55e;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
    }
    .formula-text {
        color: #15803d;
        font-weight: bold;
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("Teach AI Like a Pro")
st.subheader("Universal Templates for 10× better results")

# Core Formula Display
st.markdown("""
    <div class="formula-box">
        <p style="color: #166534; font-weight: bold; text-transform: uppercase; margin-bottom: 5px;">The Core Formula</p>
        <p class="formula-text">Role + Task + Constraints + Format + Example</p>
    </div>
""", unsafe_allow_html=True)

# Template Definitions
templates = {
    "📊 Data Analysis": {
        "fields": [
            {"id": "task", "label": "What is the task?", "placeholder": "e.g. Identify trends in user retention"},
            {"id": "data", "label": "Paste your data here", "placeholder": "e.g. Month 1: 50%, Month 2: 40%..."},
            {"id": "format", "label": "Desired output format", "placeholder": "e.g. A bulleted summary with a table"}
        ],
        "template_str": "You are an expert data analyst. {task}. Analyze this data: {data}. Provide {format}."
    },
    "📄 Resume Bullet Generator": {
        "fields": [
            {"id": "role", "label": "Target Job Role", "placeholder": "e.g. Senior Project Manager"},
            {"id": "desc", "label": "Experience Description", "placeholder": "e.g. I led a team of 5 to finish a software launch"}
        ],
        "template_str": "You are a senior recruiter for {role}. Turn this experience into powerful, quantified resume bullets: {desc}."
    },
    "📧 Email Drafter": {
        "fields": [
            {"id": "type", "label": "Email Type", "placeholder": "e.g. Follow-up after meeting"},
            {"id": "role", "label": "Your Role", "placeholder": "e.g. Sales Director"},
            {"id": "recipient", "label": "Recipient", "placeholder": "e.g. Potential Client"},
            {"id": "topic", "label": "Main Topic", "placeholder": "e.g. Pricing proposal"},
            {"id": "tone", "label": "Tone", "placeholder": "e.g. Professional yet friendly"}
        ],
        "template_str": "Write a professional {type} as {role} to {recipient} about {topic}. Tone: {tone}."
    },
    "💡 Idea Brainstormer": {
        "fields": [
            {"id": "goal", "label": "Goal", "placeholder": "e.g. Getting 100 new newsletter subscribers"},
            {"id": "constraints", "label": "Constraints", "placeholder": "e.g. Zero budget, must use LinkedIn"}
        ],
        "template_str": "Brainstorm 10 creative ideas for {goal}. Constraints: {constraints}. Rank by impact and feasibility."
    },
    "📝 Meeting Summarizer": {
        "fields": [
            {"id": "notes", "label": "Paste Notes/Transcript", "placeholder": "Paste your text here..."}
        ],
        "template_str": "Summarize these meeting notes/transcript into key decisions, action items, and follow-ups. Use bullet points and assign owners. Notes: {notes}"
    }
}

# Sidebar/Template Selection
selected_name = st.selectbox("Select a Template", list(templates.keys()))
selected_template = templates[selected_name]

# Dynamic Inputs
form_values = {}
with st.container():
    st.write("### Fill in the details")
    for field in selected_template["fields"]:
        form_values[field["id"]] = st.text_input(field["label"], placeholder=field["placeholder"])

# Options
cot_enabled = st.checkbox('Add "Chain-of-Thought" (Think step by step)', value=True)

# Logic to build prompt
base_prompt = selected_template["template_str"].format(**{k: (v if v else f"[{k}]") for k, v in form_values.items()})

if cot_enabled:
    base_prompt += "\n\nThink step by step before answering."

# Output Area
st.markdown("---")
st.write("### Your Generated Prompt")
st.code(base_prompt, language="markdown")

st.info("Copy the code above and paste it into your favorite AI tool.")