#
# Copyright (C) 2018 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Contains file I/O APIs."""
from pathlib import Path


def read_file(path: Path) -> str:
    """Reads the contents of a file into a string, closing the file."""
    with open(path) as the_file:
        return the_file.read()


def write_file(path: Path, contents: str) -> None:
    """Writes the given string to the path specified, closing the file."""
    with open(path, "w") as the_file:
        the_file.write(contents)
