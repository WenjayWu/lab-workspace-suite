# 可堆叠抽屉概念参考

这组 AI 生成的测试资料用于探索抽屉的堆叠结构、外观和程序化建模方法。仅作设计参考，不作为后续实际生产方案。

## 来源与状态

- 来源：据项目维护者回忆为 DeepSeek 生成，未核实；文件名暂使用 `deepseek`，找到原始记录后可修正。
- 原始生成日期、具体模型版本、对话记录及提示词：未记录。
- 当前状态：参考归档，未完成打印、尺寸或配合验证。
- 2026-10-02：从根目录 `stackable-drawer/` 迁入本目录，统一命名；模型几何未修改。

## 文件入口

| 文件 | 用途 |
| --- | --- |
| [drawer-box-deepseek.STL](drawer-box-deepseek.STL) | 抽屉盒与堆叠结构的网格参考 |
| [drawer-panel-deepseek.STL](drawer-panel-deepseek.STL) | 前面板与拉手的网格参考 |
| [stackable-drawer-assembly-deepseek.STL](stackable-drawer-assembly-deepseek.STL) | 抽屉盒与面板组合的装配参考 |
| [stackable-drawer-preview-deepseek.html](stackable-drawer-preview-deepseek.html) | 交互式概念预览，支持旋转、缩放、分解及 1–3 层堆叠 |
| [stackable-drawer-generator-deepseek.py](stackable-drawer-generator-deepseek.py) | 用纯 Python 生成三个 ASCII STL，尺寸参数可编辑 |

## 怎么查看与试验

- **查看概念**：用浏览器打开 HTML。页面从外部 CDN 加载 Three.js 和 OrbitControls，需要联网；它独立绘制模型，不读取本目录的 STL。
- **查看网格**：用支持 STL 的模型查看器或切片软件打开参考模型，长度数值按毫米使用。
- **试验生成脚本**：先将本目录复制到单独的试验目录，再修改脚本参数。在试验目录中执行：

  ```shell
  python stackable-drawer-generator-deepseek.py
  ```

  脚本无需第三方 Python 依赖，将在脚本所在目录写入三个同名 STL，覆盖该目录中已有的同名文件。

## 已知限制

预览页与生成脚本分别维护几何，部分位置定义不同，画面不能作为 STL 几何或配合正确的证据。脚本参数、控制台提示和预览页的尺寸文字也未完全统一。

本次整理保留原有参考几何。若后续用于实际设计，需要重新核对尺寸、实体连接与堆叠配合，并通过打印试验验证。
