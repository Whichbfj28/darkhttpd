#!/usr/bin/env python3
# This is run by the "run-tests" script.
import unittest
from test import TestHelper, Conn, parse

class TestForward(TestHelper):
    def test_no_server_id(self):
        resp = self.get('/', method = 'BOGUS')
        status, hdrs, body = parse(resp)
        self.assertContains(status, "400 Bad Request")
        self.assertFalse('Server' in hdrs)
        self.assertFalse(b'Generated by darkhttpd/' in body)

if __name__ == '__main__':
    unittest.main()

# vim:set ts=4 sw=4 et:
