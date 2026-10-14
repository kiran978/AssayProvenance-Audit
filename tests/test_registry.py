import pathlib
import subprocess
import sys
import unittest

class RegistryTests(unittest.TestCase):
    def test_stage4_integrity(self):
        root = pathlib.Path(__file__).resolve().parents[1]
        subprocess.run([sys.executable, str(root / "src/validate_R1_evidence.py")],
                       check=True, cwd=root)

if __name__ == "__main__":
    unittest.main()
