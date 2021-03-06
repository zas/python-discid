# Copyright (C) 2013  Johannes Dewender
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Please submit bug reports to GitHub:
# https://github.com/JonnyJD/python-discid/issues
"""utility functions
"""

SECTORS_PER_SECOND = 75

def _encode(string):
    """Encode (unicode) string to byte string
    """
    try:
        return string.encode()
    except AttributeError:
        # already byte string (Python 3)
        return string
    # UnicodeDecodeError (Python 2) is NOT catched
    # device names should be ascii

def _decode(byte_string):
    """Decode byte string to (unicode) string
    """
    # this test for bytes works on Python 2 and 3
    if type(byte_string) == type(b"test"):
        return byte_string.decode()
    else:
        # probably mocked for sphinx
        return None


# vim:set shiftwidth=4 smarttab expandtab:
