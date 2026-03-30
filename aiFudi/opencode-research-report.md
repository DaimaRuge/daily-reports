# OpenCode 源码深度研究报告

> **研究版本**: v1.2.24  
> **仓库地址**: https://github.com/anomalyco/opencode  
> **本地路径**: /home/admin/.openclaw/workspace/opencode-repo  
> **研究日期**: 2026-03-11  
> **分析模式**: 深度模式

---

## 📋 研究前置信息

| 项目 | 信息 |
|------|------|
| 项目名称 | OpenCode |
| 版本 | 1.2.24 |
| 核心语言 | TypeScript |
| 运行时 | Bun |
| 许可证 | MIT |
| 文件数 | 4402+ |

---

# 第1章：项目全景概览

## 1.1 核心目标

**OpenCode 是一个 100% 开源的 AI Coding Agent**，定位为：
- 终端中的 AI 编程助手
- 支持多 LLM 提供商（Provider-agnostic）
- 客户端/服务器架构（Client/Server Architecture）
- 支持 ACP (Agent Client Protocol)

## 1.2 与 Claude Code 的对比

| 维度 | OpenCode | Claude Code |
|------|----------|-------------|
| **开源** | ✅ 100% 开源 | ❌ 核心闭源 |
| **提供商** | ✅ 多提供商支持 | ❌ 仅 Anthropic |
| **架构** | ✅ Client/Server | 🔍 推断为单体 |
| **LSP** | ✅ 原生支持 | 🔍 可能支持 |
| **协议** | ✅ ACP 协议 | ❌ 私有协议 |
| **TUI** | ✅ 专注终端体验 | ✅ 终端优先 |

## 1.3 一级模块组成

```
OpenCode 系统架构：

┌─────────────────────────────────────────────────────────────┐
│                     OpenCode Core                            │
│                  (packages/opencode)                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   CLI    │  │  Agent   │  │  Tool    │  │ Session  │   │
│  │  Entry   │  │  Core    │  │ System   │  │ Manager  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Provider │  │   MCP    │  │   LSP    │  │ Permission│  │
│  │ Manager  │  │ Client   │  │ Server   │  │  System   │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Storage  │  │  Plugin  │  │  Skill   │  │   ACP    │   │
│  │ System   │  │ System   │  │ System   │  │ Protocol │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                           ↕
┌─────────────────────────────────────────────────────────────┐
│                    Supporting Packages                       │
├─────────────────────────────────────────────────────────────┤
│  SDK  │  Desktop (Electron)  │  Web  │  Console  │  Docs   │
└─────────────────────────────────────────────────────────────┘
```

## 1.4 技术栈

| 层级 | 技术 |
|------|------|
| **语言** | TypeScript |
| **运行时** | Bun (Node.js alternative) |
| **包管理** | Bun |
| **数据库** | SQLite (Drizzle ORM) |
| **验证** | Zod |
| **AI SDK** | Vercel AI SDK |
| **协议** | ACP (Agent Client Protocol) |
| **LSP** | vscode-languageserver-types |
| **配置** | JSON + YAML |

---

# 第2章：架构分层分析

## 2.1 整体架构图（8层）

