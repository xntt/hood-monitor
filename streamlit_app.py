import streamlit as st
import requests
import json
import time

# 配置页面
st.set_page_config(
    page_title="Hood链代币监控系统",
    page_icon="🔍",
    layout="centered"
)

# API基础URL
API_BASE = st.session_state.get("api_base", "https://your-app.vercel.app")

# 标题
st.title("🔍 Hood链代币监控系统")

# 侧边栏
st.sidebar.title("控制面板")

# 获取状态
def get_status():
    try:
        response = requests.get(f"{API_BASE}/status")
        return response.json()
    except:
        return {"is_running": False, "monitored_tokens": 0}

# 启动监控
def start_monitor():
    try:
        response = requests.get(f"{API_BASE}/start")
        return response.json()
    except:
        return {"status": "error", "message": "请求失败"}

# 停止监控
def stop_monitor():
    try:
        response = requests.get(f"{API_BASE}/stop")
        return response.json()
    except:
        return {"status": "error", "message": "请求失败"}

# 显示状态
status = get_status()
status_container = st.container()

with status_container:
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("监控状态", "运行中" if status["is_running"] else "已停止")
    
    with col2:
        st.metric("监控中的代币", status["monitored_tokens"])

# 控制按钮
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("启动监控", disabled=status["is_running"]):
        result = start_monitor()
        if result["status"] == "success":
            st.success("监控已启动")
            time.sleep(1)
            st.rerun()
        else:
            st.error(f"启动失败: {result.get('message', '未知错误')}")

with col2:
    if st.button("停止监控", disabled=not status["is_running"]):
        result = stop_monitor()
        if result["status"] == "success":
            st.success("监控已停止")
            time.sleep(1)
            st.rerun()
        else:
            st.error(f"停止失败: {result.get('message', '未知错误')}")

with col3:
    if st.button("刷新状态"):
        st.rerun()

# 监控中的代币列表
st.header("监控中的代币")

if status["monitored_tokens"] > 0:
    # 这里应该添加获取监控代币列表的API
    st.info("监控中的代币列表功能正在开发中")
else:
    st.info("当前没有监控中的代币")

# 设置API地址
st.sidebar.subheader("设置")
api_base = st.sidebar.text_input("API地址", value=API_BASE)
if api_base != API_BASE:
    st.session_state.api_base = api_base
    st.rerun()

# 关于
st.sidebar.subheader("关于")
st.sidebar.info("这是一个Hood链代币监控系统，用于监控热门代币的第二波行情。")
