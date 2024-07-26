    """
    {
  "from":"<USER_ID>",
  "token": "<DEVICE_FCM_TOKEN>",
  "to": ["<ID1>", "<ID2>"],
  "notification": {
    "title": "New Message",
    "body": {"row": {
    "message_id": "12345",
    "sender": "John Doe",
    "content": "Hello! How are you?",
    "action": "view_message",
    "column" : {
      "context" : {"text" : ["1"]}}  
  }, "row": {
    "message_id": "12345",
    "sender": "John Doe",
    "content": "Hello! How are you?",
    "action": "view_message"
  }, "column" : {
      "context" : {"text" : ["1"]}
  },   "column" : {
      "context" : {"text" : ["2"]}
  }
}}}
 형태의 rich notification 예시가 있을 때, 
 이것을 json, requests module을 활용해서, 
 예시의 값이 아닌 새로운 데이터인 pandas dataframe이 존재할 때, 
 예시 rich notification에 맞춰서 post를 할 수 있도록 만들어줘
"""

import pandas as pd
import json
import requests

# Example DataFrame
data = {
    "message_id": ["12345", "67890"],
    "sender": ["John Doe", "Jane Doe"],
    "content": ["Hello! How are you?", "Meeting at 10 AM"],
    "action": ["view_message", "schedule_meeting"],
    "context_text": [["1"], ["2"]]
}

df = pd.DataFrame(data)

# Function to convert DataFrame to notification JSON
def df_to_notification_json(df):
    # Convert DataFrame rows to dictionary
    rows = df.to_dict(orient='records')
    
    # Extract 'row' and 'column' data
    body = {
        "row": rows[0],  # Assuming we want the first row as example
        "column": [
            {"context": {"text": ["1"]}},
            {"context": {"text": ["2"]}}
        ]
    }
    
    # Construct final notification JSON
    notification_json = {
        "from": "<USER_ID>",
        "token": "<DEVICE_FCM_TOKEN>",
        "to": ["<ID1>", "<ID2>"],
        "notification": {
            "title": "New Message",
            "body": body
        }
    }
    
    return notification_json

# Convert DataFrame to notification JSON
notification_json = df_to_notification_json(df)

# Define the endpoint
url = "https://your-api-endpoint.com/notifications"

# Define headers (e.g., for JSON content)
headers = {
    "Content-Type": "application/json"
}

# Send POST request
response = requests.post(url, headers=headers, data=json.dumps(notification_json))

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
