# Log Parser Creation (AI-Assisted Step-by-Step Learning)

## Project Aim

Create a beginner-level log parser to learn Python fundamentals and improve my understanding of defensive security scripting.

---

## What I Did

I created a new Python file in Visual Studio Code and tested it using a simple `print("Hello World")` command to confirm Python was working correctly.

I then created a sample log file named `Sample.log` containing:

* INFO User login successful
* WARNING Failed login attempt
* ERROR Invalid password
* INFO Connection established

This sample log file was used to practice building a simple parser and understand how Python handles file reading and conditional logic.

I then created conditional statements to detect `"ERROR"` and `"WARNING"` entries inside the log file. The parser was designed to prioritise potentially suspicious or important events instead of informational logs.

When these conditions were met, the script printed the matching log lines to the terminal.

---

## What Went Well

With guidance and troubleshooting alongside AI, I successfully created a beginner-level log parser and gained a better understanding of how Python can:

* Open log files
* Read file contents
* Process lines individually
* Return filtered results to the terminal

---

## Challenges

Most issues encountered during development were related to:

* Incorrect indentation
* Case sensitivity
* Conditional statement placement

Debugging these problems helped improve my understanding of Python syntax and program flow.

---

## What I Learned

Through this project I learned:

* Basic Python file handling
* How loops process log entries line-by-line
* How conditional statements filter suspicious events
* The importance of indentation and case sensitivity
* How simple defensive security scripts can analyse log data
