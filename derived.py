import hubmapinventory
import hubmapbags
import sys

token = "this-is-my-token"
ncores = 25

assay_types = hubmapbags.apis.get_assay_types(token=token)
assay_types.remove("CODEX")
assay_types.remove("codex_cytokit")
assay_types.remove("codex_cytokit_v1")

compute_uuids = True
for assay_type in assay_types:
    print(assay_type)
    datasets = hubmapbags.apis.get_hubmap_ids(assay_type, token=token)

    for dataset in datasets:
        if (
            not dataset["is_protected"]
            and not dataset["is_primary"]
            and dataset["status"] == "Published"
        ):
            df = hubmapinventory.inventory.create(
                dataset["hubmap_id"],
                token=token,
                ncores=ncores,
                compute_uuids=compute_uuids,
            )
