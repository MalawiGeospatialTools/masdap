# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.ssh.username = 'vagrant'

  config.vm.define :production do |production|
  	production.vm.network :public_network, :bridge => 'eth0', :auto_config => false
    config.vm.network "forwarded_port", guest: 80, host: 8000
    production.vm.provider :virtualbox do |vb|
        vb.customize [ "modifyvm", :id, "--name", "{{ project_name }}-prod","--memory", 4096 ]
  	end
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
    end
  end

end
