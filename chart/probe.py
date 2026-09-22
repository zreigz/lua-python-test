ns = k8s_object_meta("", "v1", "Namespace", "", "agents")
if ns is None:
    raise RuntimeError("kube-system Namespace is not in the agent cache")

missing = k8s_object_meta("apps", "v1", "Deployment", "default", "does-not-exist")

values["observeClusterId"] = ns["uid"]
values["labels"] = ns["labels"]
values["missing"] = str(missing is None)
