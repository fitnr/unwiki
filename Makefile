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

.PHONY: install upload clean deploy

install: README.rst
    python setup.py install

README.rst: README.md
    - pandoc $< -o $@
    @touch $@
    python setup.py check --restructuredtext --strict

deploy: README.rst | clean
    python setup.py register
    python setup.py bdist_wheel
    twine upload dist/*

clean:; rm -rf dist build
