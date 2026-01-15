---
layout: post
title: "JRebel 激活方式二备份"
date: 2026-01-15 14:00:00 +0800
categories: 技术
tags: jrebel 激活 备份
---

# JRebel 激活方式二备份

## 方式二（推荐）

### 1. 准备反向代理服务包

#### 1.1 下载最新版本

访问最新 GitHub 仓库地址：

> [https://github.com/yu-xiaoyao/jrebel-license-active-server/releases/tag/v-20251111](https://github.com/yu-xiaoyao/jrebel-license-active-server/releases/tag/v-20251111)

根据你的操作系统选择对应的版本下载：
- Windows 64位：选择 `.exe` 文件
- Windows 32位：选择对应32位版本
- macOS/Linux：选择对应平台的可执行文件

![下载页面]({{ site.baseurl }}/assets/images/2026-01-15-jrebel-activation/download-page.png)

#### 1.2 运行反向代理服务

下载完成后，找到下载的 `exe` 文件（例如 `jrebel-license-active-server.exe`），双击运行：

- 运行后会出现一个命令行窗口
- 窗口中会显示服务运行状态和端口信息
- **重要**：在激活完成之前，请勿关闭此命令行窗口！

![运行代理服务]({{ site.baseurl }}/assets/images/2026-01-15-jrebel-activation/run-proxy-server.png)

### 2. IDEA 激活步骤

#### 2.1 打开 JRebel 激活界面

1. 打开 IntelliJ IDEA
2. 点击顶部菜单栏的 `Help`
3. 在下拉菜单中选择 `JRebel`
4. 点击 `Activation`

![打开激活界面]({{ site.baseurl }}/assets/images/2026-01-15-jrebel-activation/open-activation.png)

#### 2.2 生成 GUID

需要生成一个唯一的 GUID 值用于激活：

1. 访问 GUID 生成网站：[https://www.guidgen.com/](https://www.guidgen.com/)
2. 点击 `Generate GUID` 按钮生成一个新的 GUID
3. 复制生成的 GUID 值（如：`550e8400-e29b-41d4-a716-446655440000`）

![生成GUID]({{ site.baseurl }}/assets/images/2026-01-15-jrebel-activation/generate-guid.png)

#### 2.3 输入激活信息

在激活窗口中输入以下信息：

1. **License server URL**：
   ```
   http://127.0.0.1:8888/你的GUID值
   ```
   例如：`http://127.0.0.1:8888/550e8400-e29b-41d4-a716-446655440000`

2. **E-mail**：输入任意格式正确的邮箱地址
   例如：`test@example.com`

3. 点击 `Activate` 按钮进行激活

![输入激活信息]({{ site.baseurl }}/assets/images/2026-01-15-jrebel-activation/input-activation-info.png)

### 3. 设置离线使用（重要）

JRebel 激活之后默认是联网使用的，在该模式下，JRebel 会一直联网监测激活信息。为了避免后续出现激活问题，建议设置为离线使用模式：

1. 在 IDEA 的 JRebel 设置界面中
2. 找到并点击 `Work offline` 按钮
3. 确认切换到离线模式

![激活成功]({{ site.baseurl }}/assets/images/2026-01-15-jrebel-activation/activation-success.png)


### 4. 关闭代理服务

激活完成并设置为离线模式后，可以关闭之前运行的反向代理服务：

1. 回到运行代理服务的命令行窗口
2. 按 `Ctrl + C` 或关闭窗口即可停止服务

## 注意事项

1. **命令行窗口**：在激活完成之前，请勿关闭运行反向代理服务的命令行窗口

2. **GUID 唯一性**：每个激活实例应该使用唯一的 GUID 值，避免重复使用

3. **离线模式**：强烈建议设置为离线模式，避免联网监测导致的激活失效问题

4. **版本更新**：定期检查 GitHub 仓库，下载最新版本的反向代理服务包

5. **防火墙设置**：如果遇到连接问题，检查防火墙是否允许程序访问网络