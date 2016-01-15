# -*- coding: utf-8 -*-

#    unwiki - remove wiki tags from a document
#    Copyright (C) 2016 Neil Freeman

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.#

import unittest
import unwiki


class unwikiTestCase(unittest.TestCase):

    def testLink(self):
        self.assertEqual(unwiki.loads('etc [[relative|link]] foo'), 'etc link foo')
        assert unwiki.loads('[[link]]') == 'link'
        self.assertEqual(unwiki.loads('[[relative link|link]]'), 'link')
        self.assertEqual(unwiki.loads('etc [[relative-link|link]] foo'), 'etc link foo')
        assert unwiki.loads('[[link (subject)|link]]') == 'link'

        assert unwiki.loads('[[Bar, Foo|Baz]], [[Foo]]') == 'Baz, Foo'

    def testComment(self):
        assert unwiki.loads('<!-- comment -->foo') == 'foo'

    def testHeadline(self):
        self.assertEqual(unwiki.loads('=== Head ==='), ' Head ')

    def testCompressSpaces(self):
        self.assertEqual(unwiki.loads('removing this {{thing}} leaves extra spaces', True), 'removing this leaves extra spaces')

    def testInfobox(self):
        self.assertEqual(unwiki.loads('{{Infobox none}} None'), ' None')
        self.assertEqual(unwiki.loads('{{foo bar}}'), '')
        self.assertEqual(unwiki.loads("""{{foo\nbar}}"""), '')

        self.assertEqual(unwiki.loads("""{{Infobox
            foo}} None"""), ' None')

    def testRE(self):
        assert unwiki.RE.sub('x', '[[foo]]') == 'xfoox'
        assert unwiki.RE.sub('x', '{{foo}}') == 'x'
        assert unwiki.RE.sub('x', '{{foo\nbar}}') == 'x'

    def testList(self):
        lis = '* foo\n * bar\n ** [[baz]]'
        self.assertEqual(unwiki.loads(lis), "* foo\n * bar\n ** baz")

    def testFreeform(self):

        infobox = '''{{Infobox settlement
        <!--See Template:Infobox settlement for additional fields that may be available-->
        <!--See the Table at Infobox settlement for all fields and descriptions of usage-->
        <!-- General information  --------------->
        |timezone               = [[Eastern Time Zone|Eastern Standard Time]]
        |utc_offset             = -5
        }}'''

        self.assertEqual(unwiki.loads(infobox), '')

        markup = """{{about|the borough in New York City}}\n'''Staten Island ''' {{IPAc-en|ˌ|s|t|æ|t|ən|_|ˈ|aɪ|l|ə|n|d}} is one of the five [[borough (New York City)|boroughs]] of [[New York City]], in the U.S. state of [[New York]]."""
        expect = "\nStaten Island   is one of the five boroughs of New York City, in the U.S. state of New York."

        self.assertEqual(unwiki.loads(markup), expect)

        markup = """In the southwest of the city, Staten Island is the southernmost part of both the city and state of New York, with [[Conference House Park]] at the southern tip of the island and the state.<ref>{{cite web|website=http://www.nycgovparks.org/parks/conferencehousepark|title=Conference House Park|publisher=New York City Parks|accessdate=June 21, 2014}}</ref>"""
        expect = """In the southwest of the city, Staten Island is the southernmost part of both the city and state of New York, with Conference House Park at the southern tip of the island and the state."""
        self.assertEqual(unwiki.loads(markup), expect)


if __name__ == '__main__':
    unittest.main()
