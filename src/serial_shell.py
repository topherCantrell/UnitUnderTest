import serial

# Status for the shell.
SHELL_AT_LOGIN  = 'login'    # Shell is waiting for a login
SHELL_AT_PROMPT = 'prompt'   # Shell is waiting for a command
SHELL_UNKNOWN   = 'unknown'  # Shell is in unknown state

class Shell:
    
    def __init__(self, port):
        self.status = SHELL_UNKNOWN
        # TODO check status here. AT_LOGIN, AT_PROMPT, UNKNOWN
        # TODO pass in login credentials? Assuming root OK? 
        self.ser = serial.Serial(port=port, baudrate=115200, timeout=5)
        self.exit_to_login_prompt()
        self.ser.write(b'root\n')
        # TODO wait for prompt
        
    def exit_to_login_prompt(self):
        # TODO
        # Are we logged in? Do we need to? Are we at a prompt ending in #?
        # Do we need to cntrl-c to get out of a hung shell?
        self.ser(b'exit\n')
        # No waiting here or TODO wait for "logout" or wait for "login"
        self.ser.close()
        
    def execute(self,command):
        self.ser.write(command.encode())
        # TODO Wait for prompt        