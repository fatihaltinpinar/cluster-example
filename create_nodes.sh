#!/usr/bin/env bash
export SESID=$(oc whoami -c | grep -oP "(?<=\/)([0-9].*?)(?=-)")
sed -i 's/(SESID)/'"$SESID"'/g' routes.yaml
