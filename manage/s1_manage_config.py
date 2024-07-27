# -*- coding: utf-8 -*-

"""
将所有服务器的配置数据部署到 AWS S3. 在这个项目中, 因为集群上的服务器数量多, 配置的内容复杂,
最终配置数据可能会很大. 只有用 AWS S3 才可以存储任意多, 任意大的数据.

- Edit non secret config data: ``~/Documents/GitHub/acore_server_config-project/config/config.json``
- Edit secret config data: ``~/.projects/acore_server_config/config-secret.json``
"""

from s3pathlib import S3Path
from boto_session_manager import BotoSesManager
from settings import aws_profile, path_config_json, path_config_secret_json
import acore_server_config.api as acore_server_config

bsm = BotoSesManager(profile_name=aws_profile)

config = acore_server_config.Config.read(
    env_class=acore_server_config.Env,
    env_enum_class=acore_server_config.EnvEnum,
    path_config=path_config_json,
    path_secret_config=path_config_secret_json,
)

s3folder_config = (
    S3Path(f"s3://{bsm.aws_account_alias}-{bsm.aws_region}-artifacts")
    .joinpath(
        "projects",
        "acore_server_config",
        "config",
    )
    .to_dir()
)

if __name__ == "__main__":
    config.deploy(bsm=bsm, s3folder_config=s3folder_config)
    # config.delete(bsm=bsm, s3folder_config=s3folder_config, include_history=True)
    pass
