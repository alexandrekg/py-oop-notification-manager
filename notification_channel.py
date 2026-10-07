class NotificationChannel:
    def __init__(self, sender: str):
        self._sender = sender
        
    def send(self, recipient: str, message: str) -> bool:
        raise NotImplementedError