# AutoLocalPrivilegeEscalation
An automated script that download potential exploit for linux kernel from exploitdb, and compile them automatically

This script is created due to Hackademics, there are so much possible exploit for that version of kernel, as a rookie OSCP student, I am not able to find out the correct exploit, also I am too lazy to test them one by one. So I hope this script can help me in the future.

First, it search for linux pirvilege escalation from the exploitdb in local directory by searchsploit.

Pass in the kernel version as first parameter, it lists potential exploit, and ask if you want to copy them from the local directory.

After that, it asks if you want to compile the downloaded C file.

Then, it will ask if you want to make a tar ball of the directory.

And it will show the summary of the downloaded files.

Script Environment: Kali 3.18.0 kali2

Test result in Kali 4.0 is negative for this script, need to redesign the architecture, maybe python is more suitable to do this automation, need to think again.

16 Mar 25 Updated with Python version of this idea, more adaptable to different kali environment and more easy to change the code in this way.

16 Apr 30 After almost finishes with all the boxes in OSCP, I have to admit I have not use this script at all during my lab times. There is one thing I learnt from the labs, do not run exploit blindly, as exploits might cause the system to crash, or leaves your footprint in a way you cannot imagine etc. Always enumerate more and gather all the information you have to escalate. DO NOT run the exploit blindly without knowing what the exploit does.

```
root@workstation:~/utilities# ./auto_priv_exploit.sh 
[*] Usage: ./auto_priv_exploit.sh VERSION_OF_KERNEL
root@workstation:~/utilities# ls
auto_priv_exploit.sh
root@workstation:~/utilities# ./auto_priv_exploit.sh 2.6
[*] Possible Exploit

Linux Kernel 2.4.x / 2.6.x - uselib() Local Privilege Escalation Exploit                                           | /linux/local/895.c
Linux Kernel 2.4 / 2.6 - bluez Local Root Privilege Escalation Exploit (3)                                         | /linux/local/926.c
Postfix <= 2.6-20080814 - (symlink) Local Privilege Escalation Exploit                                             | /linux/local/6337.sh
Linux Kernel < 2.6.29 - exit_notify() Local Privilege Escalation Exploit                                           | /linux/local/8369.sh
Linux Kernel 2.6 - UDEV Local Privilege Escalation Exploit                                                         | /linux/local/8478.sh
Linux Kernel 2.6 UDEV < 141 - Local Privilege Escalation Exploit                                                   | /linux/local/8572.c
Linux Kernel 2.6.x - ptrace_attach Local Privilege Escalation Exploit                                              | /linux/local/8673.c
Linux Kernel <= 2.6.34-rc3 ReiserFS xattr - Privilege Escalation                                                   | /linux/local/12130.py
Linux Kernel < 2.6.36-rc1 CAN BCM - Privilege Escalation Exploit                                                   | /linux/local/14814.c
Linux Kernel < 2.6.36-rc4-git2 - x86_64 ia32syscall Emulation Privilege Escalation                                 | /linux/local/15023.c
Linux Kernel <= 2.6.36-rc8 - RDS Protocol Local Privilege Escalation                                               | /linux/local/15285.c
Linux Kernel <= 2.6.37 - Local Privilege Escalation                                                                | /linux/local/15704.c
Linux Kernel < 2.6.37-rc2 - ACPI custom_method Privilege Escalation                                                | /linux/local/15774.c
Linux Kernel 2.6.34 - CAP_SYS_ADMIN x86 - Local Privilege Escalation Exploit                                       | /linux/local/15916.c
Linux Kernel < 2.6.34 - CAP_SYS_ADMIN x86 & x64 - Local Privilege Escalation Exploit (2)                           | /linux/local/15944.c
Linux Kernel < 2.6.36.2 - Econet Privilege Escalation Exploit                                                      | /linux/local/17787.c
Linux Kernel 2.6.17 - Sys_Tee Local Privilege Escalation Vulnerability                                             | /linux/local/29714.txt
Linux Kernel 2.6.x - Ptrace Local Privilege Escalation Vulnerability                                               | /linux/local/30604.c
Linux Kernel 2.6.x - 'pipe.c' Local Privilege Escalation Vulnerability (1)                                         | /linux/local/33321.c
Linux Kernel 2.6.x - pipe.c Local Privilege Escalation Vulnerability (2)                                           | /linux/local/33322.c
Linux Kernel 2.6.x - Ext4 - 'move extents' ioctl Local Privilege Escalation Vulnerability                          | /linux/local/33395.txt
Linux Kernel 2.6.x - 'fasync_helper()' Local Privilege Escalation Vulnerability                                    | /linux/local/33523.c
[*] Do you wish to download all the exploit script to current directory and compile if possible?
1) Yes
2) No
#? 1
[*] The base directory is /usr/share/exploitdb/platforms
[*] Do you wish to compile all the exploit script written in C?
1) Yes
2) No
#? 1
**************************************************

[*] Successfully Compiled 9 executable located in linux_2.6
[*] Do you want to make a tar ball of the linux_2.6? (For convinient file transfer)
1) Yes
2) No
#? 1
[*] Auto Privilege Exploit Summary
C file in /root/utilities/linux_2.6 has 16 files
Python file in /root/utilities/linux_2.6 has 1 files
Perl file in /root/utilities/linux_2.6 has 0 files
Ruby file in /root/utilities/linux_2.6 has 0 files
TXT file in /root/utilities/linux_2.6 has 2 files

```
