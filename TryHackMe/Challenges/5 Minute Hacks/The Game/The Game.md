# TryHackMe Challenge - The Game

## Task

Cipher has gone dark, but intel reveals he’s hiding critical secrets inside *Tetris*, a popular video game. The objective was to investigate the game files and uncover the encrypted data hidden within the executable.

---

# What I Did

- Downloaded the challenge files onto my computer
- Attempted to use the TryHackMe AttackBox environment
- Encountered issues transferring the task files to the AttackBox
- Used AI assistance and troubleshooting attempts to resolve the issue
- Attempted to use Windows Command Prompt to analyse the files
- Realised Windows lacked some of the Linux tools/commands required
- Restarted the room twice while troubleshooting file transfer issues
- Opened my Kali Linux virtual machine as an alternative approach
- Forgot my Kali VM password due to inactivity
- Accessed the GRUB menu and recovery/root shell to reset the password
- Successfully regained access to the Kali VM
- Enabled drag-and-drop and shared clipboard functionality in VirtualBox
- Transferred the challenge files into the Kali VM
- Extracted the challenge files into the Downloads directory
- Navigated to the correct directory using the Linux terminal
- Used the `strings` command to inspect the Tetrix executable
- Successfully identified and recovered the challenge flag

---

# Problems Encountered

## AttackBox File Transfer Issues
I struggled to move the challenge files into the TryHackMe AttackBox environment, which caused confusion and delayed progress.

## Windows Environment Limitations
I initially attempted to complete the challenge using Windows Command Prompt, but some required Linux tools and commands were unavailable.

## Kali Linux Password Recovery
I forgot the password to my Kali VM and needed to:
- Access the GRUB menu
- Enter recovery/root shell mode
- Reset the password manually

## Linux Terminal Issues
I struggled with:
- Linux file paths
- Terminal spacing/syntax
- Navigating directories correctly

---

# What Went Well

- Continued troubleshooting despite multiple failed attempts
- Successfully reset my Kali Linux password through recovery mode
- Became more familiar with Linux terminal navigation
- Used AI assistance to better understand the challenge workflow
- Improved my understanding of troubleshooting virtual machine issues

---

# Areas For Improvement

- Prepare my virtual machine before starting challenges
- Ensure drag-and-drop and shared clipboard settings are configured beforehand
- Improve Linux terminal familiarity and command syntax
- Gain a better understanding of TryHackMe challenge workflows and environments

---

# Key Lessons Learned

- Linux commands are highly syntax-sensitive
- Environment setup is important before beginning technical tasks
- Troubleshooting is a major part of cybersecurity learning
- Persistence is important when technical issues occur
