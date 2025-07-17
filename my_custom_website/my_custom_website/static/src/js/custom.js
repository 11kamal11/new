odoo.define('my_custom_website.custom', function (require) {
    'use strict';
    var publicWidget = require('web.public.widget');
    publicWidget.registry.CustomWidget = publicWidget.Widget.extend({
        selector: '.custom-section',
        start: function () {
            console.log('Custom widget loaded!');
            // Add your JavaScript logic here
            return this._super.apply(this, arguments);
        },
    });
});