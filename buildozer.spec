[app]
title = SniperVenom25
package.name = snipervenom25
package.domain = com.harmon.snipervenom25

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.ant = auto
p4a.bootstrap = sdl2
