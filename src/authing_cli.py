import os
from authing import AuthenticationClient

# 初始化 AuthenticationClient
authentication_client = AuthenticationClient(
    # Authing 应用 ID
    app_id="6717834b204b7b910e18ffe8",
    # Authing 应用密钥
    app_secret="_",
    # Authing 应用地址
    app_host="https://ncut-jlcc.authing.cn",
    # Authing 应用配置的登录回调地址
    redirect_uri="http_",
)

