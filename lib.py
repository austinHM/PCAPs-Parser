# Conversion Tables (Hex -> ASCII)
def convEventTypeCode(code):
    # https://www.lisha.ufsc.br/teaching/shi/ine5346-2003-1/work/bluetooth/hci_commands.html
    
    evt = {
        hex(0x01): 'Inquiry Complete',
        hex(0x02): 'Inquiry Result',
        hex(0x03): 'Connection Complete',
        hex(0x04): 'Connection Request',
        hex(0x05): 'Disconnection Complete',
        hex(0x06): 'Authentication Complete',
        hex(0x07): 'Remote Name Request Complete',
        hex(0x08): 'Encryption Change',
        hex(0x09): 'Change Connection Link Key Complete',
        hex(0x0a): 'Master Link Key Complete',
        hex(0x0b): 'Read Remote Supported Features Complete',
        hex(0x0c): 'Read Removed Version Complete',
        hex(0x0d): 'QoS Setup Complete',
        hex(0x0e): 'Command Complete',
        hex(0x0f): 'Command Status',
        hex(0x10): 'Hardware Error',
        hex(0x11): 'Flush Occured',
        hex(0x12): 'Role Change',
        hex(0x13): 'Number of Completed Packets',
        hex(0x14): 'Mode Change',
        hex(0x15): 'Return Link Keys',
        hex(0x16): 'PIN Code Request',
        hex(0x17): 'Link Key Request',
        hex(0x18): 'Link Key Notification',
        hex(0x19): 'Loopback Command',
        hex(0x1a): 'Data Buffer Overflow',
        hex(0x1b): 'Max Slots Change',
        hex(0x1c): 'Read Clock Offset Complete',
        hex(0x1d): 'Connection Packet Type Change',
        hex(0x1e): 'QoS Violation',
        hex(0x1f): 'Page Scan Mode Change Event',
        hex(0x20): 'Page Scan Repetition MOde Change'
    }
    
    if evt.get(hex(code)) == None:
        return code
    else:
        return evt.get(hex(code))

# Data get methods
def getPacketNum(pkt):
    try: 
        return pkt.frame_info.number
    except AttributeError as e:
        return ""
    
def getEventType(pkt):
    try: 
        return pkt.bthci_evt.code
    except AttributeError as e:
        return ""
    
def getBD_ADDR(pkt):
    try: 
        return pkt.bthci_evt.bd_addr
    except AttributeError as e:
        return ""
        
def getPacketTime(pkt):
    try: 
        return pkt.frame_info.time
    except AttributeError as e:
        return ""
        
def getPacketLen(pkt):
    try: 
        return pkt.frame_info.cap_len
    except AttributeError as e:
        return ""        

def getPacketDirection(pkt):
    try: 
        temp = pkt.hci_h4.direction
        if temp == "0x00000000":
            return 'Sent'
        else:
            return 'Received'
    except AttributeError as e:
        return "" 



#print(eventType(2))