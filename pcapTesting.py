import pyshark
import lib, btVis

file_path = 'C:\\Users\\Austi\\OneDrive\\Desktop\\PythonPcap\\'
file_name = 'Bluetooth2.pcap'
cap = pyshark.FileCapture(file_path & file_name, only_summaries=True)

def parse_pcap(filename, maxPacket):
    # Variables
    i = 0
    z = {}
    x = []
    
    # Read .pcap file
    with pyshark.FileCapture(filename, keep_packets=False) as cap:
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
                
    
if __name__ == '__main__':
    # Generate list of values from packets
    result = parse_pcap(file_name, 10) 

    # Initialize Dataframes
    dfEVT, dfBDADDR, dfTIME = btVis.getDF(result)
    
    # Create visual display from Dataframes and view in local host
    #btVis.graphDisplay('bar', dfEVT, x = "Event", y = "Amount", title="Bluetooth .PCAP Event Breakdown", text = "Amount")
    #btVis.graphDisplay('bar', dfBDADDR, x = "BD Address", y = "Amount", title="Bluetooth .PCAP BD Address Discovery", text = "Amount")
    #btVis.graphDisplay('line', dfTIME, x = "Time", y = "Length", title="Bluetooth .pcap Time Display", text = "")
    
    for index in result:
        if index["DIRECTION"]:
            print("Packet: " + index["PACKET"] + "    TEST: " + index["DIRECTION"])
            pass