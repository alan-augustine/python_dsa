# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from abc import ABCMeta, abstractmethod           # need these definitions

class Sequence(metaclass=ABCMeta):
  """Our own version of collections.Sequence abstract base class."""

  @abstractmethod
  def __len__(self):
    """Return the length of the sequence."""

  @abstractmethod
  def __getitem__(self, j):
    """Return the element at index j of the sequence."""

  def __contains__(self, val):
    """Return True if val found in the sequence; False otherwise."""
    for j in range(len(self)):
      if self[j] == val:                          # found match
        return True
    return False

  def index(self, val):
    """Return leftmost index at which val is found (or raise ValueError)."""
    for j in range(len(self)):
      if self[j] == val:                          # leftmost match
        return j
    raise ValueError('value not in sequence')     # never found a match

  def count(self, val):
    """Return the number of elements equal to given value."""
    k = 0
    for j in range(len(self)):
      if self[j] == val:                          # found a match
        k += 1
    return k

  # Excercise R-2.22 - did not test
  def __eq__(self, other):
      # need __len__() defined
      if len(self) != len(other):
          # if different lengths, not equal
          return False
      for i in len(self):
          # need __getitem__() defined
          if self[i] != other[i]:
              return False
      return True

  # Exercise R-2.23 - did not test
  def __lt__(self, other):
      # 'z' > 'aaa' is True - try in Python terminal
      # 'a' < 'aaa' is True - try in Python terminal
      l = min(len(self), len(other))
      for i in range(l):
          if self[i] < other[i]:
              return True
          elif self[i] > other[i]:
              return False
      # at this point, all elements checked are equal
      if len(self) > len(other):
          # 'self' is larger
          return False
      else:
          return False