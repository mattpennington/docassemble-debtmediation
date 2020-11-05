# docassemble.debtmediation

## Author

Matt Pennington - [Tonic Workflows](https://workflow.tonic.works/)

## Overview

A docassemble demo interview for Debt Mediation Onboarding that uses a combination of Multi-User Interviews + SMS + Email.

## Notice

This is not intended as finished interview - it's a working example to showcase one way that SMS and Email can be used to implement a Multi-User Interview in a vaguely "real world" scenario.
## Requirements

Your Docassemble Server will need configuring with:

* A [Twilio](https://www.twilio.com/) Account (a [trial project](https://www.twilio.com/console/projects/create) is sufficient providing you have two unique mobile numbers you can add to it for the purposes of running this demo ^) - [configuration instructions](https://docassemble.org/docs/config.html#twilio)
* The ability to send emails out - [configuration instructions](https://docassemble.org/docs/config.html#mail)

^as an alternative if you only have access to one mobile number you can disable the *debtor.mobile_number == applicant.mobile_number* validation code.
## Preview

[Watch on youtube](https://youtu.be/l_9kGOIzx2U)
