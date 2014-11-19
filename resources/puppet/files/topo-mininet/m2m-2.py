#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    NODE1_IP='192.168.40.10'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    net.addController( 'c1',
                      controller=RemoteController,
                      ip=CONTROLLER_IP,
                      port=6633)

    h3 = net.addHost( 'h3', ip='10.0.0.3' )
    h4 = net.addHost( 'h4', ip='10.0.0.4' )
    h6 = net.addHost( 'h6', ip='10.0.0.6' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    s5 = net.addSwitch( 's5' )
    s6 = net.addSwitch( 's6' )
    net.addLink( h3, s3 )
    net.addLink( h4, s2 )
    net.addLink( h6, s4 )
    net.start()

    # Configure the GRE tunnel
    s5.cmd('ovs-vsctl add-port s5 s5-gre1 -- set interface s5-gre1 type=gre options:remote_ip='+NODE1_IP)
    s5.cmdPrint('ovs-vsctl show')

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()