#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
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

namespace_imports = [
    'device/xiaomi/zorn-miuicamera',
]

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libcameraopt_jni.so': blob_fixup()
        .add_needed('libprocessgroup_shim_miuicamera.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'zorn-miuicamera',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
