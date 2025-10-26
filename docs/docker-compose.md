编写docker-compose.yml文件：
```yaml
services:
  ncut-jlcc-fastapi:
    # 构建镜像
    build:
      context: . # 使用当前目录作为构建上下文
      dockerfile: Dockerfile # 指定 Dockerfile 的名字

    image: ncut-jlcc-fastapi:0.1.1

    environment:
      - AUTHING_CLIENT_SECRET=xxxxxxx

    ports:
      - "8910:8910"

    volumes:
      - ./ENV/:/app/ENV/

    container_name: ncut-jlcc-fastapi

    # 容器在退出或服务器重启时自动重启
    restart: unless-stopped
```

构建镜像：
```
docker compose build
```

运行：
```
docker compose up -d
```