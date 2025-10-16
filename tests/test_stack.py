import unittest

from src.stack import RPNStack


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        stack = RPNStack()
        stack.push(-5.0)
        stack.push(3.0)
        self.assertEqual(stack.pop(), 3.0)
        self.assertEqual(stack.pop(), -5.0)

    def test_do_operation(self):
        stack = RPNStack()
        self.assertEqual(stack.do_operation('+', 2.0, 3.0), 5.0)
        self.assertEqual(stack.do_operation('-', -5.0, 3.0), -8.0)
        self.assertEqual(stack.do_operation('/', 6.0, 3.0), 2.0)

    def test_apply_operator(self):
        stack = RPNStack()
        stack.push(2.0)
        stack.push(3.0)
        stack.apply_operator('+')
        self.assertEqual(stack.get_result(), 5.0)


if __name__ == "__main__":
    unittest.main()
