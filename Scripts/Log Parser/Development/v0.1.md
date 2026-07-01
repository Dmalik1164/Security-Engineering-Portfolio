# Development Log - Version 0.1

## Objective

Build a beginner-level Python log parser to develop foundational Python skills while learning defensive security scripting concepts.

---

## Development Process

I began by creating a new Python file in Visual Studio Code and verified my Python installation using a simple `print("Hello World")` test.

I then created a sample log file (`Sample.log`) containing example log entries:

- INFO User login successful
- WARNING Failed login attempt
- ERROR Invalid password
- INFO Connection established

This file was used to practice reading log files and filtering specific log entries.

The parser was developed to identify `ERROR` and `WARNING` events using conditional statements, printing matching entries to the terminal while ignoring informational logs.

---

## Challenges

During development I encountered several issues, including:

- Incorrect indentation
- Case sensitivity
- Conditional statement placement

Troubleshooting these problems improved my understanding of Python syntax, program flow, and debugging.

---

## Skills Developed

Through this version of the project I gained experience with:

- Opening and reading files
- Processing files line by line
- Using loops and conditional statements
- Filtering log data
- Basic defensive security scripting concepts

---

## Outcome

Version 0.1 successfully reads a log file and displays `ERROR` and `WARNING` entries in the terminal. This project established the foundation for future versions that will introduce additional filtering, reporting, and automation features.
