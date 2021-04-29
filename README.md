# convert-messages-to-SRT-format
Convert Symbl's conversation messages to SRT format file

# Pre-requirements 
* Symbl appId and appSecret from your Symbl account
* conversationId of a conversation you digested into Symbl system

# How does it work:
* Once you have a converstionId the script will run Two APIs: "conversations" and "messages"
* conversations API will get the initial startTime
* messages API will get the startTime, endTime and text for all of the messages
* Calculation of time differnt from the messages startTime and endTime will be done vs. the conversations startTime. 

# How to Install:
* git clone https://github.com/symblai/convert-messages-to-SRT-format
* cd convert-messages-to-SRT-format
# How to run:
* Edit the file with your appId, appSecret and conversationId
* Save the file
* Run the file ```python index.py```

Users can now convert conversation messages to a SRT file format.
