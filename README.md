# cytoid-fastapi

对 Cytoid 的 Graphql 接口进行再包装, 以 Fastapi 接口返回数据

# 部署

- `git clone`
- 在 env 里面填上分发给用户的 Token, 用户可以拿这个访问端点  
  like: `TOKEN=["114514c7c245e","1919810"]` 这里面就有两个 Token 了
- `poetry install`
- `uvicorn main:app --reload`

# TODO

## API Entry

- [x] Bearer Auth 别的不加 先加上验证

- [x] user/info 用户信息

- [ ] user/best 单曲最佳

- [ ] song/info 谱面信息

- [ ] song/random 随一个

- [ ] assets/song 曲目试听

- [ ] data/update 安装包

- [ ] data/challenge 直连

- [ ] image/user/* 用户头像
