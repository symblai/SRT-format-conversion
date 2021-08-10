# Symbl Devtool SRT format converter

Symbl's APIs empower developers to enable: 
- **Real-time** analysis of free-flowing discussions to automatically surface highly relevant summary discussion topics, contextual insights, suggestive action items, follow-ups, decisions, and questions.
- **Voice APIs** that makes it easy to add AI-powered conversation intelligence to either [telephony][telephony] or [WebSocket][websocket] interfaces.
- **Conversation APIs** that provide a REST interface for managing and processing your conversation data.
- **Summary UI** with a fully customizable and editable reference experience that indexes a searchable transcript and shows generated actionable insights, topics, timecodes, and speaker information.

<hr />


# Pre-requisites 
* Python
* Terminal


# Feature 
Convert Symbl.ai's conversation data into the SRT file format. 

## Setup and Deploy
1. The first step to getting setup is to [sign up][signup].  
2. Symbl `appId` and `appSecret` from your Symbl account
3. Grab the `conversationId` of a conversation you created with Symbl.ai
4. git clone https://github.com/symblai/convert-messages-to-SRT-format
5. Run `cd symbl-devtool-SRT-format-converter`
6.  Edit the `index.py`, adding your values for `appId`, `appSecret` and `conversationId`
7. Save the file.
8. Run the file `python index.py` in your terminal.

# Conclusion:
Here is a breakdown of what happens. 

* With the `converstionId` the script makes two API calls: `/conversations` and `/messages`
* The `/conversations` API fetches the initial `startTime`
* The `/messages` API fetches the `startTime`, `endTime` and text for all of the messages
* A calculation of time difference from the messages startTime and endTime is created vis-a-vis the conversation's `startTime`. 

Here is what you get: As a user you convert Symbl.ai's conversation data into the SRT file format..
