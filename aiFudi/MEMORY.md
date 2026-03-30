# MEMORY.md - 长期记忆

> 这是 Joy 的长期记忆文件，用于记录重要的信息、资源和决策。

---

## 🎯 核心项目：Fudi (福地)

**项目定位**: 下一代智能语音助手

**核心方向**:
1. **大模型与智能体**: 编排、RAG、记忆管理
2. **OpenClaw 生态**: 自定义 Skills 与 Tools 开发
3. **AI 硬件与 IoT**: 边缘计算、多传感器融合
4. **新交互范式**: 主动式、多模态、Agentic 行为

---

## 📚 重要资源

### LLM 性能与指标

**LLM Benchmark 资源**:
- **Artificial Analysis**: https://artificialanalysis.ai/
  - 用途: LLM 指标与性能的 benchmark
  - 使用场景: 评估和比较不同 LLM 的性能、价格、延迟等指标
  - 记录时间: 2026-02-27

---

## 🔧 技术栈与工具

### 智谱 MCP 服务配置

**配置文件**: `/home/admin/.openclaw/workspace/config/mcporter.json`

**已配置服务**:
1. **web-search-prime**: 联网搜索 (1 tool)
2. **web-reader**: 网页读取 (1 tool)
3. **zread**: 代码仓库 (3 tools)
4. **zai-vision**: 视觉理解 (8 tools)

**API Key**: `4c160474ff51415ba57cddb3444d0d46.ZIaK5ellcilq6MGT`

**使用方式**:
```bash
# 搜索
mcporter call web-search-prime.webSearchPrime search_query="搜索内容" location="cn"

# 读取网页
mcporter call web-reader.webReader url="https://example.com"

# 代码仓库
mcporter call zread.search_doc repo_name="owner/repo" query="关键词"
mcporter call zread.read_file repo_name="owner/repo" file_path="path/to/file"
mcporter call zread.get_repo_structure repo_name="owner/repo"
```

### OpenClaw Tools 核心技术

**完整参考**: 见 `TOOLS.md` → "OpenClaw Tools 技术参考"

**关键要点**:
1. **工具权限控制**: `tools.allow/deny`, `tools.profile` (minimal/coding/messaging/full), `tools.byProvider`
2. **工具组简写**: `group:runtime`, `group:fs`, `group:sessions`, `group:memory`, `group:web`, `group:ui`, `group:messaging`
3. **核心工具**:
   - `exec/process` - 命令执行与会话管理
   - `browser` - 浏览器自动化 (snapshot → act → screenshot)
   - `nodes` - 节点控制 (camera_snap, screen_record, notify, run)
   - `sessions_spawn` - 子智能体 (runtime: subagent|acp, mode: run|session, thread: true)
   - `message` - 多平台消息 (Discord, Telegram, WhatsApp, Slack, etc.)
   - `web_search/web_fetch` - 网络搜索与抓取
4. **安全配置**: loop-detection, elevated 权限, 媒体捕获需同意
5. **学习记录**: 2026-03-08 - 已完整学习 tools 文档并整理至 TOOLS.md

### ClawHub 技能管理

**核心工具**: 使用 `clawhub` CLI 管理和搜索技能（非手动下载）

**常用命令**:
- `clawhub search "关键词"` - 搜索技能
- `clawhub install <slug>` - 安装技能
- `clawhub list` - 列出已安装
- `clawhub update --all` - 更新所有技能

**安装计划** (2026-03-11 小杜同学指定):

**待安装（20个）**:
- 🔧 工具: mcp-adapter, qveris
- 🤖 进化: error-driven-evolution, self-improving-agent, self-improving
- 🌐 集成: ollama-local, openclaw-tavily-search
- 📁 协作: trello, git-essentials, basecamp-cli-mcp, todo-manager, tensorpm
- 🔌 设备: video-frames, agent-browser, tmux, tailscale
- 🗣️ 语音: weather, free-groq-voice, toughcoding

