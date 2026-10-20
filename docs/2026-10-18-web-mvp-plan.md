# 三维植被 Web MVP 接续计划

> 历史计划，已被实际完成的项目 README 和 implementation-plan.md 取代。下面的未勾选状态不是当前进度；早期 build_scene.py 未执行并已移除。

沿用 PROJECT_HANDOFF.md 已确定的模拟模型和发布优先级，不重新生成随机高度。

- [x] 完整读取交接；核验 origin 和远程 HEAD。
- [x] 只读核查 GDB、APRX 与 ArcGIS Pro 许可。
- [ ] 在独立派生 GDB 和 APRX 中生成三维冠体与导线，保留原始工程。
- [ ] 核验 241 个冠体的 ID、Z 上下界、封闭性，以及 73 跨的端点、弧垂和采样。
- [ ] 对派生跨段回填 14 个唯一匹配起点；S-062 在派生副本中将起点捕捉至 P-040（原偏差 0.212060 m），记录修正。
- [ ] 建立 1000 m 合成参考面，移除场景真实地形依赖。
- [ ] 发布三维 Web Scene 和依赖；匿名验证。尚未计算净距时统一 Unknown，不展示伪造风险类别。
- [ ] 更新 README 和交接，记录发布 URL 与剩余工作。

输入工程：projects/01-vegetation-corridor-inspection/arcgis/vegetation-corridor-inspection/vegetation-corridor-inspection.aprx。
脚本：projects/01-vegetation-corridor-inspection/scripts/build_scene.py。
输出：同级 arcgis/web-mvp/，不覆盖源数据。

验证使用实际 ArcPy 几何、Is Closed 3D、要素计数和逐要素 Z 比对；导线端点必须等于相应杆位挂点。Web 版先提供可旋转场景和基础弹窗；净距分析与 Experience Builder 后续接续，不能提前声称完成。
