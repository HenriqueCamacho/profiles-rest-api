# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
 
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "~> 20200304.0.0" #Specific version of image, to not break the course steps...
 
  config.vm.network "forwarded_port", guest: 8000, host: 8000 #Maps a port from our local machine to the machine in our server, make this port acessible from our host machine
  #Guest is the development server itself, by default ports are not available on any guest machine, so then we can acess by localhost:8000
  # Guest --> The os in vm Box 
  # Host --> The pc which vmBox is running
  # So if guest is running at 80, we can acess by 8080(or other port) on our guest machine

  config.vm.provision "shell", inline: <<-SHELL #Run scripts when we first create the server
    systemctl disable apt-daily.service #Disable the auto-update which conflicts with the update below
    systemctl disable apt-daily.timer #Disable the auto-update which conflicts with the update below
  
    sudo apt-get update #Update localrepository with all available packages so we can install python3-venv zip
    sudo apt-get install -y python3-venv zip
    touch /home/vagrant/.bash_aliases #Create bash aliases file which set python3 to default python version for our vagrant user
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
 end