# Copyright (c) 2016, Brandan Geise [coldfusion]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class Helpers(object):
	"""
	Helper functions
	"""
	def __init__(self):
		pass

	def print_error(self, message):
		"""
		Wrapper for error messages.
		Parameters
		----------
			message : str
				Message to display as an error.
		"""
		print("\033[1m\033[31m[-]\033[0m {0}".format(message))

	def print_status(self, message):
		"""
		Wrapper for status messages.
		Parameters
		----------
			message : str
				Message to display as a status.
		"""
		print("\033[1m\033[34m[*]\033[0m {0}".format(message))

	def print_good(self, message):
		"""
		Wrapper for success messages.
		Parameters
		----------
			message : str
				Message to display as a success.
		"""
		print("\033[1m\033[32m[+]\033[0m {0}".format(message))

	def print_warn(self, message):
		"""
		Wrapper for warning messages.
		Parameters
		----------
			message : str
				Message to display as an warning.
		"""
		print("\033[1m\033[33m[!]\033[0m {0}".format(message))
