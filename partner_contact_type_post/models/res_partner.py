# Copyright 2018 Sergi Oliva <sergi.oliva@qubiq.es>
# Copyright 2018 Xavier Jiménez <xavier.jimenez@qubiq.es>
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, tools
from odoo.modules import get_module_resource
import base64


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(
        selection_add=[('post', 'Post Address')],
    )

    @api.model
    def _get_default_image(self, partner_type, is_company, parent_id):
        res = super(ResPartner, self)._get_default_image(
            partner_type, is_company, parent_id)
        if partner_type == 'post':
            img_path = get_module_resource(
                'partner_contact_type_post', 'static/src/img', 'post.png')
            if img_path:
                with open(img_path, 'rb') as f:
                    image = f.read()

            return tools.image_resize_image_big(base64.b64encode(image))
        else:
            return res
