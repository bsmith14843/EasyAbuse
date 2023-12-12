"""
EasyAbuse
The goal of this was to make the use of the AbuseIPDB queries quicker and look somewhat decent still. 
Author-ish:bsmith14843
Date: 12/11/2023
Written/Modified from https://docs.abuseipdb.com/?python#introduction 

To get your own API key create an account with abuseipdb.com. Reference material here - https://www.abuseipdb.com/api.html

"""

import requests
import json

api_param = "[API]" #Enter your API Key here

def process_ip(ip): #Submitting / Processing the IP
   
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    #Verdict Colors
    green_text = "\033[92m"
    white_text = "\033[0m"
    yellow_text = "\033[93m"
    red_text = "\033[91m"
    
    
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90' #Age, This can be modified if you'd like. Values [0-90]
    }

    headers = {
        'Accept': 'application/json',
        'Key': api_param  
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Checks to makes sure of 200 response. 

        
        decoded_response = json.loads(response.text) # Parse the JSON response
        
        
        data = decoded_response.get("data", {}) # Extract relevant information

        # Print formatted output
        print("\n")
        print("#########################")
        print("#   AbuseIPDB Results   #")
        print("#########################")
        confidence_score = data.get("abuseConfidenceScore", "N/A")	
        print(f"Abuse Confidence Score: {confidence_score}%", "with", data.get("totalReports", "N/A"), "reports in the last 90 days.")
        print("Usage Type:", data.get("usageType", "N/A"))
        print("ISP:", data.get("isp", "N/A"))
        print("Domain:", data.get("domain", "N/A"))
        print("Location:", data.get("countryCode", "N/A"))
        print("IP Address:", data.get("ipAddress", "N/A"))
        
        #Separate colors for final verdict
        if confidence_score < 10:
        	print(f"Verdict: {green_text}This address has no reports attached and is likely safe.{white_text}")
        elif 10 <=confidence_score <=70: 
        	print(f"Verdict: {yellow_text}Verify the traffic on this one. There is a chance this is malicious.{white_text}")
        else:
        	print(f"Verdict: {red_text}There is a STRONG likelihood that this is malicious{white_text}")      
        
        #print(json.dumps(decoded_response, sort_keys=True, indent=4)) #JSON dump for testing. 

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Main program

if api_param == '[API]': #Api Check
    print("Please update your API.")
    
else:
    while True:
        ip_address = input("Enter the IP address: ")  # Prompt user to enter IP address
        process_ip(ip_address)  # Yeet this IP back up to the top to be processed

        # Prompt to continue Entering IPs
        print("\n")
        another_ip = input("Would you like to submit another IP? (yes/no): ").lower()

        if another_ip not in ['yes', 'y']:
            break



