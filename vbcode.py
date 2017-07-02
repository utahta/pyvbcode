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
from __future__ import division 
from struct import pack, unpack

def encode_number(number):
    """Variable byte code encode number.
    Usage:
      import vbcode
      vbcode.encode_number(128)
    """
    bytes_list = []
    while True:
        bytes_list.insert(0, number % 128)
        if number < 128:
            break
        number = number // 128
    bytes_list[-1] += 128
    return pack('%dB' % len(bytes_list), *bytes_list)

def encode(numbers):
    """Variable byte code encode numbers.
    Usage:
      import vbcode
      vbcode.encode([32, 64, 128])
    """
    bytes_list = []
    for number in numbers:
        bytes_list.append(encode_number(number))
    return b"".join(bytes_list)

def decode(bytestream):
    """Variable byte code decode.
    Usage:
      import vbcode
      vbcode.decode(bytestream)
        -> [32, 64, 128]
    """
    n = 0
    numbers = []
    bytestream = unpack('%dB' % len(bytestream), bytestream)
    for byte in bytestream:
        if byte < 128:
            n = 128 * n + byte
        else:
            n = 128 * n + (byte - 128)
            numbers.append(n)
            n = 0
    return numbers

