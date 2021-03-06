# -*- coding: utf-8 -*-
# © 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    ordered_works = fields.Many2many(
        comodel_name="project.task.work", compute="_compute_ordered_works")

    @api.one
    def _compute_ordered_works(self):
        # Search for all tasks because task_ids field only contains open tasks
        tasks = self.env['project.task'].search(
            [('project_id', 'in', self.ids)])
        works = tasks.mapped('work_ids')
        self.ordered_works = works.sorted(key=lambda x: x.date, reverse=True)
