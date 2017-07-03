# vim:fileencoding=utf8
#---------------------------------------------------------------------------
# Copyright 2011 utahta
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#---------------------------------------------------------------------------
from __future__ import print_function
import vbcode
from struct import unpack
import sys, random
def test_vbc():
    # format() require python 2.6 or higher.
    def test_vb_encode(numbers, ok):
        bytestream = vbcode.encode(numbers)
        assert ''.join([format(b, '08b') for b in unpack('%dB' % len(bytestream), bytestream)]) == ok
        print("test ok. %s -> %s" % (numbers, ok))
    
    test_vb_encode([1],    '10000001')
    test_vb_encode([5],    '10000101')
    test_vb_encode([127],  '11111111')
    test_vb_encode([128],  '00000001' + '10000000')
    test_vb_encode([129],  '00000001' + '10000001')
    test_vb_encode([1, 5], '10000001' + '10000101')

    def test_vb_decode():    
        n = random.randint(0, sys.maxsize)
        assert vbcode.decode(vbcode.encode([n]))[0] == n
        print("test ok. %s -> %s" % (n, n))

    test_vb_decode()
