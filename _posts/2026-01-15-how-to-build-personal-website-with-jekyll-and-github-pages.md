---
layout: post
title: "如何使用 Jekyll + GitHub Pages 搭建个人网站"
date: 2026-01-15 10:00:00 +0800
categories: 技术
tags: jekyll github-pages 博客
---

## 什么是 Jekyll 和 GitHub Pages？

Jekyll 是一个静态网站生成器，它可以将 Markdown 文件转换为静态 HTML 网站。GitHub Pages 是 GitHub 提供的静态网站托管服务，它可以免费托管你的 Jekyll 网站。

## 为什么选择 Jekyll + GitHub Pages？

1. **免费**：GitHub Pages 是完全免费的，包括域名（yourusername.github.io）
2. **简单易用**：不需要服务器配置，只需要推送代码到 GitHub 即可
3. **静态网站**：加载速度快，安全性高
4. **支持 Markdown**：方便写作和维护
5. **丰富的主题**：有很多免费的 Jekyll 主题可供选择
6. **版本控制**：使用 Git 进行版本控制，方便管理和回溯

## 搭建步骤

### 1. 创建 GitHub 仓库

首先，你需要在 GitHub 上创建一个新的仓库，仓库名称必须为 `yourusername.github.io`，其中 `yourusername` 是你的 GitHub 用户名。

### 2. 安装 Jekyll（可选，用于本地开发）

如果你想在本地预览网站效果，可以安装 Jekyll：

```bash
# 安装 Ruby（如果没有安装的话）
# Windows 用户可以从 https://rubyinstaller.org/ 下载安装

# 安装 Jekyll 和 Bundler
gem install jekyll bundler

# 检查 Jekyll 版本
jekyll -v
```

### 3. 创建 Jekyll 网站

```bash
# 在当前目录初始化 Jekyll 网站
jekyll new . --force

# 或者创建一个新目录
jekyll new myblog
cd myblog
```

### 4. 配置 Jekyll

编辑 `_config.yml` 文件，配置网站的基本信息：

```yaml
title: 我的个人博客
description: 这是我的个人博客网站
baseurl: ""
url: "https://yourusername.github.io"
theme: minima
plugins:
  - jekyll-feed
  - jekyll-seo-tag
```

### 5. 编写内容

- 创建博客文章：在 `_posts` 目录下创建以 `YYYY-MM-DD-title.md` 格式命名的文件
- 创建页面：在根目录下创建 `about.md`、`contact.md` 等页面

### 6. 本地预览（可选）

```bash
# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 在浏览器中访问 http://localhost:4000
```

### 7. 推送到 GitHub

```bash
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit"

# 添加远程仓库
git remote add origin https://github.com/yourusername/yourusername.github.io.git

# 推送到 GitHub
git push -u origin main
```

### 8. 访问网站

等待几分钟后，你就可以通过 `https://yourusername.github.io` 访问你的网站了。

## 常用命令

```bash
# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 构建网站
bundle exec jekyll build

# 清理构建文件
bundle exec jekyll clean
```

## 主题选择

Jekyll 有很多免费的主题可供选择，你可以从以下网站找到：

- [Jekyll Themes](https://jekyllthemes.io/)
- [GitHub Pages Themes](https://pages.github.com/themes/)
- [jekyllthemes.org](http://jekyllthemes.org/)

## 自定义配置

### 添加导航菜单

在 `_config.yml` 中添加：

```yaml
header_pages:
  - about.md
  - contact.md
```

### 添加作者信息

```yaml
author:
  name: "你的名字"
  email: "your.email@example.com"
  github: "yourusername"
```

### 配置分页

```yaml
paginate: 5
paginate_path: "/page:num/"
```

## 常见问题

### 1. 网站不更新

- 检查 GitHub Actions 是否成功运行
- 清除浏览器缓存
- 等待几分钟，GitHub Pages 可能需要时间来构建

### 2. 本地预览和 GitHub Pages 显示不一致

- 确保使用的是相同版本的 Jekyll 和主题
- 检查 `_config.yml` 中的配置是否正确

### 3. 域名设置

如果你想使用自定义域名，可以在 GitHub 仓库的 Settings 中设置，然后在你的域名提供商处添加 DNS 记录。

## 总结

使用 Jekyll + GitHub Pages 搭建个人网站是一个简单、免费且高效的选择。你只需要专注于写作内容，剩下的交给 Jekyll 和 GitHub Pages 处理。

希望这篇文章对你有所帮助！如果你有任何问题，欢迎在评论区留言。

## 参考资料

- [Jekyll 官方文档](https://jekyllrb.com/docs/)
- [GitHub Pages 官方文档](https://docs.github.com/en/pages)
- [Jekyll Themes](https://jekyllthemes.io/)
