# Submission name

Our solution is made by utilising IBM Cloud and Watson services, we are able to develop a system that uses machine learning to identify elderly in isolated situations and contact Community First Responders (CFRs) and SCDF First Responders during trauma or collapse cases through the myResponder application. Our code links a surveillance system to the wireless network and is able to contact emergency services through an automated messaging system when elderly exhibit signs of injury or distress.

[Project website](https://github.com/BlueTan/i-m-not-gonna-put-this-in-my-CV)

## Surveillance system
We used ESP32 and CAM Module to make up the surveillance system that takes images of a room at 5 second intervals. The ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth abilities. It is used to host a web server which then uploads the image data to the IBM Cloudant where it is stored for the image recognition model to process. With integrated Wi-Fi and dual-mode Bluetooth abilities, we are able to send an output towards IBM Cloudant.

### IBM Cloudant
IBM Cloudant® is a distributed database that is optimized for handling heavy workloads that are typical of large, fast-growing web and mobile apps. Available as an SLA-backed, fully managed IBM Cloud™ service, Cloudant elastically scales throughput and storage independently. IBM Cloudant helps us to store image data inside their database and forward it towards the image recognition services to help us analyse them.

### IBM Image Recognition using Watson Studio
IBM Image Recognition Watson services is able to analyse and classify images using our previous inputs (images of elderly injured, having cardiac arrest etc). The deep learning algorithm will be able to identify our newer inputs when our product is put into action to determine if it fits scenario that is given. If elderly is shown to be injured, the output will go towards IBM Cloud Functions so that the system will be able to send output towards myResponders which will eventually contact both Community First Responders (CFRs) and SCDF (Singapore Civil Defense Force).

### IBM Cloud Functions (based on Apache OpenWhisk)
Based on Apache OpenWhisk, IBM Cloud Functions is a polyglot functions-as-a-service (FaaS) programming platform for developing lightweight code that scalably executes on demand. IBM Cloud Functions is able to be executed a function within fractions of a second, in our solution, the function that is executed is to send data towards myResponders to nearby CFRs (elderly's address and time of incident) and SCDF First Responders (elderly's personal information and medical history if possible).

### Node Red
Node-RED is a programming tool for wiring together hardware devices, APIs and online services in new and interesting ways. It provides a browser-based editor that makes it easy to wire together flows using the wide range of nodes in the palette that can be deployed to its runtime in a single-click.



## Acknowledgments
