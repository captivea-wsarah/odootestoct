from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Spaceship(models.Model):

    _name = 'space_mission.spaceship'
    _description = "Space Mission Spaceship"
    
    #Fields definition
    name = fields.Char(string='Vessel Name')
    active = fields.Boolean(default=True)    
    type = fields.Selection(selection=[('freighter','Freighter'),
                                       ('star_destroyer', 'Star Destroyer'),
                                       ('star_cruiser', 'Star Destroyer'),
                                       ('x_wing', 'X-Wing Fighter')],
                            string='Ship Type',)
    model = fields.Char(string='Ship Model', 
                        required = True)
    crew_capacity = fields.Integer(string= "Number of Passengers",
                                        help="Maximum number of passengers in the Spaceship",)

    #Add Crew members to vessel
    crew_ids = fields.Many2many(comodel_name='res.partner',
                            string='Crew')
    mission_ids = fields.One2many(comodel_name='space_mission.mission',
                               inverse_name='spaceship_id')
            
