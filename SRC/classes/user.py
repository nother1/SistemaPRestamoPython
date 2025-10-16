class user:
    def __init__(self,userName, userPassword, userRole, userDocument):
        self._userName = userName
        self._userPassword = userPassword
        self._userRole = userRole
        self._userDocument = userDocument
        
    @property
    def userName(self):
        return self._userName
    
    @property
    def userPassword(self):
        return self._userPassword
    
    @property
    def userRole(self):
        return self._userRole
    
    @property
    def userDocument(self):
        return self._userDocument
            
    @userName.setter
    def userName(self,val):
        self._userName = val
        
    @userPassword.setter
    def userPassword(self,val):
        self._userPassword = val
        
    @userRole.setter
    def userRole(self,val):
        self._userRole = val
        
    @userDocument.setter
    def userDocument(self,val):
        self._userDocument = val