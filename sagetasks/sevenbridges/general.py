from sagetasks.sevenbridges.utils import SbgUtils


def bundle_client_args(auth_token, platform="cavatica", endpoint=None, **kwargs):
    return SbgUtils.bundle_client_args(auth_token, platform, endpoint, **kwargs)


def get_project_id(client_args, project_name, billing_group_name):
    utils = SbgUtils(client_args)
    project = utils.get_or_create_project(project_name, billing_group_name)
    project_id = utils.extract_id(project)
    return project_id


def get_copied_app_id(client_args, project, app_id=None):
    utils = SbgUtils(client_args)
    utils.open_project(project)
    copied_app = utils.get_or_create_copied_app(app_id)
    copied_app_id = utils.extract_id(copied_app)
    return copied_app_id


def get_volume_id(client_args, volume_name=None, volume_id=None):
    utils = SbgUtils(client_args)
    volumes = utils.get_volume(volume_name, volume_id)
    assert len(volumes) > 0, "This function cannot create a volume if it's missing"
    assert len(volumes) < 2, "Use a more specific volume name or use an ID instead"
    volume = volumes[0]
    volume_id = utils.extract_id(volume)
    return volume_id


def import_volume_file(client_args, project, volume_id, volume_path, project_path):
    utils = SbgUtils(client_args)
    utils.open_project(project)
    imported_file = utils.get_or_create_volume_file(
        volume_id, volume_path, project_path
    )
    imported_file_id = utils.extract_id(imported_file)
    return imported_file_id