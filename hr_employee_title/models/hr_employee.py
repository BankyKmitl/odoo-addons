# Copyright 2022 Amin Cheloh
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        self.work_contact_id.title = self.title
        return res

    def write(self, vals):
        res = super().write(vals)
        self.work_contact_id.title = self.title
        return res
