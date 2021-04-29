import requests
import os
from os.path import join, dirname
from datetime import datetime

appId = "Your appId"
appSecret = "Your appSecret"
conversationID = "Your conversationId"

def getAuthKey():
    headers = {'content-type': 'application/json'}

    json_data = {
        "appId": appId,
        "appSecret": appSecret,
        "type": "application"}

    res1 = requests.post("https://api.symbl.ai/oauth2/token:generate", headers=headers, json=json_data)
    key_json = res1.json()
    #print(key_json)
    key = key_json["accessToken"]
    return key

def getConversationStart(conversationId, key):
    headers = {'content-type': 'application/json', 'x-api-key': key}
    url = "https://api.symbl.ai/v1/conversations/{0}".format(conversationId)
    res1 = requests.get(url, headers=headers, verify=True)
    job_complition = res1.json()
    #print(job_complition)
    return job_complition["startTime"]

def timeStampCornerCase(timeStampString):
    #Corner case of returned timestamp string
    
    timeStampList = timeStampString.replace('.',':').split(':')
    timeStampLen = len(timeStampList)
    
    if timeStampLen == 4:
        timeStampStringNew = '0' + timeStampList[0] +':'+ timeStampList[1] +':'+ timeStampList[2] +'.'+ timeStampList[3][0:-3]
    elif timeStampLen == 3:
        timeStampStringNew = '0' + timeStampList[0] +':'+ timeStampList[1] +':'+ timeStampList[2] +'.000'
    elif timeStampLen == 2:
        timeStampStringNew = '0' + timeStampList[0] +':'+ timeStampList[1] +':00.000'
    elif timeStampLen == 1:
        timeStampStringNew = '0' + timeStampList[0] +':'+ '00:00.000'
    return timeStampStringNew

def convertToSRT(input_dict,startPoint):
    df_list = []
    format_string ='%Y-%m-%dT%H:%M:%S.%fZ'
    startPointDT = datetime.strptime(startPoint, format_string)
    index = 0
    outputFile = open("output.srt", "w")
    for values in input_dict["messages"]:
        text = values['text']
        startTime = values['startTime']
        endTime = values['endTime']
        startDateTime = datetime.strptime(startTime, format_string)
        endDateTime = datetime.strptime(endTime, format_string)
        startDiff = str(startDateTime - startPointDT)
        endDiff = str(endDateTime - startPointDT)
        startDiffNew = timeStampCornerCase(startDiff)
        endDiffNew = timeStampCornerCase(endDiff)    
        
        startEndSRT = startDiffNew + " --> " + endDiffNew
        outputFile.write('\n{}\n{}\n{}\n\n'.format(str(index), startEndSRT, text))
        index+=1
    outputFile.close()
    return

def checkMessages(conversationId, key):
    headers = {'content-type': 'application/json', 'x-api-key': key}
    url = "https://api.symbl.ai/v1/conversations/{0}/messages".format(conversationId)
    res1 = requests.get(url, headers=headers, verify=True)
    job_complition = res1.json()
    #print(job_complition)
    startPoint = getConversationStart(conversationId, key)
    convertToSRT(job_complition,startPoint)
    return



def main(conversationID):
    key_auth =getAuthKey()
    checkMessages(conversationID,key_auth)

main(conversationID)
