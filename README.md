# AutoLocalPrivilegeEscalation
An automated script that download potential exploit for linux kernel from exploitdb, and compile them automatically

First, it search for linux pirvilege escalation from the exploitdb in local directory by searchsploit.
Pass in the kernel version as first parameter, it lists potential exploit, and ask if you want to copy them from the local directory.
After that, it asks if you want to compile the downloaded C file.
Then, it will ask if you want to make a tar ball of the directory.
And it will show the summary of the downloaded files.

Example:
./auto_priv_exploit.sh 
[*] Usage: ./auto_priv_exploit.sh VERSION_OF_KERNEL

 ./auto_priv_exploit.sh 2.6
[*] Possible Exploit

Linux Kernel 2.4.x / 2.6.x - uselib() Local Privilege Escalation Exploit  |/linux/local/895.c
Linux Kernel 2.4 / 2.6 - bluez Local Root Privilege Escalation Exploit (3) | /linux/local/926.c
Postfix <= 2.6-20080814 - (symlink) Local Privilege Escalation Exploit   | /linux/local/6337.sh
Linux Kernel < 2.6.29 - exit_notify() Local Privilege Escalation Exploit  | /linux/local/8369.sh
.
.
.
.

[*] Do you wish to download all the exploit script to current directory and compile if possible?
1) Yes
2) No
  1
[*] Do you wish to download all the exploit script to current directory and compile if possible?
1) Yes
2) No
 1
[*] The base directory is /usr/share/exploitdb/platforms
[*] Do you wish to compile all the exploit script written in C?
1) Yes
2) No
 1

[*] Successfully Compiled 9 executable located in linux_2.6
[*] Do you want to make a tar ball of the linux_2.6? (For convinient file transfer)
1) Yes
2) No
 1
[*] Auto Privilege Exploit Summary
C file in /root/utilities/linux_2.6 has 16 files
Python file in /root/utilities/linux_2.6 has 1 files
Perl file in /root/utilities/linux_2.6 has 0 files
Ruby file in /root/utilities/linux_2.6 has 0 files
TXT file in /root/utilities/linux_2.6 has 2 files
