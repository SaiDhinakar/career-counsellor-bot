import streamlit as st
import requests
import json
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="AI Career Counsellor",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        padding: 1rem;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    
    .user-message {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        text-align: right;
        color: #000;
    }
    
    .bot-message {
        background-color: #E3F2FD;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        text-align: left;
        color: #000;
    }
    
    .career-card {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #f8f9fa;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

class CareerCounsellorApp:
    def __init__(self):
        self.rasa_url = "http://localhost:5005/webhooks/rest/webhook"
        
        # Initialize session state
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []
        if 'user_profile' not in st.session_state:
            st.session_state.user_profile = {}
        if 'career_recommendations' not in st.session_state:
            st.session_state.career_recommendations = []
    
    def send_message_to_rasa(self, message):
        """Send message to Rasa chatbot"""
        try:
            payload = {
                "sender": "streamlit_user",
                "message": message
            }
            response = requests.post(self.rasa_url, json=payload)
            
            if response.status_code == 200:
                return response.json()
            else:
                return [{"text": "Sorry, I'm having trouble connecting. Please try again later."}]
        except requests.exceptions.ConnectionError:
            return [{"text": "⚠️ Rasa server is not running. Please start the Rasa server first with: `rasa run --enable-api --cors=\"*\"`"}]
        except Exception as e:
            return [{"text": f"Error: {str(e)}"}]
    
    def display_chat_interface(self):
        """Display the chat interface"""
        st.subheader("💬 Chat with Your AI Career Counsellor")
        
        # Chat container
        chat_container = st.container()
        
        with chat_container:
            # Display conversation history
            if st.session_state.conversation_history:
                for msg in st.session_state.conversation_history:
                    if msg['type'] == 'user':
                        st.markdown(f'<div class="user-message">🧑 You: {msg["message"]}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="bot-message">🤖 AI Counsellor: {msg["message"]}</div>', unsafe_allow_html=True)
        
        # Input area
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.text_input("Type your message here...", key="user_input", placeholder="Ask me about careers, skills, or anything else!")
        
        with col2:
            send_button = st.button("Send", key="send_btn")
        
        # Quick action buttons
        st.markdown("### Quick Actions:")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🖥️ Tech Careers"):
                self.handle_message("tell me about technology careers")
        
        with col2:
            if st.button("🎨 Creative Careers"):
                self.handle_message("tell me about arts careers")
        
        with col3:
            if st.button("💼 Business Careers"):
                self.handle_message("tell me about commerce careers")
        
        with col4:
            if st.button("🔍 Skills Assessment"):
                self.handle_message("how do I assess my skills")
        
        # Handle message sending
        if send_button and user_input:
            self.handle_message(user_input)
            st.rerun()
    
    def handle_message(self, message):
        """Handle sending message and getting response"""
        # Add user message to history
        st.session_state.conversation_history.append({
            'type': 'user',
            'message': message,
            'timestamp': datetime.now()
        })
        
        # Get bot response
        bot_responses = self.send_message_to_rasa(message)
        
        # Add bot responses to history
        for response in bot_responses:
            st.session_state.conversation_history.append({
                'type': 'bot',
                'message': response.get('text', ''),
                'timestamp': datetime.now()
            })
    
    def display_career_insights(self):
        # Top trending skills
        st.subheader("🔥 Top Trending Skills 2024")
        trending_skills = [
            "Artificial Intelligence", "Data Analysis", "Cloud Computing", 
            "Digital Marketing", "UX/UI Design", "Cybersecurity",
            "Machine Learning", "Project Management", "Python Programming", "Communication Skills"
        ]
        
        cols = st.columns(5)
        for i, skill in enumerate(trending_skills):
            with cols[i % 5]:
                st.markdown(f"**{i+1}.** {skill}")
    
    def display_career_assessment(self):
        """Display career assessment tool"""
        st.subheader("🎯 Career Assessment Tool")
        
        with st.form("career_assessment"):
            st.markdown("### Tell us about yourself:")
            
            # Personal information
            col1, col2 = st.columns(2)
            
            with col1:
                interests = st.multiselect(
                    "What are your main interests?",
                    ["Technology", "Arts & Creative", "Science", "Business", "Healthcare", 
                     "Education", "Sports", "Travel", "Environment", "Social Work"]
                )
                
                work_style = st.selectbox(
                    "Preferred work style:",
                    ["Individual work", "Team collaboration", "Leadership roles", "Mixed approach"]
                )
            
            with col2:
                skills = st.multiselect(
                    "What are your strongest skills?",
                    ["Problem-solving", "Communication", "Analytical thinking", "Creativity", 
                     "Leadership", "Technical skills", "Organization", "Research", "Teaching"]
                )
                
                environment = st.selectbox(
                    "Preferred work environment:",
                    ["Office", "Remote", "Outdoor", "Laboratory", "Hospital", "School", "Flexible"]
                )
            
            values = st.multiselect(
                "What's most important to you in a career?",
                ["High salary", "Work-life balance", "Job security", "Making a difference", 
                 "Learning opportunities", "Recognition", "Flexibility", "Travel opportunities"]
            )
            
            submitted = st.form_submit_button("Get Career Recommendations")
            
            if submitted:
                # Generate assessment results
                assessment_text = f"I'm interested in {', '.join(interests)}. My strongest skills are {', '.join(skills)}. I prefer {work_style.lower()} and value {', '.join(values)} in my career."
                
                # Send to Rasa for processing
                self.handle_message(f"Based on my assessment: {assessment_text}")
                
                st.success("✅ Assessment completed! Check the chat for your personalized recommendations.")
    
    def display_resources(self):
        """Display career resources and links"""
        st.subheader("📚 Career Development Resources")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 📖 Learning Platforms")
            resources = [
                "🎓 Coursera - Online courses",
                "🎯 LinkedIn Learning - Professional skills",
                "💻 Codecademy - Programming",
                "📊 Udemy - Various skills",
                "🏫 edX - University courses"
            ]
            for resource in resources:
                st.markdown(f"• {resource}")
        
        with col2:
            st.markdown("### 💼 Job Search Platforms")
            job_sites = [
                "🔍 LinkedIn Jobs",
                "💼 Indeed",
                "🎯 Glassdoor",
                "🏢 Monster",
                "💻 Stack Overflow Jobs"
            ]
            for site in job_sites:
                st.markdown(f"• {site}")
        
        with col3:
            st.markdown("### 🛠️ Skill Assessment Tools")
            assessment_tools = [
                "🧠 16Personalities",
                "💪 StrengthsFinder",
                "🎯 Skills Matcher",
                "📊 O*NET Interest Profiler",
                "🔍 MyMajors Career Quiz"
            ]
            for tool in assessment_tools:
                st.markdown(f"• {tool}")
    
    def run(self):
        """Main application runner"""
        # Header
        st.markdown('<h1 class="main-header">🎯 AI Virtual Career Counsellor</h1>', unsafe_allow_html=True)
        
        # Sidebar
        with st.sidebar:
            st.markdown("### 🧭 Navigation")
            page = st.radio(
                "Choose a section:",
                ["💬 Chat with AI", "📊 Career Insights", "🎯 Career Assessment", "📚 Resources"]
            )
            
            st.markdown("---")
            st.markdown("### 📈 Your Progress")
            
            # Progress metrics
            conversations = len(st.session_state.conversation_history)
            bot_messages = len([msg for msg in st.session_state.conversation_history if msg['type'] == 'bot'])
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Messages", conversations)
            with col2:
                st.metric("AI Responses", bot_messages)
            
            if conversations > 0:
                st.progress(min(conversations / 20, 1.0))
                st.caption("Keep chatting to unlock more insights!")
            
            st.markdown("---")
            st.markdown("### 🔧 Quick Actions")
            
            if st.button("🗑️ Clear Chat"):
                st.session_state.conversation_history = []
                st.rerun()
            
            if st.button("💾 Download Chat"):
                chat_text = ""
                for msg in st.session_state.conversation_history:
                    sender = "You" if msg['type'] == 'user' else "AI Counsellor"
                    chat_text += f"{sender}: {msg['message']}\n"
                
                st.download_button(
                    label="📄 Download as TXT",
                    data=chat_text,
                    file_name=f"career_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
        
        # Main content based on selected page
        if page == "💬 Chat with AI":
            self.display_chat_interface()
            
            # Welcome message for new users
            if not st.session_state.conversation_history:
                st.info("👋 Welcome! I'm your AI Career Counsellor. Ask me about different career paths, skill requirements, salary information, or get personalized career recommendations!")
        
        elif page == "📊 Career Insights":
            self.display_career_insights()
        
        elif page == "🎯 Career Assessment":
            self.display_career_assessment()
        
        elif page == "📚 Resources":
            self.display_resources()
        
        # Footer
        st.markdown("---")
        st.markdown(
            "🤖 **AI Virtual Career Counsellor** | Built with Rasa NLP, NLTK, and Streamlit | "
            "Your intelligent companion for career guidance and planning"
        )

if __name__ == "__main__":
    app = CareerCounsellorApp()
    app.run()
