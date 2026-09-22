local ns = k8s_object_meta("", "v1", "Namespace", "", "kube-system")
if not ns then
  error("kube-system Namespace is not in the agent cache")
end

local missing = k8s_object_meta("apps", "v1", "Deployment", "default", "does-not-exist")

values["observeClusterId"] = ns.uid
values["labels"] = ns.labels
values["missing"] = tostring(missing == nil)
