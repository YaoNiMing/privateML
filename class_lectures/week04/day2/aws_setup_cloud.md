#Amazon Web Services
##Setting up Cloud Computing :cloud: :cloud: :cloud:

1.  Logging in  
  http://aws.amazon.com/  
  (Note:  put your user id and password somewhere for easy reference)

2.  [AWS Free Tier](https://aws.amazon.com/free/)  
  * credit card required for log-in
  * designed to enable you to get hands-on experience with AWS Cloud Services
  * includes services with a free tier available for 12 months following your AWS sign-up date, as well as additional service offers that do not automatically expire at the end of your 12 month AWS Free Tier term.

3.  AWS Console  
  Lot of options!  We will choose "Compute/EC2"  [upper left of screen]  
  EC2 = Elastic Compute Cloud (Virtual Servers in the Cloud!)  

4.  Region [on upper right of screen]  
  Select:  US West (Oregon)

5.  Create Instance  
    From your EC2 Dashboard, click the blue **Launch Instance** button.

---
##Setting up Instance

Step 1) Choose an Amazon Machine Image (AMI):  **Ubuntu Server** [press blue Select button]  
Step 2) Choose an Instance Type:  Select a **Free tier eligible** "t2.micro" instance  
Step 3) **Next: Configure Instance Details**  [accept default]  
Step 4) **Next:  Add Storage**  [set to free max of 30GB]  
Step 5) Tag Instance: `ipython`  
Step 6) **Next:  Configure Security Group**  
Name a new security group and allow some more ports to allow ipython notebook to be served remotely.  
>     Add Rule:  select 'SSH'  
      Port Range: 22
      Source:  Anywhere  

>     Add Rule:  select 'HTTPS'  
      Port Range: 443
      Source:  Anywhere  

>     Add Rule:  select 'Custom TCP Rule'  
      Port Range: 8888  (ipython will be accessable via this port)
      Source:  Anywhere  

Optionally, if you ever want to serve a website from here, do the following:

>     Add Rule:  select 'Custom TCP Rule'  
      Port Range: 80
      Source:  Anywhere  

**Review and Launch**    

Step 7) Review Instance Launch: your set-up will look like below screenshot  
**Launch**  



---

##Set up Secure Access  

1.  Choose to "Create a new key pair" and give it a name:  **aws_ipython**  
2.  Download keypair

---

###Keypair
Save file.  For me, it is in this folder:  
```
$ pwd
/Users/paulburkard/Downloads

$ ls -la *aws_ipython*
-rw-r--r--@ 1   1692 Jul 23 14:46 aws_ipython.pem

```  
Move your file to `~/.ssh/`.  (Note:  if you do not have an ssh folder, create one:  `mkdir ~/.ssh`)  
```  
$ mv aws_ipython.pem ~/.ssh/aws_ipython.pem
```
Make your file read only with `chmod 400 filename`
```
$ cd ~/.ssh
$ pwd
/Users/ablevins/.ssh
$ ls -la *aws_ipython*
-rw-r--r--@ 1   1692 Jul 23 14:46 aws_ipython.pem

$ chmod 400 aws_ipython.pem

$ ls -la *aws_ipython*
-r--------@ 1   1692 Jul 23 14:46 aws_ipython.pem
```  
Check that you have `id_rsa` and `id_rsa.pub` files within your .ssh file  
```
$ pwd
/Users/paulburkard/.ssh
$ ls -la *id_rsa*
-rw-------  1   1675 Jul  23  2015 id_rsa
-rw-r--r--  1    422 Jul  23  2015 id_rsa.pub
```  
If you do not have them, generate them with `$ ssh-keygen -t rsa`    
(When asked where to save, the default location is correct (ex: /Users/username/.ssh/id_rsa) : so hit Enter)

---

##Connecting to your Instance  
###AWS:  
**Launch Instance**

##Set Up Billing  
Find (in blue):  "Get notified of estimated charges"  
Select **Create billing alerts**  
Check all 3 preferences and select **Save preferences**  
You can then close this tab.  
Back to other AWS tab.  Scroll down and select **View Instances**

On your EC2 Dashboard, you'll soon be able to find the IP address of your new cloud computer!  
**Note:  It may take a few minutes for the instance to initialize.**

###On Your Local Machine  

**Open a new terminal window.**


####Connect to your Cloud Machine from your local computer!  

**Note:  the numbers after "ubuntu@" come from AWS; it is the Public IP.**    
```
ssh -i ~/.ssh/my_key_file.pem ubuntu@123.234.123.234


The authenticity of host '54.165.157.51 (54.165.157.51)' can't be established.
ECDSA key fingerprint is SHA256:0/xYknp2uz/6NLgHjM8RRqpsX0ykIGj8xQV9PqL3mkU.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '54.165.157.51' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.13.0-74-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Sat Jul 23 20:09:58 UTC 2016

  System load: 0.16             Memory usage: 5%   Processes:       82
  Usage of /:  9.9% of 7.74GB   Swap usage:   0%   Users logged in: 0

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ubuntu@ip-172-31-60-68:~$
```

####To exit Ubuntu machine (AWS cloud machine)  
```
ubuntu@ip-172-31-60-68:~$ exit
logout
Connection to 54.165.157.51 closed.
```
