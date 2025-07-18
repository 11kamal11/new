from odoo import http
from odoo.http import request

class CustomWebsite(http.Controller):
    @http.route('/custom-page', type='http', auth='public', website=True)
    def custom_page(self, **kwargs):
        return request.render('my_custom_website.custom_page', {
            'custom_data': 'Hello from my custom website!'
        })