#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    'libcameraopt': lambda lib, partition, *args, **kwargs: f'{lib}_miuicamera'
    if partition == 'system_ext'
    else lib,
}

module = ExtractUtilsModule(
    'zorn-miuicamera',
    'xiaomi',
    lib_fixups=lib_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
