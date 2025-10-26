# NCUT JLCC FastAPI
日语社网站后端服务。

## 容器部署：
构建镜像：
```
docker build . -t ncut-jlcc-fastapi:0.1.1
```

运行：
```
docker run -d -p 8910:8910 --name ncut-jlcc-fastapi \
  -v $(pwd)/ENV/:/app/ENV/ \
  -e AUTHING_CLIENT_SECRET=xxxx \
  ncut-jlcc-fastapi:0.1.1
```

或者[使用Docker Compose部署](docs/docker-compose.md)。

## 源代码部署：
安装依赖：
```
uv sync
```

创建.env文件：
```
echo "AUTHING_CLIENT_SECRET=xxxxxx" > ENV/.env
```

运行：
```
uv run fastapi run src/main.py --port=8910
```

## 修改KEY
修改`ENV/KEY`文件的内容为密码即可（`ENV`目录被挂载到容器，会同步到容器中）
