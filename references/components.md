# 组件与动效

核验日期：2026-10-11。技术栈指查到的材料；能否直接加入项目须检查具体条目和当前依赖。代码许可不自动覆盖演示图片、第三方素材和 Pro 产品。

## 21st — 21st.dev

- **材料与适用**：社区 React 组件、营销区块、模板和 shadcn 主题，条目提供提示与代码；适合找具体成品区块、多种同类实现或代理内检索。
- **入口与访问**：[官网](https://21st.dev/)按 Hero、Pricing、Buttons、Cards、Navigation 等类别找实际条目；[CLI/MCP](https://21st.dev/mcp)提供官方接入。[套餐](https://21st.dev/plans)区分免费浏览、复制额度与 MCP/CLI 能力，免费浏览不代表无限复制或无 key 集成。
- **技术与授权**：主要是 React/Tailwind、shadcn 风格。[条款](https://mcp.21st.dev/terms)与条目源仓库决定代码许可，演示图、视频和预览素材另有范围；保留原仓库、License 和版权信息。
- **核验**：官网、套餐、MCP 和官方许可说明已读取；未安装集成或下载组件。

## kinetics — Kinetics

- **材料与适用**：可调 stiffness/damping 的局部动效，提供 CSS、React 和 AI 提示，适合展开、反馈、弹性动作和效果参考。
- **入口与使用**：[图库](https://kinetics.colorion.co/)搜索目标动作、查看 demo，再选 CSS/React/Prompt。官网说明无需额外动画库，实际依赖按所选代码确认。
- **差异与授权**：CSS 示例可能用缓动近似弹簧，不能把所有 CSS 片段视为可中断的物理积分。公开页脚明确 CSS + React 代码为 MIT。
- **核验**：示例、代码/提示控件和许可声明已读取；未实测全部动效。图库不承担完整产品布局或控件语义。

## shadcn — shadcn/ui

- **材料与适用**：基础 UI 源码、Blocks 和图表，适合表单、对话框、导航、后台及自己的组件库。
- **入口与查找**：[组件](https://ui.shadcn.com/docs/components)、[安装](https://ui.shadcn.com/docs/installation)与 [源码](https://github.com/shadcn-ui/ui)；从具体组件的 CLI/手工安装及 API 文档继续。
- **技术与使用**：React/Tailwind，代码进入项目后由项目维护。查看现有 `components.json`、主题与 primitives；当前生态包含 Base UI/Radix 等路径，不默认旧教程的单一实现。
- **授权与核验**：仓库确认 MIT，第三方素材另查。官网、安装页和仓库已读取；组件的语义/键盘行为修改后仍要验证。

## aceternity — Aceternity UI

- **材料与适用**：动态 Hero、背景、Bento、卡片和滚动展示，偏营销页与视觉表现。
- **入口与访问**：[组件目录](https://ui.aceternity.com/components)区分效果、营销区块与模板；选中条目查看 Preview/Code、CLI/Manual 和依赖。免费组件与 All-Access/Pro 分开。
- **技术与授权**：[官网](https://ui.aceternity.com/)明确 React、Tailwind、Motion；[Licence](https://ui.aceternity.com/licence)规定最终产品用途、再分发和团队权益，条目内第三方组件许可单独适用。本次没有确认全部免费条目均为 MIT。
- **核验**：官网、组件目录和官方许可说明已读取；性能取决于选中条目与实际页面，营销宣传不是实测结果。

## magic-ui — Magic UI

- **材料与适用**：动画组件与视觉效果，适合产品官网、功能展示、数字、文字、边框与背景。
- **入口与技术**：[组件目录](https://magicui.design/docs/components)、[官网](https://magicui.design/)；React、TypeScript、Tailwind、Motion，官网说明可与 shadcn/ui 配合，依赖逐条确认。
- **访问与授权**：[仓库](https://github.com/magicuidesign/magicui)明确开源代码 MIT；[Pro](https://pro.magicui.design/)模板/Blocks 与第三方示例图片另查。
- **核验**：官网、目录与仓库已读取，未把全部效果加入项目或测试性能。

## motion-primitives — Motion Primitives

- **材料与适用**：文本/数字变化、展开、对话框、面板转场、In View 和工具栏，适合产品状态变化中的局部交互。
- **入口与查找**：[文档](https://motion-primitives.com/docs)、[Text Effect](https://motion-primitives.com/docs/text-effect)提供 Preview/Code、CLI/Manual、props 与 preset。
- **技术与授权**：[安装](https://motion-primitives.com/docs/installation)要求 Motion、Tailwind 和 class 合并工具，部分示例用 Lucide；[仓库](https://github.com/ibelick/motion-primitives)确认 MIT。Advanced/Pro 单独判断。
- **核验**：主页和 Text Effect 通过 Chrome 读取，安装页搜索结果与仓库已读取；403 抓取限制没有阻断实际浏览。触发、退出和卸载行为仍按项目验证。

## uiverse — Uiverse

- **材料与适用**：社区按钮、卡片、输入框、开关、工具提示、加载器等，适合具体控件外观或 hover/focus 方案。
- **入口与技术**：[官网](https://uiverse.io/)按控件、样式、CSS/Tailwind 类型搜索，打开条目看实际 HTML/CSS；React/Vue/Svelte 可转换格式，原生移动框架采用其视觉参考。
- **授权与核验**：官网声明 UI 元素 MIT，分类与许可已读取。选中片段的语义、键盘状态和移动布局需验证，不以社区收录代替这些检查。

## uiable — UIAble

- **材料与适用**：shadcn 风格基础控件、成品区块、模板和后台，适合较完整的 React 产品界面。
- **入口与技术**：[官网](https://uiable.com/)按 Components/Blocks/Templates/Dashboards 查找；明确 Base UI、TypeScript、Next.js/React、Tailwind、Motion 和 Figma 资源。已有项目采用其他 primitives 时确认 API 适配。
- **访问与授权**：[套餐](https://uiable.com/pricing)和 [License](https://uiable.com/legal/license)区分免费 MIT、Pro Standard、Enterprise。Standard 不允许在用户付费访问的软件/SaaS 最终产品中使用 Pro；该用途需要对应 Enterprise 权益。Pro 均限制独立组件/模板再分发。
- **核验**：官网、套餐与许可已读取。回看当前价格及具体条目，不把一次性购买视作所有用途的统一许可。

## mapcn — mapcn

- **材料与适用**：地图、控制器、标记、Popup、路线、弧线、GeoJSON 和聚类，适合物流、门店、位置展示及地理可视化。
- **入口与技术**：[文档](https://www.mapcn.dev/docs)、[安装](https://www.mapcn.dev/docs/installation)，按 Map/Markers/Routes 等能力继续；React + MapLibre GL + Tailwind，采用 shadcn 风格的可组合源码。
- **使用边界**：地图组件不提供地理编码、导航算路或位置数据服务，需另有数据来源。
- **授权与核验**：[仓库](https://github.com/AnmolSaini16/mapcn)明确代码 MIT，并说明默认 CARTO 底图商用需 Enterprise 授权，非商用需满足 grantee 条款。可换 MapLibre 兼容底图，但仍需满足对应服务条款/署名条件。官网、文档、安装页、仓库已读取；文档的“无需 API key/免费默认底图”不能替代商用条款。

## microkit — MicroKit UI

- **材料与适用**：按钮反馈、导航切换、数字输入、hover 工具栏和 focus 微交互，适合已有界面的一处动作。
- **入口与技术**：[图库](https://microkit.co/)按触发/分类筛选；[Focus Field](https://microkit.co/components/focus-input)有预览与 registry 入口。可选 TypeScript/JavaScript、CSS/Tailwind；CSS 动效也可能有 React 外壳，部分条目依赖 `lucide-react`。
- **授权与核验**：官网 FAQ 与 [仓库](https://github.com/henriquegpb/microkit)说明代码 MIT，部分交互由公开示例改写，保留适用来源。官网、Focus Field 和仓库入口已读取，未安装全量组件包。

## liquid-glass — Liquid Glass

- **材料与适用**：具有真实像素折射的 React `Glass` 透镜，包含 notification、switch、slider、context menu、video 等示例。
- **入口与技术**：[Playground](https://glass.samasante.com/?view=playground)调效果，[Docs](https://glass.samasante.com/?view=docs)看 props，[Examples](https://glass.samasante.com/?view=examples)选控件。文档要求 React 18+，包名 `@samasante/liquid-glass`；DOM 用像素副本/SVG 位移，video/canvas 用 WebGL。
- **授权与验证**：文档标注示例 MIT，实际包版本按 [源码](https://github.com/samasante/liquid-glass)核验。浏览器、内容更新和性能要在实际页面测试，不把“所有浏览器”的标题当作项目实测。
- **核验**：通过 Chrome 读取动态 Docs 的依赖、props、原理及示例许可；未安装包或跨浏览器实测。

## animejs — Anime.js

- **材料与适用**：框架无关 JavaScript 动画引擎，处理时间线、错峰、SVG 路径/描边/形变、滚动同步和拖拽，适合现成 CSS/组件无法表达的动作。
- **入口与技术**：[官网](https://animejs.com/)、[文档](https://animejs.com/documentation/)按 Animation/Timeline/Scope/Scroll/SVG/WAAPI 等模块查找。在 React/Vue/Svelte 中管理作用域和卸载清理。
- **版本与授权**：官网当前示例用 `animate`、`createTimeline` 等 API，不把旧主版本的默认导入/参数混进当前实现；以项目锁定版本文档为准。[仓库](https://github.com/juliangarnier/anime)确认 MIT。
- **核验**：官网功能/示例和仓库许可已读取，未安装或升级。简单 hover、渐隐或 loader 可先看 CSS/SVG；复杂编排再选引擎。
