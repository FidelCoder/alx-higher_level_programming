#!/usr/bin/python3
"""Provides unittest for the 'Square' class provided by the 'models' module
"""

import unittest
import sys
from io import StringIO
from os import chdir, getcwd, remove
from shutil import rmtree
from tempfile import mkdtemp

from models.base import Base
from models.square import Square
from models.square import Square


class SquareTest(unittest.TestCase):
    """Class Square unittests"""

    def setUp(self):
        """Create a temporary directory and Base instance
        """
        chdir(mkdtemp())

    def tearDown(self):
        """Remove temporary files and directories
        """
        rmtree(getcwd(), ignore_errors=True)

    def test_check_id(self):
        """Test if id of Square increments"""
        s1 = Square(10)
        s2 = Square(10)
        s3 = Square(10)
        self.assertGreater(s2.id, s1.id)
        self.assertGreater(s3.id, s2.id)

    def test_check_input_id(self):
        """Test if input id gets set"""
        s3 = Square(2, 0, 0, 12)
        self.assertEqual(s3.id, 12)

    def test_check_width(self):
        """Test width set of square"""
        s1 = Square(2)
        self.assertEqual(s1.width, 2)

        s2 = Square(10)
        self.assertEqual(s2.width, 10)

        s3 = Square(2, 0, 0, 12)
        self.assertEqual(s3.width, 2)

    def test_check_width_TypeError_01(self):
        """Test TypeError for width in Square"""
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Square,
            'string', 0, 0, 12
        )

    def test_check_width_TypeError_02(self):
        """Test TypeError for width in Square"""
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Square,
            [6, 4, 9, 9], 0, 0, 12
        )

    def test_check_width_ValueError(self):
        """Test TypeError for width in Square"""
        self.assertRaisesRegex(
            ValueError,
            'width must be > 0',
            Square,
            -1, 0, 0, 12
        )

    def test_check_height(self):
        """Test height of """
        s1 = Square(2)
        self.assertEqual(s1.height, 2)

        s2 = Square(10)
        self.assertEqual(s2.height, 10)

        s3 = Square(3, 0, 0, 12)
        self.assertEqual(s3.height, 3)

    def test_check_x(self):
        """Test x of square"""
        s1 = Square(2)
        self.assertEqual(s1.x, 0)

        s2 = Square(10, 6)
        self.assertEqual(s2.x, 6)

        s3 = Square(2, 3, 9, 12)
        self.assertEqual(s3.x, 3)

        s4 = Square(2, 0, 3, 12)
        self.assertEqual(s4.x, 0)

    def test_check_x_TypeError_01(self):
        """Test TypeError for x in Square"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Square,
            2, 'string''', 0, 12
        )

    def test_check_x_TypeError_02(self):
        """Test TypeError for x in Square"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Square,
            2, [1, 2, 3, 4], 0, 12
        )

    def test_check_x_ValueError(self):
        """Test ValueError for x in Square"""
        self.assertRaisesRegex(
            ValueError,
            'x must be >= 0',
            Square,
            2, -1, 0, 12
        )

    def test_check_y(self):
        """Test y of square"""
        s1 = Square(2)
        self.assertEqual(s1.y, 0)

        s2 = Square(10, 6, 4)
        self.assertEqual(s2.y, 4)

        s3 = Square(2, 3, 9, 12)
        self.assertEqual(s3.y, 9)

        s4 = Square(2, 3, 0, 12)
        self.assertEqual(s4.y, 0)

    def test_check_y_TypeError_01(self):
        """Test TypeError for y in Square"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Square,
            2, 0, 'string', 12
        )

    def test_check_y_TypeError_02(self):
        """Test TypeError for y in Square"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Square,
            2, 0, [1, 2, 3, 4], 12
        )

    def test_check_y_TypeError_(self):
        """Test TypeError for y in Square"""
        self.assertRaisesRegex(
            ValueError,
            'y must be >= 0',
            Square,
            2, 0, -6, 12
        )

    def test_update(self):
        """Test update"""
        output = StringIO()
        sys.stdout = output
        s1 = Square(10, 10, 10)
        s1.update(89)
        s1.update(89, 2)
        s1.update(89, 2, 3)
        s1.update(89, 2, 3, 4)
        print(s1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (89) 3/4 - 2\n"

    def test_update_extra(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        s1 = Square(10, 10, 10)
        s1.update(89, 2, 3, 4, 5, 6, 7)
        print(s1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (89) 3/4 - 2\n"

    def test_update_no_param(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        s1 = Square(10, 10, 10, 1)
        s1.update()
        print(s1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (1) 10/10 - 10\n"

    def test_kwargs(self):
        """Test kwargs"""
        output = StringIO()
        sys.stdout = output
        s1 = Square(10, 10, 10, 1)
        s1.update(x=1, size=2, y=3)
        print(s1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (1) 1/3 - 2\n"

    def test_kwargs_extra_keys(self):
        """Test kwargs with extra parameters"""
        output = StringIO()
        sys.stdout = output
        s1 = Square(10, 10, 10, 1)
        s1.update(x=1, size=2, y=3, banu=89)
        print(s1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (1) 1/3 - 2\n"

    def test_to_dictionary(self):
        """Test conversion to dictionary"""
        r = Square(1, 1, 1, 1)
        d = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), d)
        r.my_fun_new_attr = 42
        self.assertEqual(r.to_dictionary(), d)

    def test_inputs_base(self):
        b1 = Base()
        b2 = Base()
        self.assertGreater(b2.id, b1.id)
        b3 = Base(12)
        self.assertIs(b3.id, 12)

    def test_inputs_square(self):
        s1 = Square(2, 3, 4, 5)
        self.assertEqual(str(s1), "[Square] (5) 3/4 - 2")
        s2 = Square(2, 3, 4, id=1)
        self.assertEqual(str(s2), "[Square] (1) 3/4 - 2")
        s3 = Square(2, 3, id=1)
        self.assertEqual(str(s3), "[Square] (1) 3/0 - 2")
        s4 = Square(2, id=1)
        self.assertEqual(str(s4), "[Square] (1) 0/0 - 2")

    def test_square_width(self):
        """Test the __init__ method
        """
        square = Square(1)
        self.assertEqual(square.width, 1)

    def test_square_height(self):
        """Test the __init__ method
        """
        square = Square(1)
        self.assertEqual(square.height, 1)

    def test_square_x(self):
        """Test the __init__ method
        """
        square = Square(1)
        self.assertEqual(square.x, 0)

    def test_square_y(self):
        """Test the __init__ method
        """
        square = Square(1)
        self.assertEqual(square.y, 0)

    def test_square_id(self):
        """Test the __init__ method
        """
        square = Square(1)
        self.assertIsInstance(square.id, int)
        self.assertGreater(square.id, 0)

    def test_init_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Square(1), Base)
        self.assertIsInstance(Square(1), Square)
        self.assertIsInstance(Square(1, id=None), Square)
        self.assertIsInstance(Square(1, 0, 0), Square)
        self.assertIsInstance(Square(1, 0, 0, 0), Square)
        self.assertIsInstance(Square(1, id=0), Square)
        self.assertIsInstance(Square(1, id=0.0), Square)
        self.assertIsInstance(Square(1, id="0"), Square)
        self.assertIsInstance(Square(1, id=(0,)), Square)
        self.assertIsInstance(Square(1, id=[0]), Square)
        self.assertIsInstance(Square(1, id={0}), Square)
        self.assertIsInstance(Square(1, id={0: 0}), Square)
        self.assertIsInstance(Square(1, id=True), Square)
        self.assertIsInstance(Square(1, id=type), Square)

    def test_init_id_equality(self):
        """Test the __init__ method
        """
        square = Square(1)
        self.assertNotEqual(square.id, Square(1).id)
        self.assertNotEqual(square.id, Square(1, id=None).id)
        self.assertEqual(Square(1, 1, 1, 0).id, 0)
        self.assertEqual(Square(1, id=0.0).id, 0.0)
        self.assertEqual(Square(1, id="0").id, "0")
        self.assertEqual(Square(1, id=[0]).id, [0])
        self.assertEqual(Square(1, id={0}).id, {0})
        self.assertEqual(Square(1, id=(0, 0)).id, (0, 0))
        self.assertEqual(Square(1, id={0: 0}).id, {0: 0})

    def test_init_id_identity(self):
        """Test the __init__ method
        """
        self.assertIs(Square(1, id=True).id, True)
        self.assertIs(Square(1, id=type).id, type)

    def test_init_id_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Square(1).id, int)
        self.assertIsInstance(Square(1, id=None).id, int)

    def test_init_raises(self):
        """Test the __init__ method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\b__init__\\(\\) missing 1 required positional argument\\b.*",
            Square
        )

    def test_create_type(self):
        """Test the create method
        """
        self.assertIsInstance(Square.create(), Square)
        self.assertIsInstance(Square.create(id=None), Square)
        self.assertIsInstance(Square.create(id=0), Square)
        self.assertIsInstance(Square.create(id=0.0), Square)
        self.assertIsInstance(Square.create(id="0"), Square)
        self.assertIsInstance(Square.create(id=(0,)), Square)
        self.assertIsInstance(Square.create(id=[0]), Square)
        self.assertIsInstance(Square.create(id={0}), Square)
        self.assertIsInstance(Square.create(id={0: 0}), Square)
        self.assertIsInstance(Square.create(id=True), Square)
        self.assertIsInstance(Square.create(id=type), Square)

    def test_create_id_equality(self):
        """Test the create method
        """
        square = Square(1)
        self.assertNotEqual(square.id, Square.create().id)
        self.assertNotEqual(square.id, Square.create(id=None).id)
        self.assertEqual(Square.create(id=0).id, 0)
        self.assertEqual(Square.create(id=0.0).id, 0.0)
        self.assertEqual(Square.create(id="0").id, "0")
        self.assertEqual(Square.create(id=(0,)).id, (0,))
        self.assertEqual(Square.create(id=[0]).id, [0])
        self.assertEqual(Square.create(id={0}).id, {0})
        self.assertEqual(Square.create(id={0: 0}).id, {0: 0})

    def test_create_id_identity(self):
        """Test the create method
        """
        self.assertIs(Square.create(id=True).id, True)
        self.assertIs(Square.create(id=type).id, type)
        self.assertIs(Square.create(id=None).id, None)

    def test_create_id_type(self):
        """Test the create method
        """
        self.assertIsInstance(Square.create().id, int)

    def test_create_raises(self):
        """Test the create method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\bcreate\\(\\) takes 1 positional argument\\b.*",
            Square.create, 0
        )

    def test_save_to_file(self):
        """Test the save_to_file method
        """
        square = Square(1)
        types = (int, float, str, tuple, list, dict, bool)
        insts = [square] + [Square(1, id=t()) for t in types]
        fname = 'Square.json'
        try:
            remove(fname)
        except FileNotFoundError:
            pass
        self.assertIsNone(Square.save_to_file(None))
        with open(fname) as ifile:
            self.assertEqual(ifile.read(), '[]')
        for index in range(len(insts)):
            self.assertIsNone(Square.save_to_file(insts[index:]))
            with open(fname) as ifile:
                self.assertEqual(ifile.read(), Square.to_json_string(
                    [obj.to_dictionary() for obj in insts[index:]]
                ))
