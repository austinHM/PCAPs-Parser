import pyshark
import lib, btVis

file_path = 'C:\\Users\\Austi\\OneDrive\\Desktop\\PythonPcap\\Project\\'
file_name = 'Bluetooth2.pcap'
#cap = pyshark.FileCapture(file_path + file_name, only_summaries=True)

def parse_pcap(filename, maxPacket):
    # Variables
    i = 0
    z = {}
    x = []
    
    # Read .pcap file
    with pyshark.FileCapture(file_path + file_name, keep_packets=False) as cap:
            # Loop through entire .pcap file
            for pkt in cap:
                
                # Testing purpose only
                if i == -1:
                    print(pkt)
                    print("")
                
                # View specified packets
                if i < maxPacket or maxPacket == 0:

                    # Generate output data to list
                    z = {"PACKET": lib.getPacketNum(pkt),
                         "TIME": lib.getPacketTime(pkt),
                         "LENGTH": lib.getPacketLen(pkt),
                         "BD_ADDR": lib.getBD_ADDR(pkt),
                         "EVT_CODE": lib.getEventType(pkt),
                         "DIRECTION": lib.getPacketDirection(pkt)
                         }
                    
                    # Add new data to list
                    x.append(z)
                    z = {}  
                    i += 1
                    
            # Send data to calling function    
            return x
              
def UI(result, dfList):
    print("\n")
    print("1: Display Results")
    print("2: Display Dataframe")
    print("3: Display Captured Events")
    print("4: Dispaly Captured  BD_ADDR")
    print("5: Display Packet Length Over Time")
    print("0: Exit")
        
    opt = input("Select an option: ")
     
    if opt == "0":
        print("\nClosing...")
        return False
    
    elif opt == "1":
        print('')
        for index in result:
            if index["DIRECTION"]:
                print("Packet: {:6}  Direction: {} ".format(index["PACKET"], index["DIRECTION"]))
        return True
                
    elif opt == "2":
        dfOpt = input("\nPlease enter a Dataframe name: ")
        dfOpt = dfOpt.upper()
        if dfOpt in dfList:
            print('')
            print(dfList[dfOpt])
        else:
            print("\nDataframe was not found!")
        return True
                
    elif opt == "3":
        btVis.graphDisplay('bar', dfEVT, x = "Event", y = "Amount", title="Bluetooth .PCAP Event Breakdown", text = "Amount")
        return True
    
    elif opt == "4":
        btVis.graphDisplay('bar', dfBDADDR, x = "BD Address", y = "Amount", title="Bluetooth .PCAP BD Address Discovery", text = "Amount")
        return True
    
    elif opt == "5":
        btVis.graphDisplay('line', dfTIME, x = "Time", y = "Length", title="Bluetooth .pcap Time Display", text = "")
        return True
    
    else:
        print("\nOption entered is not valid!")
        return True
        
if __name__ == '__main__':
    # Generate list of values from packets
    result = parse_pcap(file_name, 10) 

    # Initialize Dataframes
    dfEVT, dfBDADDR, dfTIME = btVis.getDF(result)
    dfList = {"EVT":dfEVT, "BDADDR":dfBDADDR, "TIME":dfTIME}
    
    cont = True
    while cont:
        cont = UI(result, dfList)
    