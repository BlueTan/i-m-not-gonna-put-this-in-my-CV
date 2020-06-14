# Submission name

Our solution is made by utilising IBM Cloud and Watson services, we are able to develop a system that uses machine learning to identify elderly in isolated situations and contact Community First Responders (CFRs) and SCDF First Responders during trauma or collapse cases through the myResponder application. Our code links a surveillance system to the wireless network and is able to contact emergency services through an automated messaging system when elderly exhibit signs of injury or distress.

[Project website](https://github.com/BlueTan/i-m-not-gonna-put-this-in-my-CV)

## Surveillance system
We used ESP32 and CAM Module to make up the surveillance system that takes images of a room at 5 second intervals. The ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth abilities. It is is used to 


The system uploads the image data to the IBM Cloudant.

### IBM Cloudant
IBM Cloudant® is a distributed database that is optimized for handling heavy workloads that are typical of large, fast-growing web and mobile apps. Available as an SLA-backed, fully managed IBM Cloud™ service, Cloudant elastically scales throughput and storage independently. The image data is saved inside the IBM Cloudant is easily accessible within a short span of time from anywhere around the world. This is especially helpful for our project as time is of the essence for emergency medical services. The images uploaded into IBM Cloudant from our surveillance system is then sent to IBM Image Recognition to identify if elderly is injured or not.

### IBM Image Recognition
By utilising the Watson Machine Learning inside IBM Image Recognition services, we use it to determine if elderly has been immobile for 2 minutes. If he/she has been lying on the floor for 75% of the time (1 minute 30 seconds) and has not stood up, the data will be sent over to IBM Cloud Functions and Apache OpwnWhisk.

### IBM Cloud Functions and Apache OpenWhisk

### Node Red



## Acknowledgments
