import unittest


def formatInt(num, sep=",", size=3):
    # Preconditions: violating these doesn't indicate a test failure.
    assert type(num) == int
    assert type(sep) == str
    assert type(size) == int and size >= 0
    # Implementation
    chunk = 10 ** size
    groups = []
    while num > chunk:
        groups.insert(0,"%0*d" %(size,num % chunk))
        num = num // chunk
    groups.insert(0, str(num % chunk)) # prepend
    return sep.join(groups)

class FormatTests(unittest.TestCase):
    def testFiveDigitWithDefaults(self):
        self.assertEqual(formatInt(32767), "32,767")

    def testsixdigit(self):
        self.assertEqual(formatInt(1948800, size=4), "194,8800")

    def testseven(self):
        self.assertEqual(formatInt(1948576, sep="::"), "1::948::576")

    def testzero(self):
        self.assertEqual(formatInt(0), "0")
    def testchunkzeroes(self):
        self.assertEqual(formatInt(1948576), "1,948,576")



if __name__ == "__main__":
    unittest.main()
