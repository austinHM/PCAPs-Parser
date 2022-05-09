from sqlite3 import Date
from datetime import datetime
from typing import OrderedDict
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import lib as lib

def graphDisplay(type, df, x, y, title, text):
    """Builds Plotly graphs from the input data.

    Args:
        type (string): _description_
        df (dataframe): _description_
        x (string): _description_
        y (string): _description_
        title (string): _description_
        text (string): _description_
    """
    if type == 'bar':
        fig1 = px.bar(df, x = x, y = y, title = title, text = text)
        fig1.show()
    elif type == 'line':
        fig2 = px.line(df, x = x, y = y, title = title)
        fig2.show()
        fig2.update_layout(autotypenumbers='convert types')
    elif type == 'timeline':
        fig3 = px.line(df, x=x, y=y, color='BD_Addr', symbol="BD_Addr", title = title)
        fig3.update_xaxes(tickformat="%b %d, %Y %H:%M:%S.%f")
        fig3.update_layout(autotypenumbers='convert types')
        fig3.show()
        
def getDF(myList):
    frameTime = {}
    frameBDADDR = {}
    evtType = {}
    bdADDR = {}
    
    # Create dataframe from list, Loop through all packets in .pcap
    for index in myList:
        
        key = str(index['TIME'][:28])
        dt = datetime.strptime(key, '%b %d, %Y  %H:%M:%S.%f')
        key = dt
        if key not in frameTime:
            frameTime[key] = int(index['LENGTH'])
            if index['BD_ADDR']:
                frameBDADDR[key] = index['BD_ADDR']
            else:
                frameBDADDR[key] = "N/A"
        else:
            #frameTime.update({key:frameTime.get(key) + int(index['LENGTH'])})
            pass    
                
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
    
    dfTIME = pd.DataFrame({'Time' : list(frameTime.keys()), 'Length' : list(frameTime.values()), 'BD_Addr' : list(frameBDADDR.values())  })
    
    # Return created Dataframes back to calling method    
    return dfEVT, dfBDADDR, dfTIME          

def indexDict(diction, pkt):
    key = diction
    if key not in pkt:
        pkt[key] = 1
    else:
        pkt.update({key:pkt.get(key) + 1})
                
    return pkt