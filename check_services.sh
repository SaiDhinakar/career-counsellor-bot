#!/bin/bash

# AI Virtual Career Counsellor - Service Status Check Script
# This script checks the status of all services

echo "📊 AI Virtual Career Counsellor - Service Status"
echo "=============================================="

# Function to check if port is in use
check_port() {
    local port=$1
    local service_name=$2
    
    if lsof -i :$port > /dev/null 2>&1; then
        local pid=$(lsof -ti :$port)
        echo "✅ $service_name is running on port $port (PID: $pid)"
        return 0
    else
        echo "❌ $service_name is NOT running on port $port"
        return 1
    fi
}

# Check all services
echo "🔍 Checking service ports..."
echo ""

action_status=0
rasa_status=0
streamlit_status=0

check_port 5055 "Rasa Action Server" && action_status=1
check_port 5005 "Rasa Core Server" && rasa_status=1
check_port 8501 "Streamlit App" && streamlit_status=1

echo ""
echo "📋 Service Summary:"
echo "=================="

total_running=$((action_status + rasa_status + streamlit_status))

if [ $total_running -eq 3 ]; then
    echo "🎉 All services are running correctly!"
    echo "🌐 Access the application at: http://localhost:8501"
elif [ $total_running -eq 0 ]; then
    echo "⚠️  No services are running!"
    echo "💡 Run './start_services.sh' to start all services"
else
    echo "⚠️  Only $total_running out of 3 services are running"
    echo "💡 You may need to restart services with './start_services.sh'"
fi

echo ""
echo "📁 Log Files (if available):"
if [ -d "logs" ]; then
    for log_file in logs/*.log; do
        if [ -f "$log_file" ]; then
            echo "   📄 $(basename $log_file): $(wc -l < $log_file) lines"
        fi
    done
else
    echo "   ⚠️  No logs directory found"
fi

echo ""
echo "🔧 Useful Commands:"
echo "   • Start services: ./start_services.sh"
echo "   • Stop services:  ./stop_services.sh"
echo "   • View logs:      tail -f logs/[service].log"
echo "   • Check ports:    lsof -i :5005 -i :5055 -i :8501"
