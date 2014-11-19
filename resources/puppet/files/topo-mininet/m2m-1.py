#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    NODE2_IP='192.168.40.11'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    net.addController( 'c0',
                      controller=RemoteController,
                      ip=CONTROLLER_IP,
                      port=6633)

    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
    h5 = net.addHost( 'h5', ip='10.0.0.5' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    s5 = net.addSwitch( 's5' )
    s6 = net.addSwitch( 's6' )
    net.addLink( h1, s1 )
    net.addLink( h2, s4 )
    net.addLink( h5, s3 )
    net.start()

    # Configure the GRE tunnel
    s6.cmd('ovs-vsctl add-port s6 s6-gre1 -- set interface s6-gre1 type=gre options:remote_ip='+NODE2_IP)
    s6.cmdPrint('ovs-vsctl show')

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()