from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.typing import IS_CONFIG, IS_PATH


class ExtractPackageManagerFileInputs(TypedDict, total=False):
    sbom_vdr_file_path: Annotated[str, IS_CONFIG, IS_PATH]
    sbom_vdr_values: dict
    package_manager_file: Annotated[str, IS_CONFIG]
    upgrade_threshold: Annotated[str, IS_CONFIG]
    severity: Annotated[str, IS_CONFIG]


class ExtractPackageManagerFileOutputs(TypedDict):
    files_to_patch: list[dict]
