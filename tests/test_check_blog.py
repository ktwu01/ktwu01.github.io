import importlib.util
import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from types import SimpleNamespace


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "check_blog.py"
SPEC = importlib.util.spec_from_file_location("check_blog", SCRIPT)
CHECK_BLOG = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK_BLOG)


class BlogWorkflowTests(unittest.TestCase):
    def test_check_mode_runs_every_read_only_check(self):
        commands = [command for _, command in CHECK_BLOG.workflow(fix=False)]

        self.assertEqual(len(commands), 5)
        self.assertTrue(all(command[0] == sys.executable for command in commands))
        self.assertIn([sys.executable, "scripts/lint_blog_format.py"], commands)
        self.assertIn(
            [sys.executable, "scripts/generate_language_links.py", "--check"],
            commands,
        )
        self.assertIn(
            [sys.executable, "scripts/check_bilingual_parity.py", "--check"],
            commands,
        )
        self.assertNotIn(
            [sys.executable, "scripts/generate_language_links.py"], commands
        )

    def test_fix_mode_generates_before_checking(self):
        commands = [command for _, command in CHECK_BLOG.workflow(fix=True)]

        self.assertEqual(
            commands[:2],
            [
                [sys.executable, "scripts/generate_author_notes.py"],
                [sys.executable, "scripts/generate_language_links.py"],
            ],
        )
        self.assertIn(
            [sys.executable, "scripts/generate_author_notes.py", "--check"],
            commands,
        )

    def test_workflow_stops_on_first_failure(self):
        calls = []

        def failing_runner(command, **kwargs):
            calls.append((command, kwargs))
            return SimpleNamespace(returncode=7)

        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            result = CHECK_BLOG.run_workflow(fix=True, runner=failing_runner)

        self.assertEqual(result, 7)
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][1]["cwd"], REPO_ROOT)


if __name__ == "__main__":
    unittest.main()
