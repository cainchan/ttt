### TTT : TmpTexT
是一款免登录可自动保存的临时文本编辑器

####✨ 功能
- ✏ 无需登录/注册, 即刻开始书写
- 💾 自动保存
- 📦 一键部署你自己的私有化版本（如果你有自己的域名）

#### 部署
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
