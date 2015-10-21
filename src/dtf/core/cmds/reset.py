# Android Device Testing Framework ("dtf")
# Copyright 2013-2015 Jake Valletta (@jake_valletta)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Built-in module for reseting a project"""
import os

import dtf.core.utils as utils
import dtf.logging as log

from dtf.module import Module

TAG = 'reset'

class reset(Module):

    """Module class for reseting a project"""

    def execute(self, args):

        """Main module executor"""

        print ('Are you sure you want to delete the dtf project in this '
               'directory? This cannot be reversed! [y/N]'),

        inp = raw_input()

        if inp.lower() == 'y':
            os.remove(utils.CONFIG_FILE_NAME)
            log.i(TAG, "Reset complete!")
            return 0
        else:
            log.w(TAG, "Reset aborted.")
            return -1
