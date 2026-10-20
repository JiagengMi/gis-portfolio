# 三维植被净距项目交接

更新：2026-10-20。当前状态：**核心三维建模、净距分析、模拟分类及公开 Web MVP 已完成**。本交接替代 2026-10-18 的接续记录；旧现场审计只反映当时状态。

## 协作方式与约束

- 用户在 ArcGIS Pro / Online 中操作；助手按步骤指导，代码由用户在 Pro Python 窗口运行。不要自行批量操作或发布 ArcGIS。
- 文档收尾已授权直接处理本仓库。用户明确要求：**不用备份 arcgis 文件夹**。本轮不读取/修改/复制该文件夹，整个目录已加入 Git 忽略。
- 发布内容全部英文；操作说明中文，附英文工具名，按截图定位，不猜按钮。
- 不把 career-ops、简历原文件、个人资料、凭据加入此公开库。

## 链接

- GitHub：https://github.com/JiagengMi/gis-portfolio
- 应用：https://experience.arcgis.com/experience/af7532559e924046aec35b94c8e090f1/
- Web Scene：https://www.arcgis.com/home/item.html?id=ec1b41378db342698ce06f8b229e1836
- 应用名称：Vegetation Clearance Explorer。

保留现有应用和场景 ID。新版发布为新图层后添加到原场景，保存原场景；静态应用文字另行更新并重新发布。

## 已完成与证据

- 241 个树冠，封闭 Multipatch；73 跨导线。ArcPy 输出、属性表与发布画面由用户截图确认。
- 树冠来源：影像手工描绘；树高和线路参数为模拟。Calgary Public Trees 618 点仅为原始样本/准备背景，不能说241冠体来自该点数据的一一重建。
- Near 3D + Inside 3D：进入/完全位于冠体内的线使最终净距为0；保留原始 NEAR_DIST3。
- 21条内部关系涉及16个不同冠体；最终零净距52个。
- 0.5m与0.25m采样：最大距离差0.000134m，均值约0.000021m；内部冠体集合、零距离集合相同；模拟分类变化0。不代表真实精度达到毫米级。
- High 67（d<2）、Medium 62（2≤d<4）、Low 112（d≥4）、Unknown 0；合计241，52零距离包含在High内。
- 公开应用初版无痕验证通过。收尾时已独立匿名REST确认新版应用/场景public、说明/条款存在，最终可见冠体241、导线73，分类67/62/112和零距离52，导线采样min=max=0.25，两层显示偏移−1000，旧层隐藏；导线匿名权限为Query。见results/public-release-audit.json。未做完整浏览器/移动端视觉或所有依赖编辑权限审计。

## 工作数据和高程

- 工作路径：C:/Users/mijia/Documents/Codex/gis-portfolio。
- Pro 3.3，程序在 D:/ARCGISPRO；D盘来自旧笔记本，主机应用安装列表没有Pro。用户决定不重装/不再折腾语言。
- XY：EPSG:3776（也可能102187），米。发布Scene：EPSG:3857。
- 地面1000m；树高6/9/12/15m、冠底2/3/4m；挂点12m、弧垂1m。不是实际垂直基准。
- 网页展示：Light Gray Canvas，无真实Terrain高程源；两层绝对高度，在线偏移−1000m。Pro冠体带制图偏移发布报00236；发布偏移归0，在Scene Viewer里另设−1000。

## 实际数据集

- vegetation_canopy：二维输入，ground_z_m、tree_h_m、crown_base_m、crown_base_z、crown_depth_m。
- poles：75点；pole_id、ground_z_m、attach_h_m。杆高实际字段pole_z_m=14，语义是离地杆高。
- spans：73条二维两端点线；span_id、from_pole_id、to_pole_id、sag_m、sample_step_m。不是非空间表。
- vegetation_3d_closed：封闭结果，OID_ORIG连封闭前的vegetation_3d_v2 OBJECTID恢复属性，Z上下界重新算。
- conductors_3d：原0.5m；conductors_3d_025m：最终0.25m。两端和跨中校验通过，细版另验证间距。
- vegetation_clearance：粗版分析；vegetation_clearance_025m：最终分析，含risk_class。
- conductor_canopy_inside_025m：细版关系表；Target_ID=导线OBJECTID，Contain_ID=冠体副本OBJECTID。粗版表曾因名字/保存位置不同查找失败，现场核对来源，不凭名称猜。
- clearance_m、nearest_span_id、inside_span_ids、inside_count、distance_method。内部关系多跨同距0时按span_id排序取代表，保留全列表。
- clearance_risk_counts：分类频数。

## 方法验证与踩坑

- 10m封闭立方体：侧距3、上距5、斜距sqrt34、穿过0，Near3D均符合；完全内部线Near3D返回4而实际净距应0。Inside3D识别OBJECTID4为Partially Inside，5为Inside，因此不能只用Near3D。
- 视觉有顶面不等于封闭。原拉伸转换全No，Enclose后Yes；该工具会重建几何且不保留业务字段。
- 跨段S-062在0.1m匹配检查失败，用户用Edit Vertices修正起终点后全73跨通过。不要重新编号或重算随机高度。
- Edit Vertices选中线后还要点修改窗格下方的Edit Vertices才能进入顶点编辑。
- Add Z Information在3D Analyst → 统计，不在3D要素。
- 发布遇到00230投影差异，场景改3857；00374启用各Map/Scene独立的数字图层ID；00241显示字段改span_id；Scene三维线单独发布灰色时改到Map发布成功。
- Missing root node先查缓存生成状态，用户之后添加成功；不要直接重发/删层。

## 收尾与后续

README、实际数据模型、来源、验证、复现步骤、英文简历条目为本轮收尾内容。早期未执行的build_scene.py已移除，避免被当成已验证生产脚本。归档脚本是从对话已运行算法整理的版本，须注明未在本轮对GDB复跑。

无需等待新功能即可投简历。可描述三维净距分析、模拟分类、采样敏感性验证和Web发布；不能声称规范合规、真实电力项目、LiDAR重建、Field Maps巡检闭环或Dashboard完成。

可选后续：更全面边界/退化几何测试、最近跨段并列关系、移动端/无障碍验证、巡检与QC。先维持现有公开链接。
