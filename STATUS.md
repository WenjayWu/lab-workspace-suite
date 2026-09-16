# STATUS.md

本文件记录仓库的项目状态与进度，每次有新增/修改组件时同步更新。

## 当前状态

- 最近更新：2026-09-16（drawer 上下间隙修改完成，待打印验证）
- 可用组件：2（抽屉、可堆叠抽屉）
- 开源协议：CC BY 4.0
- 待完成：见下方「更新计划」

## 组件清单

### 抽屉 (drawer) ✅ 已完成

| 文件 | 类型 | 说明 |
| --- | --- | --- |
| `drawer/drawer-box.SLDPRT` | 零件 | 抽屉盒（容纳空间主体） |
| `drawer/drawer-front.SLDPRT` | 零件 | 抽屉（面板 + 拉手等） |
| `drawer/drawer-assembly.SLDASM` | 装配体 | 抽屉完整装配 |
| `drawer/drawer-box.STL` | STL | 抽屉盒 3D 打印网格 |
| `drawer/drawer-front.STL` | STL | 抽屉 3D 打印网格 |

### 可堆叠抽屉 (stackable-drawer) ✅ 已完成

这是AI生成的测试文件，不作为后续实际生产，只作参考

| 文件 | 类型 | 说明 |
| --- | --- | --- |
| `stackable-drawer/drawer-box.STL` | STL | 抽屉盒（带堆叠卡槽） |
| `stackable-drawer/drawer-panel.STL` | STL | 前面板 + 拉手 |
| `stackable-drawer/stackable-drawer-assembly.STL` | STL | 完整抽屉装配 |
| `stackable-drawer/stackable-drawer-viewer.html` | HTML | 交互式 3D 预览（Three.js） |
| `stackable-drawer/generate_stl.py` | Python | STL 生成脚本（可调参数） |

## 更新计划

**下一步（优先级高）**

- [ ] 打印测试与尺寸验证（验证 drawer 间隙修改效果）

**后续（无明确时间）**

- [ ] 其他工作区组件（支架、隔板、走线槽等）
- [ ] 导出 STEP 格式（中性 CAD 交换格式）

**已完成**

- [x] 修改 drawer 组件：增大抽屉与抽屉盒间隙（上下各约 2mm，详见更新记录 2026-09-16）
- [x] drawer 组件 SolidWorks 源文件名英文化（SW 内 Pack and Go）

## 更新记录

| 日期 | 类型 | 内容 |
| --- | --- | --- |
| 2026-09-16 | 修改 | drawer 组件：drawer-box 主体拉伸长度改为 150mm，盒内上下空间增至 140mm（不含圆角），drawer-front 仍为 136mm（上下间隙合计约 4mm）；已重新导出 drawer-box.STL |
| 2026-09-16 | 反馈 | 打印测试：抽屉与抽屉盒之间需留足够空隙，不仅左右两侧，上下侧同样需要；已列入更新计划，待修改模型 |
| 2026-09-14 | 重构 | 全部目录与文件改为英文 kebab-case 命名（含 drawer 组件 SW 源文件，SW 内改名保持引用）；命名约定由中文改为英文 |
| 2026-08-26 | 新增 | 可堆叠抽屉组件：STL 模型、HTML 交互预览、Python 生成脚本 |
| 2026-08-20 | 新增 | 初始化仓库，加入抽屉组件；补充 README、AGENTS、CLAUDE、STATUS 文档 |
