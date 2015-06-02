#!/usr/bin/env python3

import pyclbr
import sys
import pprint
from pprint import pprint
sys.path.append('.')
import json


def get_classes(core_modules, prefix):
    classes = {}  # class: list of functions
    for core_module in core_modules:
        classes_presentation = pyclbr.readmodule(prefix + core_module)
        for cls, cls_obj in classes_presentation.items():
            classes[cls] = sorted(list(cls_obj.methods.keys()))
    return classes


def to_sting(core_modules, prefix):
    classes = get_classes(core_modules, prefix)
    return pprint.pformat(classes)


def class_to_gliffy_json(class_name, method_names):
    # omg here goes magick
    id_ = 1
    class_name_repr = class_name_to_gliffy_json(class_name, id_)
    id_ += 2
    #pprint(class_name_repr)
    method_repr = methods_to_gliffy_json(method_names, id_)
    #pprint(method_repr)
    objects = [class_name_repr, method_repr]
    gliffy_json = to_gliffy(objects)
    return gliffy_json


def class_name_to_gliffy_json(class_name, id_):
    # add id_ + 2
    class_json = { 
        "children": [ # class name
            {
                "children": None,
                "graphic": {
                    "Text": {
                        "hposition": "none",
                        "html": "<p style=\"text-align: center;\"><span class=\"gliffy-placeholder-text\" style=\"font-family: Arial; font-size: 12px; font-weight: bold; text-decoration: none; line-height: 14px; color: rgb(0, 0, 0);\">" + class_name + "</span></p>",
                        "overflow": "none",
                        "paddingBottom": 2,
                        "paddingLeft": 2,
                        "paddingRight": 2,
                        "paddingTop": 2,
                        "tid": None,
                        "valign": "top",
                        "vposition": "none"
                    },
                    "type": "Text"
                },
                "height": 18,
                "id": id_ + 1,
                "lockAspectRatio": False,
                "lockShape": False,
                "order": "auto",
                "rotation": 0,
                "uid": None,
                "width": 140,
                "x": 0,
                "y": 0
            }
        ],
        "constraints": { # hline
                        "constraints": [
                            {
                                "HeightConstraint": {
                                    "growParent": True,
                                    "heightInfo": [
                                        {
                                            "id": id_ + 1,
                                            "magnitude": 1
                                        }
                                    ],
                                    "isMin": False,
                                    "padding": 0
                                },
                                "type": "HeightConstraint"
                            }
                        ]
                       },
        "graphic": { # hline 2
                    "Shape": {
                        "dropShadow": True,
                        "fillColor": "#FFFFFF",
                        "gradient": False,
                        "opacity": 1,
                        "shadowX": 4,
                        "shadowY": 4,
                        "state": 0,
                        "strokeColor": "#000000",
                        "strokeWidth": 2,
                        "tid": "com.gliffy.stencil.rectangle.basic_v1"
                    },
                    "type": "Shape"
                   },
        "height": 18,
        "id": id_,
        "lockAspectRatio": False,
        "lockShape": False,
        "order": "auto",
        "rotation": 0,
        "uid": None,
        "width": 140,
        "x": 0,
        "y": 0
    }

    return class_json

def methods_to_gliffy_json(method_names, id_):
    method_names_str = '<br>'.join(method_names)
    method_json = { # cl methods
                   "children": [ # name
                       { # method
                        "children": None,
                        "graphic": {
                            "Text": {
                                "hposition": "none",
                                "html": "<p style=\"text-align: left;\"><span class=\"gliffy-placeholder-text\" style=\"font-family: Arial; font-size: 12px; font-weight: normal; text-decoration: none; line-height: 14px; color: rgb(0, 0, 0);\"> " + method_names_str + " </span></p>",
                                "overflow": "none",
                                "paddingBottom": 2,
                                "paddingLeft": 2,
                                "paddingRight": 2,
                                "paddingTop": 2,
                                "tid": None,
                                "valign": "top",
                                "vposition": "none"
                            },
                            "type": "Text"
                        },
                        "height": 18,
                        "id": id_ + 1,
                        "lockAspectRatio": False,
                        "lockShape": False,
                        "order": "auto",
                        "rotation": 0,
                        "uid": None,
                        "width": 140,
                        "x": 0,
                        "y": 0
                       }
                   ],
                   "constraints": {
                       "constraints": [
                           {
                               "HeightConstraint": {
                                   "growParent": False,
                                   "heightInfo": [
                                       {
                                           "id": 0,
                                           "magnitude": 1
                                       },
                                       {
                                           "id": 1,
                                           "magnitude": -1
                                       },
                                       {
                                           "id": 3,
                                           "magnitude": -1
                                       }
                                   ],
                                   "isMin": False,
                                   "padding": 0
                               },
                               "type": "HeightConstraint"
                           },
                           {
                               "PositionConstraint": {
                                   "nodeId": 3,
                                   "px": 0,
                                   "py": 1
                               },
                               "type": "PositionConstraint"
                           }
                       ]
                   },
    "graphic": {
        "Shape": {
            "dropShadow": True,
            "fillColor": "#FFFFFF",
            "gradient": False,
            "opacity": 1,
            "shadowX": 4,
            "shadowY": 4,
            "state": 0,
            "strokeColor": "#000000",
            "strokeWidth": 2,
            "tid": "com.gliffy.stencil.rectangle.basic_v1"
        },
        "type": "Shape"
    },
    "height": 39,
    "id": id_,
    "lockAspectRatio": False,
    "lockShape": False,
    "order": "auto",
    "rotation": 0,
    "uid": None,
    "width": 140,
    "x": 0,
    "y": 36
    }
    return method_json



def to_gliffy(objects):
    out = {
    "contentType": "application/gliffy+json",
    "embeddedResources": {
        "index": 0,
        "resources": []
    },
    "metadata": {
        "exportBorder": False,
        "revision": 0,
        "title": "untitled"
    },
    "stage": {
        "autoFit": True,
        "background": "#FFFFFF",
        "drawingGuidesOn": True,
        "exportBorder": False,
        "gridOn": True,
        "height": 0,
        "lineStyles": {},
        "maxHeight": 5000,
        "maxWidth": 5000,
        "nodeIndex": 0,
        "objects": objects,
        "pageBreaksOn": False,
        "printGridOn": False,
        "printPaper": "LETTER",
        "printPortrait": True,
        "printShrinkToFit": False,
        "shapeStyles": {},
        "snapToGrid": True,
        "textStyles": {},
        "themeData": None,
        "width": 0
    },
    "version": "1.1"
    }
    return out


if __name__ == '__main__':
    # core_modules = ['alert_handler',  'alerts',  'bx_interface',  'collector',  'context',  'database',  'devices',  'download',  'emergency_checker',  'nodes_test',  'parameters',  'power_control']
    core_modules = ['python_classes']
    prefix = 'example_data.'
    classes = get_classes(core_modules, prefix)
    cls = list(classes.keys())[0]
    gliffy = class_to_gliffy_json(cls, classes[cls])
    # pprint(gliffy)
    print(json.dumps(gliffy))
