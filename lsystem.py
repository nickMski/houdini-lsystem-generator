import hou
import random
from collections import deque

class LSystemParser:
    def __init__(self):
        self.node = hou.pwd()
        self.geo = self.node.geometry()
        self.rules = {}
        self.stack = deque()
        
    def add_rule(self, predecessor, successor):
        self.rules[predecessor] = successor
        
    def setup_default_rules(self):
        self.rules = {
            'F': 'FF',  # Forward growth
            'X': 'F+[-X]F[-X]+X',  # Branching
            'Y': 'F[-FY]+FY'  # Alternate branching
        }
        
    def interpret_string(self, input_string, angle=25.0, length=1.0):
        pos = hou.Vector3(0, 0, 0)
        dir = hou.Vector3(0, 1, 0)
        up = hou.Vector3(0, 0, 1)
        
        current_point = self.geo.createPoint()
        current_point.setPosition(pos)
        
        for char in input_string:
            if char == 'F':
                new_pos = pos + dir * length
                new_point = self.geo.createPoint()
                new_point.setPosition(new_pos)
                rot = hou.Quaternion()
                
                line = self.geo.createPolygon()
                line.addVertex(current_point)
                line.addVertex(new_point)
                
                pos = new_pos
                current_point = new_point
                
            elif char == '+':
                rot.setToAngleAxis(angle, (up.x(), up.y(), up.z()))
                dir = rot.rotate(dir)
                
            elif char == '-':
                rot.setToAngleAxis(-angle, (up.x(), up.y(), up.z()))
                dir = rot.rotate(dir)
                
            elif char == '[':
                self.stack.append((pos, dir, current_point))
                
            elif char == ']':
                pos, dir, current_point = self.stack.pop()