```
┌─────────────────────────────────────────────────────────────┐
│                    8层架构模型                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Layer 8: Observability 层                                  │
│  ├── 日志系统 (Log)                                         │
│  ├── 事件追踪 (Bus)                                         │
│  └── 调试模式                                               │
│                                                             │
│  Layer 7: Safety / Guardrail 层                             │
│  ├── Permission 系统 (PermissionNext)                       │
│  ├── 用户确认 (ask)                                         │
│  └── 规则配置                                               │
│                                                             │
│  Layer 6: Execution 层                                      │
│  ├── Bash 工具 (bash.ts)                                    │
│  ├── 文件操作 (edit.ts, write.ts, read.ts)                  │
│  └── 补丁应用 (apply_patch.ts)                              │
│                                                             │
│  Layer 5: Context / Memory 层                               │
│  ├── 会话管理 (session/)                                    │
│  ├── 消息系统 (message-v2)                                  │
│  ├── Todo 管理 (todo)                                       │
│  └── 存储 (storage/)                                        │
│                                                             │
│  Layer 4: LLM Interaction 层                                │
│  ├── Provider 抽象 (provider/)                              │
│  ├── System Prompt (system.ts)                              │
│  └── 多提供商支持                                           │
│                                                             │
│  Layer 3: Tool Use 层                                       │
│  ├── 工具注册 (registry.ts)                                 │
│  ├── 工具定义 (tool.ts)                                     │
│  └── 输出截断 (truncation.ts)                               │
│                                                             │
│  Layer 2: Agent Orchestration 层                            │
│  ├── Agent 定义 (agent.ts)                                  │
│  ├── 多 Agent 支持 (build/plan/general/explore)            │
│  └── ACP 协议 (acp/agent.ts)                                │
│                                                             │
│  Layer 1: 表现层 / 交互层                                    │
│  ├── CLI 入口 (cli/)                                        │
│  ├── TUI 渲染                                               │
│  └── ACP Server (acp/server.ts)                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 2.2 逐层分析

### Layer 1: 表现层 / 交互层

**职责**：
- CLI 入口和命令解析
- TUI (Terminal UI) 渲染
- ACP 协议服务器

**核心文件**：
```
src/
├── cli/          # CLI 入口
├── acp/server.ts # ACP 服务器
└── index.ts      # 主入口
```

**ACP 协议支持**：
```typescript
// 启动 ACP 服务器
opencode acp --cwd /path/to/project

// Zed 集成
{
  "agent_servers": {
    "OpenCode": {
      "command": "opencode",
      "args": ["acp"]
    }
  }
}
```

**设计优点**：
- ✅ Client/Server 架构，支持远程控制
- ✅ 标准化协议 (ACP)，可与多个客户端集成
- ✅ TUI 专注终端体验

---

### Layer 2: Agent Orchestration 层

**职责**：
- Agent 定义和配置
- 多 Agent 支持
- 权限配置
- 模型选择

**核心文件**：
```
src/agent/
├── agent.ts      # Agent 定义和 Info Schema
└── prompt/       # Agent 提示词
    ├── compaction.txt
    ├── explore.txt
    ├── summary.txt
    └── title.txt
```

**Agent 类型** (✅ 确认)：

| Agent | 模式 | 权限 | 用途 |
|-------|------|------|------|
| **build** | primary | 完整权限 | 默认开发 Agent |
| **plan** | primary | 只读 + 计划文件编辑 | 代码探索和规划 |
| **general** | subagent | 子任务权限 | 复杂搜索和多步任务 |
| **explore** | subagent | 只读权限 | 代码探索 |

**Agent Info Schema** (✅ 确认)：
```typescript
export const Info = z.object({
  name: z.string(),
  description: z.string().optional(),
  mode: z.enum(["subagent", "primary", "all"]),
  native: z.boolean().optional(),
  hidden: z.boolean().optional(),
  topP: z.number().optional(),
  temperature: z.number().optional(),
  color: z.string().optional(),
  permission: PermissionNext.Ruleset,
  model: z.object({
    modelID: z.string(),
    providerID: z.string(),
  }).optional(),
  variant: z.string().optional(),
  prompt: z.string().optional(),
  options: z.record(z.string(), z.any()),
  steps: z.number().int().positive().optional(),
})
```

**权限系统设计** (✅ 确认)：
```typescript
// build Agent 默认权限
const permission = PermissionNext.merge(
  defaults,
  PermissionNext.fromConfig({
    question: "allow",
    plan_enter: "allow",
  }),
  user,
)

