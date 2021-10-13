import unittest
import foo


def expensive_function():
    """Pretend this uses a lot of resources."""
    return (1, 0, -1)

def make_safe(val):
    """This might clean up memory or free up resources"""
    pass

class TestSolveQuadratic(unittest.TestCase):

    def setUp(self):
        """Runs first."""
        # Can create values stored in the class instance self

        self.val = expensive_function()

    def test_solve_quadratic_part_one(self):

        self.assertEqual(foo.solve_quadratic(*self.val), (-1.0, 1.0))
        self.assertEqual(foo.solve_quadratic(1, 0, 0), 0.0)

    def test_solve_quadratic_part_two(self):
        self.assertEqual(foo.solve_quadratic(1, 0, 1), None)

    def tearDown(self):
        """Called at the end if we need to clean up."""
        make_safe(self.val)


unittest.main()
