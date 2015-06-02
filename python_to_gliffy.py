#!/usr/bin/env python3

import pyclbr
import sys
import pprint
from pprint import pprint
sys.path.append('.')
import json
from copy import deepcopy


def get_classes(core_modules, prefix):
    """" class name: list of methods """
    classes = {}  # class: list of functions
    for core_module in core_modules:
        classes_presentation = pyclbr.readmodule(prefix + core_module)
        for cls, cls_obj in classes_presentation.items():
            classes[cls] = sorted(list(cls_obj.methods.keys()))
    return classes


def to_sting(core_modules, prefix):
    classes = get_classes(core_modules, prefix)
    return pprint.pformat(classes)


class ClassFactory():
    def __init__(self):
        self.cls_counter = 0
        with open('example_data/2classes.json') as doc:
            self.reference_json = json.load(doc)
        self.class_template = self.reference_json['stage']['objects'][0]
        self.generated_classes = []

    def add_class(self, name, attrs, methods):
        cls = deepcopy(self.class_template)
        current_id = self.cls_counter * 7
        # class self id 3 = 0
        cls['id'] = current_id
        #### Class
        child = cls['children'][0]
        # id = 1
        child['id'] = current_id + 1
        #class_id 1 = 2
        child['children'][0]['id'] = current_id + 2
        # class id 2 = 2 
        child['constraints']['constraints'][0]['HeightConstraint']['heightInfo'][0]['id'] = current_id + 2

        #### Attr
        child = cls['children'][1]
        # id = 3
        child['id'] = current_id + 3
        #class_id 1 = 4
        child['children'][0]['id'] = current_id + 4
        # class id 2 = 4
        child['constraints']['constraints'][1]['HeightConstraint']['heightInfo'][0]['id'] = current_id + 4

        child['constraints']['constraints'][0]['PositionConstraint']['nodeId'] = current_id + 1

        #### Methods
        child = cls['children'][2]
        # id = 5
        child['id'] = current_id + 5


        #class_id 1 = 6
        child['children'][0]['id'] = current_id + 6
        # class id 2 = 0
        child['constraints']['constraints'][1]['PositionConstraint']['nodeId'] = current_id + 3


        #all ids
        cls['constraints']['constraints'][0]['HeightConstraint']['heightInfo'][0]['id'] = current_id + 1
        cls['constraints']['constraints'][0]['HeightConstraint']['heightInfo'][0]['id'] = current_id + 3
        cls['constraints']['constraints'][0]['HeightConstraint']['heightInfo'][0]['id'] = current_id + 6

        class_name_html = ('<p style="text-align: center;"><span class="gliffy-placeholder-text" '
    'style="font-family: Arial; font-size: 12px; font-weight: bold; '
    'text-decoration: none; line-height: 14px; color: rgb(0, 0, '
    '0);">{}</span></p>').format(name)
        cls['children'][0]['children'][0]['graphic']['Text']['html'] = class_name_html
    
        attr_html = ('<p style="text-align: left;"><span class="gliffy-placeholder-text" style="font-family: Arial; '
                    'font-size: 12px; font-weight: normal; text-decoration: none; line-height: 14px; color: '
                     'rgb(0, 0, 0);">\n</span></p>')
        for attr in attrs:
            attr_html += ('<p style="text-align: left;"><span class="gliffy-placeholder-text" style="font-family: Arial; '
                    'font-size: 12px; font-weight: normal; text-decoration: none; line-height: 14px; color: '
                     'rgb(0, 0, 0);">{}\n</span></p>').format(attr)
        cls['children'][1]['children'][0]['graphic']['Text']['html'] = attr_html

        methods_html = ('<p style="text-align: left;"><span class="gliffy-placeholder-text" style="font-family: Arial; '
                    'font-size: 12px; font-weight: normal; text-decoration: none; line-height: 14px; color: '
                     'rgb(0, 0, 0);">\n</span></p>')
        for method in methods:
            methods_html += ('<p style="text-align: left;"><span class="gliffy-placeholder-text" style="font-family: Arial; '
                    'font-size: 12px; font-weight: normal; text-decoration: none; line-height: 14px; color: '
                     'rgb(0, 0, 0);">{}\n</span></p>').format(method)
        cls['children'][2]['children'][0]['graphic']['Text']['html'] = methods_html


        cls['x'] = 100 + self.cls_counter * 200
        self.cls_counter += 1
        self.generated_classes.append(cls)
    
    def write(self, filename):
        output = deepcopy(self.reference_json)
        output['stage']['objects'] = self.generated_classes
        with open(filename, 'w') as outfile:
            json.dump(output, outfile)
    

if __name__ == '__main__':
    # core_modules = ['alert_handler',  'alerts',  'bx_interface',  'collector',  'context',  'database',  'devices',  'download',  'emergency_checker',  'nodes_test',  'parameters',  'power_control']
    core_modules = ['python_classes']
    prefix = 'example_data.'
    classes = get_classes(core_modules, prefix)
    factory = ClassFactory()
    for cls in classes:
        factory.add_class(cls, ['self'], methods=classes[cls])
    factory.write('example_data/output2.json')
