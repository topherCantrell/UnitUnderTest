import serial
import time

# Status for the shell.
SHELL_AT_LOGIN  = 'login'    # Shell is waiting for a login
SHELL_AT_PROMPT = 'prompt'   # Shell is waiting for a command
SHELL_UNKNOWN   = 'unknown'  # Shell is in unknown state

class Shell:
    
    def __init__(self, port):
        # Connect to port        
        self._ser = serial.Serial(port=port, baudrate=115200, timeout=5)
        # Return the object ready for commands
        self._get_to_prompt()
    
    def _get_to_prompt(self):
        # Make a couple of passes in case we have to log in
        for _ in range(2):
            # Get some kind of feedback from the shell
            status,_ = self.execute('')
            # If we are at the prompt, the we are all set
            if status==SHELL_AT_PROMPT:
                return
            # If we are at the login prompt, send the username 
            # (no password required for root)
            if status==SHELL_AT_LOGIN:
                self.execute('root')
        # Something is wrong. We can't get the prompt.
        raise Exception('Could not get root prompt')
        
    def _read_to_timeout(self):
        buffer = ''
        while True:
            c = self._ser.read()
            if c==b'':
                break
            if c!=b'\r':
                buffer = buffer + c.decode() 
                lns = buffer.split('\n')
                if lns[-1].startswith('root@') and lns[-1].endswith('# '):
                    return SHELL_AT_PROMPT,lns[1:-1]
        
        if lns[-1].endswith('login: '):
            return SHELL_AT_LOGIN,lns
        
        return SHELL_UNKNOWN,lns    
    
    def wait_for_prompt(self):
        # TODO Just for now ...
        print('Waiting for prompt ...')
        time.sleep(60*3) # Wait a minute
        self._get_to_prompt()
        print('... ready.')
            
    def execute(self,command):
        self._ser.write((command+"\n").encode())
        return self._read_to_timeout()        