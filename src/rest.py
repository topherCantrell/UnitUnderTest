import urllib.request
import json

class Rest:
    
    def __init__(self, host, username, password, check_cert=False):
        """Create an object to talk to a REST host.
        
        Args:
            host (string): the address of the REST host (https://1.2.3.4)
            username (string): the username credentials
            password (string): the password credentials
            check_cert (bool): set to True to force python to check the server's HTTPS 
                               certificate. The default is to talk to anybody.
        
        """
        if not check_cert:
            # WARNING we are talking to any server no matter what their certificates are
            import ssl
            ssl._create_default_https_context = ssl._create_unverified_context
            
        # TODO We should use the username/password to create a session. That allows
        # the target REST server to control session timeouts and forced logouts.
        # Maybe we subclass this to make a session-version.
               
        self._host = host
        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None,host+'/',username,password)
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.request.build_opener(handler)
        opener.open(host+'/')
        urllib.request.install_opener(opener)
        
    def get(self,path):
        """Perform a GET on the REST path.
        
        Args:
            path (string): the path within the REST tree
            
        Returns:
            dictionary: the JSON object parsed from the return
            
        Raises:
            HTTPError: for anything but a 2xx response
        
        """
        url = self._host + path
        req = urllib.request.Request(url=url)
        f = urllib.request.urlopen(req)
        ret =  json.loads(f.read().decode())
        return ret
    
    def post(self,path,data={}):   
        """Perform a POST on the REST path.
        
        Args:
            path (string): the path within the REST tree
            data (dictionary): the JSON object to send in the request
            
        Returns:
            dictionary: the JSON object parsed from the return
            
        Raises:
            HTTPError: for anything but a 2xx response
        
        """    
        d = json.dumps(data).encode()        
        url = self._host + path
        headers = {'Content-Type':'application/json'}
        req = urllib.request.Request(url=url,headers=headers,method='POST',data=d)
        f = urllib.request.urlopen(req)
        ret =  json.loads(f.read().decode())
        return ret    
    
    def patch(self,path,data):    
        """Perform a PATCH on the REST path.
        
        Args:
            path (string): the path within the REST tree
            data (dictionary): the JSON object to send in the request
            
        Returns:
            dictionary: the JSON object parsed from the return
            
        Raises:
            HTTPError: for anything but a 2xx response
        
        """       
        d = json.dumps(data).encode()        
        url = self._host + path
        headers = {'Content-Type':'application/json'}
        req = urllib.request.Request(url=url,headers=headers,method='PATCH',data=d)
        f = urllib.request.urlopen(req)
        ret =  json.loads(f.read().decode())
        return ret
    
    def put(self,path,data):
        """Perform a PUT on the REST path.
        
        Args:
            path (string): the path within the REST tree
            data (dictionary): the JSON object to send in the request
            
        Returns:
            dictionary: the JSON object parsed from the return
            
        Raises:
            HTTPError: for anything but a 2xx response
        
        """    
        d = json.dumps(data).encode()        
        url = self._host + path
        headers = {'Content-Type':'application/json'}
        req = urllib.request.Request(url=url,headers=headers,method='PUT',data=d)
        f = urllib.request.urlopen(req)
        ret =  json.loads(f.read().decode())
        return ret
    
    def delete(self,path):
        """Perform a DELETE on the REST path.
        
        Args:
            path (string): the path within the REST tree            
            
        Returns:
            dictionary: the JSON object parsed from the return
            
        Raises:
            HTTPError: for anything but a 2xx response
        
        """    
        url = self._host + path
        req = urllib.request.Request(url=url,method='DELETE')
        f = urllib.request.urlopen(req)
        ret =  json.loads(f.read().decode())
        return ret
