# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

_SLOW_CRC32C_WARNING = (
    "Currently using crcmod in pure python form. This is a slow "
    "implementation. If you can compile a c extension, you will have much "
    "better performance."
)

# If available, default to CFFI Implementation, otherwise, use pure python.
try:
    from crc32c import cffi as _crc32c
    implementation = "cffi"
except ImportError:
    from crc32c import python as _crc32c
    warnings.warn(RuntimeWarning, "_SLOW_CRC32C_WARNING",)
    implementation = "python"

extend = _crc32c.extend
value = _crc32c.value

Checksum = _crc32c.Checksum

__all__ = ["extend", "value", "Checksum", "implementation"]
