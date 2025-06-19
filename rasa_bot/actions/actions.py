from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class CareerRecommendationEngine:
    """Career recommendation engine using NLP and keyword matching"""
    
    def __init__(self):
        self.career_database = {
            "software_developer": {
                "title": "Software Developer",
                "field": "technology",
                "keywords": ["programming", "coding", "software", "development", "apps", "websites", "problem solving", "logic", "computers"],
                "description": "Design, develop, and maintain software applications",
                "skills": ["Programming languages", "Problem-solving", "Logical thinking", "Debugging"],
                "salary_range": "$70,000 - $150,000",
                "requirements": "Bachelor's degree in Computer Science or related field, programming experience"
            },
            "data_scientist": {
                "title": "Data Scientist",
                "field": "technology",
                "keywords": ["data", "analytics", "statistics", "machine learning", "python", "research", "numbers", "analysis"],
                "description": "Analyze complex data to help organizations make informed decisions",
                "skills": ["Statistics", "Python/R", "Machine Learning", "Data Visualization"],
                "salary_range": "$90,000 - $180,000",
                "requirements": "Bachelor's/Master's in Data Science, Statistics, or related field"
            },
            "graphic_designer": {
                "title": "Graphic Designer",
                "field": "arts",
                "keywords": ["design", "creative", "visual", "art", "graphics", "aesthetic", "colors", "artistic"],
                "description": "Create visual concepts to communicate ideas",
                "skills": ["Adobe Creative Suite", "Typography", "Color Theory", "Creativity"],
                "salary_range": "$40,000 - $80,000",
                "requirements": "Bachelor's degree in Graphic Design or portfolio demonstrating skills"
            },
            "marketing_manager": {
                "title": "Marketing Manager",
                "field": "commerce",
                "keywords": ["marketing", "promotion", "sales", "business", "strategy", "communication", "social media"],
                "description": "Develop and implement marketing strategies",
                "skills": ["Strategic thinking", "Communication", "Digital marketing", "Analytics"],
                "salary_range": "$60,000 - $120,000",
                "requirements": "Bachelor's degree in Marketing, Business, or related field"
            },
            "research_scientist": {
                "title": "Research Scientist",
                "field": "science",
                "keywords": ["research", "science", "laboratory", "experiments", "discovery", "analysis", "investigation"],
                "description": "Conduct scientific research to advance knowledge",
                "skills": ["Research methodology", "Data analysis", "Scientific writing", "Critical thinking"],
                "salary_range": "$70,000 - $130,000",
                "requirements": "PhD in relevant scientific field, research experience"
            },
            "registered_nurse": {
                "title": "Registered Nurse",
                "field": "healthcare",
                "keywords": ["healthcare", "caring", "helping people", "medical", "patient care", "health", "nursing"],
                "description": "Provide patient care and support in healthcare settings",
                "skills": ["Patient care", "Medical knowledge", "Empathy", "Communication"],
                "salary_range": "$60,000 - $90,000",
                "requirements": "Nursing degree and state licensing"
            },
            "teacher": {
                "title": "Teacher",
                "field": "education",
                "keywords": ["teaching", "education", "students", "learning", "instruction", "classroom", "knowledge sharing"],
                "description": "Educate and guide students in academic subjects",
                "skills": ["Communication", "Patience", "Subject expertise", "Classroom management"],
                "salary_range": "$40,000 - $70,000",
                "requirements": "Bachelor's degree in Education or subject area, teaching certification"
            }
        }
        
        self.stop_words = set(stopwords.words('english'))
    
    def preprocess_text(self, text: str) -> List[str]:
        """Preprocess text using NLTK"""
        # Convert to lowercase and tokenize
        tokens = word_tokenize(text.lower())
        
        # Remove stopwords and non-alphabetic tokens
        filtered_tokens = [
            token for token in tokens 
            if token.isalpha() and token not in self.stop_words
        ]
        
        return filtered_tokens
    
    def recommend_careers(self, user_interests: str, top_n: int = 3) -> List[Dict]:
        """Recommend careers based on user interests using TF-IDF similarity"""
        if not user_interests:
            return []
        
        # Preprocess user interests
        user_tokens = self.preprocess_text(user_interests)
        user_text = " ".join(user_tokens)
        
        # Prepare career descriptions for comparison
        career_texts = []
        career_names = []
        
        for career_id, career_data in self.career_database.items():
            career_text = " ".join(career_data["keywords"] + [career_data["description"]])
            career_texts.append(career_text)
            career_names.append(career_id)
        
        # Add user interests to the corpus
        all_texts = [user_text] + career_texts
        
        # Calculate TF-IDF similarity
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(all_texts)
        
        # Calculate cosine similarity between user interests and careers
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        
        # Get top recommendations
        top_indices = similarities.argsort()[-top_n:][::-1]
        
        recommendations = []
        for idx in top_indices:
            if similarities[idx] > 0:  # Only include careers with some similarity
                career_id = career_names[idx]
                career_data = self.career_database[career_id].copy()
                career_data['similarity_score'] = float(similarities[idx])
                recommendations.append(career_data)
        
        return recommendations

