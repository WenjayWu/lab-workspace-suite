# STATUS.md

本文件记录仓库的项目状态与进度，每次有新增/修改组件时同步更新。

## 当前状态

- 最近更新：2026-10-02（重写项目说明，整理参考目录与命名）
- 开发组件：1（抽屉，待打印验证）
- 参考方案：1（可堆叠抽屉，仅作设计参考）
- 开源协议：CC BY 4.0
- 待完成：见下方「更新计划」

## 组件清单

### 抽屉 (drawer) — 模型已修改，待打印验证

| 文件 | 类型 | 说明 |
| --- | --- | --- |
| `drawer/drawer-box.SLDPRT` | 零件 | 抽屉盒（容纳空间主体） |
| `drawer/drawer-front.SLDPRT` | 零件 | 抽屉（面板 + 拉手等） |
| `drawer/drawer-assembly.SLDASM` | 装配体 | 抽屉完整装配 |
| `drawer/drawer-box.STL` | STL | 抽屉盒 3D 打印网格 |
| `drawer/drawer-front.STL` | STL | 抽屉 3D 打印网格 |

## 参考资料

### 可堆叠抽屉 (stackable-drawer) — 仅作参考

AI 生成的测试资料，不作为后续实际生产方案。来源据回忆为 DeepSeek，未核实；现已归档到 [references/stackable-drawer/](references/stackable-drawer/README.md)，不计入开发组件数量。

| 文件 | 类型 | 说明 |
| --- | --- | --- |
| `references/stackable-drawer/drawer-box-deepseek.STL` | STL | 抽屉盒与堆叠结构参考 |
| `references/stackable-drawer/drawer-panel-deepseek.STL` | STL | 前面板与拉手参考 |
| `references/stackable-drawer/stackable-drawer-assembly-deepseek.STL` | STL | 抽屉装配参考 |
| `references/stackable-drawer/stackable-drawer-preview-deepseek.html` | HTML | 独立绘制的概念预览，与 STL 几何不完全一致 |
| `references/stackable-drawer/stackable-drawer-generator-deepseek.py` | Python | STL 参考生成脚本（可调参数） |

## 更新计划

**下一步（优先级高）**

- [ ] 打印测试与尺寸验证（验证 drawer 间隙修改效果）

**后续（无明确时间）**

- [ ] 其他工作区组件（支架、隔板、走线槽等）
- [ ] 导出 STEP 格式（中性 CAD 交换格式）

**已完成**

- [x] 重写 README，建立 references 参考目录，整理可堆叠抽屉资料与命名
- [x] 修改 drawer 组件：增大抽屉与抽屉盒间隙（上下各约 2mm，详见更新记录 2026-09-16）
- [x] drawer 组件 SolidWorks 源文件名英文化（SW 内 Pack and Go）

## 更新记录

| 日期 | 类型 | 内容 |
| --- | --- | --- |
| 2026-10-02 | 整理 | README 聚焦项目用途与使用方法；五个可堆叠抽屉参考文件迁入 references/stackable-drawer/，按名称－用途（需要时）－来源命名；来源暂记 DeepSeek（未核实）；同步脚本输出文件名与维护约定，模型几何未修改 |
| 2026-09-16 | 修改 | drawer 组件：drawer-box 主体拉伸长度改为 150mm，盒内上下空间增至 140mm（不含圆角），drawer-front 仍为 136mm（上下间隙合计约 4mm）；已重新导出 drawer-box.STL |
| 2026-09-16 | 反馈 | 打印测试：抽屉与抽屉盒之间需留足够空隙，不仅左右两侧，上下侧同样需要；已列入更新计划，待修改模型 |
| 2026-09-14 | 重构 | 全部目录与文件改为英文 kebab-case 命名（含 drawer 组件 SW 源文件，SW 内改名保持引用）；命名约定由中文改为英文 |
| 2026-08-26 | 新增 | 可堆叠抽屉组件：STL 模型、HTML 交互预览、Python 生成脚本 |
| 2026-08-20 | 新增 | 初始化仓库，加入抽屉组件；补充 README、AGENTS、CLAUDE、STATUS 文档 |
