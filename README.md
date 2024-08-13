
##### 构建镜像
```bash
docker build -t hkccr.ccs.tencentyun.com/zhengkai/ttt .
```
修改docker-compose.yml中image为最新镜像地址

##### 启动
```bash
docker-compose up -d
```
浏览器访问`http://127.0.0.1:5000`
