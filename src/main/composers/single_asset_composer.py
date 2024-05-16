from src.data.use_cases.single_asset import SingleAsset
from src.presentation.controllers.single_asset_controller import SingleAssetController

def single_asset_composer():
    use_case = SingleAsset()
    controller = SingleAssetController(use_case)

    return controller.handle
