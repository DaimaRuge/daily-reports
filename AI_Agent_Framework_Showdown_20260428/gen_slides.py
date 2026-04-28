#!/usr/bin/env python3
"""Generate AI Agent Framework Showdown HTML Slides"""
import os

OUT = "/root/.openclaw/workspace/ppt/AI_Agent_Framework_Showdown_20260428"
TOTAL = 14

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1280px; height:720px; overflow:hidden; font-family:'Segoe UI',system-ui,sans-serif; position:relative; }
.nav { position:absolute; top:0; height:100%; width:50%; z-index:10; cursor:pointer; }
.nav.left { left:0; } .nav.right { right:0; }
.nav:hover { background:rgba(255,255,255,0.03); }
.footer { position:absolute; bottom:16px; width:100%; display:flex; justify-content:space-between; padding:0 40px; font-size:12px; color:#888; z-index:5; }
.page-num { position:absolute; bottom:16px; right:40px; font-size:12px; color:#888; z-index:5; }
h1 { font-size:48px; font-weight:700; }
h2 { font-size:36px; font-weight:600; margin-bottom:24px; }
h3 { font-size:20px; font-weight:600; margin:16px 0 8px; color:#2563eb; }
p, li { font-size:17px; line-height:1.7; color:#374151; }
ul { padding-left:24px; }
li { margin:6px 0; }
.badge { display:inline-block; padding:4px 14px; border-radius:20px; font-size:13px; font-weight:600; margin:0 4px; }
.badge-lc { background:#1c3d1c; color:#4ade80; }
.badge-va { background:#1e1b4b; color:#a78bfa; }
.badge-ms { background:#0f172a; color:#38bdf8; }
.card { background:white; border-radius:16px; padding:24px; box-shadow:0 1px 3px rgba(0,0,0,0.08); margin-bottom:16px; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:20px; }
.grid3 { display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; }
.highlight { color:#2563eb; font-weight:600; }
table { width:100%; border-collapse:collapse; font-size:14px; margin-top:12px; }
th { background:#f8fafc; padding:10px 12px; text-align:left; font-weight:600; border-bottom:2px solid #e2e8f0; }
td { padding:8px 12px; border-bottom:1px solid #f1f5f9; }
tr:hover td { background:#f8fafc; }
.tag { display:inline-block; padding:2px 10px; border-radius:12px; font-size:12px; font-weight:600; }
.tag-green { background:#dcfce7; color:#166534; }
.tag-red { background:#fee2e2; color:#991b1b; }
.tag-yellow { background:#fef9c3; color:#854d0e; }
.tag-blue { background:#dbeafe; color:#1e40af; }
"""

def nav(n):
    return f'<a href="slide_{n-1:02d}.html" class="nav left"></a><a href="slide_{n+1:02d}.html" class="nav right"></a>' if n not in (1, TOTAL) else \
           f'<a href="slide_{n-1:02d}.html" class="nav left"></a>' if n == TOTAL else \
           f'<a href="slide_{n+1:02d}.html" class="nav right"></a>'

def html(n, body, title="AI Agent 框架三国杀"):
    return f"""<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>{title}</title>
<style>{CSS}</style></head><body>
{body}
<div class="footer"><span>AI Agent Framework Showdown 2026</span></div>
<div class="page-num">{n} / {TOTAL}</div>
{nav(n)}
<script>document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight')window.location='slide_{(n+1):02d}.html';if(e.key==='ArrowLeft')window.location='slide_{n-1:02d}.html';}})</script>
</body></html>"""

slides = []

# Slide 1: Title
slides.append(html(1, """
<div style="background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 50%,#1a237e 100%);width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;color:white;text-align:center;">
<div style="font-size:20px;color:#94a3b8;margin-bottom:16px;letter-spacing:4px;">2026 AI AGENT FRAMEWORK DEEP DIVE</div>
<h1 style="font-size:56px;color:white;margin-bottom:8px;">AI Agent 框架三国杀</h1>
<div style="font-size:28px;color:#38bdf8;font-weight:300;margin-bottom:32px;">LangChain vs VoltAgent vs Mastra</div>
<div style="display:flex;gap:16px;margin-bottom:40px;">
<span style="background:#1c3d1c;color:#4ade80;padding:6px 20px;border-radius:24px;font-size:16px;">🔗 LangChain</span>
<span style="background:#1e1b4b;color:#a78bfa;padding:6px 20px;border-radius:24px;font-size:16px;">🏭 VoltAgent</span>
<span style="background:#0f3450;color:#38bdf8;padding:6px 20px;border-radius:24px;font-size:16px;">🏠 Mastra</span></div>
<div style="color:#94a3b8;font-size:16px;">深度架构对比 · 选型指南 · 2026-04-28</div></div>
"""))

# Slide 2: 三大框架定位
slides.append(html(2, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">三大框架定位</h2>
<div class="grid3">
<div class="card"><div style="text-align:center;font-size:40px;margin-bottom:8px;">🔗</div>
<h3 style="text-align:center;color:#166534;">LangChain/LangGraph</h3>
<p style="text-align:center;color:#6b7280;font-size:14px;">Python 生态先行者 · 2022 年起</p>
<p style="text-align:center;"><span class="tag tag-green">500+ 集成</span> <span class="tag tag-yellow">LCEL 管道</span> <span class="tag tag-blue">LangGraph 有向图</span></p>
<p style="text-align:center;font-size:14px;color:#374151;margin-top:8px;">"一切皆可链接"</p>
</div>
<div class="card"><div style="text-align:center;font-size:40px;margin-bottom:8px;">🏭</div>
<h3 style="text-align:center;color:#4f46e5;">VoltAgent</h3>
<p style="text-align:center;color:#6b7280;font-size:14px;">Agent 工程平台 · v2.0 2026</p>
<p style="text-align:center;"><span class="tag tag-blue">MCP Client+Server</span> <span class="tag tag-blue">A2A 协议</span> <span class="tag tag-yellow">声明式 Workflow</span></p>
<p style="text-align:center;font-size:14px;color:#374151;margin-top:8px;">"Agent 是生产服务"</p>
</div>
<div class="card"><div style="text-align:center;font-size:40px;margin-bottom:8px;">🏠</div>
<h3 style="text-align:center;color:#0284c7;">Mastra</h3>
<p style="text-align:center;color:#6b7280;font-size:14px;">TS 全栈框架 · v1.0 2026.01 · 22k⭐</p>
<p style="text-align:center;"><span class="tag tag-green">Obs. Memory</span> <span class="tag tag-green">Studio 时间旅行</span> <span class="tag tag-yellow">Apache 2.0</span></p>
<p style="text-align:center;font-size:14px;color:#374151;margin-top:8px;">"Python trains, TypeScript ships"</p>
</div></div>
<div style="margin-top:32px;padding:20px;background:white;border-radius:12px;">
<p style="text-align:center;color:#64748b;font-size:16px;">三种<b>截然不同</b>的 Agent 构建哲学 — 代表了 AI Agent 框架的三条技术路线</p>
</div></div>
"""))

# Slide 3: LangChain 深度
slides.append(html(3, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">🔗 LangChain/LangGraph</h2>
<div class="grid2">
<div>
<h3>优势</h3>
<ul>
<li>最大的社区和生态（500+ 集成）</li>
<li>LangSmith 可观测性最早成熟</li>
<li>Python 原生，科研/ML 首选</li>
<li>LangGraph 有向图最灵活</li>
<li>最多教程、书籍、视频</li>
</ul></div>
<div>
<h3>痛点</h3>
<ul>
<li>抽象层过多，"为封装而封装"</li>
<li>70+ Python 包依赖</li>
<li>LCEL | 管道语法不直观</li>
<li>TypeScript 版本是二等公民</li>
<li>版本地狱（v0.1→v0.2 breaking）</li>
</ul></div></div>
<div style="margin-top:24px;background:#0f172a;border-radius:12px;padding:20px;color:#e2e8f0;font-family:monospace;font-size:14px;">
<span style="color:#4ade80;"># LCEL</span> chain = prompt | model | output_parser<br>
<span style="color:#4ade80;"># LangGraph</span> graph = StateGraph(State).add_node().add_edge()
</div></div>
"""))

# Slide 4: VoltAgent
slides.append(html(4, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">🏭 VoltAgent</h2>
<div class="grid2">
<div><h3>架构亮点</h3><ul>
<li>框架无关 Server 层（Hono/Elysia 可替换）</li>
<li>MCP <span class="highlight">双角色</span>（Client + Server）</li>
<li>A2A 协议（Agent 互操作）</li>
<li>声明式 Workflow 链式 API</li>
<li>6 种 Memory 后端适配器</li>
<li>15+ 种 RAG Chunker</li>
</ul></div>
<div><h3>代码示例</h3>
<div style="background:#1e1b4b;border-radius:12px;padding:20px;color:#c4b5fd;font-family:monospace;font-size:13px;line-height:1.6;">
<span style="color:#a78bfa;">new</span> VoltAgent({<br>
&nbsp;&nbsp;agents: {<span style="color:#fbbf24;">assistant</span>},<br>
&nbsp;&nbsp;server: <span style="color:#34d399;">honoServer</span>(),<br>
&nbsp;&nbsp;workflows: { <span style="color:#fbbf24;">wf</span> },<br>
});<br><br>
<span style="color:#a78bfa;">createWorkflowChain</span>({id,input,result})<br>
&nbsp;&nbsp;.<span style="color:#f472b6;">andThen</span>(execute)<br>
&nbsp;&nbsp;.<span style="color:#f472b6;">andAgent</span>(prompt, agent)<br>
&nbsp;&nbsp;.<span style="color:#f472b6;">andWhen</span>(condition)
</div></div></div></div>
"""))

# Slide 5: Mastra
slides.append(html(5, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">🏠 Mastra</h2>
<div class="grid2">
<div><h3>独特优势</h3><ul>
<li><span class="highlight">Observational Memory</span> — 后台 Agent 压缩长对话</li>
<li>Composite Store — domain 路由 OLTP/OLAP</li>
<li>Studio <span class="highlight">时间旅行</span>调试</li>
<li>Vercel/CF/Netlify 官方 deployer</li>
<li>Apache 2.0 全开源 + 任意 OTLP 导出</li>
<li>40+ 示例项目，npx create mastra</li>
</ul></div>
<div><h3>杀手功能：Observational Memory</h3>
<div style="background:#0f3450;border-radius:12px;padding:20px;color:#bae6fd;font-family:monospace;font-size:13px;line-height:1.6;">
<span style="color:#38bdf8;">memory</span>: <span style="color:#a78bfa;">new</span> <span style="color:#7dd3fc;">Memory</span>({<br>
&nbsp;&nbsp;options: {<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#fbbf24;">observationalMemory</span>: <span style="color:#34d399;">true</span>,<br>
&nbsp;&nbsp;}<br>
})<br><br>
<span style="color:#94a3b8;">// 后台 Agent 将旧消息压缩为</span><br>
<span style="color:#94a3b8;">// 密集观察日志，避免上下文溢出</span>
</div></div></div>
<div style="margin-top:20px;padding:16px;background:white;border-radius:12px;text-align:center;">
<p><span style="font-weight:700;color:#0284c7;">22k+</span> GitHub Stars · <span style="font-weight:700;color:#0284c7;">300k+</span> 周下载 · YC W25 · $13M 融资</p>
</div></div>
"""))

# Slide 6: Agent 设计模式对比
slides.append(html(6, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">Agent 设计模式对比</h2>
<div class="grid3">
<div class="card">
<h3 style="text-align:center;">🔗 LangChain</h3>
<p style="text-align:center;font-size:14px;color:#6b7280;">Agent = 会使用工具的 Chain</p>
<div style="background:#f0fdf4;border-radius:8px;padding:12px;margin-top:8px;text-align:center;font-family:monospace;font-size:13px;">
agent = create_react_agent(llm, tools)
</div>
<p style="font-size:13px;margin-top:8px;">Agent 本质是 Runnable 的一种</p>
</div>
<div class="card">
<h3 style="text-align:center;">🏭 VoltAgent</h3>
<p style="text-align:center;font-size:14px;color:#6b7280;">Agent = 带完整能力的服务</p>
<div style="background:#eef2ff;border-radius:8px;padding:12px;margin-top:8px;text-align:center;font-family:monospace;font-size:13px;">
new Agent({ tools, memory, mcp, retriever, guardrails })
</div>
<p style="font-size:13px;margin-top:8px;">一切能力都是属性，统一注入</p>
</div>
<div class="card">
<h3 style="text-align:center;">🏠 Mastra</h3>
<p style="text-align:center;font-size:14px;color:#6b7280;">Agent = Mastra 实例注册的服务</p>
<div style="background:#f0f9ff;border-radius:8px;padding:12px;margin-top:8px;text-align:center;font-family:monospace;font-size:13px;">
mastra.getAgentById('my-agent')
</div>
<p style="font-size:13px;margin-top:8px;">中央实例管理，共享服务注入</p>
</div></div></div>
"""))

# Slide 7: Workflow 引擎
slides.append(html(7, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">Workflow 引擎 — 最大分歧点</h2>
<table>
<tr><th>特性</th><th>LangChain/LangGraph</th><th>VoltAgent</th><th>Mastra</th></tr>
<tr><td>模型</td><td>有向图 StateGraph</td><td>声明式链式 API</td><td>图式 createStep/createWorkflow</td></tr>
<tr><td>条件分支</td><td>conditional_edges</td><td>.andWhen / .andBranch</td><td>.branch(cond, t, f)</td></tr>
<tr><td>并行</td><td>Send API</td><td>.andAll / .andRace</td><td>.parallel()</td></tr>
<tr><td>挂起/恢复</td><td>interrupt()</td><td>suspend/resume</td><td>.suspend()</td></tr>
<tr><td><span class="highlight">时间旅行</span></td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-green">✅ Studio</span></td></tr>
<tr><td>LLM 调用</td><td>ToolNode</td><td><span class="highlight">andAgent() 专用</span></td><td>step 内调用 agent</td></tr>
<tr><td>Schema</td><td>TypedDict</td><td>Zod（为主）</td><td>Zod/Valibot/ArkType</td></tr>
<tr><td>循环回边</td><td><span class="tag tag-green">✅</span></td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td></tr>
</table>
<div style="margin-top:20px;display:flex;gap:16px;">
<div style="flex:1;background:#f0fdf4;border-radius:12px;padding:16px;"><strong>最灵活：</strong>LangGraph 有向图</div>
<div style="flex:1;background:#eef2ff;border-radius:12px;padding:16px;"><strong>最简洁：</strong>VoltAgent 链式声明</div>
<div style="flex:1;background:#f0f9ff;border-radius:12px;padding:16px;"><strong>最工程化：</strong>Mastra Step 组件化</div>
</div></div>
"""))

# Slide 8: 记忆系统
slides.append(html(8, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">记忆系统 — 皇冠之争</h2>
<table>
<tr><th>能力</th><th>LangChain</th><th>VoltAgent</th><th>Mastra</th></tr>
<tr><td>消息存储</td><td>Checkpointer</td><td>userId+conversationId</td><td>resource+thread</td></tr>
<tr><td>向量搜索</td><td><span class="tag tag-green">✅</span></td><td><span class="tag tag-green">✅</span></td><td><span class="tag tag-green">✅</span></td></tr>
<tr><td>工作记忆</td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-green">✅</span></td><td><span class="tag tag-green">✅</span></td></tr>
<tr><td style="font-weight:700;">观察记忆</td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td><td style="background:#dcfce7;"><span class="tag tag-green">✅ Observational Memory</span></td></tr>
<tr><td>记忆处理器</td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-green">✅</span></td></tr>
<tr><td style="font-weight:700;">多Agent隔离</td><td>手动</td><td>手动</td><td style="background:#dcfce7;"><span class="tag tag-green">✅ 自动委派级</span></td></tr>
</table>
<div style="margin-top:24px;padding:20px;background:white;border-radius:12px;border-left:4px solid #0284c7;">
<h3>💡 Mastra Observational Memory 原理</h3>
<p style="font-size:15px;line-height:1.8;">后台 Agent 将长对话历史 <span class="highlight">压缩为观察日志</span> — 不记每个细节，只提炼关键要点。类似人类记忆：记住说了什么、做了什么决定，而非每个字。</p>
</div></div>
"""))

# Slide 9: 可观测性
slides.append(html(9, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">可观测性 — 开放性之争</h2>
<table>
<tr><th>能力</th><th>LangChain (LangSmith)</th><th>VoltAgent (VoltOps)</th><th>Mastra</th></tr>
<tr><td>追踪协议</td><td>OpenTelemetry</td><td>OpenTelemetry</td><td>OpenTelemetry</td></tr>
<tr><td>外部导出</td><td>任意 OTLP</td><td style="color:#991b1b;">VoltOps 专有</td><td style="background:#dcfce7;">Langfuse/Datadog/任意</td></tr>
<tr><td>可视化</td><td>LangSmith Studio</td><td>VoltOps Console</td><td>Mastra Studio</td></tr>
<tr><td style="font-weight:700;">时间旅行</td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td><td style="background:#dcfce7;"><span class="tag tag-green">✅</span></td></tr>
<tr><td>本地调试</td><td><span class="tag tag-red">❌</span></td><td>Console</td><td style="background:#dcfce7;">Studio + DuckDB</td></tr>
<tr><td style="font-weight:700;">敏感数据过滤</td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td><td style="background:#dcfce7;"><span class="tag tag-green">✅</span></td></tr>
<tr><td>开源程度</td><td>中等</td><td>低</td><td style="background:#dcfce7;">高</td></tr>
</table>
<div style="margin-top:24px;padding:20px;background:#f0f9ff;border-radius:12px;">
<p style="text-align:center;font-size:16px;"><span class="highlight">Mastra</span> 在可观测性开放性上碾压 — 不需要绑定任何专有平台</p>
</div></div>
"""))

# Slide 10: 开发体验
slides.append(html(10, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">开发体验对比</h2>
<div class="grid2">
<div class="card">
<h3>上手速度</h3>
<table>
<tr><th>框架</th><th>Hello World</th><th>生产 Agent</th></tr>
<tr><td>LangChain</td><td>5min</td><td>数天</td></tr>
<tr><td>VoltAgent</td><td>3min</td><td>半天</td></tr>
<tr style="background:#dcfce7;"><td><strong>Mastra</strong></td><td><strong>1min ⚡</strong></td><td><strong>半天</strong></td></tr>
</table>
</div>
<div class="card">
<h3>类型安全</h3>
<table>
<tr><th>框架</th><th>类型推导</th></tr>
<tr style="background:#eef2ff;"><td><strong>VoltAgent</strong></td><td><strong>强 ✨</strong></td></tr>
<tr><td>Mastra</td><td>中</td></tr>
<tr><td>LangChain</td><td>弱</td></tr>
</table>
</div></div>
<div class="grid2" style="margin-top:16px;">
<div class="card">
<h3>调试</h3>
<p><span class="tag tag-green">Mastra Studio</span> — Graph 视图 + 时间旅行 + 实时状态</p>
<p><span class="tag tag-yellow">LangSmith</span> — 功能强大但付费</p>
<p><span class="tag tag-yellow">VoltOps</span> — Console 本地调试弱</p>
</div>
<div class="card">
<h3>一键创建</h3>
<div style="background:#0f172a;border-radius:8px;padding:12px;color:#e2e8f0;font-family:monospace;font-size:14px;margin-top:8px;">
<span style="color:#38bdf8;">npx create mastra@latest</span><br>
<span style="color:#6b7280;">→ 项目模板 + Studio + 示例</span>
</div>
</div></div></div>
"""))

# Slide 11: 部署
slides.append(html(11, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">生产部署</h2>
<table>
<tr><th>平台</th><th>LangChain</th><th>VoltAgent</th><th>Mastra</th></tr>
<tr><td>Standalone</td><td><span class="tag tag-green">✅</span></td><td><span class="tag tag-green">✅</span></td><td><span class="tag tag-green">✅</span></td></tr>
<tr><td>Next.js</td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td><td style="background:#dcfce7;"><span class="tag tag-green">✅</span></td></tr>
<tr><td>Vercel Edge</td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td><td style="background:#dcfce7;"><span class="tag tag-green">✅</span></td></tr>
<tr><td>CF Workers</td><td><span class="tag tag-red">❌</span></td><td><span class="tag tag-red">❌</span></td><td style="background:#dcfce7;"><span class="tag tag-green">✅</span></td></tr>
<tr><td>Docker</td><td><span class="tag tag-green">✅</span></td><td><span class="tag tag-green">✅</span></td><td><span class="tag tag-green">✅</span></td></tr>
<tr><td>托管</td><td>LangServe</td><td>VoltOps</td><td>Mastra Cloud</td></tr>
</table>
<div style="margin-top:24px;padding:20px;background:white;border-radius:12px;">
<h3>📦 Mastra 部署器生态</h3>
<div style="display:flex;gap:16px;margin-top:12px;">
<div style="flex:1;text-align:center;padding:16px;background:#f0fdf4;border-radius:8px;">▲ Vercel<br><span style="font-size:12px;">官方 Deployer</span></div>
<div style="flex:1;text-align:center;padding:16px;background:#fef9c3;border-radius:8px;">☁️ Cloudflare<br><span style="font-size:12px;">Workers + D1</span></div>
<div style="flex:1;text-align:center;padding:16px;background:#f0f9ff;border-radius:8px;">🔷 Netlify<br><span style="font-size:12px;">官方 Deployer</span></div>
</div>
<p style="font-size:14px;color:#6b7280;margin-top:12px;text-align:center;">源于 Gatsby 团队的前端基因</p>
</div></div>
"""))

# Slide 12: 决策框架
slides.append(html(12, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">一句话选型</h2>
<div class="grid2">
<div class="card"><h3>选 LangChain 如果你...</h3><ul>
<li>是 Python ML/研究团队</li>
<li>需要最大社区和生态</li>
<li>需要复杂 DAG/循环工作流</li>
<li>需要最多集成选择</li></ul></div>
<div class="card"><h3>选 VoltAgent 如果你...</h3><ul>
<li>需要 Agent-as-API-Service</li>
<li>需要 MCP Server 暴露</li>
<li>追求最简洁 Workflow API</li>
<li>需要 A2A 协议互操作</li></ul></div>
<div class="card" style="background:#f0f9ff;"><h3>选 Mastra 如果你...</h3><ul>
<li>是 TS 全栈/Next.js 团队</li>
<li>需要长对话记忆</li>
<li>需要最好调试工具</li>
<li>不想绑定任何平台</li>
<li>做产品、投入生产</li></ul></div>
<div class="card"><h3>实际建议</h3>
<p style="font-size:14px;margin-bottom:8px;"><span class="highlight">研究/原型</span> → LangChain</p>
<p style="font-size:14px;margin-bottom:8px;"><span class="highlight">SaaS 产品</span> → Mastra</p>
<p style="font-size:14px;margin-bottom:8px;"><span class="highlight">Agent 服务</span> → VoltAgent</p>
<p style="font-size:14px;"><span class="highlight">多平台部署</span> → Mastra</p></div></div></div>
"""))

# Slide 13: 战争态势图
slides.append(html(13, """
<div style="padding:56px 60px;height:100%;background:#f8fafc;">
<h2 style="color:#0f172a;">战争态势图</h2>
<div style="display:flex;justify-content:center;align-items:center;height:70%;">
<div style="text-align:center;">
<div style="font-size:18px;color:#6b7280;margin-bottom:4px;">Python 生态 ← → TypeScript 生态</div>
<div style="position:relative;width:600px;height:400px;margin:0 auto;">
<!-- LangChain -->
<div style="position:absolute;top:0;left:50%;transform:translateX(-50%);text-align:center;">
<div style="background:#166534;color:#4ade80;padding:20px 40px;border-radius:16px;font-size:20px;font-weight:700;">🔗 LangChain<br>LangGraph</div>
<div style="color:#6b7280;font-size:13px;margin-top:4px;">500+ 集成 · Python 生态之王</div>
</div>
<!-- lines -->
<div style="position:absolute;top:90px;left:50%;width:2px;height:40px;background:#cbd5e1;"></div>
<div style="position:absolute;top:130px;left:160px;width:280px;height:2px;background:#cbd5e1;"></div>
<div style="position:absolute;top:130px;left:160px;width:2px;height:40px;background:#cbd5e1;"></div>
<div style="position:absolute;top:130px;right:160px;width:2px;height:40px;background:#cbd5e1;"></div>
<!-- VoltAgent -->
<div style="position:absolute;bottom:60px;left:100px;text-align:center;">
<div style="background:#312e81;color:#a78bfa;padding:16px 28px;border-radius:12px;font-size:16px;font-weight:600;">🏭 VoltAgent<br><span style="font-size:12px;">平台优先 · MCP+A2A</span></div>
</div>
<!-- Mastra -->
<div style="position:absolute;bottom:60px;right:100px;text-align:center;">
<div style="background:#0f3450;color:#38bdf8;padding:16px 28px;border-radius:12px;font-size:16px;font-weight:600;">🏠 Mastra<br><span style="font-size:12px;">前端优先 · 22k⭐ · Apache 2.0</span></div>
</div>
</div>
<div style="margin-top:16px;font-size:14px;color:#64748b;">TypeScript Agent 框架的两条路线：<b>平台化 vs 全栈化</b></div>
</div></div></div>
"""))

# Slide 14: 总结
slides.append(html(14, """
<div style="background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 50%,#1a237e 100%);width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;color:white;text-align:center;padding:60px;">
<div style="font-size:20px;color:#94a3b8;margin-bottom:8px;">CONCLUSION</div>
<h2 style="font-size:44px;color:white;margin-bottom:32px;">没有银弹。但有确定的事。</h2>
<div style="display:flex;gap:32px;margin-bottom:40px;">
<div style="background:rgba(255,255,255,0.08);border-radius:16px;padding:24px 32px;text-align:center;">
<div style="font-size:36px;margin-bottom:8px;">🔗</div><div style="font-size:18px;color:#4ade80;margin-bottom:4px;">LangChain</div>
<div style="font-size:14px;color:#94a3b8;">一切皆可链接</div></div>
<div style="background:rgba(255,255,255,0.08);border-radius:16px;padding:24px 32px;text-align:center;">
<div style="font-size:36px;margin-bottom:8px;">🏭</div><div style="font-size:18px;color:#a78bfa;margin-bottom:4px;">VoltAgent</div>
<div style="font-size:14px;color:#94a3b8;">Agent 是生产服务</div></div>
<div style="background:rgba(255,255,255,0.08);border-radius:16px;padding:24px 32px;text-align:center;">
<div style="font-size:36px;margin-bottom:8px;">🏠</div><div style="font-size:18px;color:#38bdf8;margin-bottom:4px;">Mastra</div>
<div style="font-size:14px;color:#94a3b8;">Agent 融入全栈应用</div></div>
</div>
<div style="font-size:22px;color:#38bdf8;font-weight:300;">TypeScript Agent 框架的春天来了 🌱</div>
<div style="font-size:14px;color:#94a3b8;margin-top:12px;">2026-04-28 · 基于官方文档 + 源码分析</div>
</div>
"""))

# Write all slides
for i, s in enumerate(slides, 1):
    with open(f"{OUT}/slide_{i:02d}.html", "w") as f:
        f.write(s)

print(f"Generated {len(slides)} slides in {OUT}/")
