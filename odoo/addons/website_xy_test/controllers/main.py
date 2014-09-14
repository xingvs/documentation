# -*- coding: utf-8 -*-
import cStringIO
import datetime
from itertools import islice
import json
import xml.etree.ElementTree as ET

import logging
import re

from sys import maxint

import werkzeug.utils
import urllib2
import werkzeug.wrappers

from PIL import Image

import openerp
from openerp.addons.web import http
from openerp.http import request, Response


logger = logging.getLogger(__name__)

# Completely arbitrary limits
MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT = IMAGE_LIMITS = (1024, 768)
LOC_PER_SITEMAP = 45000
SITEMAP_CACHE_TIME = datetime.timedelta(hours=12)

class MWebsite(openerp.addons.website.controllers.main.Website):
    #------------------------------------------------------
    # View
    #------------------------------------------------------
    @http.route('/', type='http', auth="public", website=True)
    def indexe(self, **kw):
        print "invoke me"
        page = 'homepage'
        try:
            main_menu = request.registry['ir.model.data'].get_object(request.cr, request.uid, 'website', 'main_menu')
        except Exception:
            pass
        else:
            first_menu = main_menu.child_id and main_menu.child_id[0]
            if first_menu:
                if not (first_menu.url.startswith(('/page/', '/?', '/#')) or (first_menu.url=='/')):
                    return request.redirect(first_menu.url)
                if first_menu.url.startswith('/page/'):
                    return request.registry['ir.http'].reroute(first_menu.url)
                
        return self.page(page)
