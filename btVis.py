import plotly.express as px
import pandas as pd
import lib

def graphDisplay(type, df, x, y, title, text):
    if type == 'bar':
        fig = px.bar(df, x = x, y = y, title = title, text = text)
        fig.show()
    elif type == 'line':
        fig = px.line(df, x = x, y = y, title = title)
        fig.show()
        fig.update_layout(autotypenumbers='convert types')
        
def getDF(myList):
    frameTime = {}
    evtType = {}
    bdADDR = {}
    
    # Create dataframe from list, Loop through all packets in .pcap
    for index in myList:
        
        key = str(index['TIME'][:24])
        if key not in frameTime:
            frameTime[key] = int(index['LENGTH'])
        else:
            frameTime.update({key:frameTime.get(key) + int(index['LENGTH'])})
                
        if index['EVT_CODE']:
            evtType = indexDict(str(lib.convEventTypeCode(int(index["EVT_CODE"]))), evtType)
        else:
            evtType = indexDict('N/A', evtType)
            
        if index['BD_ADDR']:
            bdADDR = indexDict(str(index["BD_ADDR"]), bdADDR)
        else:
            bdADDR = indexDict('N/A', bdADDR)
        
    # Create and return Dataframes from list   
    dfEVT = pd.DataFrame({'Event' : list(evtType.keys()), 'Amount' : list(evtType.values())})
    dfBDADDR = pd.DataFrame({'BD Address' : list(bdADDR.keys()), 'Amount' : list(bdADDR.values())})
    dfTIME = pd.DataFrame({'Time' : list(frameTime.keys()), 'Length' : list(frameTime.values())})
    
    # Return created Dataframes back to calling method    
    return dfEVT, dfBDADDR, dfTIME          

def indexDict(diction, pkt):
    key = diction
    if key not in pkt:
        pkt[key] = 1
    else:
        pkt.update({key:pkt.get(key) + 1})
                
    return pkt