#!/bin/bash

# Define the API URLs for the backend and data APIs
BACKEND_API_URL="http://backend-api-service-unique.backend-namespace/"
DOWNLOAD_LOGS_URL="http://backend-api-service-unique.backend-namespace//download_external_logs?env=development" 
DATA_API_URL="http://data-api-service-unique.data-namespace/"

# Log file to store the health check results
LOG_FILE="/var/log/health_check.log"

# Function to check API health
check_api_health() {
    local url=$1
    local api_name=$2

    # Send a request to the API and capture the HTTP response code
    http_response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

    # Check if the response is 200 (OK)
    if [ "$http_response" = "200" ]; then
        echo "$(date): $api_name at $url is reachable - Health check passed" >> "$LOG_FILE"
    else
        echo "$(date): $api_name at $url is unreachable - Health check failed (HTTP $http_response)" >> "$LOG_FILE"
    fi
}

# Check the health of the backend API main endpoint
check_api_health "$BACKEND_API_URL" "Backend API"

# Check the health of the download external logs endpoint
check_api_health "$DOWNLOAD_LOGS_URL" "Download External Logs API"

# Check the health of the data API
check_api_health "$DATA_API_URL" "Data API"

