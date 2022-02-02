import os
import custom_logger
import config

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

logger = custom_logger.init_logger()


class Twilio:
    """@brief Twilio client class. Initializes account sid, token and cell numbers.

        Method
        """
    # Twilio account details & cell numbers
    account_sid = config.twilio["tw_account_sid"]
    auth_token = config.twilio["tw_auth_token"]
    twilio_phone_number = config.twilio["tw_phone_number"]
    cell_phone_number = config.twilio["tw_cell_phone_number"]

    def __init__(self):
        """
        @brief A simple function which initializes the Twilio client
            """
        self.client = Client(self.account_sid, self.auth_token)
        logger.info(f'Twilio client created for account sid: {self.account_sid}')

    def send_sms(self, sms_body):
        """
        @brief A simple function which takes an sms body and sends the sms to the desired
        cell phone number using Twilio client.

        :param sms_body: The body of the SMS
        :return: True if message sends successfully. False otherwise.
            """
        try:
            self.client.messages.create(from_=self.twilio_phone_number,
                                        to=self.cell_phone_number,
                                        body=sms_body, messaging_service_sid=self.account_sid)
            logger.info(f'SMS sent to {self.cell_phone_number} with SMS body: {sms_body}')
            return True

        except TwilioRestException as e:
            logger.critical(f'SMS FAILED to send to {os.environ.get("CELL_PHONE_NUMBER")} with SMS body: {sms_body}')
            logger.error(e)
            return False