// plan Agent 限制编辑
const permission = PermissionNext.merge(
  defaults,
  PermissionNext.fromConfig({
    question: "allow",
    plan_exit: "allow",
    edit: {
      "*": "deny",  // 禁止所有编辑
      ".opencode/plans/*.md": "allow",  // 只允许计划文件
    },
  }),
  user,
)
```

**设计亮点**：
- ✅ 权限系统基于规则合并 (merge)
- ✅ 支持路径级别的权限控制
- ✅ 多 Agent 设计，不同任务用不同 Agent
- ✅ 原生 Agent + 用户自定义 Agent

---

### Layer 3: Tool Use 层

**职责**：
- 工具定义和注册
- 参数验证
- 执行和输出处理
- 输出截断

**核心文件**：
```
src/tool/
├── tool.ts           # 工具接口定义
├── registry.ts       # 工具注册表
├── truncation.ts     # 输出截断
├── bash.ts           # Shell 命令
├── edit.ts           # 文件编辑
├── read.ts           # 文件读取
├── write.ts          # 文件写入
├── grep.ts           # 搜索
├── glob.ts           # 文件匹配
├── webfetch.ts       # 网页抓取
├── websearch.ts      # 网页搜索
├── lsp.ts            # LSP 支持
├── task.ts           # 任务工具
├── skill.ts          # 技能工具
└── ...
```

**工具接口定义** (✅ 确认)：
```typescript
export interface Info<Parameters extends z.ZodType = z.ZodType, M extends Metadata = Metadata> {
  id: string
  init: (ctx?: InitContext) => Promise<{
    description: string
    parameters: Parameters
    execute(
      args: z.infer<Parameters>,
      ctx: Context,
    ): Promise<{
      title: string
      metadata: M
      output: string
      attachments?: Omit<MessageV2.FilePart, "id" | "sessionID" | "messageID">[]
    }>
    formatValidationError?(error: z.ZodError): string
  }>
}
```

**工具上下文** (✅ 确认)：
```typescript
export type Context<M extends Metadata = Metadata> = {
  sessionID: string
  messageID: string
  agent: string
  abort: AbortSignal
  callID?: string
  extra?: { [key: string]: any }
  messages: MessageV2.WithParts[]
  metadata(input: { title?: string; metadata?: M }): void
  ask(input: Omit<PermissionNext.Request, "id" | "sessionID" | "tool">): Promise<void>
}
```

**工具列表** (✅ 确认)：

| 工具 | 文件 | 职责 |
|------|------|------|
| bash | bash.ts | Shell 命令执行 |
| edit | edit.ts | 文件编辑 |
| multiedit | multiedit.ts | 批量编辑 |
| read | read.ts | 文件读取 |
| write | write.ts | 文件写入 |
| grep | grep.ts | 文本搜索 |
| glob | glob.ts | 文件匹配 |
| ls | ls.ts | 目录列表 |
| codesearch | codesearch.ts | 代码搜索 |
| webfetch | webfetch.ts | 网页抓取 |
| websearch | websearch.ts | 网页搜索 |
| lsp | lsp.ts | LSP 支持 |
| task | task.ts | 子任务 |
| skill | skill.ts | 技能调用 |
| todo | todo.ts | Todo 管理 |
| question | question.ts | 用户问答 |
| plan | plan.ts | 计划管理 |
| apply_patch | apply_patch.ts | 补丁应用 |
| batch | batch.ts | 批量操作 |

**输出截断机制** (✅ 确认)：
```typescript
// 自动截断长输出
const truncated = await Truncate.output(result.output, {}, initCtx?.agent)
return {
  ...result,
  output: truncated.content,
  metadata: {
    ...result.metadata,
    truncated: truncated.truncated,
    ...(truncated.truncated && { outputPath: truncated.outputPath }),
  },
}
```

**设计亮点**：
- ✅ Zod Schema 参数验证
- ✅ 统一的工具接口
- ✅ 自动输出截断
- ✅ 支持附件返回
- ✅ AbortSignal 支持

---

### Layer 4: LLM Interaction 层

**职责**：
- Provider 抽象
- 多提供商支持
- System Prompt 构造
- 模型请求和响应处理

**支持的提供商** (✅ 确认)：

| 提供商 | 包名 |
|--------|------|
| Anthropic | @ai-sdk/anthropic |
| OpenAI | @ai-sdk/openai |
| Google | @ai-sdk/google |
| Azure | @ai-sdk/azure |
| AWS Bedrock | @ai-sdk/amazon-bedrock |
| Groq | @ai-sdk/groq |
| Mistral | @ai-sdk/mistral |
| Cohere | @ai-sdk/cohere |
| xAI | @ai-sdk/xai |
| Cerebras | @ai-sdk/cerebras |
| DeepInfra | @ai-sdk/deepinfra |
| Perplexity | @ai-sdk/perplexity |
| Together AI | @ai-sdk/togetherai |
| 等等... | |

**Provider 抽象**：
```typescript
// 推断的 Provider 接口
interface Provider {
  id: string
  models: Record<string, ModelInfo>
  client: AIProvider
}

