#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so': blob_fixup()
        .sig_replace('9A 0A 00 94', '1F 20 03 D5'),
    'vendor/lib64/camera/components/com.mi.node.watermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    'vendor/lib64/vendor.qti.hardware.camera.device@1.0.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.camera.device@1.0.so', 'vendor.qti.hardware.camera.device@1.0_vendor.so'),
    (
        'vendor/lib64/libMIAIHDRhvx_interface.so',
        'vendor/lib64/libarcsoft_hdrplus_hvx_stub.so',
        'vendor/lib64/libarcsoft_super_night_raw.so',
        'vendor/lib64/libmialgo_rfs.so',
    ): blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open')
        .clear_symbol_version('remote_register_buf')
        .clear_symbol_version('remote_register_buf_attr'),
    (
        'vendor/lib64/libalAILDC.so',
        'vendor/lib64/libalLDC.so',
        'vendor/lib64/libalhLDC.so',
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),

}  # fmt: skip

namespace_imports = [
    'hardware/qcom/sm7250/display',
    'hardware/xiaomi',
    'vendor/xiaomi/sm7250-common',
    'vendor/qcom/opensource/display',
]

module = ExtractUtilsModule(
    'monet',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
