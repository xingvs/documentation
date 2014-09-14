
import base64
import logging
from email.utils import formataddr
from urlparse import urljoin

from openerp import api, tools
from openerp import SUPERUSER_ID
from openerp.addons.base.ir.ir_mail_server import MailDeliveryException
from openerp.osv import fields, osv
from openerp.tools.safe_eval import safe_eval as eval
from openerp.tools.translate import _
import openerp.tools as tools

class xy_maintance(osv.Model):
    
    _name = "xy.maintance"
    
    def search_read(self, cr, uid, domain=None, fields=None, offset=0, limit=None, order=None, context=None):
        rlist = self.pool.obj_list()
        
        a = type(self).__base__
        print a
        print a.__module__
        print a.__dict__
        
        return [{"name" : v, "info" : type(self.pool[v]).__base__.__module__} for v in rlist] 
    
    
    def create(self, vals):
        pass
    
    _columns = {
        "name"  : fields.text(string = "name" , size = 128),  
        "info"  : fields.text(string = "info", size = 512)      
    }
    
    
    
    
    
    
    
    