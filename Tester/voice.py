import os
import wave

AUDIO_PATH = './static/audio/'
AUDIO_PATH_FRAGMENT = './static/audio/fragment/'

def GenerarionTextToVoice(vtext):
    #1 find audio
    err = checkAudio(vtext)
    if err:
        vtext = vtext.replace(' ', '_', -1)
        return vtext + '.wav'

    #2 find fragment
    vt = vtext.split()
    
    for word in vt:
        err = checkFragment(word)
        if err != None:
            return 'alert.wav'
    
    #3 merge
    nameAudio = vtext.replace(' ', '_', -1)
    err = mergeAudioFragment(nameAudio, vtext)
    
    if err != None:
        return 'alert.wav'
    
    return nameAudio + '.wav'
    
def checkAudio(vtext):
    t = vtext.replace(' ', '_', -1)
    err = os.path.exists(AUDIO_PATH + t + '.wav')
    return err

def checkFragment(word):
    err = os.path.exists(AUDIO_PATH_FRAGMENT + word + '.wav')
    if err:
        err = downloadFragment(word)
        if err != None:
            return err
    return None    

def mergeAudioFragment(nameAudio, vtext):
    vt = vtext.split()
    inputFiles = []
    
    for fr in vt:
        inputFiles.append(AUDIO_PATH_FRAGMENT + fr + '.wav')
    
    outputFile = AUDIO_PATH + nameAudio + '.wav'
    err = mergeWAVFiles(inputFiles, outputFile)
    if err != None:
        return err
    return None

def downloadFragment(voice):
    pass
    
def mergeWAVFiles(inputFiles, outputFile):
    new = open(outputFile, 'w')
    new.close()
    merged = wave.open('./static/audio' + outputFile, mode='w')
    
    for filename in inputFiles:
        fr = wave.open(filename, mode='r')
        params= fr.getparams() 
        #(cannals, BytePerSample, framerate, frames, comptype, compname)
        allFrames += params[3]
        content += fr.readframes(params[3])
        fr.close()
        newParams = (params[0], params[1], params[2], allFrames, params[4], params[5])
    merged.setparams(newParams)
    merged.writeframesraw(content)
    merged.close()
    