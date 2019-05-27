======
pyttsx
======

Cross-platform Python wrapper for text-to-speech synthesis


Help Wanted
===========

RapidWareTech say.: As you can probably tell, I have not had time or in some cases the resources (e.g., specific versions of OSes) to maintain pyttsx very well for some time now. If you are using pyttsx in your day to day work and would like to take over as maintainer of the project, please let me know.

Rick Sanchez say.: No problem man, i work for expend tech.


Quickstart
==========

::

   import pyttsx
   engine = pyttsx.init()
   engine.say('Greetings!')
   engine.say('How are you today?')
   engine.runAndWait()

See http://pyttsx.readthedocs.org/ for documentation of the full API.

Included drivers
================

* nsss - NSSpeechSynthesizer on Mac OS X 10.5 and higher
* sapi5 - SAPI5 on Windows XP, Windows Vista, and (untested) Windows 7
* espeak - eSpeak on any distro / platform that can host the shared library (e.g., Ubuntu / Fedora Linux)

Contributing drivers
====================

Email the author if you have wrapped or are interested in wrapping another text-to-speech engine for use with pyttsx.

Project links
=============

* Python Package Index for downloads (http://pypi.python.org/pyttsx)
* GitHub site for source, bugs, and q&a (https://github.com/parente/pyttsx)
* ReadTheDocs for docs (http://pyttsx.readthedocs.org)

See Also
========

https://github.com/parente/espeakbox - espeak in a 16.5 MB Docker container with a simple REST API

License
=======

Copyright (c) 2009, 2013 Peter Parente
All rights reserved.

http://creativecommons.org/licenses/BSD/


Voices
=======

id: com.apple.speech.synthesis.voice.Alex - gender: VoiceGenderMale - age: 35 - languages: [u'en-US'] - name: Alex

id: com.apple.speech.synthesis.voice.alice - gender: VoiceGenderFemale - age: 35 - languages: [u'it-IT'] - name: Alice

id: com.apple.speech.synthesis.voice.alva - gender: VoiceGenderFemale - age: 35 - languages: [u'sv-SE'] - name: Alva

id: com.apple.speech.synthesis.voice.amelie - gender: VoiceGenderFemale - age: 35 - languages: [u'fr-CA'] - name: Amelie

id: com.apple.speech.synthesis.voice.anna - gender: VoiceGenderFemale - age: 35 - languages: [u'de-DE'] - name: Anna

id: com.apple.speech.synthesis.voice.carmit - gender: VoiceGenderFemale - age: 35 - languages: [u'he-IL'] - name: Carmit

id: com.apple.speech.synthesis.voice.damayanti - gender: VoiceGenderFemale - age: 35 - languages: [u'id'] - name: Damayanti

id: com.apple.speech.synthesis.voice.daniel - gender: VoiceGenderMale - age: 35 - languages: [u'en-GB'] - name: Daniel

id: com.apple.speech.synthesis.voice.diego - gender: VoiceGenderMale - age: 35 - languages: [u'es-ES'] - name: Diego

id: com.apple.speech.synthesis.voice.ellen - gender: VoiceGenderFemale - age: 35 - languages: [u'nl-BE'] - name: Ellen

id: com.apple.speech.synthesis.voice.fiona - gender: VoiceGenderFemale - age: 35 - languages: [u'en-US'] - name: Fiona

id: com.apple.speech.synthesis.voice.Fred - gender: VoiceGenderMale - age: 30 - languages: [u'en-US'] - name: Fred

id: com.apple.speech.synthesis.voice.ioana - gender: VoiceGenderFemale - age: 35 - languages: [u'ro-RO'] - name: Ioana

id: com.apple.speech.synthesis.voice.joana - gender: VoiceGenderFemale - age: 35 - languages: [u'pt-PT'] - name: Joana

id: com.apple.speech.synthesis.voice.jorge - gender: VoiceGenderMale - age: 35 - languages: [u'es-ES'] - name: Jorge

id: com.apple.speech.synthesis.voice.juan - gender: VoiceGenderMale - age: 35 - languages: [u'es-419'] - name: Juan

id: com.apple.speech.synthesis.voice.kanya - gender: VoiceGenderFemale - age: 35 - languages: [u'th-TH'] - name: Kanya

id: com.apple.speech.synthesis.voice.karen - gender: VoiceGenderFemale - age: 35 - languages: [u'en-AU'] - name: Karen

id: com.apple.speech.synthesis.voice.kyoko - gender: VoiceGenderFemale - age: 35 - languages: [u'ja-JP'] - name: Kyoko

id: com.apple.speech.synthesis.voice.laura - gender: VoiceGenderFemale - age: 35 - languages: [u'sk-SK'] - name: Laura

id: com.apple.speech.synthesis.voice.lekha - gender: VoiceGenderFemale - age: 35 - languages: [u'hi-IN'] - name: Lekha

id: com.apple.speech.synthesis.voice.luca - gender: VoiceGenderMale - age: 35 - languages: [u'it-IT'] - name: Luca

id: com.apple.speech.synthesis.voice.luciana - gender: VoiceGenderFemale - age: 35 - languages: [u'pt-BR'] - name: Luciana

id: com.apple.speech.synthesis.voice.maged - gender: VoiceGenderMale - age: 35 - languages: [u'ar'] - name: Maged

id: com.apple.speech.synthesis.voice.mariska - gender: VoiceGenderFemale - age: 35 - languages: [u'hu-HU'] - name: Mariska

id: com.apple.speech.synthesis.voice.mei-jia - gender: VoiceGenderFemale - age: 35 - languages: [u'zh-Hant'] - name: Mei-Jia

id: com.apple.speech.synthesis.voice.melina - gender: VoiceGenderFemale - age: 35 - languages: [u'el-GR'] - name: Melina

id: com.apple.speech.synthesis.voice.milena - gender: VoiceGenderFemale - age: 35 - languages: [u'ru-RU'] - name: Milena

id: com.apple.speech.synthesis.voice.moira - gender: VoiceGenderFemale - age: 35 - languages: [u'en-IE'] - name: Moira

id: com.apple.speech.synthesis.voice.monica - gender: VoiceGenderFemale - age: 35 - languages: [u'es-ES'] - name: Monica

id: com.apple.speech.synthesis.voice.nora - gender: VoiceGenderFemale - age: 35 - languages: [u'nb-NO'] - name: Nora

id: com.apple.speech.synthesis.voice.paulina - gender: VoiceGenderFemale - age: 35 - languages: [u'es-419'] - name: Paulina

id: com.apple.speech.synthesis.voice.samantha - gender: VoiceGenderFemale - age: 35 - languages: [u'en-US'] - name: Samantha

id: com.apple.speech.synthesis.voice.sara - gender: VoiceGenderFemale - age: 35 - languages: [u'da-DK'] - name: Sara

id: com.apple.speech.synthesis.voice.satu - gender: VoiceGenderFemale - age: 35 - languages: [u'fi-FI'] - name: Satu

id: com.apple.speech.synthesis.voice.sin-ji - gender: VoiceGenderFemale - age: 35 - languages: [u'zh-Hant'] - name: Sin-ji

id: com.apple.speech.synthesis.voice.tessa - gender: VoiceGenderFemale - age: 35 - languages: [u'en-US'] - name: Tessa

id: com.apple.speech.synthesis.voice.thomas - gender: VoiceGenderMale - age: 35 - languages: [u'fr-FR'] - name: Thomas

id: com.apple.speech.synthesis.voice.ting-ting - gender: VoiceGenderFemale - age: 35 - languages: [u'zh-Hans'] - name: Ting-Ting

id: com.apple.speech.synthesis.voice.veena - gender: VoiceGenderFemale - age: 35 - languages: [u'en-US'] - name: Veena

id: com.apple.speech.synthesis.voice.Victoria - gender: VoiceGenderFemale - age: 35 - languages: [u'en-US'] - name: Victoria

id: com.apple.speech.synthesis.voice.xander - gender: VoiceGenderMale - age: 35 - languages: [u'nl-NL'] - name: Xander

id: com.apple.speech.synthesis.voice.yelda - gender: VoiceGenderFemale - age: 35 - languages: [u'tr-TR'] - name: Yelda

id: com.apple.speech.synthesis.voice.yuna - gender: VoiceGenderFemale - age: 35 - languages: [u'ko-KR'] - name: Yuna

id: com.apple.speech.synthesis.voice.yuri - gender: VoiceGenderMale - age: 35 - languages: [u'ru-RU'] - name: Yuri

id: com.apple.speech.synthesis.voice.zosia - gender: VoiceGenderFemale - age: 35 - languages: [u'pl-PL'] - name: Zosia

id: com.apple.speech.synthesis.voice.zuzana - gender: VoiceGenderFemale - age: 35 - languages: [u'cs-CZ'] - name: Zuzana


