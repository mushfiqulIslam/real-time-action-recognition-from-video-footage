#!/usr/bin/python3
import random
import os
'''
    This script will save 3 files: train.txt, val.txt, test.txt.
    each file has the following format:
    --------------------------------------------------------------
    PathFileNameOfFile <Tab> ActionName
    ex:
        data/video/video_1	slap
        data/video/video_2	punch
        data/video/video_2	kick

	--------------------------------------------------------------
'''

LIST_OF_SLAP_DIR = ["/home/mushfiqul/Mushfiqul/CSE/Thesis2.0/Codes/Dataset_scale/slap/"]
LIST_OF_PUNCH_DIR = ["/home/mushfiqul/Mushfiqul/CSE/Thesis2.0/Codes/Dataset_scale/punch/"]
LIST_OF_KICK_DIR = ["/home/mushfiqul/Mushfiqul/CSE/Thesis2.0/Codes/Dataset_scale/kick/"]

VAL_SET_RATIO = 0.1
TEST_SET_RATIO = 0.4   # NUMBER_OF_TEST_SET = NUMBER_OF_TOTAL_DATA * TEST_SET_RATIO

PATH_TO_SAVE_SPLITED_DATASET = "/home/mushfiqul/Mushfiqul/CSE/Thesis2.0/Codes/data"

def AccumulateAllVideoFromDifferentDir(LIST_OF_DIR_THAT_CONTAINS_VIDEOS_):
    listOfPathToVideos = []
    for eachDir in LIST_OF_DIR_THAT_CONTAINS_VIDEOS_:
        listOfVideos = os.listdir(eachDir)
        for eachVideo in listOfVideos:
            listOfPathToVideos.append(eachDir + eachVideo)
    return listOfPathToVideos

def AppendLabelToEachData(LIST_OF_DATA_, action_):
    listOfDataWithLabel = []
    for eachData in LIST_OF_DATA_:
        eachData += "\t" + action_
        listOfDataWithLabel.append(eachData)
    return listOfDataWithLabel

def Split_Train_Val_Test_Data(LIST_OF_VIDEOS_):
    random.shuffle(LIST_OF_VIDEOS_)
    NUMBER_OF_TOTAL_DATA = len(LIST_OF_VIDEOS_)
    NUMBER_OF_TEST_VIDEOS = int(NUMBER_OF_TOTAL_DATA * TEST_SET_RATIO)
    NUMBER_OF_VAL_VIDEOS = int(NUMBER_OF_TOTAL_DATA * VAL_SET_RATIO)

    listOfTestVideos = LIST_OF_VIDEOS_[ : NUMBER_OF_TEST_VIDEOS]
    listOfValVideos = LIST_OF_VIDEOS_[NUMBER_OF_TEST_VIDEOS : (NUMBER_OF_TEST_VIDEOS+NUMBER_OF_VAL_VIDEOS)]
    listOfTrainVideos = LIST_OF_VIDEOS_[(NUMBER_OF_TEST_VIDEOS+NUMBER_OF_VAL_VIDEOS) : ]
    return listOfTrainVideos, listOfValVideos, listOfTestVideos

def WriteDataSetToFile(LIST_OF_DATA_, targetFileName_):
    with open(targetFileName_, 'w') as fileWriter:
        for eachData in LIST_OF_DATA_:
            fileWriter.write(eachData + "\n")

if __name__ == "__main__":
    #Preparing Dataset List
    #slap
    listofSlapVideos = AccumulateAllVideoFromDifferentDir(LIST_OF_SLAP_DIR)
    listOfSlapVideos = AppendLabelToEachData(listofSlapVideos, "slap")
    trainSlapVideos, valSlapVideos, testSlapVideos = Split_Train_Val_Test_Data(listOfSlapVideos)
    #punch
    listofPunchVideos = AccumulateAllVideoFromDifferentDir(LIST_OF_PUNCH_DIR)
    listofPunchVideos = AppendLabelToEachData(listofPunchVideos, "punch")
    trainPunchVideos, valPunchVideos, testPunchVideos = Split_Train_Val_Test_Data(listofPunchVideos)
    #kick
    listofKickVideos = AccumulateAllVideoFromDifferentDir(LIST_OF_KICK_DIR)
    listofKickVideos = AppendLabelToEachData(listofKickVideos, "kick")
    trainKickVideos, valKickVideos, testKickVideos = Split_Train_Val_Test_Data(listofKickVideos)

    #Preparing Dataset
    listOfTrainData = trainSlapVideos + trainPunchVideos + trainKickVideos
    random.shuffle(listOfTrainData)
    WriteDataSetToFile(listOfTrainData, os.path.join(PATH_TO_SAVE_SPLITED_DATASET, 'train.txt') )

    listOfValData = valSlapVideos + valPunchVideos + valKickVideos
    random.shuffle(listOfValData)
    WriteDataSetToFile(listOfValData, os.path.join(PATH_TO_SAVE_SPLITED_DATASET, 'val.txt') )

    listOfTestData = testSlapVideos + testPunchVideos + testKickVideos
    random.shuffle(listOfTestData)
    WriteDataSetToFile(listOfTestData, os.path.join(PATH_TO_SAVE_SPLITED_DATASET, 'test.txt') )
