#!/usr/bin/env python3

""" Python print uml diagram to Gliffy. """

import imp
import inspect
import os
import re
import json
import argparse
from copy import deepcopy

import sys
sys.path.append('.')
import logging

logging.basicConfig(level=logging.DEBUG)

__version__ = '0.1rc'

reference_json = {'embeddedResources': {'resources': [], 'index': 0}, 'metadata': {'revision': 0, 'title': 'untitled', 'exportBorder': False}, 'contentType': 'application/gliffy+json', 'version': '1.1', 'stage': {'height': 255, 'gridOn': True, 'shapeStyles': {}, 'snapToGrid': True, 'printPortrait': True, 'exportBorder': False, 'maxHeight': 5000, 'background': '#FFFFFF', 'themeData': None, 'textStyles': {}, 'width': 632, 'nodeIndex': 14, 'printShrinkToFit': False, 'autoFit': True, 'lineStyles': {}, 'printPaper': 'LETTER', 'drawingGuidesOn': True, 'objects': [{'height': 75, 'lockShape': False, 'uid': 'com.gliffy.shape.uml.uml_v1.default.class', 'width': 140, 'linkMap': [], 'children': [{'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': [{'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': None, 'id': 2, 'lockAspectRatio': False, 'order': 'auto', 'graphic': {'type': 'Text', 'Text': {'valign': 'top', 'paddingTop': 2, 'paddingBottom': 2, 'hposition': 'none', 'paddingRight': 2, 'html': '<p style="text-align: center;"><span class="gliffy-placeholder-text" style="font-family: Arial; font-size: 12px; font-weight: bold; text-decoration: none; line-height: 14px; color: rgb(0, 0, 0);">newClassName</span></p>', 'overflow': 'none', 'paddingLeft': 2, 'tid': None, 'vposition': 'none'}}, 'rotation': 0, 'y': 0, 'x': 0}], 'id': 1, 'y': 0, 'x': 0, 'order': 'auto', 'graphic': {'Shape': {'gradient': False, 'strokeWidth': 2, 'dropShadow': True, 'shadowX': 4, 'fillColor': '#FFFFFF', 'state': 0, 'shadowY': 4, 'tid': 'com.gliffy.stencil.rectangle.basic_v1', 'opacity': 1, 'strokeColor': '#000000'}, 'type': 'Shape'}, 'rotation': 0, 'constraints': {'constraints': [{'HeightConstraint': {'growParent': True, 'isMin': False, 'padding': 0, 'heightInfo': [{'magnitude': 1, 'id': 2}]}, 'type': 'HeightConstraint'}]}, 'lockAspectRatio': False}, {'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': [{'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': None, 'id': 4, 'lockAspectRatio': False, 'order': 'auto', 'graphic': {'type': 'Text', 'Text': {'valign': 'top', 'paddingTop': 2, 'paddingBottom': 2, 'hposition': 'none', 'paddingRight': 2, 'html': '<p style="text-align: left;"><span class="gliffy-placeholder-text" style="font-family: Arial; font-size: 12px; font-weight: normal; text-decoration: none; line-height: 14px; color: rgb(0, 0, 0);">Attribute</span></p>', 'overflow': 'none', 'paddingLeft': 2, 'tid': None, 'vposition': 'none'}}, 'rotation': 0, 'y': 0, 'x': 0}], 'id': 3, 'y': 18, 'x': 0, 'order': 'auto', 'graphic': {'Shape': {'gradient': False, 'strokeWidth': 2, 'dropShadow': True, 'shadowX': 4, 'fillColor': '#FFFFFF', 'state': 0, 'shadowY': 4, 'tid': 'com.gliffy.stencil.rectangle.basic_v1', 'opacity': 1, 'strokeColor': '#000000'}, 'type': 'Shape'}, 'rotation': 0, 'constraints': {'constraints': [{'type': 'PositionConstraint', 'PositionConstraint': {'nodeId': 1, 'px': 0, 'py': 1}}, {'HeightConstraint': {'growParent': True, 'isMin': False, 'padding': 0, 'heightInfo': [{'magnitude': 1, 'id': 4}]}, 'type': 'HeightConstraint'}]}, 'lockAspectRatio': False}, {'height': 39, 'lockShape': False, 'uid': None, 'width': 140, 'children': [{'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': None, 'id': 6, 'lockAspectRatio': False, 'order': 'auto', 'graphic': {'type': 'Text', 'Text': {'valign': 'top', 'paddingTop': 2, 'paddingBottom': 2, 'hposition': 'none', 'paddingRight': 2, 'html': '<p style="text-align: left;"><span class="gliffy-placeholder-text" style="font-family: Arial; font-size: 12px; font-weight: normal; text-decoration: none; line-height: 14px; color: rgb(0, 0, 0);">Method</span></p>', 'overflow': 'none', 'paddingLeft': 2, 'tid': None, 'vposition': 'none'}}, 'rotation': 0, 'y': 0, 'x': 0}], 'id': 5, 'y': 36, 'x': 0, 'order': 'auto', 'graphic': {'Shape': {'gradient': False, 'strokeWidth': 2, 'dropShadow': True, 'shadowX': 4, 'fillColor': '#FFFFFF', 'state': 0, 'shadowY': 4, 'tid': 'com.gliffy.stencil.rectangle.basic_v1', 'opacity': 1, 'strokeColor': '#000000'}, 'type': 'Shape'}, 'rotation': 0, 'constraints': {'constraints': [{'HeightConstraint': {'growParent': False, 'isMin': False, 'padding': 0, 'heightInfo': [{'magnitude': 1, 'id': 0}, {'magnitude': -1, 'id': 1}, {'magnitude': -1, 'id': 3}]}, 'type': 'HeightConstraint'}, {'type': 'PositionConstraint', 'PositionConstraint': {'nodeId': 3, 'px': 0, 'py': 1}}]}, 'lockAspectRatio': False}], 'id': 0, 'y': 180, 'x': 290, 'order': 0, 'graphic': None, 'rotation': 0, 'constraints': {'constraints': [{'HeightConstraint': {'growParent': False, 'isMin': True, 'padding': 0, 'heightInfo': [{'magnitude': 1, 'id': 1}, {'magnitude': 1, 'id': 3}, {'magnitude': 1, 'id': 6}]}, 'type': 'HeightConstraint'}]}, 'lockAspectRatio': False}, {'height': 75, 'lockShape': False, 'uid': 'com.gliffy.shape.uml.uml_v1.default.class', 'width': 140, 'linkMap': [], 'children': [{'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': [{'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': None, 'id': 9, 'lockAspectRatio': False, 'order': 'auto', 'graphic': {'type': 'Text', 'Text': {'valign': 'top', 'paddingTop': 2, 'paddingBottom': 2, 'hposition': 'none', 'paddingRight': 2, 'html': '<p style="text-align:center;"><span style="font-size: 12px; font-family: Arial; white-space: pre-wrap; font-weight: bold; text-decoration: none; line-height: 14px; color: rgb(0, 0, 0);">newClassName2</span></p>', 'overflow': 'none', 'paddingLeft': 2, 'tid': None, 'vposition': 'none'}}, 'rotation': 0, 'y': 0, 'x': 0}], 'id': 8, 'y': 0, 'x': 0, 'order': 'auto', 'graphic': {'Shape': {'gradient': False, 'strokeWidth': 2, 'dropShadow': True, 'shadowX': 4, 'fillColor': '#FFFFFF', 'state': 0, 'shadowY': 4, 'tid': 'com.gliffy.stencil.rectangle.basic_v1', 'opacity': 1, 'strokeColor': '#000000'}, 'type': 'Shape'}, 'rotation': 0, 'constraints': {'constraints': [{'HeightConstraint': {'growParent': True, 'isMin': False, 'padding': 0, 'heightInfo': [{'magnitude': 1, 'id': 9}]}, 'type': 'HeightConstraint'}]}, 'lockAspectRatio': False}, {'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': [{'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': None, 'id': 11, 'lockAspectRatio': False, 'order': 'auto', 'graphic': {'type': 'Text', 'Text': {'valign': 'top', 'paddingTop': 2, 'paddingBottom': 2, 'hposition': 'none', 'paddingRight': 2, 'html': '<p style="text-align:left;"><span style="font-size: 12px; font-family: Arial; white-space: pre-wrap; font-weight: normal; text-decoration: none; line-height: 14px; color: rgb(0, 0, 0);">Attribute2</span></p>', 'overflow': 'none', 'paddingLeft': 2, 'tid': None, 'vposition': 'none'}}, 'rotation': 0, 'y': 0, 'x': 0}], 'id': 10, 'y': 18, 'x': 0, 'order': 'auto', 'graphic': {'Shape': {'gradient': False, 'strokeWidth': 2, 'dropShadow': True, 'shadowX': 4, 'fillColor': '#FFFFFF', 'state': 0, 'shadowY': 4, 'tid': 'com.gliffy.stencil.rectangle.basic_v1', 'opacity': 1, 'strokeColor': '#000000'}, 'type': 'Shape'}, 'rotation': 0, 'constraints': {'constraints': [{'type': 'PositionConstraint', 'PositionConstraint': {'nodeId': 8, 'px': 0, 'py': 1}}, {'HeightConstraint': {'growParent': True, 'isMin': False, 'padding': 0, 'heightInfo': [{'magnitude': 1, 'id': 11}]}, 'type': 'HeightConstraint'}]}, 'lockAspectRatio': False}, {'height': 39, 'lockShape': False, 'uid': None, 'width': 140, 'children': [{'height': 18, 'lockShape': False, 'uid': None, 'width': 140, 'children': None, 'id': 13, 'lockAspectRatio': False, 'order': 'auto', 'graphic': {'type': 'Text', 'Text': {'valign': 'top', 'paddingTop': 2, 'paddingBottom': 2, 'hposition': 'none', 'paddingRight': 2, 'html': '<p style="text-align:left;"><span style="font-size: 12px; font-family: Arial; white-space: pre-wrap; font-weight: normal; text-decoration: none; line-height: 14px; color: rgb(0, 0, 0);">Method2</span></p>', 'overflow': 'none', 'paddingLeft': 2, 'tid': None, 'vposition': 'none'}}, 'rotation': 0, 'y': 0, 'x': 0}], 'id': 12, 'y': 36, 'x': 0, 'order': 'auto', 'graphic': {'Shape': {'gradient': False, 'strokeWidth': 2, 'dropShadow': True, 'shadowX': 4, 'fillColor': '#FFFFFF', 'state': 0, 'shadowY': 4, 'tid': 'com.gliffy.stencil.rectangle.basic_v1', 'opacity': 1, 'strokeColor': '#000000'}, 'type': 'Shape'}, 'rotation': 0, 'constraints': {'constraints': [{'HeightConstraint': {'growParent': False, 'isMin': False, 'padding': 0, 'heightInfo': [{'magnitude': 1, 'id': 7}, {'magnitude': -1, 'id': 8}, {'magnitude': -1, 'id': 10}]}, 'type': 'HeightConstraint'}, {'type': 'PositionConstraint', 'PositionConstraint': {'nodeId': 10, 'px': 0, 'py': 1}}]}, 'lockAspectRatio': False}], 'id': 7, 'y': 180, 'x': 490, 'order': 13, 'graphic': None, 'rotation': 0, 'constraints': {'constraints': [{'HeightConstraint': {'growParent': False, 'isMin': True, 'padding': 0, 'heightInfo': [{'magnitude': 1, 'id': 8}, {'magnitude': 1, 'id': 10}, {'magnitude': 1, 'id': 13}]}, 'type': 'HeightConstraint'}]}, 'lockAspectRatio': False}], 'printGridOn': False, 'maxWidth': 5000, 'pageBreaksOn': False}}

