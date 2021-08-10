# Symbl Devtool SRT format converter

Symbl's APIs empower developers to enable: 
- **Real-time** analysis of free-flowing discussions to automatically surface highly relevant summary discussion topics, contextual insights, suggestive action items, follow-ups, decisions, and questions.
- **Voice APIs** that makes it easy to add AI-powered conversation intelligence to either [telephony][telephony] or [WebSocket][websocket] interfaces.
- **Conversation APIs** that provide a REST interface for managing and processing your conversation data.
- **Summary UI** with a fully customizable and editable reference experience that indexes a searchable transcript and shows generated actionable insights, topics, timecodes, and speaker information.

<hr />


## Pre-requisites 
* Python
* Terminal


## Feature 
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

## Conclusion:
Here is a breakdown of what happens. 

* With the `converstionId` the script makes two API calls: `/conversations` and `/messages`
* The `/conversations` API fetches the initial `startTime`
* The `/messages` API fetches the `startTime`, `endTime` and text for all of the messages
* A calculation of time difference from the messages startTime and endTime is created vis-a-vis the conversation's `startTime`. 

Here is what you get: As a user you convert Symbl.ai's conversation data into the SRT file format..

## Community

If you have any questions, feel free to reach out to us at devrelations@symbl.ai or through our [Community Slack][slack] or our [forum][developer_community].

This guide is actively developed, and we love to hear from you! Please feel free to [create an issue][issues] or [open a pull request][pulls] with your questions, comments, suggestions and feedback.  If you liked our integration guide, please star our repo!

This library is released under the [Apache License][license]

[license]: LICENSE.txt
[telephony]: https://docs.symbl.ai/docs/telephony/overview/post-api
[websocket]: https://docs.symbl.ai/docs/streamingapi/overview/introduction
[developer_community]: https://community.symbl.ai/?_ga=2.134156042.526040298.1609788827-1505817196.1609788827
[slack]: https://join.slack.com/t/symbldotai/shared_invite/zt-4sic2s11-D3x496pll8UHSJ89cm78CA
[signup]: https://platform.symbl.ai/?_ga=2.63499307.526040298.1609788827-1505817196.1609788827
[issues]: https://github.com/symblai/symbl-devtool-SRT-format-converter/issues
[pulls]: https://github.com/symblai/symbl-devtool-SRT-format-converter/pulls
