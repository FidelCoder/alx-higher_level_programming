#!/usr/bin/python3
"""Provides unittest for the 'Rectangle' class provided by the 'models' module
"""

import unittest
import sys
from io import StringIO
from os import chdir, getcwd, remove
from shutil import rmtree
from tempfile import mkdtemp

from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Class Rectangle unittests"""

    def setUp(self):
        """Create a temporary directory and Base instance
        """
        chdir(mkdtemp())

    def tearDown(self):
        """Remove temporary files and directories
        """
        rmtree(getcwd(), ignore_errors=True)

    def test_check_id(self):
        """Test if id of Rectangle increments"""
        r1 = Rectangle(2, 10)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(2, 10)
        self.assertGreater(r2.id, r1.id)
        self.assertGreater(r3.id, r2.id)

    def test_check_input_id(self):
        """Test if input id gets set"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_check_width(self):
        """Test width set of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(5, 2, 0, 0, 12)
        self.assertEqual(r3.width, 5)

    def test_check_width_TypeError_01(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            'string', 2, 0, 0, 12
        )

    def test_check_width_TypeError_02(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            [6, 4, 9, 9], 2, 0, 0, 12
        )

    def test_check_width_ValueError(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'width must be > 0',
            Rectangle,
            -1, 2, 0, 0, 12
        )

    def test_check_height(self):
        """Test height of """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)

        r3 = Rectangle(5, 3, 0, 0, 12)
        self.assertEqual(r3.height, 3)

    def test_check_height_TypeError_01(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'height must be an integer',
            Rectangle,
            2, 'string', 0, 0, 12
        )

    def test_check_height_TypeError_02(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'height must be an integer',
            Rectangle,
            3, [1, 2, 3, 4], 0, 0, 12
        )

    def test_check_height_ValueError(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'height must be > 0',
            Rectangle,
            1, -2, 0, 0, 12
        )

    def test_check_x(self):
        """Test x of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(2, 10, 6)
        self.assertEqual(r2.x, 6)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.x, 3)

        r4 = Rectangle(5, 2, 0, 3, 12)
        self.assertEqual(r4.x, 0)

    def test_check_x_TypeError_01(self):
        """Test TypeError for x in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Rectangle,
            4, 2, 'string''', 0, 12
        )

    def test_check_x_TypeError_02(self):
        """Test TypeError for x in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Rectangle,
            4, 2, [1, 2, 3, 4], 0, 12
        )

    def test_check_x_ValueError(self):
        """Test ValueError for x in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'x must be >= 0',
            Rectangle,
            4, 2, -1, 0, 12
        )

    def test_check_y(self):
        """Test y of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 6, 4)
        self.assertEqual(r2.y, 4)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.y, 9)

        r4 = Rectangle(5, 2, 3, 0, 12)
        self.assertEqual(r4.y, 0)

    def test_check_y_TypeError_01(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Rectangle,
            4, 2, 0, 'string', 12
        )

    def test_check_y_TypeError_02(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Rectangle,
            4, 2, 0, [1, 2, 3, 4], 12
        )

    def test_check_y_TypeError_(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'y must be >= 0',
            Rectangle,
            4, 2, 0, -6, 12
        )

    def test_update(self):
        """Test update"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_extra(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6, 7)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_no_param(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update()
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 10/10 - 10/10\n"

    def test_kwargs(self):
        """Test kwargs"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(x=1, height=2, y=3, width=4)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 1/3 - 4/2\n"

    def test_kwargs_extra_keys(self):
        """Test kwargs with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(x=1, height=2, y=3, width=4, banu=89)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 1/3 - 4/2\n"

    def test_to_dictionary(self):
        """Test conversion to dictionary"""
        r = Rectangle(1, 1, 1, 1, 1)
        d = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), d)
        r.my_fun_new_attr = 42
        self.assertEqual(r.to_dictionary(), d)

    def test_inputs_base(self):
        b1 = Base()
        b2 = Base()
        self.assertGreater(b2.id, b1.id)
        b3 = Base(12)
        self.assertIs(b3.id, 12)

#   def test_square_update(self):
#       """ test square update """
#       s1 = Square(17)
#       print(s1)
#       self.assertEqual(str(s1, "[Square] (1) 0/0 - 17"))

    def test_inputs_rectangle(self):
        Rectangle._Base__nb_objects = 0
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r2), "[Rectangle] (1) 3/4 - 1/2")
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(str(r3), "[Rectangle] (2) 3/0 - 1/2")
        r4 = Rectangle(1, 2)
        self.assertEqual(str(r4), "[Rectangle] (3) 0/0 - 1/2")

    def test_rectangle_width(self):
        """Test the __init__ method
        """
        rect = Rectangle(1, 1)
        self.assertEqual(rect.width, 1)

    def test_rectangle_height(self):
        """Test the __init__ method
        """
        rect = Rectangle(1, 1)
        self.assertEqual(rect.height, 1)

    def test_rectangle_x(self):
        """Test the __init__ method
        """
        rect = Rectangle(1, 1)
        self.assertEqual(rect.x, 0)

    def test_rectangle_y(self):
        """Test the __init__ method
        """
        rect = Rectangle(1, 1)
        self.assertEqual(rect.y, 0)

    def test_rectangle_id(self):
        """Test the __init__ method
        """
        rect = Rectangle(1, 1)
        self.assertIsInstance(rect.id, int)
        self.assertGreater(rect.id, 0)

    def test_init_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Rectangle(1, 1), Base)
        self.assertIsInstance(Rectangle(1, 1), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=None), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, 0, 0), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, 0, 0, 0), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=0), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=0.0), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id="0"), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=(0,)), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=[0]), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id={0}), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id={0: 0}), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=True), Rectangle)
        self.assertIsInstance(Rectangle(1, 1, id=type), Rectangle)

    def test_init_id_equality(self):
        """Test the __init__ method
        """
        rect = Rectangle(1, 1)
        self.assertNotEqual(rect.id, Rectangle(1, 1).id)
        self.assertNotEqual(rect.id, Rectangle(1, 1, id=None).id)
        self.assertEqual(Rectangle(1, 1, 1, 1, 0).id, 0)
        self.assertEqual(Rectangle(1, 1, id=0.0).id, 0.0)
        self.assertEqual(Rectangle(1, 1, id="0").id, "0")
        self.assertEqual(Rectangle(1, 1, id=[0]).id, [0])
        self.assertEqual(Rectangle(1, 1, id={0}).id, {0})
        self.assertEqual(Rectangle(1, 1, id=(0, 0)).id, (0, 0))
        self.assertEqual(Rectangle(1, 1, id={0: 0}).id, {0: 0})

    def test_init_id_identity(self):
        """Test the __init__ method
        """
        self.assertIs(Rectangle(1, 1, id=True).id, True)
        self.assertIs(Rectangle(1, 1, id=type).id, type)

    def test_init_id_type(self):
        """Test the __init__ method
        """
        self.assertIsInstance(Rectangle(1, 1).id, int)
        self.assertIsInstance(Rectangle(1, 1, id=None).id, int)

    def test_init_raises(self):
        """Test the __init__ method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\b__init__\\(\\) missing 2 required positional arguments\\b.*",
            Rectangle
        )

    def test_create_type(self):
        """Test the create method
        """
        self.assertIsInstance(Rectangle.create(), Rectangle)
        self.assertIsInstance(Rectangle.create(id=None), Rectangle)
        self.assertIsInstance(Rectangle.create(id=0), Rectangle)
        self.assertIsInstance(Rectangle.create(id=0.0), Rectangle)
        self.assertIsInstance(Rectangle.create(id="0"), Rectangle)
        self.assertIsInstance(Rectangle.create(id=(0,)), Rectangle)
        self.assertIsInstance(Rectangle.create(id=[0]), Rectangle)
        self.assertIsInstance(Rectangle.create(id={0}), Rectangle)
        self.assertIsInstance(Rectangle.create(id={0: 0}), Rectangle)
        self.assertIsInstance(Rectangle.create(id=True), Rectangle)
        self.assertIsInstance(Rectangle.create(id=type), Rectangle)

    def test_create_id_equality(self):
        """Test the create method
        """
        rect = Rectangle(1, 1)
        self.assertNotEqual(rect.id, Rectangle.create().id)
        self.assertNotEqual(rect.id, Rectangle.create(id=None).id)
        self.assertEqual(Rectangle.create(id=0).id, 0)
        self.assertEqual(Rectangle.create(id=0.0).id, 0.0)
        self.assertEqual(Rectangle.create(id="0").id, "0")
        self.assertEqual(Rectangle.create(id=(0,)).id, (0,))
        self.assertEqual(Rectangle.create(id=[0]).id, [0])
        self.assertEqual(Rectangle.create(id={0}).id, {0})
        self.assertEqual(Rectangle.create(id={0: 0}).id, {0: 0})

    def test_create_id_identity(self):
        """Test the create method
        """
        self.assertIs(Rectangle.create(id=True).id, True)
        self.assertIs(Rectangle.create(id=type).id, type)
        self.assertIs(Rectangle.create(id=None).id, None)

    def test_create_id_type(self):
        """Test the create method
        """
        self.assertIsInstance(Rectangle.create().id, int)

    def test_create_raises(self):
        """Test the create method
        """
        self.assertRaisesRegex(
            TypeError,
            ".*\\bcreate\\(\\) takes 1 positional argument\\b.*",
            Rectangle.create, 0
        )

    def test_save_to_file(self):
        """Test the save_to_file method
        """
        rect = Rectangle(1, 1)
        types = (int, float, str, tuple, list, dict, bool)
        insts = [rect] + [Rectangle(1, 1, id=t()) for t in types]
        fname = 'Rectangle.json'
        try:
            remove(fname)
        except FileNotFoundError:
            pass
        self.assertIsNone(Rectangle.save_to_file(None))
        with open(fname) as ifile:
            self.assertEqual(ifile.read(), '[]')
        for index in range(len(insts)):
            self.assertIsNone(Rectangle.save_to_file(insts[index:]))
            with open(fname) as ifile:
                self.assertEqual(ifile.read(), Rectangle.to_json_string(
                    [obj.to_dictionary() for obj in insts[index:]]
                ))