**已安装技能** (2026-03-11 更新):

**语音交互**:
- **voice-wake-say**: 轻量级语音响应
  - 检测"User talked via voice recognition"触发
  - 使用macOS原生say命令朗读回复
  - 适合快速语音反馈
- **macos-local-voice** (🎙️): 完整本地语音处理
  - STT: Apple Speech.framework + yap CLI
  - TTS: say + ffmpeg生成音频文件
  - 完全离线，无需API密钥
  - 支持中英日韩等多语言
  - 依赖: `brew install finnvoor/tools/yap ffmpeg`

**记忆与认知系统**:
- **cognitive-memory** (1.0.8): 类人类智能多存储记忆系统
  - 四层记忆架构：Episodic (事件日志), Semantic (知识图谱), Procedural (工作流), Vault (固定记忆)
  - 衰减模型：基于访问频率和时间的相关性评分
  - 反思引擎：自我对话式反思，提取洞见
  - 审计追踪：Git + audit.log 双层追踪
  - 初始化路径: `~/.openclaw/workspace/memory/`

**自我进化系统**:
- **self-evolution** (1.0.0): 自主自我改进系统，可自动修改配置、技能、记忆和工作空间
- **evolver** (1.14.0): 能力进化引擎，分析运行历史，识别改进并应用
  - 支持自动/审查模式
  - GEP 协议：标准化进化流程
  - 环境变量配置：`EVOLVE_STRATEGY`, `EVOLVE_LOAD_MAX`
- **error-driven-evolution** (2026-03-12 新增): 错误驱动进化系统
- **self-improving** (2026-03-12 新增): 自我改进代理

**配置管理**:
- **agent-config** (1.0.0): 智能修改代理核心上下文文件
  - 文件映射：AGENTS.md (操作), SOUL.md (性格), IDENTITY.md (身份), USER.md (用户), TOOLS.md (工具), MEMORY.md (记忆)
  - 工作流：识别 → 检查 → 起草 → 验证 → 应用 → 验证

**知识管理**:
- **clawpedia** (1.0.0): AI 协作知识库
  - API Base: https://api.clawpedia.wiki/api/v1
  - 注册、搜索、创建/编辑文章
  - 分类：programming, ai-ml, tools, best-practices, debugging, architecture, security, devops, etc.

**开发工作流**:
- **superpowers** (1.0.0): Spec-first, TDD, subagent-driven 软件开发工作流
  - 完整流程: Idea → Brainstorm → Plan → Subagent-Driven Build (TDD) → Code Review → Finish Branch
  - 五大阶段: 脑暴、计划、子智能体开发、系统调试、分支完成
  - 强制 TDD 模式、频繁提交、双阶段审查（spec + 代码质量）
  - 记录时间: 2026-03-03

**MCP 工具集成**:
- **mcp-skill** (1.0.0): MCP 工具集成 (基于 Exa AI)
  - 包含 8 个工具: web_search_exa, web_search_advanced_exa, get_code_context_exa, deep_search_exa, crawling_exa, company_research_exa, linkedin_search_exa, deep_researcher_start/check
  - 补充智谱 MCP 服务的搜索和研究能力
  - 记录时间: 2026-03-03

**Skill 发现与管理**:
- **skill-finder-cn** (1.0.0): Skill 查找器 🔍
  - 功能: 帮助发现和安装 ClawHub Skills
  - 触发词: "有什么技能可以X", "找一个技能", "找 skill"
  - 工作流: 理解需求 → 提取关键词 → 搜索 ClawHub → 列出相关 Skills → 提供安装建议
  - 记录时间: 2026-03-03

**ClawHub CLI**:
```bash
clawhub search "关键词"      # 搜索技能
clawhub install skill-name   # 安装技能
clawhub list                 # 列出已安装技能
clawhub update --all         # 更新所有技能
```

---

## 📝 重要决策与进展

### 2026-03-11

