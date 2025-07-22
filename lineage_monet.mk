#
# Copyright (C) 2021 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from monet device
$(call inherit-product, device/xiaomi/monet/device.mk)

# Camera
$(call inherit-product-if-exists, device/xiaomi/camera/miuicamera.mk)

# Build Flags
TARGET_SCREEN_HEIGHT          := 2400
TARGET_SCREEN_WIDTH           := 1080
TARGET_USES_MINI_GAPPS        := true
TARGET_BUILD_DEVICE_AS_WEBCAM := true
TARGET_HAS_UDFPS              := true
TARGET_INCLUDE_ACCORD         := false
BUILD_BCR                     := true

PRODUCT_NAME := lineage_monet
PRODUCT_DEVICE := monet
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := M2002J9G

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="monet-user 12 SKQ1.211006.001 V13.0.2.0.SJIEUXM release-keys" \
    BuildFingerprint=Xiaomi/monet_eea/monet:12/SKQ1.211006.001/V13.0.2.0.SJIEUXM:user/release-keys