interface ModelInfo {
  limit: {
    context: number
    output?: number
  }
  cost: {
    input: number
    output: number
  }
}
```

---

### Layer 5: Context / Memory 层

**职责**：
- 会话管理
- 消息历史
- Todo 管理
- 持久化存储

**核心文件**：
```
src/session/
├── message-v2.ts   # 消息格式
├── system.ts       # System Prompt
├── todo.ts         # Todo 管理
└── ...

src/storage/
└── ...             # 存储系统
```

**消息格式** (✅ 推断)：
```typescript
interface MessageV2 {
  id: string
  sessionID: string
  role: "user" | "assistant" | "system"
  parts: Part[]
  tokens: {
    input: number
    output: number
    cache?: {
      read: number
      write: number
    }
  }
  cost: number
  providerID: string
  modelID: string
}

type Part = 
  | TextPart
  | FilePart
  | ToolPart
  | ImagePart
```

---

### Layer 6: Execution 层

**职责**：
- Bash 命令执行
- 文件读写
- 代码编辑
- 补丁应用

**安全机制**：
- Permission 系统拦截
- 用户确认
- 路径限制

---

### Layer 7: Safety / Guardrail 层

**职责**：
- 权限控制
- 危险操作拦截
- 用户确认
- 规则配置

**权限规则** (✅ 确认)：
```typescript
// 默认权限规则
const defaults = PermissionNext.fromConfig({
  "*": "allow",
  doom_loop: "ask",          // 无限循环询问
  external_directory: {
    "*": "ask",
    [whitelistedDir]: "allow",
  },
  question: "deny",
  read: {
    "*": "allow",
    "*.env": "ask",          // .env 文件询问
    "*.env.*": "ask",
    "*.env.example": "allow",
  },
})
```

**权限类型**：
- `allow` - 允许
- `deny` - 拒绝
- `ask` - 询问用户

---

### Layer 8: Observability 层

**职责**：
- 日志记录
- 事件追踪
- 调试支持

**核心文件**：
```
src/util/log.ts    # 日志系统
src/bus/           # 事件总线
```

---

# 第3章：核心 Agent 运行流程

## 3.1 完整调用链追踪

**用户输入示例**："帮我重构这个函数"

```
Step 1: 用户输入
  → CLI 入口
  → 解析命令

Step 2: Session 创建/加载
  → SessionManager.create() / load()
  → 初始化上下文（工作目录、配置）

Step 3: Agent 选择
  → 默认使用 "build" Agent
  → 用户可切换（Tab 键）

Step 4: Prompt 构造
  → System Prompt 生成
  → 上下文注入（文件、历史消息）
  → 工具描述注入

Step 5: LLM 请求
  → Provider 选择（用户配置）
  → 流式请求
  → 响应解析

Step 6: 工具调用
  → 检测工具调用意图
  → Permission 检查
  → 工具执行
  → 结果回传

