import json

class Controller:
    def __init__(self, request):
        self.request = request
        self.body = json.loads(request.data) if request.data else {}