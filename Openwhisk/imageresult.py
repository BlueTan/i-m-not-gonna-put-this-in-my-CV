#!/usr/bin/env python
# coding: utf-8

# In[8]:


from ibm_watson import VisualRecognitionV4
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from ibm_watson.visual_recognition_v4 import AnalyzeEnums, FileWithMetadata
import details

"""Authentication step with IBM"""

authenticator = IAMAuthenticator('{your_api_key}')
visual_recognition = VisualRecognitionV4(
    version='2020/06/14',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/ff7b2df2-cfd1-47a5-9bce-778b0661850f')

"""Using IBM Watson Studio to classify image and determine if there is injury"""


"""Threshold set to low since it's safer to assume"""

with open('./frame.jpg', 'rb') as images_file:
    result = visual_recognition.analyze(
        collection_ids=["{collection_id}"],
        features=[AnalyzeEnums.Features.OBJECTS.value]
        images_file=[FileWithMetadata(images_file)],
        threshold='0.5',
        ).get_result()

result_dict=json.loads(result)


# In[ ]:





# In[ ]:


"""Getting only the first image result"""

resultsdict= jsondict["images"][0]['objects']['collections'][0]['objects'][0]


# In[ ]:


#set confidence level to raise alarm
alert_threshold=0.75 


if (resultsdict['object']=='falling') and(resultsdict['score']>alert_threshold):
    details.send_details()
    #send location details

