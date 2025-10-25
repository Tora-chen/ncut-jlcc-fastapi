# NCUT JLCC FastAPI
日语社网站后端服务。

## 容器部署：
构建镜像：
```
podman compose build
```

运行：
```
podman compose up -d
```

## 源代码部署：
安装依赖：
```
uv sync
```

运行：
```
uv run fastapi run src/main.py --port=8910
```

## 修改BOX_KEY
创建目录BOX_KEY，BOX_KEY目录下创建KEY文件，写入值即可（BOX_KEY目录被挂载到容器，会同步到容器中）
