# 🎯 AI Virtual Career Counsellor

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Rasa](https://img.shields.io/badge/Rasa-3.6.13-green.svg)](https://rasa.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌟 Overview

An intelligent AI-powered Virtual Career Counsellor built with **Rasa Framework** that provides personalized career guidance, recommendations, and advice based on user interests, skills, and career goals. The system combines Natural Language Processing (NLP) with machine learning to deliver comprehensive career counseling services through an intuitive web interface.

## ✨ Key Features

### 🤖 **Intelligent Conversational AI**

- **15+ Intent Recognition**: Handles career inquiries, skill assessments, salary questions, and more
- **Smart NLU Pipeline**: Advanced natural language understanding with DIET classifier
- **Contextual Conversations**: Maintains conversation flow with memory and context awareness
- **Fallback Handling**: Gracefully handles unknown queries with appropriate responses

### 🎯 **Personalized Career Recommendations**

- **Skills-Based Matching**: Analyzes user skills and interests using NLTK and scikit-learn
- **Multi-Domain Coverage**: Technology, Arts, Commerce, Science, Healthcare, Education
- **Salary Insights**: Provides realistic salary ranges for different career paths
- **Job Requirements**: Detailed requirements and qualifications for each career

### 📊 **Interactive Web Interface**

- **Modern Streamlit UI**: Beautiful, responsive design with custom CSS styling
- **Real-time Chat**: Seamless conversation experience with the AI counsellor
- **Career Assessment Tool**: Comprehensive questionnaire for personalized recommendations
- **Progress Tracking**: Monitor conversation history and career exploration progress
- **Resource Library**: Curated learning platforms, job sites, and assessment tools

### 🔧 **Advanced NLP Capabilities**

- **NLTK Integration**: Text preprocessing, tokenization, and keyword extraction
- **TF-IDF Vectorization**: Semantic similarity matching for career recommendations
- **Custom Actions**: Dynamic career analysis and personalized advice generation
- **Form Validation**: Structured data collection for better recommendations

## 🏗️ Architecture

```
AI Virtual Career Counsellor
├── 🎨 Frontend (Streamlit)
│   ├── Interactive Chat Interface
│   ├── Career Assessment Tool
│   ├── Progress Dashboard
│   └── Resource Library
│
├── 🧠 Rasa NLU Engine
│   ├── Intent Classification (15+ intents)
│   ├── Entity Extraction
│   ├── Conversation Management
│   └── Response Generation
│
├── ⚡ Custom Actions Server
│   ├── Career Recommendation Engine
│   ├── Skills Analysis (NLTK + scikit-learn)
│   ├── Form Validation
│   └── Dynamic Response Generation
│
└── 📚 Knowledge Base
    ├── Career Database (15+ career paths)
    ├── Skills Taxonomy
    ├── Salary Information
    └── Job Requirements
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip package manager

### Option A: Automated Setup (Recommended)

**1. Clone the Repository**

```bash
git clone <repository-url>
cd career-counsellor-bot
```

**2. Run Setup Script**

**Linux/macOS:**

```bash
./scripts/setup.sh
```

**Windows:**

```batch
scripts\setup.bat
```

The setup script will automatically:

- ✅ Create a Python virtual environment (`venv/`)
- ✅ Install all Python dependencies
- ✅ Download required NLTK data
- ✅ Train the Rasa model
- ✅ Create necessary directories

**3. Start All Services**

**Linux/macOS:**

```bash
./scripts/start_services.sh
```

**Windows:**

```batch
scripts\start_services.bat
```

**4. Access the Application**
Open your browser and navigate to: `http://localhost:8501`

### Option B: Manual Setup

**1. Clone the Repository**

```bash
git clone <repository-url>
cd career-counsellor-bot
```

**2. Install Dependencies**

```bash
pip install -r requirements.txt
```

**3. Download NLTK Data**

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

**4. Train the Rasa Model**

```bash
cd rasa_bot
rasa train
cd ..
```

**5. Start the Services**

**Terminal 1 - Start Rasa Action Server:**

```bash
cd rasa_bot
rasa run actions --port 5055
```

**Terminal 2 - Start Rasa Core Server:**

```bash
cd rasa_bot
rasa run --enable-api --cors="*" --port 5005
```

**Terminal 3 - Launch Streamlit App:**

```bash
cd streamlit_app
streamlit run app.py
```

**6. Access the Application**

Open your browser and navigate to: `http://localhost:8501`

## 🛠️ Service Management

### Check Service Status

**Linux/macOS:**

```bash
./scripts/check_services.sh
```

**Windows:**

```batch
scripts\check_services.bat
```

### Stop All Services

**Linux/macOS:**

```bash
./scripts/stop_services.sh
```

**Windows:**

```batch
scripts\stop_services.bat
```

### Restart Services

**Linux/macOS:**

```bash
./scripts/stop_services.sh
./scripts/start_services.sh
```

**Windows:**

```batch
scripts\stop_services.bat
scripts\start_services.bat
```

## 📁 Project Structure

```
career-counsellor-bot/
├── 📄 README.md                    # Project documentation
├── 📄 LICENSE                      # MIT License
├── 📋 requirements.txt             # Python dependencies
├── 🚫 .gitignore                   # Git ignore rules
│
├── 🤖 rasa_bot/                    # Rasa chatbot core
│   ├── 📄 config.yml               # Rasa pipeline configuration
│   ├── 📄 domain.yml               # Intents, entities, slots, responses
│   ├── 📄 endpoints.yml            # Action server endpoints
│   │
│   ├── 📊 data/                    # Training data
│   │   ├── 📄 nlu.yml              # NLU training examples (15+ intents)
│   │   ├── 📄 stories.yml          # Conversation flows
│   │   └── 📄 rules.yml            # Conversation rules
│   │
│   ├── ⚡ actions/                 # Custom actions
│   │   ├── 📄 __init__.py          # Package initialization
│   │   └── 📄 actions.py           # Career recommendation engine
│   │
│   └── 🎯 models/                  # Trained models
│       └── 📦 [trained-model].tar.gz
│
├── 🎨 streamlit_app/               # Web interface
│   └── 📄 app.py                   # Streamlit application
│
├── 🛠️ scripts/                     # Automation scripts
│   ├── 📄 setup.sh                 # Linux/macOS setup script
│   ├── 📄 setup.bat                # Windows setup script
│   ├── 📄 start_services.sh        # Linux/macOS service starter
│   ├── 📄 start_services.bat       # Windows service starter
│   ├── 📄 stop_services.sh         # Linux/macOS service stopper
│   ├── 📄 stop_services.bat        # Windows service stopper
│   ├── 📄 check_services.sh        # Linux/macOS service checker
│   └── 📄 check_services.bat       # Windows service checker
│
├── 📚 src/                         # Additional modules
│   ├── 📄 career_engine.py         # Career recommendation logic
│   └── 📄 analytics.py             # Analytics and insights
│
└── 📁 logs/                        # Runtime logs (created automatically)
    ├── 📄 actions.log              # Action server logs
    ├── 📄 rasa.log                 # Rasa server logs
    └── 📄 streamlit.log            # Streamlit app logs
```

## 🔧 Configuration

### Rasa Configuration

The system uses a sophisticated NLP pipeline:

- **WhitespaceTokenizer**: Text tokenization
- **RegexFeaturizer**: Pattern recognition
- **CountVectorsFeaturizer**: Text vectorization
- **DIETClassifier**: Intent classification and entity extraction
- **ResponseSelector**: Response selection
- **FallbackClassifier**: Handling unknown inputs

### Career Database

The recommendation engine includes:

- **15+ Career Paths**: Technology, Arts, Commerce, Science, Healthcare, Education
- **Skills Mapping**: 50+ skills and competencies
- **Salary Information**: Current market rates
- **Job Requirements**: Education, experience, certifications

## 🎯 Supported Career Fields

| Field                       | Careers Included                                  | Sample Roles                                           |
| --------------------------- | ------------------------------------------------- | ------------------------------------------------------ |
| 🖥️**Technology**    | Software Development, Data Science, Cybersecurity | Software Developer, Data Scientist, Security Analyst   |
| 🎨**Arts & Creative** | Design, Media, Entertainment                      | Graphic Designer, Content Creator, Art Director        |
| 💼**Commerce**        | Business, Finance, Marketing                      | Business Analyst, Financial Advisor, Marketing Manager |
| 🔬**Science**         | Research, Engineering, Analytics                  | Research Scientist, Engineer, Lab Technician           |
| 🏥**Healthcare**      | Medical, Nursing, Therapy                         | Doctor, Nurse, Physical Therapist                      |
| 🎓**Education**       | Teaching, Training, Academia                      | Teacher, Professor, Training Specialist                |

## 🛠️ Technical Details

### NLP Pipeline

- **Language**: English
- **Tokenization**: NLTK word tokenization
- **Preprocessing**: Stop word removal, text normalization
- **Vectorization**: TF-IDF for semantic similarity
- **Classification**: DIET classifier with 100 epochs training

### Custom Actions

1. **`action_recommend_career`**: Analyzes user input and recommends suitable careers
2. **`action_provide_career_details`**: Provides detailed information about specific careers
3. **`validate_interest_form`**: Validates user input in interest collection forms

### Machine Learning Features

- **Cosine Similarity**: For matching user interests with career requirements
- **Keyword Extraction**: Identifying relevant skills and interests from user input
- **Skill Assessment**: Evaluating user competencies against career requirements

## 📊 Training Data

### Intent Coverage

- **15+ Intents**: Comprehensive coverage of career-related queries
- **150+ Training Examples**: Diverse examples for robust classification
- **Contextual Responses**: Dynamic responses based on user context

### Sample Intents

- `ask_career_advice` - General career guidance
- `ask_tech_careers` - Technology career inquiries
- `ask_salary_info` - Salary and compensation questions
- `ask_skills_assessment` - Skills evaluation requests
- `provide_interests` - User interest collection

## 🚀 Deployment

### Local Development

Follow the Quick Start guide above for local development setup.

### Production Deployment

1. **Docker Containerization** (Recommended)
2. **Cloud Platforms**: AWS, Google Cloud, Azure
3. **Heroku Deployment** for quick prototyping
4. **Kubernetes** for scalable deployment

### Environment Variables

```bash
RASA_SERVER_URL=http://localhost:5005
ACTION_SERVER_URL=http://localhost:5055
STREAMLIT_SERVER_PORT=8501
```

## 🧪 Testing

### Manual Testing

1. [ ] Start all services as described in Quick Start
2. [ ] Test various conversation flows:
    - [ ] Career recommendations
    - [ ] Skills assessment
    - [ ] Salary inquiries
    - [ ] Different career fields

### Automated Testing

```bash
# Test Rasa model
cd rasa_bot
rasa test

# Test custom actions
python -m pytest actions/test_actions.py
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Training Statistics

- **Training Epochs**: 100
- **Model Size**: ~50MB
- **Training Time**: ~5 minutes
- **Supported Languages**: English

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### 🌟 **Star this repository if you found it helpful!**

**Built with ❤️ by [Sai Dhinakar](https://github.com/SaiDhinakar)**

*Empowering careers through AI-driven guidance and personalized recommendations.*
