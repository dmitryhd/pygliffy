#!/usr/bin/env python3

""" Python print uml diagram to Gliffy. """

import pyclbr
import json
import argparse
from copy import deepcopy

import sys
sys.path.append('.')

__version__ = '0.1'


def get_classes(core_modules, prefix):
    """" Return {class name: {attrs=[list of attrs], methods=[list of methods]}
    """
    classes = {}  # class: list of functions
    for core_module in core_modules:
        classes_presentation = pyclbr.readmodule(prefix + core_module)
        for cls, cls_obj in classes_presentation.items():
            classes[cls] = {}
            classes[cls]['methods'] = sorted(list(cls_obj.methods.keys()))
            classes[cls]['attrs'] = []  # TODO: get attributes
    return classes


class ClassFactory():
    """ Can produce json gliffy from class devinition.
        Example:
        factory = pg.ClassFactory()
        factory.add_classes(self.classes)
        factory.write('/tmp/gliffy_tmp.json')
    """
    def __init__(self):
        self.cls_counter = 0
        with open('example_data/2classes.json') as doc:
            self.reference_json = json.load(doc)
        self.class_template = self.reference_json['stage']['objects'][0]
        self.generated_classes = []
        self.header_html = (
            '<p style="text-align: center;">'
            '<span class="gliffy-placeholder-text"'
            'style="font-family: Arial; font-size: 12px; font-weight: bold; '
            'text-decoration: none; line-height: 14px; color: rgb(0, 0, '
            '0);">{}\n</span></p>')
        self.common_html = (
            '<p style="text-align: left;">'
            '<span class="gliffy-placeholder-text"'
            'style="font-family: Arial; font-size: 12px; font-weight: normal; '
            'text-decoration: none; line-height: 14px; color: rgb(0, 0, '
            '0);">{}\n</span></p>')

    def add_classes(self, classes):
        """ Classes from get_classes. """
        for cls in sorted(list(classes.keys())):
            self.add_class(cls, classes[cls]['attrs'], classes[cls]['methods'])

    def write(self, filename):
        """ Write gliffy to file. It will be overwrited. """
        with open(filename, 'w') as outfile:
            outfile.write(self.produce_gliffy())

    def produce_gliffy(self):
        """ Return full json string. """
        output = deepcopy(self.reference_json)
        output['stage']['objects'] = self.generated_classes
        return json.dumps(output)

    def add_class(self, name, attrs, methods):
        """ Add single class to inner presentation of json. """
        # TODO: split to several methods.
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
        constr = child['constraints']['constraints'][0]['HeightConstraint']
        constr['heightInfo'][0]['id'] = current_id + 2

        #### Attr
        child = cls['children'][1]
        # id = 3
        child['id'] = current_id + 3
        #class_id 1 = 4
        child['children'][0]['id'] = current_id + 4
        # class id 2 = 4
        constr = child['constraints']['constraints']
        constr[1]['HeightConstraint']['heightInfo'][0]['id'] = current_id + 4
        constr[0]['PositionConstraint']['nodeId'] = current_id + 1

        #### Methods
        child = cls['children'][2]
        # id = 5
        child['id'] = current_id + 5


        #class_id 1 = 6
        child['children'][0]['id'] = current_id + 6
        # class id 2 = 0
        constr = child['constraints']['constraints']
        constr[1]['PositionConstraint']['nodeId'] = current_id + 3


        #all ids
        constr = cls['constraints']['constraints'][0]['HeightConstraint']
        constr['heightInfo'][0]['id'] = current_id + 1
        constr['heightInfo'][1]['id'] = current_id + 3
        constr['heightInfo'][2]['id'] = current_id + 6

        class_name_html = self.header_html.format(name)
        class_name_id = cls['children'][0]['children'][0]['graphic']['Text']
        class_name_id['html'] = class_name_html

        attr_html = ''
        for attr in attrs:
            attr_html += self.common_html.format(attr)
        attrs_id = cls['children'][1]['children'][0]['graphic']['Text']
        attrs_id['html'] = attr_html

        methods_html = ''
        for method in methods:
            methods_html += self.common_html.format(method)
        methods_id = cls['children'][2]['children'][0]['graphic']['Text']
        methods_id['html'] = methods_html

        cls['x'] = 100 + self.cls_counter * 200
        self.cls_counter += 1
        self.generated_classes.append(cls)



def parse_args():
    """ Process command line arguments. """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version",
                        help="Print version and exit.",
                        action="store_true")
    parser.add_argument("-o", "--output_file", type=str,
                        default='/tmp/gliffy.json',
                        help="Output file")
    args = parser.parse_args()
    if args.version:
        print('Version: ', __version__)
        sys.exit(0)
    return args


def main():
    """ Main. """
    # core_modules = ['alert_handler',  'alerts',  'bx_interface',
    # 'collector',  'context',  'database',  'devices',  'download',
    # 'emergency_checker',  'nodes_test',  'parameters',  'power_control']
    args = parse_args()
    core_modules = ['python_classes']
    prefix = 'example_data.'
    classes = get_classes(core_modules, prefix)
    factory = ClassFactory()
    factory.add_classes(classes)
    factory.write(args.output_file)


if __name__ == '__main__':
    main()
