# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_home = Path.home()
dir_manage = Path(__file__).parent
path_config_json = dir_manage.joinpath("config.json")
path_config_secret_json = dir_home / ".projects" / "acore_server_config" / "config-secret.json"
aws_profile = "bmt_app_dev_us_east_1"

