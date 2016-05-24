# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, :path => "vagrantboot.sh"
  config.vm.network "forwarded_port", guest: 5000, host: 8050
end
