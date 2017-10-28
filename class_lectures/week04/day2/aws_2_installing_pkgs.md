# AWS - Setting up your machine
## Let's start installing packages!

#### Check which version of python is installed
```console
ubuntu@ip-172-31-60-68:~$ python --version
Python 2.7.6
ubuntu@ip-172-31-60-68:~$
```
#### Let's use Anaconda instead. Go to the continuum website and copy the link address for the latest version of Anaconda
```console
ubuntu@ip-172-31-60-68:~$ wget http://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh
ubuntu@ip-172-31-60-68:~$ bash Anaconda3-4.1.1-Linux-x86_64.sh
```
#### Lets confirm we are using the correct version of python
```console
ubuntu@ip-172-31-60-68:~$ which python
```
if its not using the anaconda install, we may need to reload or .bashrc with `source .bashrc`

---
## Some Helpful Notes

#### We can run things as root by prefixing our commands with `sudo`
#### To update your libraries, use `apt-get update`
```
ubuntu@ip-172-31-60-68:~$ sudo apt-get update
```
#### [`apt-get` Package Management Tool](https://help.ubuntu.com/12.04/serverguide/apt-get.html)   
Read more about `apt-get` at above link.  

---

### Add user
```console
ubuntu@ip-172-31-60-68:/home$ sudo adduser ablevins
```
**Note:  pick a password (save it in an easy-to-find place !! )**; enter through all the other questions (name fields, etc.)  

### Delete user
```console
$ sudo userdel -r olduser
```

#### User privileges  
Make yourself special by granting yourself root privileges: type `sudo visudo`. This will open up _nano_ (a text editor) to edit the sudoers file. Find the line that says `root    ALL=(ALL:ALL) ALL`. Give yourself a line beneath that which says `[username] ALL=(ALL:ALL) ALL`.
#### User privilege specification  
```
root     ALL=(ALL:ALL) ALL
ablevins  ALL=(ALL:ALL) ALL
```
**Save file in _nano_ editor:  Ctrl-o** then Enter when asked for the file name.    
**Exit file from _nano_ editor: Ctrl-x**  

----

#### Setting up User Account

Now you have a user account, but you can't just log in with a password. Passwords aren't secure enough.  
Copy your public key (from your local machine) `~/.ssh/id_rsa.pub` to your remote machine to the authorized keys file.  
(Create the authorized_keys file as follows:)  

**on your remote machine (AWS):**  
1.  create the directory  
2.  then copy key from local machine to remote machine  
```console
sudo mkdir -p /home/my_cool_username/.ssh/
sudo vi /home/my_cool_username/.ssh/authorized_keys
```

**My example:**  
```
1)  get output from your (local machine) public key file like this:
ablevins$ pwd
/Users/ablevins/.ssh
ablevins$ cat id_rsa.pub

2) Copy everything (Command c)

3) On your AWS machine:  
after you run:
$ sudo nano /home/ablevins/.ssh/authorized_keys

To paste in the current window:  Command v
then hit  
ctrl o (to save)  
enter
ctrl x (to exit)
```
**on your local machine:**   
Don't log out until you verify that this has worked! **Open a new shell on your local machine.** You should be able to log in to your remote machine like this:
```console
$ ssh my_cool_username@123.234.123.234
```
**My example:**  
```console
ablevins$ ssh ablevins@54.172.80.95
```

---

Nobody wants to type all that. Edit your `~/.ssh/config` (on your local machine):

```
Host machine_name_goes_here
Hostname 123.234.123.234
User my_cool_username
```
**My example:**  
```
Host aws_ipython
     HostName 54.172.80.95
     User ablevins
```
Now you can log in to your remote machine with `ssh machine_name_goes_here`.

**My example:**  
```
$ ssh aws_ipython
```

####Send a file from your local machine to your remote machine
```
scp cool_file.png machine_name_goes_here:~
```
**My Example:**  
```console
$ scp trysql.py :~
```
Note:  check your user account on AWS.  The file was copied there!!!

---

## Setting up Jupyter Notebook to use anywhere

```console
$ ipython
In [1]:from IPython.lib import passwd
In [2]:passwd()
```

your output will have a string that starts with `'sha1:'` copy this string somewhere for later use


```console
$ mkdir .certs
$ cd .certs
$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
```

``` console
$ cd ~/.jupyter/
$ vi jupyter_notebook_config.py
```

```
c = get_config()

# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want  plotting support always in your notebook

# Notebook config
c.NotebookApp.certfile = u'/home/ubuntu/.certs/mycert.pem' #location of your certificate file
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False  #so that the ipython notebook does not opens up a browser by default
c.NotebookApp.password = u'sha1:68c136a5b064...'  #the encrypted password we generated above
# Set the port to match the port we opened in the security group
c.NotebookApp.port = 8888
```

```
$ cd ~
$ mkdir Notebooks
$ cd Notebooks
$ jupyter notebook
```
