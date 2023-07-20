## Contact Form

## Project Description

This project implements a contact form using Django and Bootstrap. It allows users to send contact messages via a web form to an email specified in the project configuration and has a security to spam bots with a captcha.

## Usage

The contact form consists of the following fields:

- Name: The name of the sender of the message.
- Email: The email address of the sender.
- Subject: The subject of the message.
- Message: The body of the message to send.
- Captcha: The security for spam bots.

Users must fill in all required fields before submitting the form. When the "Send" button is clicked, the message will be emailed to the recipient specified in the project settings.
Also, manage possible errors by not filling in the required fields and display the information you submitted.
