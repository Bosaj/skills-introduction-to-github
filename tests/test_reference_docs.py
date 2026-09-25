import os
import unittest

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class TestGitReferenceManuals(unittest.TestCase):
    def test_reference_directory_has_manuals(self):
        ref_dir = os.path.join(repo_root, "reference")
        self.assertTrue(os.path.isdir(ref_dir), "reference directory must exist")
        md_files = [f for f in os.listdir(ref_dir) if f.endswith(".md")]
        self.assertGreater(len(md_files), 20, "Should have more than 20 git command reference manuals")

        for f in md_files:
            file_path = os.path.join(ref_dir, f)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
            self.assertGreater(len(content), 100, f"{f} should be a comprehensive reference")

    def test_advanced_references_exist(self):
        refs_dir = os.path.join(repo_root, "references")
        self.assertTrue(os.path.isdir(refs_dir), "references directory must exist")
        md_files = [f for f in os.listdir(refs_dir) if f.endswith(".md")]
        self.assertGreater(len(md_files), 10, "Should have more than 10 advanced topic manuals")


if __name__ == "__main__":
    unittest.main()
