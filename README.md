# 实验室工作区套件 (lab-workspace-suite)

为实验室工作台设计和制作收纳及配套组件，保存 SolidWorks 设计源文件与用于 3D 打印的 STL，便于按实际使用需求调整尺寸、试制和迭代。

目前主要开发抽屉组件，后续计划扩展支架、隔板、走线槽等工作区配件。AI 生成的概念方案单独收录在参考目录中，用于探索结构和外观。

## 当前组件

### 抽屉 (drawer)

用于工作台收纳，已完成基础设计、打印与使用（维护者反馈）。`drawer-front` 是实际抽拉与容纳物品的完整抽屉，`drawer-box` 是容纳抽屉的外层壳体，并实现堆叠。抽屉内腔约为宽 270 × 深 260 × 高 134 mm。

| 文件入口 | 用途 |
| --- | --- |
| [drawer-assembly.SLDASM](drawer/drawer-assembly.SLDASM) | 查看整体装配和零件配合 |
| [drawer-front.SLDPRT](drawer/drawer-front.SLDPRT) | 编辑实际抽屉与收纳内腔 |
| [drawer-box.SLDPRT](drawer/drawer-box.SLDPRT) | 编辑外层容纳与堆叠壳体 |
| [drawer-box.STL](drawer/drawer-box.STL)、[drawer-front.STL](drawer/drawer-front.STL) | 导入切片软件，准备试制 |

## 怎么使用

### 查看或修改设计

1. 下载或克隆整个仓库，保留 `drawer/` 内零件与装配体的相对位置。
2. 使用 SolidWorks 打开 `drawer/drawer-assembly.SLDASM` 查看装配；打开对应 `.SLDPRT` 编辑零件。
3. 修改模型后，重新导出对应 STL，再用于切片和打印。

### 3D 打印与验证

将 `drawer/` 中的两个 STL 分别导入切片软件，根据打印机、材料和实际使用需求设置打印参数。打印后检查抽屉滑动、上下及左右间隙，再决定是否调整模型。

STL 是设计导出的快照，修改源模型后需同步导出。具体进度、使用反馈与尺寸变更见 [STATUS.md](STATUS.md)。

### 查看设计参考

[references/](references/README.md) 存放概念模型、预览页、图片和生成脚本：

- [抽屉内部分区](references/drawer-organizer/README.md)：可拆隔板与固定隔舱，共四种构造。浏览器打开 HTML 即可离线切换方案、旋转、俯视和拆分隔板，并查看图片参考。
- [可堆叠抽屉](references/stackable-drawer/README.md)：早期 AI 生成的参考模型与脚本，HTML 概念预览需联网加载库，与 STL 几何不完全一致。

这些资料用于设计参考，具体尺寸和配合在实际建模时确定；各方案的来源、使用方法与限制见对应目录。

## 目录导览

```text
lab-workspace-suite/
├── drawer/                     # 实际开发的抽屉组件：SolidWorks / STL
├── references/                 # 设计参考资料
│   ├── README.md               # 参考索引与命名方式
│   ├── drawer-organizer/       # 抽屉内部分区：离线 HTML / 图片 / 提示词
│   └── stackable-drawer/       # AI 生成的可堆叠抽屉概念方案
├── README.md                   # 项目用途与使用入口
├── STATUS.md                   # 开发进度、验证状态与更新记录
├── AGENTS.md                   # AI 助手维护约定
├── CLAUDE.md                   # Claude Code 维护约定
├── LICENSE
└── .gitignore
```

开发计划、进度与更新记录统一维护在 [STATUS.md](STATUS.md)。
