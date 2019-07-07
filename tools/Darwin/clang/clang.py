"""
Copyright (C) 2019 Cisco Systems, Inc. and/or its affiliates. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
from pathlib import Path

from tools.tool import BaseTool


class Tool(BaseTool):
    """
    Tool to detect Apple LLVM version 10 (Apple clang)
    """

    name = "clang"
    version = "10"
    url = ""

    path_mods = {
        "usr": {"host": []},
        "local": {"host": [os.path.join("/usr", "local", "bin")]},
    }

    file_checks = {
        "usr": [os.path.join("/usr", "bin", "clang")],
        "local": [os.path.join("/usr", "local", "bin", "clang")],
    }

    # Install script to use in case the tool isn't already available and must be installed.
    install_script = """
    """