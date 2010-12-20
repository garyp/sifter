from sieve.grammar.test import SieveTest

# section 5.3
class SieveTestAnyOf(SieveTest):

    RULE_IDENTIFIER = 'ANYOF'

    def __init__(self, arguments=None, tests=None):
        super(SieveTestAnyOf, self).__init__(arguments, tests)
        self.validate_arguments_size(0)

    def evaluate(self, message, state):
        # short-circuit evaluation if a test is true. the base standard does
        # not specify if all tests must be evaluated or in what order, but the
        # "ihave" extension requires short-circuit left-to-right evaluation
        # (RFC 5463, section 4). so we might as well do that.
        for test in self.tests:
            if test.evaluate(message, state):
                return True
        return False

SieveTestAnyOf.register()