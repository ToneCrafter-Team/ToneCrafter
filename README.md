<h1 align=left><img src="ToneCrafter_logo.png" width="60">&emsp;ToneCrafter</h1>

ToneCrafter is a project developped by students at [ENSEA](https://www.ensea.fr/).  
Our goal is to develop an algorithm capable of analyzing any audio file containing guitar sounds and retrieve its parameters. ToneCrafter will then generate a numeric filter that will modulate your guitar sound and make it sound like the recording you fed it. Exciting isn't it ?  
We are also working on a hardware implementation using a STM32 µC that will allow musicians to use ToneCrafter on stage and tune the different parameters.
## Our work so far 
### Software :
We are currently using magenta's [DDSP](https://www.github.com/magenta/ddsp) library on a conda installation with Python 3.8, and are currently able to create simple filters such as a reverb, delay, flanger, chorus, vibrato, and soon a distortion !
### Hardware :
We started working on different PCB designs using [Eagle](https://www.autodesk.com/products/eagle/overview) and working on a STM32F7 discovery kit for testing purposes.
## What's next ?
We are trying to figure out how to convert our DDSP output into a numeric filter in order to begin training our model. In the mean time, we will try to implement a simple filter on our STM32F7 and feed it a guitar input to test the viability of our project.

Enjoy!
