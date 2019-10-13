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

from mussels.recipe import BaseRecipe


class Recipe(BaseRecipe):
    """
    Recipe to build nghttp2.
    """

    mussels_version = "0.1"

    name = "nghttp2"
    version = "1.39.2"
    url = "https://github.com/nghttp2/nghttp2/archive/v1.39.2.zip"
    archive_name_change = ("v", "nghttp2-")
    platforms = {
        "Windows": {
            "x86": {
                # "patches": "patches_windows", # (optional) Apply a patch set in this directory before the "configure" build step
                "install_paths": {
                    "license/nghttp2": ["COPYING"],
                    "include": [os.path.join("lib", "includes", "nghttp2")],
                    "lib": [
                        os.path.join("lib", "Release", "nghttp2.dll"),
                        os.path.join("lib", "Release", "nghttp2.lib"),
                    ],
                },
                "dependencies": ["openssl>=1.0.1", "zlib>=1.2.3"],
                "required_tools": ["cmake", "visualstudio>=2017"],
                "build_script": {
                    "configure": """
                            CALL cmake.exe -G "Visual Studio 15 2017" -T v141 \
                                -DCMAKE_CONFIGURATION_TYPES=Release \
                                -DBUILD_SHARED_LIBS=ON \
                                -DOPENSSL_ROOT_DIR="{install}" \
                                -DOPENSSL_INCLUDE_DIR="{includes}" \
                                -DLIB_EAY_RELEASE="{libs}/libcrypto.lib" \
                                -DSSL_EAY_RELEASE="{libs}/libssl.lib" \
                                -DZLIB_ROOT="{includes}" \
                                -DZLIB_LIBRARY="{libs}/zlibstatic.lib"
                        """,
                    "make": """
                            CALL cmake.exe --build . --config Release
                        """,
                },
            },
            "x64": {
                # "patches": "patches_windows",
                "install_paths": {
                    "license/nghttp2": ["COPYING"],
                    "include": [os.path.join("lib", "includes", "nghttp2")],
                    "lib": [
                        os.path.join("lib", "Release", "nghttp2.dll"),
                        os.path.join("lib", "Release", "nghttp2.lib"),
                    ],
                },
                "dependencies": ["openssl>=1.0.1", "zlib>=1.2.3"],
                "required_tools": ["cmake", "visualstudio>=2017"],
                "build_script": {
                    "configure": """
                            CALL cmake.exe -G "Visual Studio 15 2017 Win64" -T v141 \
                                -DCMAKE_CONFIGURATION_TYPES=Release \
                                -DBUILD_SHARED_LIBS=ON \
                                -DOPENSSL_ROOT_DIR="{install}" \
                                -DOPENSSL_INCLUDE_DIRS="{includes}" \
                                -DLIB_EAY_RELEASE="{libs}/libcrypto.lib" \
                                -DSSL_EAY_RELEASE="{libs}/libssl.lib" \
                                -DZLIB_ROOT="{includes}" \
                                -DZLIB_LIBRARY="{libs}/zlibstatic.lib"
                        """,
                    "make": """
                            CALL cmake.exe --build . --config Release
                        """,
                },
            },
        },
        "Darwin": {
            "host": {
                "install_paths": {"license/nghttp2": ["COPYING"]},
                "dependencies": ["openssl>=1.0.1", "zlib>=1.2.3", "libxml2>=2.9.9"],
                "required_tools": ["cmake", "make", "clang"],
                "build_script": {
                    "configure": """
                            cmake . \
                                -DCMAKE_CONFIGURATION_TYPES=Release \
                                -DBUILD_SHARED_LIBS=ON \
                                -DOPENSSL_ROOT_DIR="{install}" \
                                -DOPENSSL_INCLUDE_DIRS="{includes}" \
                                -DOPENSSL_LIBRARIES="{libs}" \
                                -DOPENSSL_CRYPTO_LIBRARY="{libs}/libcrypto.1.1.dylib" \
                                -DOPENSSL_SSL_LIBRARY="{libs}/libssl.1.1.dylib" \
                                -DLIBXML2_INCLUDE_DIRS="{includes}" \
                                -DLIBXML2_LIBRARY="{libs}/libxml2.dylib" \
                                -DZLIB_ROOT="{includes}" \
                                -DZLIB_LIBRARY="{libs}/libz.a" \
                                -DCMAKE_INSTALL_PREFIX="{install}/{target}"
                        """,
                    "make": """
                            cmake --build . --config Release
                        """,
                    "install": """
                            make install
                            install_name_tool -add_rpath @executable_path/../lib "{install}/{target}/lib/libnghttp2.dylib"
                        """,
                },
            }
        },
    }
