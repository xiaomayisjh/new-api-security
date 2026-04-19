# NewAPI 自动化测试脚本

这是一套完整的 Python 自动化测试脚本，用于测试 NewAPI 的所有主要功能。

## 文件结构

```
tests/api_tests/
├── api_client.py          # API 客户端封装
├── test_basic.py         # 基础功能测试
├── test_user.py          # 用户功能测试
├── test_token.py         # Token 管理测试
├── run_all.py            # 综合测试脚本
├── requirements.txt      # Python 依赖
└── README.md             # 本文件
```

## 测试功能覆盖

### 1. 基础功能 (test_basic.py)
- ✅ 获取系统状态
- ✅ 获取公告
- ✅ 获取关于信息
- ✅ 获取用户协议
- ✅ 获取隐私政策
- ✅ 获取首页内容
- ✅ 获取价格信息
- ✅ 获取比例配置

### 2. 用户管理 (test_user.py)
- ✅ 用户注册
- ✅ 用户登录
- ✅ 获取当前用户信息
- ✅ 获取用户分组
- ✅ 获取用户可用模型
- ✅ 生成访问令牌
- ✅ 获取邀请码
- ✅ 获取充值信息
- ✅ 获取充值记录
- ✅ 更新用户设置
- ✅ 签到功能
- ✅ 日志查询
- ✅ 获取用户数据
- ✅ 订阅相关功能
- ✅ Midjourney 和任务功能
- ✅ OAuth 绑定
- ✅ 用户登出

### 3. Token 管理 (test_token.py)
- ✅ 添加 Token
- ✅ 获取所有 Token
- ✅ 获取单个 Token
- ✅ 获取 Token Key
- ✅ 更新 Token
- ✅ 搜索 Token
- ✅ 删除 Token
- ✅ 批量操作 Token
- ✅ 创建不同类型 Token

## 安装和使用

### 1. 安装依赖

```bash
cd tests/api_tests
pip install -r requirements.txt
```

### 2. 运行单个测试

可以分别运行每个测试文件：

```bash
# 基础功能测试
python test_basic.py --base-url http://localhost:3000

# 用户功能测试
python test_user.py --base-url http://localhost:3000 --username test_user --password Test@123456

# Token 管理测试
python test_token.py --base-url http://localhost:3000 --username test_user --password Test@123456
```

### 3. 运行全部测试

使用综合测试脚本运行所有测试：

```bash
python run_all.py --base-url http://localhost:3000
```

可以选择性跳过某些测试：

```bash
# 跳过基础测试，只运行用户和 Token 测试
python run_all.py --base-url http://localhost:3000 --skip-basic

# 使用指定的测试用户
python run_all.py --base-url http://localhost:3000 --username existing_user --password UserPassword
```

## API 客户端使用

你也可以直接使用 `NewAPIClient` 来进行 API 调用：

```python
from api_client import NewAPIClient

client = NewAPIClient(base_url="http://localhost:3000")

# 获取系统状态
success, data = client.get_status()
print(data)

# 用户注册
success, data = client.register("testuser", "Test@123456")

# 用户登录
success, data = client.login("testuser", "Test@123456")

# 创建 Token
success, data = client.add_token("my_api_key")
```

## 注意事项

1. **服务器状态**：确保 NewAPI 服务正在运行并可以访问
2. **注册功能**：如果测试环境禁用了注册功能，请使用已有的用户账号
3. **邮箱验证**：如果启用了邮箱验证，测试注册可能会失败
4. **测试账号**：建议使用专门的测试账号，避免影响生产数据
5. **清理**：测试完成后，生成的测试 Token 可以在脚本中自动删除，也可以手动清理

## 配置说明

所有脚本都支持以下参数：

- `--base-url`: NewAPI 服务器地址，默认 `http://localhost:3000`
- `--username`: 测试用用户名（可选，脚本会自动生成）
- `--password`: 测试用密码（可选，脚本会使用默认密码）

用户和 Token 测试脚本会在需要时自动创建测试用户。

## 输出示例

运行测试后，你会看到彩色的输出，显示每个测试的状态：

```
============================================================
基础功能测试
============================================================

[INFO] 正在测试获取系统状态...
[SUCCESS] 获取系统状态成功!
  系统名称: NewAPI
  版本号: x.x.x

============================================================
测试结果汇总:
============================================================
  test_get_status: 通过 - 成功获取系统状态
  test_get_notice: 通过 - 成功获取公告
  ...

总计: 8 个测试
通过: 8 个
失败: 0 个
```

## 许可证

与 NewAPI 使用相同的许可证。
