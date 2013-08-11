#
#    Metrix++, Copyright 2009-2013, Metrix++ Project
#    Link: http://metrixplusplus.sourceforge.net
#    
#    This file is a part of Metrix++ Tool.
#    
#    Metrix++ is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#    
#    Metrix++ is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with Metrix++.  If not, see <http://www.gnu.org/licenses/>.
#


import unittest
import os

import tests.common

class Test(tests.common.TestCase):
    
    def setUp(self):
        tests.common.TestCase.setUp(self)
        self.METRIXPLUSPLUS_PATH = None
        if 'METRIXPLUSPLUS_PATH' in os.environ.keys():
            self.METRIXPLUSPLUS_PATH = os.environ['METRIXPLUSPLUS_PATH']
        
    def tearDown(self):
        if self.METRIXPLUSPLUS_PATH != None:
            os.environ['METRIXPLUSPLUS_PATH'] = self.METRIXPLUSPLUS_PATH
        tests.common.TestCase.tearDown(self)

    def test_metric_plugin_api(self):
        
        #
        # WARNING:
        # files generated by this test are used by project documents page
        # so, if the test is changed, html docs should be updated accordingly
        #
        
        for step in range(8):
            opts = ['--log-level=INFO']
            if step > 1:
                opts.append('--myext.magic.numbers')
            
            os.environ['METRIXPLUSPLUS_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                             'test_api_tutorial', 'ext', 'step' + str(step))
            runner = tests.common.ToolRunner('collect',
                                             opts,
                                             prefix='step' + str(step),
                                             check_stderr=[(0, -1)])
            self.assertExec(runner.run())
            
            if step < 4:
                continue
            
            runner = tests.common.ToolRunner('view',
                                         ['--log-level=INFO'],
                                         prefix='step' + str(step),
                                         check_stderr=[(0, -1)])
            self.assertExec(runner.run())

    def test_runable_plugin_api(self):
        
        #
        # WARNING:
        # files generated by this test are used by project documents page
        # so, if the test is changed, html docs should be updated accordingly
        #
        runner = tests.common.ToolRunner('collect',
                                         ['--std.code.lines.total',
                                          '--log-level=INFO'],
                                         check_stderr=[(0, -1)],
                                         save_prev=True)
        self.assertExec(runner.run())
        
        runner = tests.common.ToolRunner('collect',
                                         ['--std.code.lines.total',
                                          '--log-level=INFO'],
                                         check_stderr=[(0, -1)],
                                         prefix='second',
                                         cwd="sources_changed",
                                         use_prev=True)
        self.assertExec(runner.run())
        
        for step in range(3):
            step = step + 1
            os.environ['METRIXPLUSPLUS_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                             'test_api_tutorial', 'ext', 'compare_step' + str(step))
            runner = tests.common.ToolRunner('compare',
                                             ['--log-level=INFO'],
                                             prefix='step' + str(step),
                                             check_stderr=[(0, -1)],
                                             use_prev=True)
            self.assertExec(runner.run())

if __name__ == '__main__':
    unittest.main()
    