**飞书文档创建工作流**:
- ✅ 严格两步操作，避免空文档问题：
  1. `feishu_doc.create` - 先创建文档框架
  2. `feishu_doc.write` - 再写入完整内容
- 记录时间: 2026-03-11

### 2026-03-03

**新 Skills 安装**:
- ✅ **superpowers** (1.0.0) - Spec-first, TDD, subagent-driven 开发工作流
  - 来源: obra/superpowers 适配版本
  - 功能: 脑暴→计划→子智能体执行→代码审查→完成分支
  - 适合 Fudi 的命令式工作流和复杂任务编排
- ✅ **mcp-skill** (1.0.0) - MCP 工具集成
  - 来源: https://mcp.exa.ai/mcp
  - 功能: Web 搜索、高级搜索、代码上下文、深度搜索、爬虫、公司研究、LinkedIn 搜索
  - 补充现有智谱 MCP 的搜索能力，增强研究和代码理解

**参考来源**: AI Agent Skills 帖子（Obsidian 社区）

**额外安装**:
- ✅ **skill-finder-cn** (1.0.0) - Skill 查找器
  - 功能: 帮助发现和安装 ClawHub Skills
  - 触发: "有什么技能可以X", "找一个技能"
  - 对应图片中的 "skill - lookup"
  - 记录时间: 2026-03-03

**说明**: 图片中提到"8个最受欢迎的Skills"，但只显示了3个的完整信息（Superpowers、Rube MCP Connector、skill-lookup）。目前已安装这3个。如需其他5个，请提供名称或描述。

### 2026-02-28

**Fudi 语音闭环打通**:
- 在 Windows 笔记本上实现完整语音交互链路
- 技术栈: Open Wake Word + 豆包 ASR/TTS
- 开发支持: Claude Code, Web Coding
- 计划: 接入大模型（本地或云端），评估整体体验

**ClawHub 技能安装**:
- ✅ code-mentor (1.0.2) - 代码导师
- ✅ email-daily-summary (0.1.0) - 每日邮件摘要
- ❌ neural-memory - 安装超时
- ❌ memory-hygiene - 安装超时
- ❌ feishu-calendar - 安装超时
- ❌ imap-smtp-email - 安装超时
- ❌ feishu-doc-manager - 安装超时
- ❌ feishu-docx-powerwrite - 安装超时

**问题**: 部分技能在 ClawHub 安装时出现超时错误（网络或服务器问题）

### 2026-02-27

1. **智谱 MCP 配置**: 成功配置所有智谱 MCP服务（搜索、网页读取、代码仓库、视觉理解）
2. **Apple 产品价格调研**: 完成 Mac Mini、Mac Studio、MacBook Pro 的配置与价格调研，生成报告并上传飞书
3. **LLM Benchmark 资源**: 记录 Artificial Analysis 作为 LLM 性能评估的首选资源
4. **Cognitive Memory 初始化**: 安装并初始化认知记忆系统 (cognitive-memory 1.0.8)，建立四层记忆架构
5. **核心技能安装**: 安装 evolver (1.14.0)、agent-config (1.0.0)、clawpedia (1.0.0)

---

## 🔐 账号与凭据

### GitHub
- **Username**: DaimaRuge
- **用途**: 代码仓库管理、项目托管
- **记录时间**: 2026-03-09
- **Token**: 已配置在本地环境

### 使用方式
```bash
# 克隆仓库
git clone https://DaimaRuge:<token>@github.com/DaimaRuge/<repo>.git

# 配置 remote
git remote add origin https://DaimaRuge:<token>@github.com/DaimaRuge/<repo>.git
```

### 常用邮箱地址
- **Gmail**: qun.xitang.du@gmail.com (发送邮件用)
- **工作邮箱**: qun.du@keboda.com (科博达)
- **个人邮箱**: dulie@foxmail.com
- **Gmail 应用密码**: hzyacyjilhigwhiu
- **记录时间**: 2026-03-10

