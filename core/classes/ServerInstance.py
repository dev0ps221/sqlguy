

class ServerInstance:
    host = None
    user = None
    pwd = None

    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd  = pwd
    