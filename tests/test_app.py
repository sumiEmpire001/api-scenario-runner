import unittest
from app import evaluate
class Tests(unittest.TestCase):
    def test_pass(self):
        r=evaluate([{"actual":{"status":200,"body":{"ok":True}},"expected":{"status":200,"body":{"ok":True}}}])
        self.assertEqual(r["passed"],1)
    def test_failure(self):
        r=evaluate([{"actual":{"status":500},"expected":{"status":200}}])
        self.assertEqual(r["results"][0]["failures"],["status"])
    def test_partial_body(self):
        r=evaluate([{"actual":{"body":{"a":1,"b":2}},"expected":{"body":{"a":1}}}])
        self.assertEqual(r["passed"],1)
    def test_bad_input(self):
        with self.assertRaises(ValueError): evaluate({})
if __name__=="__main__": unittest.main()
