from odoo import models, fields


class HrContractOvertime(models.Model):
    _inherit = 'hr.contract'
    salary_per_h = fields.Float(string= "Standard Salary per Hour")
    over_hour = fields.Monetary('Overtime Hour Wage')
    over_day = fields.Monetary('Overtime Day Wage')
