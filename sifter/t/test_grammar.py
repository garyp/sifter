# type: ignore

import unittest

import sifter.extension
from sifter.grammar.state import EvaluationState


class TestEvaluationState(unittest.TestCase):

    def setUp(self) -> None:
        sifter.extension.register('ext1')
        sifter.extension.register('ext2')
        self.state = EvaluationState()

    def test_require_extension(self) -> None:
        self.state.require_extension('ext1')
        self.assertTrue(self.state.check_required_extension('ext1', 'ext1'))
        self.assertRaises(
            RuntimeError,
            self.state.check_required_extension,
            'ext2',
            'ext2',
        )


if __name__ == '__main__':
    unittest.main()