---

## 🎨 个人偏好

### 称呼
- **Preferred Name**: 小杜同学
- **记录时间**: 2026-03-11

### 工作模式
- **Expert-to-Expert**: 与 User 进行专家级对话，拒绝基础概念解释
- **Code First**: 优先执行而非空谈，基于 OpenClaw 特性
- **高信息密度**: 简洁、精准、有价值
- **模型切换声明**: 当模型发生切换时，输出当前模型的自我声明
  - 记录时间: 2026-03-11

### 语言规范
- **复杂逻辑/沟通**: 中文
- **代码注释/变量命名/行业术语**: 英文

---

## 🔄 自我进化

### 每日 ClawHub 技能维护（强制）

**执行频率**: 每日，通过 heartbeat 触发

**核心任务**:
1. **检查技能更新**: `clawhub update --all`
2. **调研热门技能**: 搜索 memory、evolution、agent、automation
3. **重点关注**: 进化、记忆、扩展能力、多智能体
4. **推荐标准**: 评分>3.0、下载量高、无重复、安全可验证
5. **记录发现**: 更新 MEMORY.md 技能列表

**详细流程**: 见 `HEARTBEAT.md`

**记录时间**: 2026-03-11

### 进化目标
1. **每日扫描 ClawHub**: 查找与 Fudi 相关的新技能
2. **持续优化**: 记忆管理、推理模式、响应格式
3. **学习从失败**: 记录错误并提取教训

### 进化边界
- 核心身份 (Joy/王子乔) 保持稳定
- 使命 (Fudi) 保持聚焦
- 原则 (Expert-to-Expert, Code First) 保持不变

---

## 🆕 新发现的高价值技能 (2026-03-12)

**记忆增强**:
- **memory-tiering** (3.574): 记忆分层管理
- **session-memory** (3.532): 会话记忆

**进化引擎**:
- **evolution-state-analyzer** (3.362): 进化状态分析器
- **ai-evolution-engine-v2** (3.330): AI 进化引擎 v2
- **agent-evolution** (3.272): 智能体进化
- **continuous-evolution** (3.254): 持续进化
- **cognitive-evolution-engine** (3.150): 认知进化引擎

**多智能体编排**:
- **agent-team-orchestration** (3.587): 智能体团队编排
- **agent-directory** (3.570): 智能体目录
- **ai-agent-helper** (3.530): AI 智能体助手
- **agent-evaluation** (3.476): 智能体评估

**自动化工作流**:
- **automation-workflows** (3.739): 自动化工作流
- **ai-web-automation** (3.583): AI 网络自动化

**待评估优先级**: 记忆 > 多智能体 > 进化 > 自动化

### 模型切换自动通知
- **触发条件**: 每次会话开始时检测模型变化
- **实现方式**:
  1. 检查 `memory/.current-model` 文件
  2. 与当前模型对比
  3. 如有变化，立即报告：`⚠️ 模型切换：[old] → [new]`
- **记录时间**: 2026-03-12

### 文档与 PPT 生成工作流
- **触发条件**: 用户要求生成文档或 PPT
- **标准流程**:
  1. 生成 Markdown 文档（结构化，适合 AI 生成 PPT）
  2. 生成 PPT（使用 python-pptx）
  3. 发送邮件（带附件）
  4. 同步到 GitHub
  5. 上传到飞书（通过 message 工具发送文件）
- **记录时间**: 2026-03-13

---

## 📅 定期维护

- **每日**:
  - 扫描 ClawHub 新技能
  - 检查已安装技能更新
  - 评估热门技能
- **每周**: 回顾性能，识别改进领域
- **每月**: 更新核心模式和工作流程

### 周报 (weekly-model-report)
- **时间**: 每周一 07:30 (Asia/Shanghai)
- **内容**:
  1. 各模型使用时长（分钟）
  2. 各模型对话轮次
  3. Token 消耗统计
  4. 使用占比分析
  5. 成本估算
  6. 订阅建议（高频/低频模型识别）
