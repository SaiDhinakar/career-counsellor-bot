#!/bin/bash

# AI Virtual Career Counsellor - Initial Setup Script (Linux/macOS)
# This script handles the initial setup and installation

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Change to project root directory
cd "$PROJECT_ROOT"

echo "🎯 AI Virtual Career Counsellor - Initial Setup"
echo "==============================================="

# Check Python version
echo "🐍 Checking Python version..."
python_version=$(python3 --version 2>&1)
if [[ $? -eq 0 ]]; then
    echo "✅ Found: $python_version"
else
    echo "❌ Python 3 is not installed or not in PATH"
    echo "Please install Python 3.9+ from https://python.org"
    exit 1
fi

# Create virtual environment
echo "🏗️  Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    if [[ $? -eq 0 ]]; then
        echo "✅ Virtual environment created: venv/"
    else
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
else
    echo "✅ Virtual environment already exists: venv/"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

if [[ $? -eq 0 ]]; then
    echo "✅ Virtual environment activated"
else
    echo "❌ Failed to activate virtual environment"
    exit 1
fi

# Upgrade pip in virtual environment
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [[ $? -eq 0 ]]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    echo "Please check your internet connection and try again"
    exit 1
fi

# Download NLTK data
echo "📚 Downloading NLTK data..."
python3 -c "
import nltk
print('Downloading punkt...')
nltk.download('punkt')
print('Downloading stopwords...')
nltk.download('stopwords')
print('Downloading wordnet...')
nltk.download('wordnet')
print('✅ NLTK data downloaded successfully')
"

if [[ $? -eq 0 ]]; then
    echo "✅ NLTK data downloaded successfully"
else
    echo "❌ Failed to download NLTK data"
    exit 1
fi

# Train Rasa model
echo "🤖 Training Rasa model..."
cd rasa_bot
rasa train

if [[ $? -eq 0 ]]; then
    echo "✅ Rasa model trained successfully"
    cd ..
else
    echo "❌ Failed to train Rasa model"
    cd ..
    exit 1
fi

# Create logs directory
mkdir -p logs

echo ""
echo "🎉 Setup completed successfully!"
echo "================================"
echo ""
echo "📌 IMPORTANT: Remember to activate the virtual environment before running services:"
echo "   source venv/bin/activate"
echo ""
echo "🚀 Quick Start:"
echo "   Linux/macOS: ./scripts/start_services.sh"
echo "   Windows:     scripts\\start_services.bat"
echo ""
echo "📊 Check Status:"
echo "   Linux/macOS: ./scripts/check_services.sh"
echo "   Windows:     scripts\\check_services.bat"
echo ""
echo "🌐 Access URL: http://localhost:8501"
echo ""
echo "Happy Career Counselling! 🎯"
