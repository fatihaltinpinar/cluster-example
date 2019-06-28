#!/usr/bin/env bash
export HOSTMAIN=$(oc whoami -c | grep -oP "(?<=\/).*?(?=:)")
sed -i 's/(hostname)/'"$HOSTMAIN"'/g' routes.yaml
