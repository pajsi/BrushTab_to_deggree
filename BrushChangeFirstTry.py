                            CurrentPaintValueList = re.findall('\d+', Paintline)
                            CurrentPaintValue = float(CurrentPaintValueList[1])
                            CurrentFlowValueList = re.findall('\d+', Flowline)
                            CurrentFlowValue = float(CurrentFlowValueList[1])
                                lines[i + 701] = x + str(round(CurrentPaintValue + procent1 * CurrentPaintValue * 0.01)) + "\n"
                                lines[i + 702] = w + str(round(CurrentFlowValue + procent2 * CurrentFlowValue * 0.01)) + "\n"
