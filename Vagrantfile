# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-alpine")
  raise 'vagrant-alpine is not installed!'
end

VAGRANT_ROOT = File.dirname(File.expand_path(__FILE__))
file_to_disk = File.join(VAGRANT_ROOT, 'disk.vdi')

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|
  config.vm.box = "maier/alpine-3.3-x86_64"

  config.vm.synced_folder ".", "/vagrant", type: "rsync",
    rsync__exclude: ".git/"

  config.vm.provider "virtualbox" do |vb|
    unless File.exist?(file_to_disk)
      vb.customize ['createhd', '--filename', file_to_disk, '--size', 500 * 1024]
    end
   vb.customize ["storagectl", :id, "--name", "SATA Controller" , "--portcount", 3, "--hostiocache", "on"]

   vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', file_to_disk]

       #vb.customize ['storagectl', :id, '--name', 'Second Controller', '--add', 'sata', '--controller', 'ICH6']
    #vb.customize ['storageattach', :id, '--storagectl', 'Second Controller', '--port', 1, '--device', 1, '--type', 'hdd', '--medium', file_to_disk]
  end

  config.vm.provision 'shell', inline: <<ENDL
    apk update && apk upgrade && apk add python
ENDL

end


