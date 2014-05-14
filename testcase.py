""" test_utils.py -- a place for unit testing tools """

import unittest
import mock


class PatchingTestCase(unittest.TestCase):
    """ A simpler way of patching with Mocks.

    The Mock module supports decorators and context managers, but both are
    pretty challenging to use with customized mocks. This mixin provides the
    patch method, which correctly invokes the patch call, starts the patch,
    and registers the cleanup call properly.

    In an example case, consider the case of generating a CSRF token. The
    token is 42 random letters and numbers. We make it random by using
    random.choice, but by its very nature, random.choice makes unit testing
    hard -- how can you get predictable results when the whole point is to
    generate a random sequence? (Let's pretend we don't know how to seed the
    randomizer here.)

    So the approach is to install a Mock object that returns predictable
    results in the place of random.choice.

    The code module we are testing is imported as `csrf`. The random module
    is imported inside it via `import random`. So we would do the following:

    ```
    class CsrfTokenTest(PatchingTestCase):
        def test_01_generate_csrf(self):
            self.patch(csrf.random, 'choice', mock.Mock(return_value='A'))
            token = csrf.generate_csrf_token()
            self.assertEqual(token, 'A' * 42)
    ```

    This monkeypatches csrf.random.choice to be a Mock object that will always
    return 'A'. We then generate a token and assert that it is a string of A's,
    42 characters long.
    """
    def patch(self, target, attribute, obj=None):
        """ Patches the target with a Mock and sets a cleanup call.
        """
        if obj is None:
            obj = mock.Mock()
        patched = mock.patch.object(target, attribute, obj)
        obj = patched.start()
        self.addCleanup(patched.stop)
        return obj
