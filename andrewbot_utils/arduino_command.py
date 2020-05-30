def create_empty_command(size=18):
    return [0x00]*18

def prepare_message(command):
    """
    Add checksum to command
    """
    checksum = 0
    for v in command[:16]:
        checksum += v

    command[16]=(checksum >> 8) & 0xff
    command[17]= checksum & 0xff
    return command
