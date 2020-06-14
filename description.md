# Submission name

Our solution is made by utilising IBM Cloud and Watson services, we are able to develop a system that uses machine learning to identify elderly in isolated situations and contact Community First Responders (CFRs) and SCDF First Responders during trauma or collapse cases through the myResponder application. Our code links a surveillance system to the wireless network and is able to contact emergency services through an automated messaging system when elderly exhibit signs of injury or distress.

[Project website](https://github.com/BlueTan/i-m-not-gonna-put-this-in-my-CV)

## Surveillance system
We used ESP32 and CAM Module to make up the surveillance system that takes images of a room at 5 second intervals. The ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth abilities. It is used to host a web server which then uploads the image data to the IBM Cloudant where it is stored for the image recognition model to process.

### IBM Cloudant
IBM Cloudant® is a distributed database that is optimized for handling heavy workloads that are typical of large, fast-growing web and mobile apps. Available as an SLA-backed, fully managed IBM Cloud™ service, Cloudant elastically scales throughput and storage independently. The image data is saved inside the IBM Cloudant database. 

### IBM Image Recognition using Watson Studio

When image is fed into Watson Studio from IBM Cloudant, it will process the image using a trained model, outputting a 



### IBM Cloud Functions (formerly Apache OpenWhisk)
IBM Cloud Functions is able to be executed a function within fractions of a second.

### Node Red



## Acknowledgments
