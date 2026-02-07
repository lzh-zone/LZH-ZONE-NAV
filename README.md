# LZH-ZONE 💎

> 一个高颜值、现代化的个人导航站 (A Premium Personal Navigation System)

**LZH-ZONE** 是基于 WebStackPage 二次开发的高端导航主题。我们移除了传统的 Bootstrap 风格，采用现代化的 **Glassmorphism (拟态玻璃)** 设计语言，配合丝滑的动画效果，为你打造极致的视觉体验。

## ✨ 特性 (Features)

- **🎨 极致UI**: 
  - 全局拟态玻璃效果 (Glassmorphism)
  - 动态径向渐变背景 (Dynamic Radial Gradients)
  - 霓虹光感侧边栏 (Neon Glow Sidebar)
  - 交互式卡片光效 (Card Shine Effects)

- **🚀 现代技术栈**:
  - 纯 HTML5 + CSS3 + Vanilla JS
  - **零依赖**: 移除了 jQuery, Bootstrap 等重型库
  - 响应式设计: 完美适配移动端和桌面端

- **🔄 动态数据**:
  - 支持从 API 动态获取导航数据 (当前集成 `nav.eooce.com`)
  - 自动适配 FontAwesome 图标
  - 支持高清 Logo 显示

## 🛠️ 使用方法 (Usage)

1. **Clone 项目**
   ```bash
   git clone https://github.com/lzh-zone/WebStackPage.github.io.git
   ```

2. **本地预览**
   直接打开 `cn/index.html` 即可浏览。

3. **自定义数据**
   - 修改 `cn/index.html` 中的 HTML 结构即可添加/删除链接。
   - 或者修改 `cn/generate_index.py` 脚本对接你自己的 API。

## 📂 目录结构

```
.
├── assets/
│   ├── css/
│   │   └── lzh-modern.css  # 核心样式文件
│   ├── js/
│   │   └── lzh-main.js     # 核心逻辑文件
│   └── images/             # 图片资源
├── cn/
│   └── index.html          # 中文主页
├── en/
│   └── index.html          # 英文主页 (English Version)
└── about.html              # 关于页面
```

## 🤝 致谢 (Credits)

本项目基于 [WebStackPage](https://github.com/WebStackPage/WebStackPage.github.io) 开源项目进行现代化重构。

---
**LZH-ZONE** - Designed for visual excellence.
