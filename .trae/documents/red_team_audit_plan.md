# 红队自动化审计系统计划

## 1. 项目分析结论

### 1.1 技术栈识别
- **后端**: Go语言，使用Gin框架
- **前端**: React + JavaScript
- **数据库**: 可能使用MySQL/PostgreSQL（基于SQL迁移文件）
- **鉴权中间件**: 存在auth.go中间件
- **其他组件**: Redis（用于缓存和速率限制）

### 1.2 关键目录结构
- `controller/`: API控制器
- `middleware/`: 中间件（包含鉴权）
- `router/`: 路由定义
- `relay/`: 第三方服务集成
- `service/`: 业务逻辑
- `web/`: 前端代码

## 2. 审计计划

### 2.1 阶段一：全局建模与清单 (Matrix Generation)
- **Action**: 扫描全路径，识别技术栈和架构
- **Output**: 创建 AUDIT_LOG.md 文件
- **任务**:
  1. 识别所有 Entry_Points (路由)
  2. 标记 Sensitive_Sinks (执行/查询/文件操作)
  3. 生成按目录深度排序的待审计文件列表

### 2.2 阶段二：解耦审计 (Sub-Agent Tasking)
- **Action**: 逐一派发任务给 subagent
- **Sub-Agent 指令模板**:
  ```
  请细致审计 [File_Path]。要求：
  1. 识别所有外部输入变量
  2. 追踪这些变量是否传递给其他文件（列出目标文件与函数）
  3. 寻找潜在的 Interaction_Logic 风险
  4. 将发现的所有疑似点（未经验证）写入 /tmp/potential_findings/ 下的独立 JSON 文件中
  ```
- **关联性维护**: 构建 Global_Taint_Graph

### 2.3 阶段三：环境自建与影子验证 (Self-Validation)
- **Action**: 本地环境构建
- **动态验证流**:
  1. 从 /tmp/potential_findings/ 读取所有疑似点
  2. 确认服务存活状态
  3. 编写并执行 Python 验证脚本 (poc.py)
  4. 分析日志，排除误报

### 2.4 阶段四：标准化成果输出 (Reporting)
- **Output**: 为每个验证成功的案例创建 Case 文件夹
- **内容**:
  1. logic_trace.json: 跨文件调用链
  2. poc.py: 本地环境验证脚本
  3. reproduction_guide.md: 详细复现指南

## 3. 工具与方法

### 3.1 扫描工具
- 使用 `SearchCodebase` 工具识别 Entry_Points
- 使用 `Grep` 工具搜索 Sensitive_Sinks

### 3.2 分析工具
- 使用 `Read` 工具读取代码文件
- 使用 `general_purpose_task` 工具执行子代理审计

### 3.3 验证工具
- 使用 `RunCommand` 构建和启动环境
- 使用 `run_mcp` 调用浏览器工具进行验证

## 4. 风险处理

### 4.1 误报处理
- 对每个疑似点进行详细验证
- 分析失败原因，排除误报

### 4.2 环境安全
- 在隔离环境中执行验证
- 避免对生产环境造成影响

### 4.3 数据保护
- 不收集或存储敏感信息
- 验证后清理临时文件

## 5. 输出格式

### 5.1 AUDIT_LOG.md
- 项目架构描述
- 技术栈识别结果
- 待审计文件清单
- Entry_Points 和 Sensitive_Sinks 标记

### 5.2 案例输出
- **Case_[ID]_[Logic_Type] 文件夹**
  - logic_trace.json: 调用链分析
  - poc.py: 验证脚本
  - reproduction_guide.md: 复现指南

### 5.3 拓扑图
- 对复杂调用（超过3个文件关联）生成文本拓扑图

## 6. 执行顺序

1. 全局扫描与建模
2. 逐文件子代理审计
3. 环境构建与验证
4. 案例分析与报告

## 7. 注意事项

- 严格遵循术语脱敏要求
- 保持主上下文清晰，使用子代理执行具体分析
- 原子化操作，完成一个文件审计后再移动到下一个
- 保存所有原始分析建议到 /tmp/audit_raw/ 目录