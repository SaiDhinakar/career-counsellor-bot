#!/bin/bash

# AI Virtual Career Counsellor - Service Stop Script
# This script stops all running services

echo "🛑 Stopping AI Virtual Career Counsellor Services..."
echo "=================================================="

# Function to stop process by PID file
stop_service() {
    local service_name=$1
    local pid_file=$2
    
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if ps -p "$pid" > /dev/null 2>&1; then
            echo "⏹️  Stopping $service_name (PID: $pid)..."
            kill "$pid"
            sleep 2
            # Force kill if still running
            if ps -p "$pid" > /dev/null 2>&1; then
                echo "🔨 Force stopping $service_name..."
                kill -9 "$pid"
            fi
            echo "✅ $service_name stopped"
        else
            echo "⚠️  $service_name was not running"
        fi
        rm -f "$pid_file"
    else
        echo "⚠️  No PID file found for $service_name"
    fi
}

# Stop all services
if [ -d "logs" ]; then
    stop_service "Rasa Action Server" "logs/action_server.pid"
    stop_service "Rasa Core Server" "logs/rasa_server.pid"
    stop_service "Streamlit App" "logs/streamlit_app.pid"
else
    echo "⚠️  No logs directory found. Attempting to stop services by port..."
    
    # Try to kill processes by port
    echo "🔍 Stopping processes on ports 5005, 5055, 8501..."
    pkill -f "rasa run actions --port 5055" 2>/dev/null
    pkill -f "rasa run --enable-api --cors" 2>/dev/null
    pkill -f "streamlit run app.py" 2>/dev/null
fi

echo ""
echo "✅ All services stopped successfully!"
echo "🔍 To verify, check: ps aux | grep -E '(rasa|streamlit)'"
