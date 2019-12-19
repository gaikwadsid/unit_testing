import unittest


class ListManipulator:
    def __init__(self, list):
        self.list = list

    def min(self):
        if len(self.list) == 0:
            return None

        min = self.list[0]
        for item in self.list:
            if item < min:
                min = item
        return min

    def max(self):
        if len(self.list) == 0:
            return None

        max = self.list[0]
        for item in self.list:
            if item > max:
                max = item
        return max

    def remove(self, value):
        to_remove = []
        for i, item in enumerate(self.list):
            if item == value:
                to_remove.append(i)

        removed_count = 0
        for index in to_remove:
            self.list.pop(index - removed_count)
            removed_count += 1


class Testmin(unittest.TestCase):
    def test1(self):
        li = ListManipulator([1, 2, 3, 4])
        self.assertEqual(li.min(), 1)

    def test2(self):
        li = ListManipulator([1, 2, 1, 4])
        self.assertEqual(li.min(), 1)


class Testmax(unittest.TestCase):
    def test1(self):
        li = ListManipulator([1, 2, 3, 4])
        self.assertEqual(li.max(), 4)

    def test2(self):
        li = ListManipulator([1, 4, 3, 4])
        self.assertEqual(li.max(), 4)


class Testremove(unittest.TestCase):
    def test1(self):
        li = ListManipulator([1, 2, 3, 4])
        li.remove(2)
        self.assertEqual(li.list, [1, 3, 4])

    def test2(self):
        li = ListManipulator([1, 2, 2, 4])
        li.remove(2)
        self.assertEqual(li.list, [1, 4])

    def test2(self):
        li = ListManipulator([1, 2, 3, 4])
        li.remove(5)
        self.assertEqual(li.list, [1, 2, 3, 4])

unittest.main()

