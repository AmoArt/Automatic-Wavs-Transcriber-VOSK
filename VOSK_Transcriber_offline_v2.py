
#How to use #Vosk -- the Offline Speech Recognition Library for Python
#https://www.youtube.com/watch?v=3Mga7_8bYpw

#how to load wav file
#https://towardsdatascience.com/transcribe-large-audio-files-offline-with-vosk-a77ee8f7aa28

#delate all the old text files when starting the programs
#https://www.tutorialspoint.com/How-to-delete-all-files-in-a-directory-with-Python

import os
import glob
import sys
import json
#from vosk import Model, KaldiRecognizer
from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio

import wave
import json

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import os, re, os.path

#directory to the model being used, at moment of writting this, im using the 'vosk-model-en-us-0.22'
#https://alphacephei.com/vosk/models
#swap it with other ones if you feel like it
#DO NOT FORGET TO EDIT THIS DIRECTORY TO YOURS MODEL!
#DO NOT FORGET TO EDIT THIS DIRECTORY TO YOURS MODEL!
#DO NOT FORGET TO EDIT THIS DIRECTORY TO YOURS MODEL!
#DO NOT FORGET TO EDIT THIS DIRECTORY TO YOURS MODEL!
#DO NOT FORGET TO EDIT THIS DIRECTORY TO YOURS MODEL!
theModelDir = (r"R:\_ppp\pyTranscriber\VOSK_Transcriber_offline\vosk-model-en-us-0.22")







#master string for the master transcription export
masterTEXT = ''


def nukeOldFiles():
    mypath = "_transcriptMaster"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))
    
    mypath = "_transcriptInvidual"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

print('wait around 30 seconds for model to load')
#Im assuming you are using a mono WAV file with rate of 22050, change this number to fit your needs
audioFrameHz = 22050
model = Model(theModelDir, model_name=None, lang=None)

def transcriberLoop(whereX, whatY):
    dirCombo = whereX + "\\" + whatY
    #print('transcribe this\n' + dirCombo)

    wav_file = dirCombo
    
    wf = wave.open(wav_file, "rb")
#    #Im assuming you are using a mono WAV file with rate of 22050, change this number to fit your needs
#    audioFrameHz = 22050
#    model = Model(theModelDir, model_name=None, lang=None)

    rec = KaldiRecognizer(model, wf.getframerate())

    transcription = []
    #loop for listing to cheack if wav is correct, and than than extracting the trancript from wav and extracting just plain text resoult from that.
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # Convert json output to dict
            result_dict = json.loads(rec.Result())
            # Extract text values and append them to transcription list
            transcription.append(result_dict.get("text", ""))
    #post processing the resoult into plain text
    final_result = json.loads(rec.FinalResult())
    transcription.append(final_result.get("text", ""))

    transcription_text = ' '.join(transcription)
    #print file transcription to user (can coment this bit out, it just to for me to see how fast it works)
#    print('\n' + transcription_text)

    tmpTranscript = str(transcription_text)

    with open('_transcriptInvidual/' + (whatY[0:-4]) + '.txt', 'a') as f:
        f.write(tmpTranscript)
        f.close()


    #conver above for aster transcript list
#wavs/00_00_00_Nameless_Neutral__I got the rum from Skip. But he gave me no more than two bottles.wav|I got the rum from Skip. But he gave me no more than two bottles.;

    masterTEXT = """wavs/""" + whatY + "|" + tmpTranscript + ";"

    print(masterTEXT)

    masterTEXTcollection = tmpTranscript
    
    with open('_transcriptMaster/_transcriptTraning.txt', 'a') as f:
        f.write('\n' + masterTEXT)
        f.close()







#Start first print, info
print('make sure you read thru the README file before starting this script')
print('\npaste directory of your mono WAVS files, than press enter (also remeber to correct the Model directory for transcription model)\n')
#input directory for your vav files
strInput = str(input())
#take ddirectory, only look for wav files
wavPath = strInput + r'/*.wav'
#make list, by taking the whole list of wav files, look for file names only for the amount of files in detected
names = [os.path.basename(x) for x in glob.glob(wavPath)]

#remove all old files before starting making new ones, keep in mind that and copy/move all the files you need to move first
nukeOldFiles()

#first loop,
for iNames in range(0, len(names)):
    #print("\n" + names[iNames])



    tmpFileName = names[iNames]

    #pass the location of wavs and the wav file name to get processed by the transcriber
    transcriberLoop(strInput, tmpFileName)

    
    #print(str(len(names)))
    #print(str(iNames))
    #wait until the amount of files is same as amont of objects in the list to print last message
    if (iNames == (len(names)-1)):

        
        #one last edit to remove the empty line from the start of the master trinscribe txt file
        with open('_transcriptMaster/_transcriptTraning.txt') as reader, open('_transcriptMaster/_transcriptTraning.txt', 'r+') as writer:
          for line in reader:
            if line.strip():
              writer.write(line)
          writer.truncate()
          writer.close()

        
        print("\n\n* * *\n\nTranscriptions is done\n")
        print('remeber, the script do not add any puncuations in middle or at end of the transcribe text so\n')
        print("double check the quality of it in the transcript folder, and add those when needed\n\n* * *")





































































