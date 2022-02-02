import unittest
import custom_logger
from sms_bot import Twilio

logger = custom_logger.init_logger()


class TestTransactionBot(unittest.TestCase):

    def test_1(self):
        twilio = Twilio()
        self.assertEqual(twilio.send_sms("Hello You!"), True)
        logger.info(f'SMS send successfully.')


if __name__ == '__main__':
    # Set logger
    unittest.main()
