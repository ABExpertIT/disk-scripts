# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANT_ROOT = File.dirname(File.expand_path(__FILE__))

disk_files = Array(0..2).map{ |x| File.join(VAGRANT_ROOT, "disk#{x}.vdi") }

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"

  config.vm.synced_folder ".", "/vagrant", type: "rsync",
    rsync__exclude: ".git/"

  config.vm.provider "virtualbox" do |vb|
    disk_files.map{ |file| 
      unless File.exist?(file)
        vb.customize ['createhd', '--filename', file, '--size', 500 * 1024]
      end
    }

   vb.customize ["storagectl", :id,  "--name", "SATA Controller", "--add", "sata", "--controller", "IntelAhci", "--portcount", 4, "--hostiocache", "on"]

   Array(0..2).map{ |x|
    vb.customize [
      'storageattach', :id, 
      '--storagectl', 'SATA Controller', 
      '--port', x, 
      '--device', 0, 
      '--type', 'hdd', 
      '--medium', disk_files[x] ]
   }
  end

  #config.vm.provision 'shell', inline: <<ENDL
#    apk update && apk upgrade && apk add python
#ENDL

end


