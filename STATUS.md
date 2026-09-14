# STATUS.md

本文件记录仓库的项目状态与进度，每次有新增/修改组件时同步更新。

## 当前状态

- 最近更新：初始化阶段
- 可用组件：2（抽屉、可堆叠抽屉）
- 开源协议：CC BY 4.0
- 待完成：见下方「待办」及 `README.md` 中的规划

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

| 文件 | 类型 | 说明 |
| --- | --- | --- |
| `stackable-drawer/drawer-box.STL` | STL | 抽屉盒（带堆叠卡槽） |
| `stackable-drawer/drawer-panel.STL` | STL | 前面板 + 拉手 |
| `stackable-drawer/stackable-drawer-assembly.STL` | STL | 完整抽屉装配 |
| `stackable-drawer/stackable-drawer-viewer.html` | HTML | 交互式 3D 预览（Three.js） |
| `stackable-drawer/generate_stl.py` | Python | STL 生成脚本（可调参数） |

## 待办

- [ ] 其他工作区组件（支架、隔板、走线槽等）
- [ ] 导出 STEP 格式（中性 CAD 交换格式）
- [ ] 打印测试与尺寸验证
- [x] drawer 组件 SolidWorks 源文件名英文化（SW 内 Pack and Go）

## 更新记录

| 日期 | 内容 |
| --- | --- |
| 2026-08-20 | 初始化仓库，加入抽屉组件；补充 README、AGENTS、CLAUDE、STATUS 文档 |
| 2026-08-26 | 新增可堆叠抽屉组件：STL模型、HTML交互预览、Python生成脚本 |
| 2026-09-14 | 全部目录与文件改为英文 kebab-case 命名（含 drawer 组件 SW 源文件，SW 内改名保持引用）；命名约定由中文改为英文 |
