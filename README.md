# 实验室工作区套件 (lab-workspace-suite)

为实验室工作台设计和制作收纳及配套组件，保存 SolidWorks 设计源文件与用于 3D 打印的 STL，便于按实际使用需求调整尺寸、试制和迭代。

目前主要开发抽屉组件，后续计划扩展支架、隔板、走线槽等工作区配件。AI 生成的概念方案单独收录在参考目录中，用于探索结构和外观。

## 当前组件

### 抽屉 (drawer)

用于工作台收纳，包含抽屉盒、抽屉及完整装配体。已调整抽屉与盒体的上下间隙，并重新导出抽屉盒 STL；当前等待打印测试与尺寸验证。

| 文件入口 | 用途 |
| --- | --- |
| [drawer-assembly.SLDASM](drawer/drawer-assembly.SLDASM) | 查看整体装配和零件配合 |
| [drawer-box.SLDPRT](drawer/drawer-box.SLDPRT)、[drawer-front.SLDPRT](drawer/drawer-front.SLDPRT) | 编辑抽屉盒与抽屉（面板、拉手等）的设计 |
| [drawer-box.STL](drawer/drawer-box.STL)、[drawer-front.STL](drawer/drawer-front.STL) | 导入切片软件，准备试制 |

## 怎么使用

### 查看或修改设计

1. 下载或克隆整个仓库，保留 `drawer/` 内零件与装配体的相对位置。
2. 使用 SolidWorks 打开 `drawer/drawer-assembly.SLDASM` 查看装配；打开对应 `.SLDPRT` 编辑零件。
3. 修改模型后，重新导出对应 STL，再用于切片和打印。

### 3D 打印与验证

将 `drawer/` 中的两个 STL 分别导入切片软件，根据打印机、材料和实际使用需求设置打印参数。打印后检查抽屉滑动、上下及左右间隙，再决定是否调整模型。

STL 是设计导出的快照。当前间隙修改尚待打印验证，具体进度和尺寸变更见 [STATUS.md](STATUS.md)。

### 查看设计参考

[references/](references/README.md) 存放 AI 生成的概念模型、预览页和生成脚本，现有方案为 [可堆叠抽屉](references/stackable-drawer/README.md)。用浏览器打开其中的 HTML 可查看概念预览，页面依赖联网加载的库。

这些资料用于设计参考，未作为实际生产方案验证。预览页独立绘制模型，与 STL 的几何不完全一致；文件说明与使用方法见参考目录。

## 目录导览

```text
lab-workspace-suite/
├── drawer/                     # 实际开发的抽屉组件：SolidWorks / STL
├── references/                 # 设计参考资料
│   ├── README.md               # 参考索引与命名方式
│   └── stackable-drawer/       # AI 生成的可堆叠抽屉概念方案
├── README.md                   # 项目用途与使用入口
├── STATUS.md                   # 开发进度、验证状态与更新记录
├── AGENTS.md                   # AI 助手维护约定
├── CLAUDE.md                   # Claude Code 维护约定
├── LICENSE
└── .gitignore
```

开发计划、进度与更新记录统一维护在 [STATUS.md](STATUS.md)。
