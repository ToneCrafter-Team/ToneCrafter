<h1 align=left><img src="ToneCrafter_logo.png" width="60">&emsp;ToneCrafter</h1>

ToneCrafter is a project developped by students at [ENSEA](https://www.ensea.fr/).  
Our goal is to develop an algorithm capable of analyzing any audio file containing guitar sounds and retrieve its parameters. ToneCrafter will then generate a numeric filter that will modulate your guitar sound and make it sound like the recording you fed it. Exciting isn't it ?  
We are also working on a hardware implementation using a STM32 µC that will allow musicians to use ToneCrafter on stage and tune the different parameters.

- [Our work so far](#our-work-so-far)
  * [Software :](#software--)
  * [Hardware :](#hardware--)
- [How to use ToneCrafter](#how-to-use-tonecrafter)
  * [Installing Anaconda and TensorFlow](#installing-anaconda-and-tensorflow)
  * [Dataset](#dataset)
  * [Useful links](#useful-links)
- [What's next ?](#what-s-next--)

## Our work so far
### Software :
We started out trying to use Magenta's [DDSP](https://www.github.com/magenta/ddsp), but this was a bit too ambitious for AI newbies like us, so we tried implementing our own algorithms.  
This sparked three different approaches to our problem:  
  * A CNN based approach where we tried to teach a neural network to recreate a distortion.
  * A "bare coding" approach using math and clever algorithms to recreate a distortion from an audio file
  * A VAE based approach trying to recreate the mechanisms behind Magenta's DDSP

### Hardware :
We started working on different PCB designs using [Eagle](https://www.autodesk.com/products/eagle/overview) and working on a STM32F7 discovery kit for testing purposes.

## How to use ToneCrafter
### Installing Anaconda and TensorFlow
To begin with, if you want to work locally and not on Colabs as we did, you will have to install Anaconda.
To do this, go to: https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/  
And follow the instructions that are given to you.


Then, if you want to have fun on the models created by the Google team with the Magenta project, follow the installation guide on their GitHub: https://github.com/magenta/magenta


### Dataset
To train our CNN, we searched for a dataset containing clean audio from a guitar and different distortions. As we could not find any we had to create our own. We recorded a guitar for 1 minute and added various levels of distortion. To increase the size of our base, we applied an EQ filter with various settings.  
We ended up with a lot of .wav files that you can find [here](https://github.com/ToneCrafter-Team/ToneCrafter/tree/main/Software/CNN%20Models/Dataset).  
In order to train our CNN, we splitted our files in 200ms chunks using our [Preparing Data Notebook](https://github.com/ToneCrafter-Team/ToneCrafter/blob/main/Software/CNN%20Models/Preparing_Data.ipynb)  
We then organised our files in the following way :  

- X_train :  
  * Clean  
  * Clean_TrebbleBoost  
  * Clean_BassBoost  
  * Clean_BassCut  

- y_train :
  * Disto  
  * Disto_TrebbleBoost  
  * Disto_BassBoost  
  * Disto_BassCut  

- Validation data :
  * Clean_TrebbleCut as X_valid  
  * Disto_TrebbleCut as y_valid  
We are concious that this dataset is far from perfect (please don't listen to it, the guitar playing is awful) from a recording standpoint and the way we splitted our audio might cause some problems.

For the maths oriented approach, we used the excellent [IDMT-SMT-Audio_Effects Dataset](https://www.idmt.fraunhofer.de/en/business_units/m2d/smt/audio_effects.html), which enabled us to link each note played to it's distorted counterpart.  
### Useful links

## What's next ?
We are trying to figure out how to convert our DDSP output into a numeric filter in order to begin training our model. In the mean time, we will try to implement a simple filter on our STM32F7 and feed it a guitar input to test the viability of our project.

Enjoy!
