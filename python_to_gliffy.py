#!/usr/bin/env python3

import pyclbr
import sys
import pprint
from pprint import pprint
sys.path.append('.')


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



def class_to_gliffy_json(class_name, functions):
    # omg here goes magick
    class_name_repr = class_name_to_gliffy_json(class_name, 2)
    pprint(class_name_repr)
    return

def class_name_to_gliffy_json(class_name, id_):
    class_json = [
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
    ]
    return class_json

def class_function_to_gliffy_json(class_function, id_):
    function_json = [

    ]



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
    class_to_gliffy_json(cls, classes[cls])
