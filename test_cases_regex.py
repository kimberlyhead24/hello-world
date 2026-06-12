import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))

class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_three(self):
        testcase = " Carla. She is the girl that cryed Abacadabra"
        expected = ['a', 'a', 'a', 'c', 'b', 'a', 'c', 'a', 'a', 'b']
        self.assertEqual(LetterCompiler(testcase), expected)
        
    def test_four(self):
        testcase = ""
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)
    
    def test_five(self):
        testcase = "XYZ 123 ?!"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)
        
    def test_six(self):
        testcase = "xyz a"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)
        
    def test_seven(self):
        testcase = "abc"
        expected = ['a', 'b']
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main(argv = ['first-arg-is-ignored'], exit = False)
