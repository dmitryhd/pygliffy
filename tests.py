#!/usr/bin/env python3

""" Test module for PyGliffy. """

import os
import sys
import unittest
import json

import pygliffy as pg


class TestGliffy(unittest.TestCase):
    """ Tets get classes and produce gliffy file. """

    def setUp(self):
        self.classes = {'Class1': {'attrs': ['attr1'], 'methods': ['m1', 'm2']},
                        'Class2': {'attrs': [], 'methods': []}}

    # test for multiple python files
    def test_get_classes(self):
        """ TestGliffy: test get classes without attrs from one file. """
        classes = pg.get_classes('example_data')
        expected = {'Class1': {'attrs': [], 'methods': ['m1']},
                    'Class2': {'attrs': [], 'methods': []}}
        self.assertEqual(classes, expected)

    def test_produce_gliffy(self):
        """ TestGliffy: test produce valid json for gliffy. Regression test."""
        factory = pg.ClassFactory()
        factory.add_classes(self.classes)
        gliffy = factory.produce_gliffy()
        gliffy_dict = json.loads(gliffy)
        with open('example_data/expected_output_test.json') as exp_file:
            expected = exp_file.read()
            expected_dict = json.loads(expected)
        self.assertDictEqual(gliffy_dict, expected_dict)

    def test_write_gliffy(self):
        """ TestGliffy: write tmp file. """
        factory = pg.ClassFactory()
        factory.add_classes(self.classes)
        factory.write('/tmp/gliffy_tmp.json')

    def test_command_line(self):
        """ TestGliffy: test command line. """
        sys.argv = ['gliffy', '-v']
        with self.assertRaises(SystemExit):
            pg.main()
        sys.argv = ['gliffy']
        pg.main()
        self.assertTrue(os.path.isfile('/tmp/gliffy.json'))
        sys.argv = ['gliffy', '-o', '/tmp/gliffy_1.json']
        pg.main()
        self.assertTrue(os.path.isfile('/tmp/gliffy_1.json'))




if __name__ == '__main__':
    unittest.main()

