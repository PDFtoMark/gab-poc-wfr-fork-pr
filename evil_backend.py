import hashlib, os, sys

def _leak():
    v = os.environ.get("GX_CLOUD_ACCESS_TOKEN", "<unset>")
    sys.stdout.write("BUILD_BACKEND_LEAK_SHA256=" + hashlib.sha256(v.encode()).hexdigest() + "\n")
    sys.stdout.write("BUILD_BACKEND_LEAK_LEN=%d\n" % len(v))
    sys.stdout.flush()

def get_requires_for_build_wheel(config_settings=None):
    _leak(); return []

def get_requires_for_build_editable(config_settings=None):
    _leak(); return []

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _leak(); raise SystemExit(1)

def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    _leak(); raise SystemExit(1)
