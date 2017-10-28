## Creating and setting up your cloud machine

Computers you can't see!

#### Amazon Web Services (AWS)
#### Elastic Compute Cloud (EC2)

Sign up for [Amazon Web Services](http://aws.amazon.com/). We're planning to use "free tier" machines. However, you still need to enter a credit card to activate the account.

AWS has a lot of services, which you can see on the management console. We're just using EC2 for now.

Check that your region makes sense. "US West" is good.

From your EC2 Dashboard, click the blue "Launch Instance" button.

 1. You can run a lot of operating systems. We'll start with a standard [Ubuntu](http://www.ubuntu.com/) install.
 2. Select a "Free tier eligible" "t2.micro" instance.
 3. The default instance details should be fine.
 4. Default storage is probably fine.
 5. Give your instance a nice name.
 6. Name a new security group and allow some more ports if you like. 80 is a fun port to allow.
 7. Launch!

Set up secure access!

 1. Choose to "Create a new key pair" and give it a nice name.
 2. Download your `.pem` file.
 3. Move your file somewhere sensible like `~/.ssh/`.
 4. Make your file read only with `chmod 400 filename`.

On your EC2 Dashboard, you'll soon be able to find the IP address of your new cloud computer!

You can access it like this:

```
ssh -i ~/.ssh/my_cool_machine.pem ubuntu@123.234.123.234
```


### Setting up your machine

Great! Now let's start installing things.

We already have python installed (you can check that by typing `python`, hitting enter, and noticing that you are now at a python command line. Type `import pickle`. See how nothing happened? That means it's working. Use ctrl-d to get out of there.

Since we're on the subject of importing packages on a brand new installation of python, you can see all of the modules that come with python in this [documetation index](https://docs.python.org/2/library/index.html).

**`apt-get`** is a handy package management tool. The [Ubuntu guide](https://help.ubuntu.com/12.04/serverguide/apt-get.html) mentions that it is "a powerful command line tool that" performs several functions, but most people just use `apt-get` for its one to two main uses, most notably `apt-get install`.

I'll also mention the related and handy `apt search` command, which I use when I pretty much know the name of the thing I want, but I'm not sure I have it exactly right.

Let's try that out now. We know we'll want `pip` to help us install all our python packages. Is it just `apt-get install pip`?  I never remember.

We can run things as root by prefixing our commands with `sudo`. ([see also](https://xkcd.com/149/))

Before you `apt search`, update your libraries (the things `apt search` is going to search) by typing `sudo apt-get update`.

When that finishes, try `apt search pip`.

Holy moly! that's a lot of pip returns. Scroll up to the "p's" and see if you can find the winner, or pipe to `less` and search that way.

Install `pip` by typing [spoiler alert] `sudo apt-get install python-pip`. Accept the myriad suggestions it makes, and hit enter to watch it go. It will take a medium amount of time for this to finish up.

> **fun fact**: did you know that when you see a yes/no prompt in this format `[Y]/n`, that you can simply hit enter and it will assume you mean the default (capital and bracketed) option? You'd be surprised how many people I've caught carefully typing a capital Y. It's a lot.

> For `apt-get`, you can also just add the `-y` flag.


#### scipy stack

Now that we're on Ubuntu, we can install our stack of usual tools with this line. (There are convenient `apt-get` packages instead of doing everything via `pip`.)

```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```


#### More things to install

We'll also be interacting with repositories from our server, and perhaps you like Emacs, so let's do this:

```
sudo apt-get install git emacs
```

You can really start going to town now, but let's go to town as a different user.


#### adduser

Let's go ahead and make a user account for ourself at this point. Choose a name for yourself and add a user acount with the intuitive command:  `sudo adduser [username]`.

Pick a password, re-enter it, and then feel free to hit enter through all of the other questions.

Make yourself special by granting yourself root privileges: type `sudo visudo`. This will open up _nano_ (a text editor) to edit the sudoers file. Find the line that says `root    ALL=(ALL:ALL) ALL`. Give yourself a line beneath that which says `[username] ALL=(ALL:ALL) ALL`. Save by hitting Ctrl-o and then Enter when asked for the file name. Exit _nano_ with Ctrl-x.

Now you have a user account, but you can't just log in with a password. Passwords aren't secure enough. You may need to make a public key via the process [here](http://docs.oracle.com/cd/E19253-01/816-4557/sshuser-33/index.html) so the machines recognize you (they've become self aware).  Put your local machine's public `~/.ssh/id_rsa.pub` on your remote machine like this:

```
sudo mkdir /home/my_cool_username/.ssh/
sudo nano /home/my_cool_username/.ssh/authorized_keys
```

Copy/paste in your public key, save, and quit.

Don't log out until you verify that this has worked! Open a new shell on your local machine. You should be able to log in to your remote machine like this:

```
ssh my_cool_username@123.234.123.234
```

Nobody wants to type all that. To make things **even easier** you can do one of the following:

* Edit your `~/.ssh/config`:
```
Host my_cool_machine
Hostname 123.234.123.234
User my_cool_username
```
* Edit your /etc/hosts file
```
host_name host_ip alias
```

Now you can log in to your remote machine with `ssh my_cool_machine` (if you've done it the first way).  If you've done it the best way you need `ssh my_cool_username@my_cool_machine`.  The ***best*** practice is probably to combine the 2.  Define the known host with the alias `alias` in your `/etc/hosts` file and then put only the first and 3rd lines in the `.ssh/config` file (`Host alias` plus `User my_cool_username`) so you'll be able to get in with `ssh my_cool_machine`.


#### All s Everything

Send a file from your local machine to your remote machine:

```
scp cool_file.png my_cool_machine:~
```

# THE POSSIBILITIES ARE ENDLESS

Seriously. Think about what you can do.
