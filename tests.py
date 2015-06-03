#!/usr/bin/env python3

import unittest
import json

import python_to_gliffy as pg


class TestGliffy(unittest.TestCase):
    """ Tets get classes and produce gliffy file. """

    # test for multiple python files
    def test_get_classes(self):
        """ TestGliffy: test get classes without attrs from one file. """
        core_modules = ['python_classes']
        prefix = 'example_data.'
        classes = pg.get_classes(core_modules, prefix)
        expected = {'Class1': {'attrs': [], 'methods': ['m1']},
                    'Class2': {'attrs': [], 'methods': []}}
        self.assertEqual(classes, expected)

    def test_produce_gliffy(self):
        """ TestGliffy: test produce valid json for gliffy. Regression test."""
        classes = {'Class1': {'attrs': ['attr1'], 'methods': ['m1', 'm2']},
                   'Class2': {'attrs': [], 'methods': []}}
        factory = pg.ClassFactory()
        factory.add_classes(classes)
        gliffy = factory.produce_gliffy()
        gliffy_dict = json.loads(gliffy)
        with open('example_data/expected_output_test.json') as exp_file:
            expected = exp_file.read()
            expected_dict = json.loads(expected)
        self.assertDictEqual(gliffy_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()

