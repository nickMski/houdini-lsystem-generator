import hou

class GrowthParameters:
    def __init__(self):
        self.node = hou.pwd()
    
    def create_parm_if_not_exists(self, pgroup, template):
        if not self.node.parm(template.name()):
            pgroup.append(template)
        
    def setup_parameters(self):
        pgroup = self.node.parmTemplateGroup()
        
        params = [
            hou.FloatParmTemplate("angle", "Branch Angle", 1),
            hou.FloatParmTemplate("length", "Segment Length", 1),
            hou.IntParmTemplate("iterations", "Growth Iterations", 1),
            hou.FloatParmTemplate("light_influence", "Light Influence", 1),
            hou.FloatParmTemplate("space_check_radius", "Space Check Radius", 1),
            hou.FloatParmTemplate("max_neighbors", "Max Neighbors", 1),
            hou.FloatParmTemplate("noise_freq", "Noise Frequency", 1),
            hou.FloatParmTemplate("noise_amount", "Noise Amount", 1)
        ]
        
        for param in params:
            self.create_parm_if_not_exists(pgroup, param)
            
        if pgroup != self.node.parmTemplateGroup():
            self.node.setParmTemplateGroup(pgroup)
