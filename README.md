# Prize Generator

# Introduction 

This project saw the development of a basic account and prize generator. It is made up of four individual services: A random 4 digit number generator, a random 4 letter generator, a service which concatenates the two and finally the flask application that displays this result. The purpose of this is to demonstrate the dockerization of a project split into microservices.

# Brief

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.   
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.   
- If a change is made to a code base, then Web hooks should be used so that Jenkins recreates and redeploys the changed application 
- The project must follow the Micro Services architecture that has been asked for. 
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project you need to create an Ansible Playbook that will provision the environment that your application needs to run.


# Application Diagram

This Diagram shows what the final product will look like. 

<img width="298" alt="APPDIAGRAM" src="https://user-images.githubusercontent.com/9552989/78503400-38b15b80-775e-11ea-9071-7e9f2f0e218a.PNG">



# Risk Assessment


<img width="752" alt="riskass" src="https://user-images.githubusercontent.com/9552989/78533158-6b039d00-77e0-11ea-9645-10b1c9c8403d.PNG">

# Sprint 1 Board

<img width="427" alt="SPRINT1" src="https://user-images.githubusercontent.com/9552989/78503453-90e85d80-775e-11ea-9440-0f1aef89f96f.PNG">



# Sprint 2 Board

<img width="437" alt="SPRINT2" src="https://user-images.githubusercontent.com/9552989/78503459-947be480-775e-11ea-8ee5-a4d4c0121356.PNG">



# Sprint 3 Board

<img width="478" alt="SPRINT3" src="https://user-images.githubusercontent.com/9552989/78503519-ff2d2000-775e-11ea-81ad-7f8551365575.PNG">

# Sprint 4 Board

This final sprint board shows that three tasks were not completed.  Creating a webpage for account tracking was only of Would priority and does not impact the final product significantly. Then the second database with prizes was of Could priority so similarly is not too impactful that it is not in the project. Finally we have creating the database service. This was of Must priority, I had the minimum viable product in mind and decided last minute due to difficulties with the database service to remove it from the project as I deemed it non essential.


<img width="487" alt="SPRINT4" src="https://user-images.githubusercontent.com/9552989/78503522-048a6a80-775f-11ea-95a9-9778fc8c575b.PNG">


# MoSCoW Priority

Below is a breakdown of the MoSCoW Priority I completed

<img width="205" alt="moscow" src="https://user-images.githubusercontent.com/9552989/78503549-2edc2800-775f-11ea-85d2-f29eb1b80414.PNG">


# Jenkins

I used a Jenkinsfile to create a CI pipeline job with Jenkins. 

<img width="387" alt="Jenkins" src="https://user-images.githubusercontent.com/9552989/78530266-3fca7f00-77db-11ea-9b39-5d656efcf136.PNG">

# Docker Swarm

Docker swarm allowed me to containerise and deploy the app across two VMs. A Master node and a Worker Node. Below is the output of the Swarm Stack.

<img width="811" alt="SWARM" src="https://user-images.githubusercontent.com/9552989/78530388-7607fe80-77db-11ea-8410-b78b3007486e.PNG">

<img width="810" alt="STACKDEPLOY" src="https://user-images.githubusercontent.com/9552989/78530405-7accb280-77db-11ea-97ad-88257042fef8.PNG">

# Ansible

I used ansible in order to automate the setting up of the environment for the app to be running on. 
It will configure 3 fresh VMs to have:
- Jenkins setup
- A docker manager node with a joined worker node
- Dependencies for environements

Future strecth would be to get a fourth VM with NGINX setup on it. 





# User Stories 

- As a User I would like to be able to generate account numbers
- As a User I would like to be able to access my account.
- As a Developer I would like to easily follow and edit code
- As a product owner I would like for any changes to be rolled out automatically with ease


# CI Pipeline

![CI Pipeline (2)](https://user-images.githubusercontent.com/9552989/78531293-14e12a80-77dd-11ea-96ff-8df58e0b271f.jpg)

# Tests

For this project I did not create any pytests due to the lack of complexity of the final system. During development however I did make use of Postman in order to test each service for responses while developing each section.

# Discussion

During this project I encountered a variety of problems that changed the final product. Firstly I did not expect the configuration of the Playbook.yaml to take as much time as it did. This cost me on the functionality of the app.

Working on this project in the future I would definitely create pytest's in order to test functionality of the system. Hopefully I will be able to add more end user functionality to the system to make it necessary.

The project did not have an ERD as there was no database. Taking the project forward I would work on creating a database service for the user to store accounts in and also generate a prize that is stored with their account number.
Discuss challenges
Discuss test results
Discuss planning


# Conclusion

Overall I would consider this project a success as it proves a useful conecpt of a working CI pipeline with fucntioning Version Control System and rolling updates. The application itself is not very useful, and the lack of tests is a draw back. However moving forward I would be working to develop these two further to create a better application. 
