VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network :forwarded_port, host: 8000, guest: 8000
  config.vm.network :forwarded_port, host: 8080, guest: 8080
  config.vm.provision :shell, path: "config/vagrant_root.sh"
  config.vm.provision :shell, path: "config/vagrant_user.sh", privileged: false
end
