from nbresult import ChallengeResultTestCase


class TestData(ChallengeResultTestCase):

    def test_data_is_above_82(self):
        self.assertEqual(len(self.result.data), 5)
