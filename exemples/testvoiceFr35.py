#coding: utf-8

import pyttsx
engine = pyttsx.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 190)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', "com.apple.speech.synthesis.voice.thomas")   #changing index, changes voices. 1 for female

#for v in voices:#used for listing voices
#	print "id:",v.id,"- gender:",v.gender,"- age:",v.age,"- languages:",v.languages,"- name:",v.name


engine.say("Bonjour Rick!")
engine.say('Ratio de ' + str(rate))
engine.say("Entrainement des programmes en cours.")
engine.runAndWait()
engine.stop()
exit(0)

