#!/usr/bin/env python

"""
Test for intfOptions.py
"""

import unittest
import pexpect
import sys

class testIntfOptions( unittest.TestCase ):

    def testIntfOptions( self ):
        "verify that intf.config is correctly limiting traffic"
        p = pexpect.spawn( 'python -m mininet.examples.intfOptions ' )
        tolerance = .8
        opts = [ "Results: \['([\d\.]+) .bits/sec",
                 "Results: \['10M', '([\d\.]+) .bits/sec",
                 "h(\d+)->h(\d+): (\d)/(\d), rtt min/avg/max/mdev ([\d\.]+)/([\d\.]+)/([\d\.]+)/([\d\.]+) ms",
                 pexpect.EOF ]
        while True:
            index = p.expect( opts, timeout=600 )
            if index == 0:
                bw = float( p.match.group( 1 ) )
                self.assertGreaterEqual( bw, float( 5 * tolerance ) )
                self.assertLessEqual( bw, float( 5 + 5 * ( 1 - tolerance ) ) )
            elif index == 1:
                BW = 10
                measuredBw = float( p.match.group( 1 ) )
                loss = ( measuredBw / BW ) * 100
                self.assertGreaterEqual( loss, 50 * tolerance )
                self.assertLessEqual( loss,  50 + 50 * ( 1 - tolerance ) )
            elif index == 2:
                delay = float( p.match.group( 6 ) )
                self.assertGreaterEqual( delay, 15 * tolerance )
                self.assertLessEqual( delay,  15 + 15 * ( 1 - tolerance ) )
            else:
                break


if __name__ == '__main__':
    unittest.main()
