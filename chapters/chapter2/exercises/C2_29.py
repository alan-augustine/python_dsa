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

from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""
  
  def __init__(self, customer, bank, acnt, limit, apr, _min_month_pay_percent=10):
    """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit)  # call super constructor
    self._apr = apr
    self._monthly_transactions = 0
    self._min_month_pay_percent = _min_month_pay_percent
    self._min_month_payment = 0

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    success = super().charge(price)          # call inherited method
    # Creativity C-2.28
    self._monthly_transactions += 1
    if self._monthly_transactions > 10:
        self._balance += 1
    if not success:
      self._balance += 5                     # assess penalty
    return success                           # caller expects return value

  def process_month(self):
    """Assess monthly interest on outstanding balance."""
    if self._balance > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      self._balance *= monthly_factor
      # Creativity C-2.28
      self._monthly_transactions = 0

      # Creativity excercise C-2.29
      if self._min_month_payment > 0:
        self._balance += 5 # assume $5 penalty for not making min. payment
      self._min_month_payment = self._balance * (self._min_month_pay_percent/100)

  # TODO: testing
  # override for Creativity C-2.29 (did not test)
  # Calculate min. monthly payment in monthly batch(process_month() function)
  # For each payment made, decrease min. monthly payment and outstanding balance
  # Apply penalty , if prev. month's min. payment is not zero
  # reset min. monthly payment, after charging penalty
  def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    self._balance -= amount
    # C-2.29 - to track min. payment
    self._min_month_payment -= amount