class ProjectParser(object):
    """ ProjectParser: . """
    def __init__(self, proj_dir):
        self.exclude_dirs = ['ropeproject', 'tests']
        self.proj_dir = proj_dir

    def get_classes(self):
        """ Get all classes from project. """
        sys.path.append(self.proj_dir)
        all_classes = {}
        for fname in self.python_files():
            logging.info('Processing classes from:' + fname)
            classes = self.get_classes_from_file(fname)
            all_classes.update(classes)
        return all_classes

    def python_files(self):
        """ Generator for getting python files. """
        for dirpath, _, files in os.walk(self.proj_dir):
            if self.do_skip_dir(dirpath):
                continue
            for fname in files:
                if re.search(r'\.py$', fname) and not re.search(r'setup\.py',
                                                                fname):
                    yield os.path.abspath(os.path.join(dirpath, fname))

    def do_skip_dir(self, dirname):
        """ Do we need to skip this dir. """
        skipdir = False
        for excl_dir in self.exclude_dirs:
            if re.search(excl_dir, dirname):
                skipdir = True
                break
        return skipdir

    @staticmethod
    def get_methods(cls_):
        """ Get methods of class. """
        res = []
        for func_name, func in cls_.__dict__.items():
            if func_name[:2] != '__' and inspect.isfunction(func):
                argnames = [argname for argname in func.__code__.co_varnames
                            if argname != 'self']
                res.append('+ {}({})'.format(func_name, ', '.join(argnames)))
        return res

    @staticmethod
    def get_attrs(cls_):
        """ Get attrs of class. """
        basic = [i for i in cls_.__dict__.keys() if i[:2] != '__' and not
                 inspect.isfunction(cls_.__dict__[i])]
        try:
            init_lines = inspect.getsourcelines(cls_.__dict__['__init__'])
        except (KeyError, OSError):
            init_lines = []
        for inits in init_lines:
            if not isinstance(inits, list):
                continue
            for line in inits:
                if line:
                    par_name = re.findall(r'self\.(.+)\s=', line)
                    if par_name: 
                        print(par_name[0])
                        basic.append(par_name[0])
        return basic

    def get_classes_from_file(self, fname):
        """ Return dict of classes from given file """
        classes = {}
        try:
            module = imp.load_source(fname, fname)
        except:
            return classes
        for clsname, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__ == fname:
                classes[clsname] = {'attrs': self.get_attrs(cls),
                                    'methods': self.get_methods(cls)}
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
        self.reference_json = reference_json
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
        self.horiz_spacing = 150

    def add_classes(self, classes):
        """ Classes from get_classes. """
        for cls in sorted(list(classes.keys())):
            self.add_class(cls, classes[cls]['attrs'], classes[cls]['methods'])

    def write(self, filename):
        """ Write gliffy to file. It will be overwrited. """
        with open(filename, 'w') as outfile:
            outfile.write(self.produce_gliffy())
            logging.warning('Wrote to file: ' + filename)

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
        constr[0]['HeightConstraint']['heightInfo'][0]['id'] = current_id + 0
        constr[0]['HeightConstraint']['heightInfo'][1]['id'] = current_id + 1
        constr[0]['HeightConstraint']['heightInfo'][2]['id'] = current_id + 3


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

        cls['x'] = 20 + self.cls_counter * self.horiz_spacing
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
    parser.add_argument("-p", "--project_directory", type=str,
                        default='.',
                        help="Path to project to analyse.")
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
    classes = ProjectParser(args.project_directory).get_classes()
    factory = ClassFactory()
    factory.add_classes(classes)
    factory.write(args.output_file)


if __name__ == '__main__':
    main()

