# Automatic-Wavs-Transcriber-VOSK
Codedump for the script designed to use VOSK to transcribe the wav dataset files offline on CPU

to use it start by creaing two empty folders "_transcriptInvidual" and "_transcriptMaster".

unzip 'vosk-model-en-us-0.22' and edit the main pythin file to add the directory to it e.g.
theModelDir = (r"C:\PYTHON_CODE\Automatic-Wavs-Transcriber-VOSK-main\vosk-model-en-us-0.22")


install modules "vosk" and "pyaudio", 

than start the main script and paste the fold directory of WAVs in main terminal when prompted.

///////////////////////////////////////////////////////////////////////////////////////////////


from README.txt :

INFO: This is a 100% offline transcriber for when you have a whole pile of already 
seperated mono wav files in 1 second to 10 second format. 
This script will need at least 4GB of your RAM to run.
After runing this script, pass the directory of your wav files
e.g. "D:\Project_Files\character\wavs\n"
when successful, you will get text transcript in two folders:

"_transcriptMaster" : one file, contains ALL wav files in prepared in the standard training
format, waiting for you to seperate them into their own 'Validation' and 'Training' files

"_transcriptInvidual" : invidual files, in format of the orginal transcript PPP system, 
text file named same as wav, containg the transcription of the audio.


PREPERATIONS:


Zero, you will need to download "vosk-model-en-us-0.22" transcript model from below link 
and edit the line for it in the 'VOSK_Transcriber_offline' 
to the directory of where it's saved on your PC
https://alphacephei.com/vosk/models

First, this is a Python script (written in 3.7), it uses additional modules 
so you will need to install those two modules 
(maybe more if the cmd will shout at you for missing modules)

pip install vosk

pip install pyaudio



Secondly, before runing the code, make sure that whatever files in '_transcriptInvidual' 
and '_transcriptMaster' have been copied to desired location as this script will 
automatially remove anything inside of those two when running new project

Fourth, make sure your wavs are saved in mono, 
and that sample rate of the files is written in the scrip 'audioFrameHz' portion.

Fifth, the process is bit slow, it may takes 30 seconds per single file transcription and
I do not have any query system so it all needs to be done in one go (or you can seperate
the boundles of audio files into smaller groups in their folder and move them back together
once you are done transcribing them in batches)


Finally, the transcipt do NOT adds any puncuation, so you will have to re-listing to all the
audio clips and add all the necessary fullstops, commas, question marks and exclamation marks to create a functioning audio dataset.
Yes, this is pretty slow process but its faster than doing it by hand, also the transcript
is not perfect so you will need to correct minor mistakes anyway when they happen for
better quality training files.
