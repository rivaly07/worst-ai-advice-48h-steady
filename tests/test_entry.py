import os
from pathlib import Path
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]


class EntryProgramTests(unittest.TestCase):
    def test_output_contract_outside_repository(self):
        with tempfile.TemporaryDirectory(prefix="entry-test-") as output_dir:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=output_dir)
            subprocess.run(
                ["python3", "-P", "-s", str(REPO / "main.py")],
                cwd="/",
                env=env,
                check=True,
            )
            raw = (Path(output_dir) / "entry.txt").read_bytes()

        text = raw.decode("utf-8")
        self.assertEqual(text.count("\n"), 1)
        line = text[:-1]
        self.assertTrue(line.strip())
        self.assertGreaterEqual(len(line), 1)
        self.assertLessEqual(len(line), 140)


if __name__ == "__main__":
    unittest.main()
