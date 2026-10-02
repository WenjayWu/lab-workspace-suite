# AGENTS.md

本文件为 AI 编码助手（opencode、Claude Code、Cline 等）在本仓库工作时的约定。

## 项目概况

实验室工作台配套组件的 SolidWorks 三维模型仓库。开发组件保存 CAD 源文件（`.SLDPRT` / `.SLDASM`）与导出网格（`.STL`）；`references/` 单独保存设计参考，可包含 AI 生成的 STL、HTML 概念预览与 Python 生成脚本。

## 仓库约定

- 组件按目录组织：`component-name/` 下放该组件的所有文件
- 每个组件包含：零件（`.SLDPRT`）、装配体（`.SLDASM`，如适用）、3D 打印网格（`.STL`）
- 文件命名用英文小写 + kebab-case，与组件名一致（如 `drawer-box.SLDPRT`）
- SolidWorks 源文件（`.SLDPRT` / `.SLDASM` / `.SLDDRW`）的改名/移动必须在 SolidWorks 内完成（Pack and Go 或另存为更新引用），不要直接在文件管理器中操作，否则装配体引用会断
- 目录与文件一律使用 UTF-8；文件名不要混用中英文
- 新增组件时同步更新 `README.md` 的组件清单
- 参考资料按 `references/<方案名称>/` 组织；命名采用名称－用途（需要时）－来源，后缀已表达的文件类型不重复添加，详见 `references/README.md`
- 参考方案 README 记录用途、来源及其确定程度、使用方法与已知限制；参考资料不计入开发组件数量，不标为已验证的生产方案
- 参考文件改名或移动前先预演路径，修改时同步脚本输出名称、关联引用与文档链接；保留原始几何，未经模型变更不重导 STL

## 提交信息规范

采用 Conventional Commits（约定式提交）：英文类型前缀 + 中文描述，格式为 `类型: 描述`。2026-09 之前的提交未按此规范，无需重写。

| 类型 | 用途 |
| --- | --- |
| `feat` | 新组件、新预览页、新生成脚本 |
| `fix` | 尺寸 / 配合 / 模型错误修复 |
| `docs` | README / STATUS / CLAUDE.md / AGENTS.md |
| `refactor` | 改名、目录重组（几何不变） |
| `chore` | 单独重导 STL、`.gitignore` 等杂务 |

- 描述写清楚改了什么、关键数值（如尺寸），避免「更新模型」这类含糊说法
- 组件多了可加 scope 标明组件，如 `fix(drawer): 修正面板尺寸`
- 模型修改与随之重导的 STL 合并为一条提交，不单独来一条 `chore`

## 修改文件时必须做的事

1. 编辑后同步更新 `STATUS.md`（有新增/修改组件或参考资料时）
2. 更新 `README.md` 中的组件列表、目录结构；参考资料变化时同步更新参考索引与方案说明
3. 运行 `git status` 检查是否有遗漏文件

## 禁止事项

- 不提交 SolidWorks 临时文件（`~$*` 已在 `.gitignore` 中过滤）
- 不提交二进制大文件的重复副本；STL 仅在模型变更后重新导出
- 不随意删除组件目录；删除前先确认
