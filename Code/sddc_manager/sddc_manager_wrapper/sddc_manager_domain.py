# sddc_manager_wrapper/sddc_manager_domain.py

class Domain(object):
    def __init__(self, id):
        self.id = id

    def info(self):
        return {'id': self.id}