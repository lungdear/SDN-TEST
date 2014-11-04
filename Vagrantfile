# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  #config.vm.boot_timeout = 600
  #config.vm.provider :virtualbox do |vb|
  #  vb.gui = true
  #end

  config.vm.box = "puppetlabs-precise64"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/ubuntu-server-12042-x64-vbox4210.box" # (Puppetlabs)
  config.ssh.forward_x11 = true

  #config.vm.box = "precise32"
  #config.vm.box = "precise64"
  #config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-i386-vagrant-disk1.box" # (Official)
  #config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-vagrant-disk1.box" # (Official)

  #config.vm.box = "trusty32"
  #config.vm.box = "trusty64"
  #config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box" # (Official)
  #config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box" # (Official)

  #config.vm.provision "shell", path: "resources/puppet/scripts/upgrade_puppet.sh"
  config.vm.provision "shell", path: "resources/puppet/scripts/bootstrap.sh"

  #config.vm.provision "puppet" do |puppet|
  #    puppet.working_directory = "/vagrant/resources/puppet"
  #    puppet.hiera_config_path = "resources/puppet/hiera.yaml"
  #    puppet.manifests_path = "resources/puppet/manifests"
  #    puppet.manifest_file  = "base.pp"
  #end

#################################################################################################################

  ## OpenDaylight for Mininet
  config.vm.define "opendaylight-mininet" do |odl_mininet|
    odl_mininet.vm.hostname = "opendaylight-mininet"
    odl_mininet.vm.network "private_network", ip: "192.168.40.10"
    odl_mininet.vm.network "forwarded_port", guest: 8080, host: 9090
    odl_mininet.vm.network "forwarded_port", guest: 8181, host: 9191
    odl_mininet.vm.provider :virtualbox do |vb|
      #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--memory", "2048"]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
    end
    odl_mininet.vm.provision "puppet" do |puppet|
      puppet.working_directory = "/vagrant/resources/puppet"
      puppet.hiera_config_path = "resources/puppet/hiera-mininet.yaml"
      puppet.manifests_path = "resources/puppet/manifests"
      puppet.manifest_file  = "opendaylight-mininet.pp"
    end
  end

  ## Mininet Node
  config.vm.define "mininet" do |mininet|
    mininet.vm.box = "trusty64"
    mininet.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    mininet.vm.hostname = "mininet"
    mininet.vm.network "private_network", ip: "192.168.40.15"
    #mininet.vm.network "forwarded_port", guest: 1234, host: 1234
    mininet.vm.provider :virtualbox do |vb|
      #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--memory", "1024"]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
    end
    mininet.vm.provision "puppet" do |puppet|
      puppet.working_directory = "/vagrant/resources/puppet"
      puppet.hiera_config_path = "resources/puppet/hiera-mininet.yaml"
      puppet.manifests_path = "resources/puppet/manifests"
      puppet.manifest_file  = "mininet.pp"
    end
  end

  ## RouteFlow & OpenDaylight(Source)
  config.vm.define "routeflow" do |routeflow|
    routeflow.vm.hostname = "routeflow"
    routeflow.vm.network "private_network", ip: "192.168.40.16"
    routeflow.vm.network "forwarded_port", guest: 8080, host: 8090
    routeflow.vm.provider :virtualbox do |vb|
      #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--memory", "2048"]
      #vb.customize ["modifyvm", :id, "--vrde", "on"]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
    end
    routeflow.vm.provision "puppet" do |puppet|
      puppet.working_directory = "/vagrant/resources/puppet"
      puppet.hiera_config_path = "resources/puppet/hiera-mininet.yaml"
      puppet.manifests_path = "resources/puppet/manifests"
      puppet.manifest_file  = "routeflow.pp"
    end
  end

