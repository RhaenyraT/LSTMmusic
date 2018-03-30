#***********************************************************************************************************************
#                                                    SWARA PARINAMA  
# *********************************************************************************************************************** 
#                        Maintain   Varna(syllable)        Swara(accent)      Maatra(duration)     
#                                   Balam(time-duration)   Sama(even tone )   Santana(continuity)
#***********************************************************************************************************************

#  import MIDO music library

from mido import MidiFile, MidiTrack, Message
from mido import MetaMessage
import numpy as np
import mido
import csv
import glob
import time
np.set_printoptions(threshold=np.nan)

#***************************************************************************************************************************************************************
#       MIDI TO MATRICE ! 
#        GET PIANO ROLL
#***************************************************************************************************************************************************************

#  1)   Decide Sampling
Sampling=.01
time = float(0)
prev = float(0)

files_dir="C:/Users/Poori/Desktop/Parinama/MakePianoRoll/SmallDataSet/set13/"
train_files = glob.glob("%s*.mid" %(files_dir))

notes = []
Note_StartTime_Velocity=np.zeros((1,3))

#***********************************************************************************************************************
#   2)     FIND  [Note, StartTime, Velocity], Get Highest and Lowest Note

for file_dir in train_files:
    file_path = "%s" %(file_dir)
    mid = MidiFile(file_path)    
                  
    for msg in mid:
    	### this time is in seconds, not ticks
        time += msg.time

        if not msg.is_meta:
			### only interested in piano channel
            if msg.channel == 0:
                if msg.type == 'note_on':
                    #note in vector form to train on
                    note = msg.bytes() 
                    if not note[1]>88:
					# message is in the form of [type, note, velocity]
                        note = note[1:2]
                        note.append(time)  # [ note, total time, velocity]
                        note.append(msg.velocity)
                        note=np.array([note])                    
                        prev = time
                        Note_StartTime_Velocity=np.vstack((Note_StartTime_Velocity,note))    
    
#np.savetxt("C:/Users/Poori/Desktop/Parinama/MakePianoRoll/ExcelFiles/Note_timeElapsed_Velocity_alb.csv", Note_StartTime_Velocity, delimiter=",")
highNote=int(max(Note_StartTime_Velocity[1:,0]))
print(time)
print(highNote)
lowNote=int(min(Note_StartTime_Velocity[1:,0]))
print(lowNote)
TotalTime=int(Note_StartTime_Velocity[-1][1]//Sampling)
#print(000)
#***********************************************************************************************************************
#   3)    FIND   [ Note , StartTime , Length it was ON ]

Note_StartTime_Length = []
for i, message in enumerate(Note_StartTime_Velocity):
    if message[2] != 0: #if note type is 'note_on'
        start_time = int(message[1]/Sampling)
        for event in Note_StartTime_Velocity[i:]: 
            if event[0] == message[0] and event[2] == 0:
                length = int(event[1]/Sampling) - start_time
                break
                
        Note_StartTime_Length.append([int(message[0]), start_time, length])

#np.savetxt("C:/Users/Poori/Desktop/Parinama/MakePianoRoll/ExcelFiles/Note_StartTime_Length_alb.csv", Note_StartTime_Length, delimiter=",") 

#print(111)
#***********************************************************************************************************************
#   4)    FIND  PIANO ROLL !!

piano_roll = np.zeros((TotalTime, 88-22+1), dtype=np.float32)
for row in Note_StartTime_Length:
    piano_roll[row[1]:(row[1]+row[2]), row[0]-22] = 1
np.savetxt("C:/Users/Poori/Desktop/Parinama/MakePianoRoll/SmallDataSet/PianoRolls/piano_roll_set13.csv", piano_roll, delimiter=",") 

print(222)
#***************************************************************************************************************************************************************
