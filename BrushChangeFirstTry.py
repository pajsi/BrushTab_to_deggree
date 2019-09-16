import os
import sys
import PySimpleGUI as sg
import re

def BrushTab_to_deg(dir_path, procent1, procent2):


    x = 'PaintFlow1='
    w = 'ShapingAir1='
    ProcesseBrushes = []


    for filename in os.listdir(dir_path):
        if filename.startswith("brushtab"):

            print(filename)

            ProcesseBrushes.append(filename)

            with open(dir_path + '\\' + filename, 'r') as f:
                lines = f.readlines()

            with open(dir_path + '\\' + filename, 'w') as f:
                BrushCount = 1

                for [i, line] in enumerate(lines):
                    BrushName = '[Brush' + str(BrushCount) + ']'

                    while BrushName in line and BrushCount < 101:
                        if x in lines[i + 1]:

                            Paintline = lines[i + 1]
                            Flowline = lines[i + 2]

                            CurrentPaintValueList = re.findall('\d+', Paintline)
                            CurrentPaintValue = float(CurrentPaintValueList[1])

                            CurrentFlowValueList = re.findall('\d+', Flowline)
                            CurrentFlowValue = float(CurrentFlowValueList[1])

                            print(CurrentPaintValue)
                            #print(CurrentFlowValue)

                            if CurrentPaintValue != 0:
                                lines[i + 701] = x + str(round(CurrentPaintValue + procent1 * CurrentPaintValue * 0.01)) + "\n"
                                lines[i + 702] = w + str(round(CurrentFlowValue + procent2 * CurrentFlowValue * 0.01)) + "\n"
                                lines[i + 703] = lines[i + 3]
                                lines[i + 704] = lines[i + 4]
                                lines[i + 705] = lines[i + 5]
                                lines[i + 706] = lines[i + 6]
                                BrushCount = BrushCount + 1
                            else:
                                BrushCount = BrushCount + 1
                f.truncate(0)
                f.seek(0)
                f.writelines(lines)
        else:
            continue
    return ProcesseBrushes

layout = [[sg.Text('This porgram is for making brushes for degree mode. It copies brushes: 1 -> 101, 2 -> 102, ...', size=(80, 1), auto_size_text=False, justification='center', font=("Helvetica", 10), text_color='blue')],
            [sg.Text('_' * 80)],
            [sg.Text(' ' * 80)],
            [sg.Text('Select Folder with brushes you want to change!', justification='center')],
            [sg.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Source'),
            sg.FolderBrowse()],
            [sg.Text('_' * 80)],
            [sg.Text(' ' * 80)],
            [sg.Text(' ' * 80)],
            [sg.Text('Procentage increase of Paint flow')],
            [sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
            [sg.Text(' ' * 80)],
            [sg.Text('Procentage increase of Shaping air')],
            [sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
            [sg.Submit(), sg.Cancel()]]

event, values = sg.Window('Brush Changer', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()

sg.Popup('list of changed brushes',
         BrushTab_to_deg(values[0],values[1],values[2]))