Step 7: 循环判断
  → 是否需要更多操作？
  → 是 → 返回 Step 5
  → 否 → 结束

Step 8: 输出
  → 格式化响应
  → 渲染到 TUI
```

## 3.2 关键数据结构

**Session**：
```typescript
interface Session {
  id: string
  directory: string
  agent: Agent.Info
  messages: MessageV2[]
  todos: Todo[]
  createdAt: number
  updatedAt: number
}
```

**Message**：
```typescript
interface MessageV2 {
  id: string
  sessionID: string
  role: "user" | "assistant" | "system"
  parts: Part[]
  tokens: TokenInfo
  cost: number
}
```

**Tool Call**：
```typescript
interface ToolPart {
  type: "tool"
  tool: string
  args: Record<string, any>
  result?: string
  error?: string
}
```

## 3.3 状态变化过程

```
Session 状态机：

[Idle] → [Planning] → [Executing] → [Observing] → [Done]
           ↑                              │
           └──────────────────────────────┘
                    (循环)
```

---

# 第4章：Agent 设计思想拆解

## 4.1 设计模式识别

| 模式 | 是否使用 | 代码位置 | 实现方式 |
|------|---------|---------|---------|
| **ReAct** | ✅ | agent.ts, tool/ | 工具调用循环 |
| **Plan-and-Execute** | ✅ | plan Agent | 只读探索 + 规划 |
| **Tool-use** | ✅ | tool/*.ts | 标准工具接口 |
| **Human-in-the-loop** | ✅ | PermissionNext | 权限询问 |
| **Multi-Agent** | ✅ | agent.ts | build/plan/general/explore |
| **Subagent** | ✅ | general Agent | 子任务执行 |
| **Progressive Disclosure** | ✅ | truncation.ts | 输出截断 |
| **Provider Abstraction** | ✅ | provider/ | 多 LLM 支持 |
| **Protocol Compliance** | ✅ | acp/ | ACP 协议 |

## 4.2 与简单 "LLM + 工具脚本" 的差异

| 维度 | 简单脚本 | OpenCode |
|------|---------|----------|
| **架构** | 单文件 | 分层架构 |
| **工具管理** | 硬编码 | 注册表 + Schema |
| **权限** | 无 | 完整权限系统 |
| **多 Agent** | 不支持 | 原生支持 |
| **协议** | 无 | ACP 协议 |
| **状态管理** | 无 | Session + Storage |
| **LSP** | 无 | 原生支持 |
| **提供商** | 单一 | 多提供商 |

---

# 第5章：Prompt / Context Engineering 分析

## 5.1 提示词结构

**System Prompt 组成** (🔍 推断)：
```
System Prompt
├── 角色定义
├── Agent 特定指令
├── 工具描述
├── 输出格式要求
└── 安全约束
```

**Agent 提示词文件** (✅ 确认)：
```
src/agent/prompt/
├── compaction.txt   # 上下文压缩
├── explore.txt      # 探索模式
├── summary.txt      # 摘要生成
└── title.txt        # 标题生成
```

## 5.2 上下文管理

**消息历史**：
- MessageV2 格式
- Token 计数
- Cost 追踪

**输出截断**：
- 自动截断长输出
- 保存到临时文件
- 元数据记录

---

# 第6章：Tool Use 机制深挖

## 6.1 工具分类

| 类别 | 工具 | 数量 |
|------|------|------|
| **文件操作** | read, write, edit, multiedit, apply_patch | 5 |
| **Shell** | bash | 1 |
| **搜索** | grep, glob, ls, codesearch | 4 |
| **网络** | webfetch, websearch | 2 |
| **LSP** | lsp | 1 |
| **任务** | task, batch | 2 |
| **技能** | skill | 1 |
| **管理** | todo, question, plan | 3 |

**总计**: 19+ 工具

## 6.2 工具抽象

**接口设计** (✅ 确认)：
```typescript
interface Tool.Info {
  id: string
  init(ctx?): Promise<{
    description: string
    parameters: ZodSchema
    execute(args, ctx): Promise<{
      title: string
      metadata: object
      output: string
      attachments?: FilePart[]
    }>
  }>
}
```

## 6.3 工具定义示例

```typescript
Tool.define("bash", {
  description: "Execute a bash command",
  parameters: z.object({
    command: z.string(),
    timeout: z.number().optional(),
  }),
  execute: async (args, ctx) => {
    // 执行命令
    const result = await executeBash(args.command)
    return {
      title: `Bash: ${args.command}`,
      metadata: { exitCode: result.exitCode },
      output: result.stdout,
    }
  },
})
```

## 6.4 工具执行流程

```
Tool Selection → Permission Check → Validation → Execution → Truncation → Return
      ↓                ↓                ↓             ↓             ↓
   Agent 决定      PermissionNext    Zod.parse()   execute()   Truncate.output()
