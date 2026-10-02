# 图片生成提示词与来源记录

- 日期：2026-10-02。
- 工具：OpenAI 内置 image_gen；没有使用外部 CLI。
- 用途：用于观察外形和构造的概念参考，具体尺寸、间隙与配合由实际建模确定。
- 内腔比例：宽 270 × 深 260 × 高 134 mm，来自项目维护者测量。
- 本文保存实际提交给生成工具的两组提示词。图片中的槽口、交汇及圆角可能偏离 HTML 示意，应分别核对。

## 可拆隔板：A / B

```text
Use case: product-mockup
Asset type: drawer partition design reference board for a mechanical design project.
Primary request: Create a clear landscape 3D industrial design reference board with two side-by-side concepts A and B for the INSIDE of an actual pull-out storage drawer. Cavity approximate width 270 mm, front-to-back depth 260 mm, inner height 134 mm: almost square footprint, noticeably deep. Focus on construction ideas, not dimensional precision.
Scene/backdrop: warm light neutral studio background, no decorative objects.
Subject A, left half: sage green removable half-lap divider grid inside a pale gray open-top drawer body. Exactly TWO longitudinal and TWO transverse dividers form a 3-by-3 grid of NINE compartments. Dividers about half the cavity height. One main assembled isometric view, plus a smaller exploded view below showing the two longitudinal plates and two transverse plates above the empty drawer. Show complementary half-height slots: longitudinal plates slots from TOP halfway down, transverse plates slots from BOTTOM halfway up.
Subject B, right half: same drawer shell, one sage green longitudinal divider positioned about 36% of the width from the left, leaving a FULL-LENGTH uninterrupted LEFT channel; two short transverse dividers divide ONLY the remaining right-hand area into THREE compartments. Main assembled isometric view plus a smaller exploded view. A small close-up can show a short divider's stepped end engaging a top-entry notch in the long main divider. Do not imply tested or dimensionally exact locking.
Style/medium: clean realistic matte 3D printed product concept render with subtle fine layer texture, crisp readable edges and soft shadows. Drawer front is at the bottom of the image. Main drawer views use a cutaway low front wall and low right outer wall to reveal internal structure, full rear and left walls.
Composition/framing: landscape 3:2, editorial reference sheet, two equally sized columns, comfortable margins. Make the full assembled views prominent and the construction details large enough to understand.
Text (verbatim): only simple labels "A" and "B", no other text.
Constraints: all partitions are INSIDE the drawable storage drawer, not inside an external cabinet sleeve. No items, no separate storage bins, no tools, no cabinet housing, no dimensions, no logos, no watermarks. Keep geometry simple and visually consistent between assembled and exploded views.
```

## 固定隔舱：C / D

```text
Use case: product-mockup
Asset type: drawer partition design reference board for a mechanical design project.
Primary request: Create a clear landscape 3D industrial design reference board comparing two fixed integral divider concepts C and D for the INSIDE of an actual pull-out storage drawer. Cavity approximate width 270 mm, front-to-back depth 260 mm, inner height 134 mm: almost square footprint, noticeably deep. Focus on shape and construction ideas, not dimensional precision.
Scene/backdrop: warm light neutral studio background, no decorative objects.
Subject C, left half: a matte pale gray open-top drawer body with warm ochre integral internal walls about half its cavity height. EXACTLY ONE longitudinal main wall positioned 40% of cavity width from the left. On the left of main wall, ONE transverse wall positioned about 65% of the depth creates one large front compartment and one smaller rear compartment. On the right, TWO transverse walls at about one-third and two-thirds of depth create THREE compartments. Total FIVE compartments. All dividers have SAME height and are integrated directly into the continuous drawer floor. Use subtle filleted wall-to-floor connections, no separate insert trays.
Subject D, right half: identical FIVE-compartment footprint as C. Main longitudinal wall higher, approximately three-quarters of the cavity height. LEFT transverse wall LOW, approximately one-third of cavity height. The FRONT transverse wall on the right LOW; the REAR transverse wall on the right MEDIUM, approximately half of cavity height. The variation should be clearly visible. Small smooth rounded transitions where low walls meet higher ones, allowing easier finger access. All walls integrated into floor.
Style/medium: clean realistic matte 3D printed product concept render, subtle fine layer texture, crisp edges and soft shadows.
Composition/framing: landscape 3:2, two equal columns. Each concept has a main assembled high-angle isometric view and a smaller top-down view beneath it showing the same compartment plan. Drawer front is at the bottom. Low cutaway front and right outer walls reveal internal structure, full-height rear and left walls. One close-up detail of filleted floor-wall junction, if space allows. Comfortable margins.
Text (verbatim): only simple labels "C" and "D", no other text.
Constraints: all partitions INSIDE the actual storage drawer, not inside an external stacking cabinet sleeve. No exploded or detachable walls: these concepts are one-piece constructions. No stored items, no tools, no separate boxes, no cabinet housing, no dimensions, no logos, no watermark. Maintain five compartments in both concepts.
```
