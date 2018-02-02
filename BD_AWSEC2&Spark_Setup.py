# Spark works on data sets that are too large to handle locally, cloud based
# implementation is standard production deployment. Here we use free tier
# Amazon Web Serive AWS Elastic Compute Cloud EC2 for this experiment.

# Create EC2 VM
# Go to https://aws.amazon.com/free to create an 12 months available account
# you may need a US cedit card and a US telephone number to activate account.
# After activating the AWS account, create EC2 instance by Launch Instance,
# Select free tier eligible options from here on, first is Ubuntu Server xxx 
# LTS Amazon Machine Image AMI, then t2.micro Instance Type, set Number of
# Instances to 1 in the Instance Details setting, keep default settings in Add
# Storage, use anything you can remember or noted in Tag Instance, here we use
# myspark for both Key and Value, in Security Group choose All traffic for Type
# in this experiment but use more specific settings for production environment,
# Review Instance Launch and Launch, choose Create a new Key Pair in the next
# pop window and DOWNLOAD the key pair file with pem extention, then Launch
# Instances. Click the instance link to navigate to instance console, here
# remember to TERMINATE the instance after experiment to save available time
# unit for this free tier AWS subscriptioin.

# Prepare SSH
# In windows machine use PuTTY to create connection with EC2, the guide could
# be found by googling "ssh windows ec2" and find the Amazon official guide
# We need install PuTTY and get puttygen, get EC2 instance ID and public DNS
# name, and use puttygen convert pem file into the key for PuTTY to use.
# Start puttygen, load, choose all files to display, choose the pem file, 
# choose RSA as the type of key to generate, save private key. Start PuTTY, in
# Session pane go to Host Name and unput ubuntu@<EC2 instance public DNS name>,
# select connection type as SSH. Category pane, expand Connection, SSH, Auth,
# choose browse to specify the converted private key. Back to Sesstion pane to
# save the configuration for futher reuse then click open to satart session.
# In Linux or iOS, just open terminal and go to the folder with that pem key
# file, enter chmod 400 <xxx.pem> to modify the key file accessibility then
# enter: ssh - i <xxx.pem> ubuntu@<EC2 instance public DNS name>. That's all.

# Prepare Anaconda
# From SSH session on follow the steps bellow. Go to http://repo.continuum.io/
# archive/ to find the latest version of Anaconda for Linux x86_64, copy its
# link then back to SSH session with EC2 ubuntu server, enter wget <link> to
# download the Anaconda installation package. Then enter bash Ana and press
# tab to auto finish its name and install, enter yes to agree the license,
# enter to confirm install location, enter yes to modify the PATH variable.
# After installation, input "which python" to confirm python under Anaconda is
# used, otherwise input "source .bashrc" then confirm it again.

# Prepare Jupyter Notebook
# In SSH session, enter "mkdir certs" to create a folder, then "cd certs" and 
# "sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem
# -out mycert.pem" and input some meaningful thing to create a certificate.
# enter "jupyter notebook --generate-config" to create a config file, then
# "cd ~/.jupyter" and "vi jupyter_notebook_config.py". In vi editor, press i to
# change into insert mode, from the second blank line type following code:
# c = get_config()
# c.NotebookApp.certfile = u'/home/ubuntu/certs/mycert.pem'
# c.NotebookApp.open_browser = False
# c.NotebookApp.port = 8888
# then press "ESC" key then imput ":qw" to quit and wirte the file.
# enter "jupyter notebook" to start the Jupyter Notebook application, confirm
# everything works well and notice there is a messages at last says we need to
# use TOKEN to access it from URI address in the first time.
# Last, open a browser and use public DNS name of the EC2 on port 8888 to
# access jupyter notebook, input TOKEN if necessary.
# Notice: "jupyter notebook" should be run from someplace with public
# accessbility, other wise a 404 error may pop says access denied.

# Install Spark
# Spark depends on Scala and Java, so we have to install them. Back to SSH
# session, use "Ctrl + C" to terminate the jupyter notebook application. Enter
# "sudo apt-get update", then "sudo apt-get install default-jre". After that
# enter "java -version" to confirm java is installed, then "sudo apt-get
# install scala" and "scala -version" to confirm it is installed. For allowing
# python to access java, install py4j library with pip. Enter "export PATH=
# $PATH:$HOME/anaconda3/bin" then "conda install pip" to conda version pip.
# Enter "which pip" to confirm pip is from anaconda. Enter "pip install py4j"
# and make sure it is installed into anaconda lib folder. Go to http://apache.
# mirrors.tds.net/spark/ to find the latest version of spark-xx-hadoopxx.tgz
# file copy its link and back to SSH, enter "wget <link> to download it. Unzip
# the installation file with "sudo tar -zxvf spark" then press tab to auto
# complete its name and enter. For letting python know where Spark is, enter
# "export SPARK_HOME='/home/ubuntu/spark' press tab to auto complete it. Then
# "export PATH=$SPARK_HOME:$PATH" and "export PYTHONPATH=$SPARK_HOME/python:
# $PYTHONPATH". Launch jupyter notebook, go to browser to access notebook and
# fire a new book, run following code to confirm installation:
# from pyspark import SparkContext
# sc = SparkContext()
# if the two lines of code above run well withoug error, then it is ready.