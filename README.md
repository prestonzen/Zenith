<H1 align="center">
    Zénith V1.0 ☯
</H1>

Zénith is a cybersecurity AI NLP chatbot that references the MITRE ATT&CK Framework. Zénith sources information from open-source intelligence platforms to relay situationally relevant intelligence and achieve cyber objectives through automated processes. </br>

<H2 align="center">
	Disclaimer ‼
</H1>

Zénith is for educational & simulation purposes only. I am not responsible for any illicit activities performed as a result of utilizing Zénith's capabilities. </br>

<H1 align="center">
    Quickstart Usage ⚡
</H1>

<H2 align="center">
    Windows 🪟 
</H2>

install the linux sub-system </br>
install node.js (NPM is included) https://nodejs.org/en/download/ </br>
install latest NET framework (https://dotnet.microsoft.com/download/dotnet-framework) </br>
install docker desktop https://www.docker.com/products/docker-desktop </br>
extract Zénith-master </br>
```cd Zénith-master```</br> (Move into Zénith's directory where you can see .botfront) </br>
Open up powershell as an administrator </br>
Change the Execution policy to allow remote signed scripts: ```Set-ExecutionPolicy RemoteSigned``` </br>
```npm install -g npm``` </br>
```npm install -g botfront``` </br>
restart computer & Boot up to BIOS and confirm/enable SVM virtualization settings </br>
Install the wsl kernel https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package </br>
Confirm that WSL for Docker is installed correctly </br>
open up docker-desktop as an admin (You may need to log out of windows for docker-users to take affect) </br>
Move to a location where you want to make the project folder </br>
```botfront init``` </br>
Create a new project folder per the prompt
cd C:</br>Users</br>NAME</br>Desktop</br>Zénith</br>botfront</br>cli && npm link</br>
This binds botfront to the npm node-modules </br>
```botfront up``` </br>
Docker containers will download then start botfront
Open a browser and navigate to localhost:8888 </br>

For running custom docker-compose.yml files
```docker-compose up```


##Linux 🐧 </br>
```sudo apt-get install docker-ce```</br>
```sudo apt install nodejs npm```</br>
```sudo npm install -g botfront```</br>

##Mac 🍎 </br>
Currently Untested </br>

##Actions Enviornment Prep </br>

Dependencies: </br>
requests
SpeechRecognition
PyAudio
pandas
beautifulsoup4
scipy == 1.4.1
Numpy == 1.16.0

##Planned Features </br>
Social Engineering Module Expansion for Computer Vision Micro Expression Analysis: https://github.com/JostineHo/mememoji </br>
Voice Functionality to Talk to and receive voice responses from Zénith using Rasa's voice module: https://github.com/RasaHQ/rasa-voice-interface | https://www.youtube.com/watch?v=vX7IkUHU8m4&list=PLtFHvora00y-LU27sZGzzpHSNSpR1pUCW </br>


#Features
##Open Bullet 2
##Social Fish
Username: root
Password: zenith
#Donate 💸 </br>
I haven't completely decided on a monetization structure yet so to delay that my donation links are below: </br>
BTC: ```bc1qlnvj4r90ga5ntw0j7mvjtdt2uwa8hcyz5flvny``` </br>
ETH: ```0x0aDDf7b7915bbe5B8da1777565e20C6972dD9927``` </br>
LTC: ```ltc1qq9aqyy8wyjqnyh2y6ygn7curqxvu226cvmhp9c``` </br>
XMR: ```46HekyoxQACdipGjGPTDVE6Doppe7iYSrTMHoNLzrnXuHuP9feFS8DxckWtH9MjjjqGvSeVAFq9QxM6n3wMqVWXzJJLy4EU``` </br>
Paypal: ```https://paypal.me/prestonzen``` </br>
Venmo: ```@prestonzen``` </br>
Cashapp: ```$prestonzen``` </br>
