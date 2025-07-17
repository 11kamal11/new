{
    'name': 'My Custom Website',
    'version': '1.0',
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'my_custom_website/static/src/css/custom.css',
            'my_custom_website/static/src/js/custom.js',
        ],
    },
    'installable': True,
    'auto_install': False,
}