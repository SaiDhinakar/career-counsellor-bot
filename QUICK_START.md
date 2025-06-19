# 🚀 Quick Setup Guide

## Installation Steps

### 1. System Requirements

- Python 3.9 or higher
- 4GB RAM minimum
- 2GB free disk space

### 2. Clone & Setup

```bash
git clone <repository-url>
cd career-counsellor-bot
```

### 3. Automated Setup (Recommended)

**Linux/macOS:**

```bash
./scripts/setup.sh
```

**Windows:**

```batch
scripts\setup.bat
```

This will automatically:

- ✅ Create a Python virtual environment (`venv/`)
- ✅ Install all Python dependencies
- ✅ Download required NLTK data
- ✅ Train the Rasa model
- ✅ Create necessary directories

### 4. Manual Setup (Alternative)

**Create Virtual Environment (Recommended):**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate.bat  # Windows
```

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

**Initialize NLTK Data:**

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

**Train the Model:**

```bash
cd rasa_bot && rasa train && cd ..
```

## Running the Application

### 5. Start All Services

**Linux/macOS:**

```bash
./scripts/start_services.sh
```

**Windows:**

```batch
scripts\start_services.bat
```

### 6. Access Application

Open browser: `http://localhost:8501`

## Service Management

### Check Status

**Linux/macOS:**

```bash
./scripts/check_services.sh
```

**Windows:**

```batch
scripts\check_services.bat
```

### Stop Services

**Linux/macOS:**

```bash
./scripts/stop_services.sh
```

**Windows:**

```batch
scripts\stop_services.bat
```

### Manual Start (Alternative)

**Option A: Manual Start (3 terminals)**

```bash
# Terminal 1 - Action Server
cd rasa_bot && rasa run actions --port 5055

# Terminal 2 - Rasa Server  
cd rasa_bot && rasa run --enable-api --cors="*" --port 5005

# Terminal 3 - Streamlit App
cd streamlit_app && streamlit run app.py
```

## Troubleshooting

### Common Issues

**Issue**: Rasa server connection error
**Solution**: Ensure all three services are running on correct ports

**Issue**: NLTK data missing
**Solution**: Run the NLTK download commands again

**Issue**: Model not found
**Solution**: Run `rasa train` in the rasa_bot directory

### Service Status Check

```bash
# Check if services are running
lsof -i :5005  # Rasa server
lsof -i :5055  # Action server  
lsof -i :8501  # Streamlit app
```

## Usage Examples

### Basic Conversation

1. Start with: "Hello" or "Hi"
2. Ask: "What tech careers are available?"
3. Follow up: "Tell me about software development"
4. Get assessment: "How do I assess my skills?"

### Career Assessment

1. Go to "Career Assessment" tab
2. Fill out the form with your interests and skills
3. Click "Get Career Recommendations"
4. View personalized suggestions in the chat

### Quick Actions

- Use the quick action buttons for fast navigation
- Download chat history for future reference
- Clear chat to start fresh conversations

## Features Overview

✅ **Implemented Features**

- Natural language conversation
- 15+ career fields covered
- Skills-based recommendations
- Interactive web interface
- Career assessment tool
- Progress tracking
- Resource library

🔄 **In Development**

- Multi-language support
- Advanced analytics
- Resume analysis
- Interview preparation
- Mobile application

## Need Help?

1. Check the main README.md for detailed documentation
2. Review troubleshooting section above
3. Create an issue on GitHub

**Happy Career Exploring! 🎯**