```

---

# 第7章：状态管理与记忆机制

## 7.1 Session 管理

**Session 结构** (✅ 推断)：
```typescript
interface Session {
  id: string
  directory: string
  agent: Agent.Info
  messages: MessageV2[]
  todos: Todo[]
}
```

## 7.2 持久化

**存储层**：
- SQLite (Drizzle ORM)
- 本地文件系统

## 7.3 上下文窗口管理

**Token 追踪**：
```typescript
interface TokenInfo {
  input: number
  output: number
  cache?: {
    read: number
    write: number
  }
}
```

**Context Limit 查询**：
```typescript
async function getContextLimit(providerID, modelID) {
  const model = providers[providerID]?.models[modelID]
  return model?.limit.context ?? null
}
```

---

# 第8章：软件工程实现质量评估

## 8.1 工程质量评价

| 维度 | 评分 | 评价 |
|------|------|------|
| 模块边界清晰度 | ⭐⭐⭐⭐⭐ | 8层架构，职责清晰 |
| 抽象合理性 | ⭐⭐⭐⭐⭐ | 工具、Agent、Provider 都是优秀抽象 |
| 耦合度 | ⭐⭐⭐⭐ | 低耦合，依赖注入 |
| 可测试性 | ⭐⭐⭐⭐ | 测试框架完善 |
| 可扩展性 | ⭐⭐⭐⭐⭐ | 插件、技能、MCP 支持 |

## 8.2 最优雅的 3 个设计点

1. **Tool.Info 接口设计**
   - Zod Schema 验证
   - 统一上下文
   - 自动输出截断

2. **Permission 系统**
   - 规则合并 (merge)
   - 路径级别控制
   - ask/allow/deny 三态

3. **多 Agent 设计**
   - build/plan/general/explore
   - 不同权限配置
   - 原生 + 自定义

## 8.3 最可能有技术债的 3 个地方

1. **ACP 流式响应** - 文档说明尚未实现
2. **Session Persistence** - session/load 功能有限
3. **Terminal Support** - 文档标记为 stub

## 8.4 如果重构

优先改进：
1. **ACP 流式响应** - 提升用户体验
2. **Session 持久化** - 支持完整历史恢复
3. **错误处理统一** - 更一致的错误类型

---

# 第9章：面向复现的知识提炼

## 9.1 核心能力清单

| 能力 | 必须保留 | 可简化 | 难度 |
|------|---------|--------|------|
| 工具系统 | ✅ | | 中 |
| Agent 定义 | ✅ | | 低 |
| 权限系统 | ✅ | 可简化 | 中 |
| Session 管理 | ✅ | | 中 |
| 多 Provider | 🔵 | 可先支持一个 | 低 |
| LSP | 🔵 | 可延后 | 高 |
| ACP 协议 | 🔵 | 可延后 | 中 |
| TUI | 🔵 | 可用简单 REPL | 中 |

## 9.2 MVP 架构

```
┌─────────────────────────────────────────────────────────────┐
│                      MVP Agent Demo                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   REPL   │  │  Agent   │  │  Tool    │  │ Session  │   │
│  │  Entry   │  │  Core    │  │ Registry │  │ Manager  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                 │
│  │ Provider │  │Permission│  │ Storage  │                 │
│  │ (Single) │  │ (Basic)  │  │ (SQLite) │                 │
│  └──────────┘  └──────────┘  └──────────┘                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 9.3 模块清单

