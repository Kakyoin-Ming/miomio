# app.py
import time
import random
import streamlit as st
from datetime import datetime

# ======================
# 🌌 初始化会话状态
# ======================
if 'wish_count' not in st.session_state:
    st.session_state.wish_count = 0
if 'keep_going' not in st.session_state:
    st.session_state.keep_going = True

# ======================
# ⏳ 核心配置
# ======================
MAX_WISHES = 3
TIME_BASE = datetime(2025, 2, 27, 18, 30)
REAL_START = datetime(2023, 1, 1)

def get_virtual_time():
    return TIME_BASE + (datetime.now() - REAL_START)

# ======================
# 🎇 特效模块
# ======================
def show_exit_animation():
    """退出系统专属特效"""
    # 星尘消散动画
    with st.expander("✨ 正在关闭时空通道...", expanded=True):
        particles = st.empty()
        for i in range(5, 0, -1):
            particle_text = "🌠" * i + "✨" * (5-i)
            particles.markdown(
                f'<div style="font-size:30px; text-align:center">{particle_text}</div>',
                unsafe_allow_html=True
            )
            time.sleep(0.3)

    # 爱心雨特效
    st.markdown("""
    <style>
    @keyframes fall {
        to { transform: translateY(100vh) rotate(360deg); }
    }
    .heart-rain::after {
        content: "❤️";
        position: fixed;
        animation: fall 2s linear infinite;
        left: 5%;
        opacity: 0.8;
    }
    </style>
    <div class="heart-rain"></div>
    """, unsafe_allow_html=True)

    # 最终关闭提示
    time.sleep(2)
    st.success("✅ 时空档案已加密保存")
    st.balloons()

# ======================
# 🌈 愿望处理模块
# ======================
def process_wish(wish):
    """愿望处理动画"""
    with st.spinner('🪐 建立超空间连接...'):
        progress_bar = st.progress(0)
        for percent in range(100):
            time.sleep(0.02)
            progress_bar.progress(percent + 1)
        
    quotes = [
        "🔮 愿望已送达仙女座星云",
        "🌌 愿望已存入黑洞保险库",
        "🪐 正在曲速传输到星际联盟总部...",
        "⌛ 已存入姐姐的专属愿望银行（利息5.21❤%）"
    ]
    st.success(random.choice(quotes))

def show_overload_animation():
    """能量超载动画"""
    particles = ["💫", "🌌", "✨", "⭐"]
    status = st.empty()
    for i in range(3, 0, -1):
        particle_trail = ' '.join(random.choice(particles) for _ in range(5))
        status.markdown(f"⚠️ **能量超载！信道维持剩余 {i}秒**  \n{particle_trail}")
        time.sleep(1)
    st.error("🔒 时空信道已安全关闭")
    st.balloons()

# ======================
# 🎮 主界面模块
# ======================
def show_main_interface():
    """主交互界面"""
    # 界面美化
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(45deg, #0F2027, #203A43, #2C5364);
        color: #FFFFFF;
    }
    .stTextInput input {
        background-color: rgba(255,255,255,0.1) !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🌠 时空许愿机")
    st.caption("输入你的愿望，穿越时空的祝福")

    # 动态时钟
    time_placeholder = st.empty()
    current_time = get_virtual_time().strftime("%m-%d %H:%M:%S")
    time_placeholder.markdown(f"🕰️ **时空历 [{current_time}]**")

    # 许愿输入
    wish = st.text_input("请姐姐在这里许下愿望~：", key=f"wish_{st.session_state.wish_count}")

    if wish:
        process_wish(wish)
        st.session_state.wish_count += 1

        if st.session_state.wish_count >= MAX_WISHES:
            show_overload_animation()
            st.session_state.keep_going = False
        else:
            choice = st.selectbox(
                "✨ 继续许愿？",
                ["继续许愿", "退出系统"],
                index=0
            )
            
            if choice == "退出系统":
                show_exit_animation()
                st.session_state.keep_going = False
                st.stop()
            else:
                st.session_state.keep_going = True

# ======================
# 🚀 程序入口
# ======================
if __name__ == '__main__':
    if st.session_state.keep_going and st.session_state.wish_count < MAX_WISHES:
        show_main_interface()
    else:
        st.markdown("## 🌟 姐姐的愿望已安全保存，要早点回来哦~")
        st.markdown("### 你的专属时空坐标：")
        st.code(f"📍 银河系·猎户座旋臂·星际时间 {get_virtual_time().strftime('%Y-%m-%d %H:%M')}")
        # st.image("https://i.imgur.com/7pYp9XU.gif")  # 星空动图
        
        if st.button("✨ 重启许愿机"):
            st.session_state.clear()
            st.rerun()