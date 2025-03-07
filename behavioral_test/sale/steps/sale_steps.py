from odoo import models

def setUp():
    return ReturnContext.returnContext()

class ReturnContext(models.BaseModel):

    def returnContext(self):
        return self.env

print(setUp())