| 模块 | 职责 | 核心接口 |
|------|------|---------|
| **REPL** | 用户交互 | `start()`, `handleInput()` |
| **Agent** | Agent 定义 | `Info`, `create()` |
| **Tool** | 工具管理 | `Tool.define()`, `Registry` |
| **Session** | 会话管理 | `create()`, `load()`, `addMessage()` |
| **Provider** | LLM 调用 | `chat()`, `stream()` |
| **Permission** | 权限控制 | `check()`, `ask()` |
| **Storage** | 持久化 | `save()`, `load()` |

## 9.4 开发路线图

| 阶段 | 目标 | 验收标准 |
|------|------|---------|
| **P0** | 最小闭环 | 能完成简单文件读写任务 |
| **P1** | 工具扩展 | 支持更多工具（grep, bash） |
| **P2** | 权限系统 | 支持用户确认 |
| **P3** | 多 Agent | 支持 build/plan 切换 |
| **P4** | 持久化 | Session 保存和恢复 |
| **P5** | 多 Provider | 支持多个 LLM 提供商 |

## 9.5 推荐技术栈

| 层级 | 技术 |
|------|------|
| **语言** | TypeScript |
| **运行时** | Bun 或 Node.js |
| **验证** | Zod |
| **数据库** | SQLite + Drizzle ORM |
| **AI SDK** | Vercel AI SDK |
| **测试** | Bun test |

---

# 第10章：研究结论

## 10.1 核心竞争力

OpenCode 的核心竞争力：

1. **100% 开源** - 完全透明的代码
2. **Provider-agnostic** - 不绑定任何提供商
3. **Client/Server 架构** - 支持远程控制
4. **ACP 协议** - 标准化集成
5. **LSP 原生支持** - 代码理解能力
6. **完善的权限系统** - 安全可控

## 10.2 Agent 性体现

| 维度 | OpenCode 实现 |
|------|-------------|
| **自主决策** | Agent 根据任务选择工具 |
| **多步推理** | 工具调用循环 |
| **环境感知** | 文件系统、LSP |
| **人机协作** | Permission 询问 |
| **多 Agent** | build/plan/general/explore |
| **协议支持** | ACP 协议 |

## 10.3 最值得借鉴的 10 条经验

1. **工具接口标准化** - 使用 Zod Schema 定义参数
2. **权限规则合并** - 默认 + 用户配置合并
3. **多 Agent 设计** - 不同任务用不同 Agent
4. **输出自动截断** - 避免上下文爆炸
5. **Provider 抽象** - 多 LLM 支持
6. **Session 管理** - 完整的状态追踪
7. **Token/Cost 追踪** - 使用量可视化
8. **ACP 协议** - 标准化集成
9. **工具注册表** - 动态工具发现
10. **AbortSignal 支持** - 可取消操作

## 10.4 下一步研究方向

**优先阅读**：
1. `src/tool/registry.ts` - 工具注册机制
2. `src/session/message-v2.ts` - 消息格式
3. `src/provider/provider.ts` - Provider 抽象
4. `src/permission/next.ts` - 权限系统
5. `src/acp/agent.ts` - ACP 协议实现

**深入方向**：
- ACP 协议规范
- LSP 集成细节
- 流式响应实现
- 多 Agent 协作

---

*报告版本: v1.0*  
*研究时间: 2026-03-11*  
*基于: OpenCode v1.2.24*
