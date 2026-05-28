# Address Book Assistant Bot

This project is a simple command-line assistant bot written in Python.
The bot allows users to manage an address book by adding, editing, searching, and deleting contact records.

## Description

The program implements an address book system using object-oriented programming principles.

It includes several main classes:

* `Field` — base class for contact fields
* `Name` — class for storing a contact name
* `Phone` — class for storing and validating phone numbers
* `Record` — class for storing one contact with a name and a list of phone numbers
* `AddressBook` — class for storing and managing all contact records

## Features

* Add new contacts
* Store multiple phone numbers for one contact
* Validate phone numbers
* Edit existing phone numbers
* Remove phone numbers
* Search contacts by name
* Delete contacts

## Phone Number Validation

Each phone number must contain exactly 10 digits.

Valid example:

```text
1234567890
```

Invalid examples:

```text
12345
abc1234567
123-456-7890
```

## Technologies Used

* Python 3
* Object-Oriented Programming
* `collections.UserDict`

## Main Concepts Practiced

* Classes and objects
* Inheritance
* Encapsulation
* Working with lists and dictionaries
* Error handling
* Command-line interaction
* Phone number validation
