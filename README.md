# Twilio SMS Bot

This program uses a Twilio client to send SMS messages to a desired cell number.
The user must first create a Twilio account, purchase a number and top up their 
account with money in order to use the service.

You can do this by signing up for Twilio using [this](https://www.twilio.com/go/twilio-brand-sales-1?utm_source=google&utm_medium=cpc&utm_term=twilio%20sign%20up&utm_campaign=G_S_EMEA_Brand_UKI_EN_NV&gclid=EAIaIQobChMI27Lh1azh9QIViaztCh1s-w-qEAAYASAAEgKwkPD_BwE) link.

## Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Compilation and Usage](#compilation-and-usage)
4. [Known Issues](#known-issues)

## Overview

This program simply takes a string body and sends it to a desired cell number. This functionality comes
in useful in services you create where you wish to send automated messages to users, reminders or status
updates.

## Requirements

- python3.8 (last I checked)
- Twilio accounts with money balance

## Compilation and Usage

Once you configure your secrets inside the config.py file:

```python
twilio = {
    "tw_account_sid": 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    "tw_auth_token": 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    "tw_phone_number": '+XXXXXXXX',
    "tw_cell_phone_number": '+XXXXXXXXXX'
}
```

You may trigger the test in sms_bot.py to validate your SMS is 
completing without issue.

## Known Issues

None at present.
