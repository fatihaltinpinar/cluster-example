The deployment config cannot automatically rollout since it requires a trigger fom an external webserver called [WEBHOOKS](https://docs.openshift.com/container-platform/3.5/dev_guide/builds/triggering_builds.html#webhook-triggers). Since I do not know the host ip and the port I can't use it now.


With the command

```shell
oc rollout latest dc/counter
```

a manual rollout can be initiated to get latest image running on the pods.
