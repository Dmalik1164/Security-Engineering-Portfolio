Tryhackme notes



GUI - Graphical User Interface

CLI - Command Line Interface



cmd.exe - the default command-line interpreter in the Windows environment. 



ipconfig - You can check your network information. The terminal output below shows our IP address, subnet mask, and default gateway.



ipconfig / all - You can also use ipconfig /all for more information about your network configuration. We can view our DNS servers and confirm that DHCP is enabled.

\------------------------------

Network Troubleshooting:



One common troubleshooting task is checking if the server can access a particular server on the Internet. The command syntax is **ping target\_name**. Inspired by ping-pong, we send a specific ICMP packet and listen for a response. If a response is received, we know that we can reach the target and that the target can reach us.





Another valuable tool for troubleshooting is **tracert**, which stands for trace route. The command tracert target\_name traces the network route traversed to reach the target. Without getting into more details, it expects the routers on the path to notify us if they drop a packet because its **time-to-live (TTL)** has reached zero. The terminal output below shows that we passed through 15 routers before reaching our target.





One networking command worth knowing is **nslookup.** It looks up a host or domain and returns its IP address. The syntax **nslookup** example.com will look up example.com using the default name server; however, **nslookup example.com 1.1.1.1** will use the name server one.one.one.one. 





Netstat - This command displays current network connections and listening ports. A basic netstat command with no arguments will show you established connections.



If you are curious about the other options, you can run **netstat -h,** where **-h** displays the help page.

\-----------------------------------------------------

File And Disk Management:



cd - You can use cd without parameters to display the current drive and directory. It is the equivalent of asking the system, where am I?



You can view the child directories using **dir**.



dir /a - Displays hidden and system files as well.

dir /s - Displays files in the current directory and all subdirectories.



You can type tree to visually represent the child directories and subdirectories.



You can change to any directory by using the command cd target\_directory; this is equivalent to double-clicking the target\_directory on your desktop. Furthermore, you can use cd .. to go up one level. 



To create a directory, use **mkdir** directory\_name; **mkdir** stands for make directory. To delete a directory, use **rmdir** directory\_name; **rmdir** stands for remove directory.



type - This command will dump the contents of the text file on the screen; this is convenient for files that fit within your terminal window. (consider **more** for longer text files)



copy -  command allows you to copy files from one location to another



We can use the wildcard character \* to refer to multiple files. For example, copy \*.md C:\\Markdown will copy all files with the extension md to the directory C:\\Markdown.

\----------------------------------

Task and Process Management:



Tasklist -list the running processes



Some filtering is helpful because the output is expected to be very long. You can check all available filters by displaying the help page using **tasklist /?**

**Let’s say that we want to search for tasks related to sshd.exe, we can do that with the command tasklist /FI "imagename eq sshd.exe". Note that /FI is used to set the filter image name equals sshd.exe.**



&#x20;