class ActionRecommendCareer(Action):
    """Custom action to recommend careers based on user interests"""
    
    def name(self) -> Text:
        return "action_recommend_career"
    
    def __init__(self):
        self.recommendation_engine = CareerRecommendationEngine()
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get user interests from slot
        user_interests = tracker.get_slot("user_interests")
        
        if not user_interests:
            dispatcher.utter_message(text="I'd love to help you find the perfect career! Could you tell me more about your interests, hobbies, or what you enjoy doing?")
            return []
        
        # Get career recommendations
        recommendations = self.recommendation_engine.recommend_careers(user_interests)
        
        if not recommendations:
            dispatcher.utter_message(text="I couldn't find specific career matches for your interests, but let me suggest some general career exploration tips! Consider taking online career assessments or speaking with professionals in fields that interest you.")
            return []
        
        # Format and send recommendations
        response = "🎯 **Based on your interests, here are my top career recommendations:**\n\n"
        
        for i, career in enumerate(recommendations, 1):
            response += f"**{i}. {career['title']}**\n"
            response += f"   📝 {career['description']}\n"
            response += f"   💰 Salary Range: {career['salary_range']}\n"
            response += f"   🛠️ Key Skills: {', '.join(career['skills'])}\n"
            response += f"   📋 Requirements: {career['requirements']}\n\n"
        
        response += "Would you like more details about any of these careers, or do you have questions about the requirements?"
        
        dispatcher.utter_message(text=response)
        
        return []

class ActionProvideCareerDetails(Action):
    """Provide detailed information about specific careers"""
    
    def name(self) -> Text:
        return "action_provide_career_details"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        career_field = tracker.get_slot("career_field")
        
        if career_field:
            if career_field == "technology":
                dispatcher.utter_message(response="utter_tech_careers")
            elif career_field == "arts":
                dispatcher.utter_message(response="utter_arts_careers")
            elif career_field == "commerce":
                dispatcher.utter_message(response="utter_commerce_careers")
            elif career_field == "science":
                dispatcher.utter_message(response="utter_science_careers")
            elif career_field == "healthcare":
                dispatcher.utter_message(response="utter_healthcare_careers")
            elif career_field == "education":
                dispatcher.utter_message(response="utter_education_careers")
        else:
            dispatcher.utter_message(response="utter_ask_career_field")
        
        return []

class ValidateInterestForm(FormValidationAction):
    """Validate the interest form"""
    
    def name(self) -> Text:
        return "validate_interest_form"
    
    def validate_user_interests(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate user interests input"""
        
        if slot_value and len(slot_value.strip()) > 5:
            return {"user_interests": slot_value}
        else:
            dispatcher.utter_message(text="Could you provide a bit more detail about your interests? For example, specific activities you enjoy or subjects that fascinate you.")
            return {"user_interests": None}
