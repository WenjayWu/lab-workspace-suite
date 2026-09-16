# 实验室工作区套件 (lab-workspace-suite)

实验室工作台配套组件的 SolidWorks 三维模型库，持续扩展中。

## 命名规范

目录与文件统一使用英文小写 + kebab-case（连字符分隔），不使用中文、空格。3D 打印网格（`.STL`）与 CAD 源文件同名放置。SolidWorks 源文件的改名必须在 SolidWorks 内完成（Pack and Go / 另存为更新引用），不要直接在文件管理器中改名。

## 开源协议

本项目采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hans)（知识共享-署名 4.0 国际）协议开源：任何人可自由使用、修改、商用，但需保留署名。完整条款见 [LICENSE](./LICENSE)。

## 当前组件

### 抽屉 (drawer)

| 文件 | 类型 | 说明 |
| --- | --- | --- |
| `drawer/drawer-box.SLDPRT` | 零件 | 抽屉盒（容纳空间主体） |
| `drawer/drawer-front.SLDPRT` | 零件 | 抽屉（面板 + 拉手等） |
| `drawer/drawer-assembly.SLDASM` | 装配体 | 抽屉完整装配 |
| `drawer/drawer-box.STL` | STL | 抽屉盒 3D 打印网格 |
| `drawer/drawer-front.STL` | STL | 抽屉 3D 打印网格 |

### 可堆叠抽屉 (stackable-drawer)

| 文件 | 类型 | 说明 |
| --- | --- | --- |
| `stackable-drawer/drawer-box.STL` | STL | 抽屉盒（带堆叠卡槽） |
| `stackable-drawer/drawer-panel.STL` | STL | 前面板 + 拉手 |
| `stackable-drawer/stackable-drawer-assembly.STL` | STL | 完整抽屉装配 |
| `stackable-drawer/stackable-drawer-viewer.html` | HTML | 交互式 3D 预览（Three.js） |
| `stackable-drawer/generate_stl.py` | Python | STL 生成脚本（可调参数） |

## 目录结构

```
lab-workspace-suite/
├── drawer/              # 抽屉组件（零件 / 装配体 / STL）
├── stackable-drawer/    # 可堆叠抽屉系统（STL / HTML 预览 / 生成脚本）
├── LICENSE              # CC BY 4.0 开源协议
├── README.md            # 项目说明
├── STATUS.md            # 项目状态
├── AGENTS.md            # AI 助手约定
├── CLAUDE.md            # Claude Code 约定
└── .gitignore           # SolidWorks 临时与系统文件过滤
```

## 使用方法

- **设计查看 / 编辑**：使用 SolidWorks 打开 `.SLDPRT` / `.SLDASM` 文件
- **3D 打印**：直接使用 `.STL` 文件导入切片软件

## 使用说明

- 建议在 SolidWorks 中保持零件、装配体相对路径一致，移动整个文件夹即可
- STL 文件为导出快照，修改模型后如需打印请重新导出

## 待办 / 规划

开发计划、进度与更新记录统一维护在 [STATUS.md](./STATUS.md)。