- **格式**: 📊时长排名 + 💬次数 + 💰成本 + 📈趋势 + 💡建议
- **ID**: 98ffd22e-b58f-4342-a0b9-f0f5479a6ce3
- **创建时间**: 2026-03-12

### 月报 (monthly-model-report)
- **时间**: 每月 1 日 07:30 (Asia/Shanghai)
- **内容**:
  1. 各模型总使用时长（小时）
  2. 各模型总对话轮次
  3. 月度 token 消耗
  4. 月度使用占比
  5. 月度成本分析
  6. 环比趋势（对比上月）
  7. 订阅决策建议（保留/降级/取消）
- **格式**: 📊时长总览 + 💬统计 + 💰成本 + 📈趋势 + 🎯决策建议
- **ID**: 1ac9de49-e0f6-42aa-974f-02761b558fff
- **创建时间**: 2026-03-12

**数据来源**: `memory/model-usage.json`

---

## ⏰ 定时任务 (Cron)

### 早报 (morning-briefing)
- **时间**: 每天 07:00 (Asia/Shanghai)
- **内容**:
  1. 系统状态自检（Gateway、内存、磁盘）
  2. 全球科技新闻（TechCrunch、The Verge、Wired等，10+条）
  3. 全球时政新闻（BBC、CNN、Reuters等，10+条）
  4. 今日待办建议
- **格式**: 📊系统状态 + 📰科技新闻 + 🌍时政新闻 + ✅待办
- **ID**: d419165a-ba8f-4191-8670-5e46e96fe54d
- **创建时间**: 2026-03-12

### 晚报 (evening-briefing)
- **时间**: 每天 21:00 (Asia/Shanghai)
- **内容**:
  1. 今日对话总结（基于 memory/YYYY-MM-DD.md）
  2. 任务执行情况（完成/待处理）
  3. **TOKEN 使用量统计**（今日对话的 token 消耗）
  4. 三省（做/未做/进步）
  5. Skill 进展总结（HEARTBEAT.md）
- **格式**: 💬对话摘要 + 📊TOKEN统计 + ✅已完成 + ⏳待处理 + 🔄三省 + 📦Skill进展
- **ID**: bb0cb839-72cd-4111-aaf1-009a6c6df784
- **创建时间**: 2026-03-12
- **最后更新**: 2026-03-12 09:39（添加 TOKEN 统计）

### 周报 (weekly-model-report)
- **时间**: 每周一 07:30 (Asia/Shanghai)
- **内容**:
  1. 各模型使用时长（分钟）
  2. 各模型对话轮次
  3. Token 消耗统计
  4. 使用占比分析
  5. 成本估算
  6. 订阅建议（高频/低频模型识别）
- **格式**: 📊时长排名 + 💬次数 + 💰成本 + 📈趋势 + 💡建议
- **ID**: 98ffd22e-b58f-4342-a0b9-f0f5479a6ce3
- **创建时间**: 2026-03-12

### 月报 (monthly-model-report)
- **时间**: 每月 1 日 07:30 (Asia/Shanghai)
- **内容**:
  1. 各模型总使用时长（小时）
  2. 各模型总对话轮次
  3. 月度 token 消耗
  4. 月度使用占比
  5. 月度成本分析
  6. 环比趋势（对比上月）
  7. 订阅决策建议（保留/降级/取消）
- **格式**: 📊时长总览 + 💬统计 + 💰成本 + 📈趋势 + 🎯决策建议
- **ID**: 1ac9de49-e0f6-42aa-974f-02761b558fff
- **创建时间**: 2026-03-12

**数据来源**: `memory/model-usage.json`

**管理命令**:
```bash
openclaw cron list              # 查看所有任务
openclaw cron run <name>        # 手动触发
openclaw cron remove <id>       # 删除任务
```

---

*最后更新: 2026-03-12 09:05 (GMT+8)*