#################################################################################################################

  ## OpenDaylight for OpenStack (Pre-Built)
  config.vm.define "opendaylight-openstack" do |odl_openstack|
    odl_openstack.vm.hostname = "opendaylight-openstack"
    odl_openstack.vm.network "private_network", ip: "192.168.50.10"
    odl_openstack.vm.network "forwarded_port", guest: 8080, host: 8080
    odl_openstack.vm.network "forwarded_port", guest: 8181, host: 8181
    odl_openstack.vm.provider :virtualbox do |vb|
      #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--memory", "2048"]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
    end
    odl_openstack.vm.provision "puppet" do |puppet|
      puppet.working_directory = "/vagrant/resources/puppet"
      puppet.hiera_config_path = "resources/puppet/hiera-openstack.yaml"
      puppet.manifests_path = "resources/puppet/manifests"
      puppet.manifest_file  = "opendaylight-openstack.pp"
    end
  end

  #num_compute_nodes = (ENV['DEVSTACK_NUM_COMPUTE_NODES'] || 1).to_i
  num_compute_nodes = 1 ## (Max: 3)

  ## ip pre-configuration
  control_ip = "192.168.50.20" ## DevStack Controller Node
  compute_ip_base = "192.168.50." ## DevStac Compute Nodes
  compute_ips = num_compute_nodes.times.collect { |n| compute_ip_base + "#{n+21}" }

  ## Devstack Control Node
  config.vm.define "devstack-control" do |control|
    #control.vm.box = "trusty64"
    #control.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    control.vm.box = "opscode_ubuntu-14.04_chef-provisionerless"
    control.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_ubuntu-14.04_chef-provisionerless.box"
    control.vm.hostname = "devstack-control"
    control.vm.network "private_network", ip: "#{control_ip}"
    control.vm.network "forwarded_port", guest: 80, host: 8081
    control.vm.provider :virtualbox do |vb|
      #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--memory", "2048"]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
    end
    control.vm.provision "puppet" do |puppet|
      puppet.working_directory = "/vagrant/resources/puppet"
      puppet.hiera_config_path = "resources/puppet/hiera-openstack.yaml"
      puppet.manifests_path = "resources/puppet/manifests"
      puppet.manifest_file  = "devstack-control.pp"
    end
  end

  ## Devstack Compute Nodes
  num_compute_nodes.times do |n|
    config.vm.define "devstack-compute-#{n+1}" do |compute|
      compute_ip = compute_ips[n]
      compute_index = n+1
      #compute.vm.box = "trusty64"
      #compute.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
      compute.vm.box = "opscode_ubuntu-14.04_chef-provisionerless"
      compute.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_ubuntu-14.04_chef-provisionerless.box"
      compute.vm.hostname = "devstack-compute-#{compute_index}"
      compute.vm.network "private_network", ip: "#{compute_ip}"
      compute.vm.provider :virtualbox do |vb|
        #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
        vb.customize ["modifyvm", :id, "--cpus", "2"]
        vb.customize ["modifyvm", :id, "--memory", "2048"]
        #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
        #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
      end
      compute.vm.provision "puppet" do |puppet|
        puppet.working_directory = "/vagrant/resources/puppet"
        puppet.hiera_config_path = "resources/puppet/hiera-openstack.yaml"
        puppet.manifests_path = "resources/puppet/manifests"
        puppet.manifest_file  = "devstack-compute.pp"
      end
    end
  end

#################################################################################################################

  ## VXLAN - Router (Must be deploy first)
  config.vm.define "vxlan_router" do |vxlan_router|
    vxlan_router.vm.box = "trusty64"
    vxlan_router.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    vxlan_router.vm.hostname = "vxlan-router"
    vxlan_router.vm.network "private_network", ip: "192.168.1.1"
    vxlan_router.vm.network "private_network", ip: "192.168.2.1"
    #vxlan_router.vm.network "forwarded_port", guest: 80, host: 8081
    vxlan_router.vm.provider :virtualbox do |vb|
      #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--memory", "1024"]
      vb.customize ["modifyvm", :id, "--nic2", "intnet"]
      vb.customize ["modifyvm", :id, "--nic3", "intnet"]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
    end
    vxlan_router.vm.provision "shell", inline: <<-SCRIPT
      sed -i 's/^#net.ipv4.ip_forward.*/net.ipv4.ip_forward=1/g' /etc/sysctl.conf && sysctl -p
      iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    SCRIPT
    vxlan_router.vm.provision "puppet" do |puppet|
      puppet.working_directory = "/vagrant/resources/puppet"
      puppet.hiera_config_path = "resources/puppet/hiera-vxlan.yaml"
      puppet.manifests_path = "resources/puppet/manifests"
      puppet.manifest_file  = "vxlan_router.pp"
    end
  end

  ## VXLAN - server1
  config.vm.define "vxlan_server1" do |vxlan_server1|
    vxlan_server1.vm.box = "trusty64"
    vxlan_server1.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    vxlan_server1.vm.hostname = "vxlan-server1"
    vxlan_server1.vm.network "private_network", ip: "192.168.1.10"
    #vxlan_server1.vm.network "forwarded_port", guest: 80, host: 8081
    vxlan_server1.vm.provider :virtualbox do |vb|
      #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--memory", "1024"]
      vb.customize ["modifyvm", :id, "--nic2", "intnet"]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
    end
    vxlan_server1.vm.provision "shell", inline: <<-SCRIPT
      route del default && route add default gw 192.168.1.1
    SCRIPT
    vxlan_server1.vm.provision "puppet" do |puppet|
      puppet.working_directory = "/vagrant/resources/puppet"
      puppet.hiera_config_path = "resources/puppet/hiera-vxlan.yaml"
      puppet.manifests_path = "resources/puppet/manifests"
      puppet.manifest_file  = "vxlan_servers.pp"
    end
  end

  ## VXLAN - server2
  config.vm.define "vxlan_server2" do |vxlan_server2|
    vxlan_server2.vm.box = "trusty64"
    vxlan_server2.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    vxlan_server2.vm.hostname = "vxlan-server2"
    vxlan_server2.vm.network "private_network", ip: "192.168.2.20"
    #vxlan_server2.vm.network "forwarded_port", guest: 80, host: 8081
    vxlan_server2.vm.provider :virtualbox do |vb|
      #vb.customize ["modifyvm", :id, "--cpus", "1", "--hwvirtex", "off"] ## without VT-x
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--memory", "1024"]
      vb.customize ["modifyvm", :id, "--nic2", "intnet"]
      #vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      #vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
    end
    vxlan_server2.vm.provision "shell", inline: <<-SCRIPT
      route del default && route add default gw 192.168.2.1
    SCRIPT
    vxlan_server2.vm.provision "puppet" do |puppet|
      puppet.working_directory = "/vagrant/resources/puppet"
      puppet.hiera_config_path = "resources/puppet/hiera-vxlan.yaml"
      puppet.manifests_path = "resources/puppet/manifests"
      puppet.manifest_file  = "vxlan_servers.pp"
    end
  end

end
