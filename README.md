# TempTracker
A weather tracker for gardeners and general home diagnostics.

<img width="590" height="332" alt="Adobe Express - Video Project" src="https://github.com/user-attachments/assets/c00cd38f-c30b-46a0-b4bc-3c9350df2d61" />


**[Try now with this link]() (Work In Progress)**

## Features
- [x] Dynamic background 
- [ ] Next and Previous 3 days average temperatures
- [x] Database for storing previous data
- [ ]  Diagnostics collecting station 


## How it works
The entire Backend and Website both run on a proxmox virtual machine usign ubuntu server.
The **backend** uses FastAPI and interacts with an ESP32 which sends data using JSON which is then processed and requested on the 
**frontend** which uses javascript and fetch to handle the backgrounds and presentation of data.
Pyhon interacts with the mySQL, which was chosen for its ease of use and reliability, to select and store data which is then passed to fastAPI to handle the transfers  


