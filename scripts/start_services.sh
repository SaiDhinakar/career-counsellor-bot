#!/bin/bash

# AI Virtual Career Counsellor - Service Startup Script
# This script starts all required services for the application

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Change to project root directory
cd "$PROJECT_ROOT"

echo "🎯 Starting AI Virtual Career Counsellor Services..."
echo "=================================================="

# Check if virtual environment exists and activate it
if [ -d "venv" ]; then
    echo "🔄 Activating virtual environment..."
    source venv/bin/activate
    echo "✅ Virtual environment activated"
else
    echo "⚠️  No virtual environment found. Running with system Python."
    echo "💡 Run './scripts/setup.sh' to create a virtual environment."
fi

# Check if required directories exist
if [ ! -d "rasa_bot" ]; then
    echo "❌ Error: rasa_bot directory not found!"
    echo "Make sure you're running this script from the correct location."
    exit 1
fi

if [ ! -d "streamlit_app" ]; then
    echo "❌ Error: streamlit_app directory not found!"
    exit 1
fi

# Check if model exists
if [ ! -f "rasa_bot/models/"*.tar.gz ]; then
    echo "📚 No trained model found. Training new model..."
    cd rasa_bot
    rasa train
    cd ..
    echo "✅ Model training completed!"
fi

echo "🚀 Starting services..."

# Start Rasa action server in background
echo "▶️  Starting Rasa Action Server (Port 5055)..."
cd rasa_bot
nohup rasa run actions --port 5055 > ../logs/actions.log 2>&1 &
ACTION_PID=$!
cd ..

# Wait for action server to start
sleep 3

# Start Rasa core server in background
echo "▶️  Starting Rasa Core Server (Port 5005)..."
cd rasa_bot
nohup rasa run --enable-api --cors="*" --port 5005 > ../logs/rasa.log 2>&1 &
RASA_PID=$!
cd ..

# Wait for Rasa server to start
sleep 5

# Start Streamlit app
echo "▶️  Starting Streamlit App (Port 8501)..."
cd streamlit_app
nohup streamlit run app.py > ../logs/streamlit.log 2>&1 &
STREAMLIT_PID=$!
cd ..

# Create logs directory if it doesn't exist
mkdir -p logs

# Save process IDs for later cleanup
echo $ACTION_PID > logs/action_server.pid
echo $RASA_PID > logs/rasa_server.pid
echo $STREAMLIT_PID > logs/streamlit_app.pid

echo ""
echo "✅ All services started successfully!"
echo "=================================================="
echo "🌐 Access the application at: http://localhost:8501"
echo ""
echo "📊 Service Status:"
echo "   • Rasa Action Server: Running (PID: $ACTION_PID)"
echo "   • Rasa Core Server:   Running (PID: $RASA_PID)"
echo "   • Streamlit App:      Running (PID: $STREAMLIT_PID)"
echo ""
echo "📁 Logs Location:"
echo "   • Action Server: logs/actions.log"
echo "   • Rasa Server:   logs/rasa.log"
echo "   • Streamlit App: logs/streamlit.log"
echo ""
echo "🛑 To stop all services, run: ./scripts/stop_services.sh"
echo "📊 To check service status, run: ./scripts/check_services.sh"
echo ""
echo "🎉 Happy Career Counselling!"
