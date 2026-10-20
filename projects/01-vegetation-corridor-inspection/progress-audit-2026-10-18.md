# 实际工程核查 — 2026-10-18

> 历史快照：本文仅记录2026-10-18初次核查，已被后续用户操作和当前 PROJECT_HANDOFF.md / README 取代。本文提及的未执行 build_scene.py 已在收尾移除，不是最终成果生成脚本。

## GitHub

本地 origin 已配置为 https://github.com/JiagengMi/gis-portfolio.git。
联网读取远程 HEAD 成功：a3846a30e9556c1d5a20ee3c6cfcc018191d7513，与本地 main 一致。
本轮未提交或推送；未将工作 GDB、缓存或私人资料上传。

## 环境和实际文件

- ArcGIS Pro 安装于 D:/ARCGISPRO，版本 3.3。
- 用户完成登录；沙箱外 ArcPy 确认 3D Analyst Available。
- 当前学校账号包含 publishFeatures、publishScenes、shareToPublic 权限。
- 实际 APRX：arcgis/vegetation-corridor-inspection/vegetation-corridor-inspection.aprx。
- 工作 GDB：同目录 vegetation-corridor-inspection.gdb，整目录复制已包含数据。
- ArcPy 确认保存工程内列出的图层均无断链。
- 保存的 Scene 为 Local Scene，但坐标系仍为 EPSG:3857，仅含默认底图，并保留 WorldElevation3D/Terrain3D 真实地形引用；尚未配置植被建模场景。

## 要素与字段

| 数据 | 实际数量 | 已核实情况 |
|---|---:|---|
| corridors | 17 | 存在 |
| inspection_zones | 17 | 存在；数量相同不能证明 Append 的几何和参数完全正确 |
| vegetation_canopy | 241 | veg_id 全部唯一；二维面；EPSG:3776 |
| poles | 75 | pole_id 全部唯一；地面 1000；挂点相对高 12 |
| spans | 73 | span_id 全部唯一；二维线；sag=1，sample_step=0.5 |
| vegetation_observations | 0 | 尚无巡检记录 |
| vegetation_3d / conductors_3d | 不存在 | 尚未生成 |

全部 241 个树冠已存在 crown_base_z 和 crown_depth_m；逐记录公式检查异常数为 0。
树高范围 6–15 m，冠底绝对高程最低 1002 m，冠顶最高 1015 m。
不要重新随机赋值。

杆高字段实际叫 pole_z_m，全部值为 14；结合交接应解释为模拟离地杆高，不应误当成绝对 Z=14。

## 跨段端点检查

直接读取原始跨段几何两端，与全部 75 杆进行 0.1 m 半径候选检查。
现有非空端点杆号全部与唯一候选一致。73 跨没有发现重复杆对。
15 跨缺 from_pole_id，其中以下 14 跨有唯一候选，可在派生副本回填：

| 跨段 | 起点杆 |
|---|---|
| S-063 | P-053 |
| S-064 | P-054 |
| S-065 | P-040 |
| S-066 | P-041 |
| S-067 | P-042 |
| S-068 | P-043 |
| S-069 | P-044 |
| S-070 | P-045 |
| S-072 | P-043 |
| S-073 | P-047 |
| S-074 | P-048 |
| S-075 | P-049 |
| S-076 | P-050 |
| S-077 | P-051 |

S-062 起点在 0.1 m 内无匹配；最近 P-040 距离 0.212060109 m，第二近杆约 62.49 m。
计划仅在派生副本将其起点捕捉至 P-040 并记录偏差；本轮尚未修改。

## 本轮执行状态

scripts/build_scene.py 已准备，目标为独立 arcgis/web-mvp 输出，不覆盖源 APRX/GDB。
运行脚本所需的沙箱外许可请求被用户拒绝，脚本未执行。
只能声明已做语法检查；Multipatch 转换、闭合性、Z 校验和三维导线验证均尚未执行。
未发布 ArcGIS Online 图层或 Web Scene，尚无演示 URL。

下一步：获准运行本地派生建模后，核验输出；再发布场景及依赖并验证匿名访问。
净距尚未计算，任何先行 Web 演示必须明确分析状态 Unknown，不能展示未经计算的风险等级。
