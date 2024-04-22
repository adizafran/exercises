import unittest

from general.textEditor.main import editor


class Test(unittest.TestCase):
    def test_1(self):
        actions = []
        actual = editor(actions)
        self.assertEqual(actual, [])

    def test_2(self):
        actions = [["Insert", "az"],
                   ["Left", "8"],
                   ["Print", "4"]]
        actual = editor(actions)
        self.assertEqual(actual, ["az"])

    def test_3(self):
        actions = [["Insert", "az"],
                   ["Right", "8"],
                   ["Print", "4"]]
        actual = editor(actions)
        self.assertEqual(actual, [""])

    def test_4(self):
        actions = [["Insert", "hello word"],
                   ["Left", "7"],
                   ["Delete", "3"],
                   ["Print", "4"]]
        actual = editor(actions)
        self.assertEqual(actual, ["word"])

    def test_5(self):
        actions = [["Insert", "hello word"],
                   ["Backspace", "8"],
                   ["Left", "7"],
                   ["Print", "4"]]
        actual = editor(actions)
        self.assertEqual(actual, ["he"])

    def test_6(self):
        actions = [["Insert", "hello word"],
                   ["Left", "8"],
                   ["Print", "4"]]
        actual = editor(actions)
        self.assertEqual(actual, ["llo "])


if __name__ == '__main__':
    unittest.main()
