import streamlit as st
import random

# --- 1. 页面基础配置 ---
st.set_page_config(page_title="Ultech Master Training", page_icon="📱", layout="wide")

# --- 2. CSS 美化样式 (优化版) ---
st.markdown("""
<style>
    .big-font { font-size:18px !important; font-weight: 500; }
    .success-box { padding: 15px; background-color: #d1e7dd; color: #0f5132; border-radius: 8px; margin-bottom: 10px; border: 1px solid #badbcc;}
    .error-box { padding: 15px; background-color: #f8d7da; color: #842029; border-radius: 8px; margin-bottom: 10px; border: 1px solid #f5c2c7;}
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; font-weight: bold; font-size: 16px;}
    h1 { color: #2c3e50; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 题库 1：普通版 (Standard - 基础 S.O.P)
# ==========================================
STANDARD_QUESTIONS = [
    {
        "question": "SOP: What is the very first step when a customer asks for a phone case?",
        "options": ["Show them the most expensive one", "Confirm the phone model", "Ask for their budget", "Clean the shelf"],
        "answer": "Confirm the phone model",
        "explanation": "Appendix A3: Model Unconfirmed = No Recommendation. This is the first Red Line."
    },
    {
        "question": "Script: If a customer says 'Just looking', you should say:",
        "options": ["Okay", "No rush at all, feel free to have a look", "Buying anything today?", "Please don't touch"],
        "answer": "No rush at all, feel free to have a look",
        "explanation": "Appendix A1: Give them space but stay connected."
    },
    {
        "question": "Intake: What is the 'Golden Rule' for liquid-damaged devices?",
        "options": ["Plug in to test immediately", "Put in rice", "Do NOT plug in power before assessment", "Shake it"],
        "answer": "Do NOT plug in power before assessment",
        "explanation": "Intake SOP: Plugging in liquid-damaged devices can cause short circuits."
    },
    {
        "question": "Warranty: What is the warranty period for a standard screen repair?",
        "options": ["3 months", "12 months (excluding physical/liquid damage)", "Lifetime", "No warranty"],
        "answer": "12 months (excluding physical/liquid damage)",
        "explanation": "Delivery SOP: Screens have a 1-year warranty."
    },
    {
        "question": "Sales: What is the '3-Second Rule'?",
        "options": ["Greet in 3 seconds", "If they stare at an item for 3s, offer to take it out", "Checkout in 3s", "Speak fast"],
        "answer": "If they stare at an item for 3s, offer to take it out",
        "explanation": "Appendix A2: Staring indicates interest. Proactively assist."
    },
    {
        "question": "Intake: For iPhone X/11 repairs involving front cameras, what risk must be disclosed?",
        "options": ["Data loss", "Face ID may fail", "Battery drain", "None"],
        "answer": "Face ID may fail",
        "explanation": "Intake SOP 3.6: Face ID is a structural risk for these models."
    },
    {
        "question": "Difficult Customer: What is the first sentence to an angry customer?",
        "options": ["Calm down", "I'm sorry to see this happened. Let me understand the situation", "It's not my fault", "Please leave"],
        "answer": "I'm sorry to see this happened. Let me understand the situation",
        "explanation": "Difficult Manual: Start with empathy and support."
    },
    {
        "question": "Delivery: What must happen before the customer leaves with the device?",
        "options": ["Payment only", "Demo functions -> Payment -> Sign-off -> Warranty explanation", "Just sign", "High five"],
        "answer": "Demo functions -> Payment -> Sign-off -> Warranty explanation",
        "explanation": "Delivery SOP 7.3: Complete the delivery loop."
    },
    {
        "question": "Privacy: What do we say about the Access PIN?",
        "options": ["We need to see your photos", "We only test functions, not personal data", "We don't need it", "Trust us"],
        "answer": "We only test functions, not personal data",
        "explanation": "Intake SOP 4.2: Reassure data privacy."
    },
    {
        "question": "Intake: Are overseas order deposits refundable?",
        "options": ["Yes, always", "No, they are non-refundable", "Maybe", "Only 50%"],
        "answer": "No, they are non-refundable",
        "explanation": "Intake SOP 5.2: Overseas orders are strict."
    },
    {
        "question": "Sales: If a customer is slow-paced and hesitant, you should:",
        "options": ["Rush them", "Give them information and space (Take your time)", "Push for a sale", "Walk away"],
        "answer": "Give them information and space (Take your time)",
        "explanation": "Sales Manual: Slow customers need confidence, not pressure."
    },
    {
        "question": "Intake: When is a deposit mandatory?",
        "options": ["Always", "Overseas parts / High value / Device not left", "Never", "Cash only"],
        "answer": "Overseas parts / High value / Device not left",
        "explanation": "Intake SOP 5.1: Deposit secures the part."
    },
    {
        "question": "Sales: What is the best selling point for an 'Office Worker'?",
        "options": ["Sparkly", "Heavy duty", "Slim and simple", "Waterproof"],
        "answer": "Slim and simple",
        "explanation": "Appendix A5: Emphasize 'slim and simple' so it doesn't feel bulky."
    }
]

# ==========================================
# 题库 2：进阶版 (Advanced - 场景与话术填空)
# ==========================================
ADVANCED_QUESTIONS = [
    {
        "question": "Scenario: A customer yells at you. You say 'Please calm down'. Why is this WRONG?",
        "options": ["You didn't say it loud enough", "It invalidates their emotion and sounds condescending", "You should have called security immediately", "It is correct"],
        "answer": "It invalidates their emotion and sounds condescending",
        "explanation": "Difficult Manual: Never tell an angry person to calm down. It escalates conflict."
    },
    {
        "question": "Scenario: Customer claims 'Screen quality is bad' because it cracked again in 2 weeks. The BEST technical explanation is:",
        "options": ["You are clumsy", "Glass breaks if you drop it", "Screen damage depends more on impact angle than frequency/quality", "Bad luck"],
        "answer": "Screen damage depends more on impact angle than frequency/quality",
        "explanation": "Difficult Scenario: Use the 'Angle vs Frequency' logic to explain physics without blaming."
    },
    {
        "question": "Scenario: A customer demands a full refund for a repair done 2 months ago. This exceeds your authority. You must:",
        "options": ["Say NO immediately", "Say 'I need manager confirmation' and escalate within 3 minutes", "Give the refund to avoid trouble", "Ignore them"],
        "answer": "Say 'I need manager confirmation' and escalate within 3 minutes",
        "explanation": "Escalation Rules: Requests for full refunds/waivers must go to a manager."
    },
    {
        "question": "Scenario: 'Black Spot' appears on LCD. Customer swears they didn't drop it. You suspect pressure damage. You should:",
        "options": ["Say 'You definitely dropped it'", "Explain that hidden pressure (e.g., keys in bag) can cause internal damage without external cracks", "Refuse warranty immediately", "Laugh"],
        "answer": "Explain that hidden pressure (e.g., keys in bag) can cause internal damage without external cracks",
        "explanation": "Difficult Scenario: Explain the 'How' (pressure) without attacking the 'Who' (customer)."
    },
    {
        "question": "Scenario: You are quoting a logic board repair. You are unsure of the price. You should:",
        "options": ["Guess $100", "Quote a Range (e.g., $200-$300) and state 'Needs Manager Confirmation'", "Say nothing until fixed", "Quote high"],
        "answer": "Quote a Range (e.g., $200-$300) and state 'Needs Manager Confirmation'",
        "explanation": "Intake SOP: Never guess. Use ranges + confirmation for complex jobs."
    },
    {
        "question": "Scenario: Water damage returns. Customer says 'It should be waterproof'. You say:",
        "options": ["You put it in water again", "Resealing is not the same as factory waterproof testing; we can't guarantee 100%", "It is waterproof", "Bad luck"],
        "answer": "Resealing is not the same as factory waterproof testing; we can't guarantee 100%",
        "explanation": "Difficult Scenario: Clarify the difference between Repair Sealing and Factory Sealing."
    },
    {
        "question": "Scenario: Bent frame causes screen lifting. Customer pressed it and made it worse. You say:",
        "options": ["You ruined it", "Frame deformation affects fit. Pressing it concentrates force", "Buy a new phone", "We will fix it for free"],
        "answer": "Frame deformation affects fit. Pressing it concentrates force",
        "explanation": "Difficult Scenario: Explain physics (Frame Fit) rather than blaming actions."
    },
    {
        "question": "Scenario: Customer misheard the quote range ($600-$700) as fixed ($600). You should:",
        "options": ["Demand $700", "Show the notes/record where the range was documented", "Give it for $600", "Call them a liar"],
        "answer": "Show the notes/record where the range was documented",
        "explanation": "Difficult Scenario: Use transparency and records to resolve the misunderstanding."
    },
    {
        "question": "Scenario: Motherboard issue appears after Screen Repair. Customer blames you. You say:",
        "options": ["Correlation is not causation. We will run diagnostics to check the true cause", "Coincidence", "Not our problem", "We broke it"],
        "answer": "Correlation is not causation. We will run diagnostics to check the true cause",
        "explanation": "Difficult Scenario: Don't deny immediately, but use diagnostics to prove the cause."
    },
    {
        "question": "Scenario: A customer is crying in the store. What is your Priority #1?",
        "options": ["Fix the phone", "Emotional Stabilisation", "Check payment", "Ask for a review"],
        "answer": "Emotional Stabilisation",
        "explanation": "Emotional Handling: Stabilize the person before fixing the device."
    },
    {
        "question": "ORDERING: What is the correct 6-step sequence for handling a 'Budget-Conscious' dispute?",
        "options": ["Explain -> Quote -> Listen", "Listen -> Empathy -> Remove Fear -> Reframe Loss -> Explain -> Loyalty Solution", "Manager -> Police -> Ban", "Empathy -> Explain -> Listen"],
        "answer": "Listen -> Empathy -> Remove Fear -> Reframe Loss -> Explain -> Loyalty Solution",
        "explanation": "Difficult Manual: You MUST ease money pain (steps 1-4) BEFORE explaining technical details (step 5)."
    },
    {
        "question": "ORDERING: Correct sequence for Intake?",
        "options": ["Quote -> Test -> Ask", "Confirm Model -> Timeline/Scenario -> Visual Check -> Basic Test -> Quote", "Take deposit -> Ask Model", "Fix -> Quote"],
        "answer": "Confirm Model -> Timeline/Scenario -> Visual Check -> Basic Test -> Quote",
        "explanation": "Intake SOP: Model first. Visual check before test. Test before quote."
    },
    {
        "question": "RED LINE: If a customer threatens legal action or police, what is the '3-Minute Rule'?",
        "options": ["Fight back", "Return within 3 minutes with a manager (or update)", "Hide for 3 minutes", "Call the police immediately"],
        "answer": "Return within 3 minutes with a manager (or update)",
        "explanation": "Escalation: Don't leave them hanging. Update or escalate within 3 mins."
    },
    {
        "question": "RED LINE: Can you promise 100% data safety?",
        "options": ["Yes", "No. We advise backup. We take care but risks exist", "Only for VIPs", "Yes, if they pay extra"],
        "answer": "No. We advise backup. We take care but risks exist",
        "explanation": "Intake SOP: Never guarantee 100% data safety."
    },
    {
        "question": "RED LINE: If a customer asks 'Is this an original part?', and we use high-quality 3rd party, you must:",
        "options": ["Lie and say yes", "Be transparent: 'It is a high-quality aftermarket part with warranty'", "Say 'It's the same'", "Ignore the question"],
        "answer": "Be transparent: 'It is a high-quality aftermarket part with warranty'",
        "explanation": "Core Value: Honesty. Never lie about part origin."
    }
]

# ==========================================
# 3. 游戏逻辑函数 (Core Logic)
# ==========================================
def init_game(mode):
    st.session_state.mode = mode
    st.session_state.score = 0
    st.session_state.health = 3
    st.session_state.q_index = 0
    st.session_state.answered = False
    st.session_state.user_choice = None
    st.session_state.finished = False
    
    # 题库选择
    if mode == "Standard":
        # 如果题库不够10道，则复制以填充（防止随机抽取报错）
        bank = STANDARD_QUESTIONS * 2 
    else:
        bank = ADVANCED_QUESTIONS * 2
        
    # 随机抽取 10 道
    st.session_state.exam_questions = random.sample(bank, min(10, len(bank)))

def reset_game():
    init_game(st.session_state.mode)
    st.rerun()

# 初始化默认状态
if "mode" not in st.session_state:
    init_game("Standard")

# ==========================================
# 4. 侧边栏布局 (Sidebar)
# ==========================================
with st.sidebar:
    st.title("Ultech Training")
    
    # 模式选择
    new_mode = st.selectbox(
        "Difficulty Level:",
        ["Standard", "Advanced"],
        index=0 if st.session_state.mode == "Standard" else 1
    )
    
    # 监听模式切换
    if new_mode != st.session_state.mode:
        init_game(new_mode)
        st.rerun()
        
    st.markdown("---")
    st.write(f"❤️ Lives: {'🔴' * st.session_state.health}")
    st.write(f"🏆 Score: **{st.session_state.score}**")
    st.write(f"📊 Progress: {st.session_state.q_index + 1} / 10")
    
    if st.button("🔄 Restart"):
        reset_game()

# ==========================================
# 5. 主界面内容 (Main Interface)
# ==========================================
st.header(f"{'🟢' if st.session_state.mode == 'Standard' else '🔥'} Ultech {st.session_state.mode} Quiz")

if st.session_state.mode == "Advanced":
    st.caption("Challenge: Scenario Judgment, Sequence Ordering, Red Lines.")
else:
    st.caption("Basics: SOP, Scripts, Warranty Rules.")

# --- 游戏结束判断 ---
if st.session_state.health <= 0:
    st.error("💀 **GAME OVER**")
    st.write("You ran out of lives. Please review the SOPs.")
    if st.button("Try Again"):
        reset_game()
    st.stop()

if st.session_state.q_index >= 10:
    st.balloons()
    st.success(f"🎉 **COMPLETED!** Final Score: {st.session_state.score} / 10")
    
    if st.session_state.score >= 8:
        st.markdown("### Result: ✅ PASS")
    else:
        st.markdown("### Result: ❌ FAIL (Needs 8/10)")
    
    if st.button("Start New Round"):
        reset_game()
    st.stop()

# --- 题目显示 ---
q = st.session_state.exam_questions[st.session_state.q_index]

st.progress((st.session_state.q_index) / 10)
st.markdown(f"#### Q{st.session_state.q_index + 1}: {q['question']}")

# --- 答题交互区 ---
placeholder = st.empty()

# 如果还没回答，显示表单
if not st.session_state.answered:
    with placeholder.form(key=f"form_{st.session_state.q_index}"):
        opts = q['options'].copy()
        random.shuffle(opts) # 选项随机排列，防止背答案
        
        choice = st.radio("Select Answer:", opts, index=None)
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if choice:
                st.session_state.user_choice = choice
                st.session_state.answered = True
                st.rerun()
            else:
                st.warning("Please select an option.")

# 如果已回答，显示结果和解析
else:
    correct = st.session_state.user_choice == q['answer']
    
    if correct:
        st.markdown(f"<div class='success-box'>✅ **Correct!**</div>", unsafe_allow_html=True)
        # 加分逻辑：防止刷新页面重复加分
        if "score_added" not in st.session_state:
            st.session_state.score += 1
            st.session_state.score_added = True
    else:
        st.markdown(f"<div class='error-box'>❌ **Incorrect.**</div>", unsafe_allow_html=True)
        st.write(f"**Correct Answer:** `{q['answer']}`")
        # 扣血逻辑
        if st.session_state.health > 0 and "health_deducted" not in st.session_state:
             st.session_state.health -= 1
             st.session_state.health_deducted = True

    # 显示解析
    st.info(f"💡 **SOP Insight:** {q['explanation']}")
    
    if st.button("➡️ Next Question"):
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.session_state.user_choice = None
        # 清理临时状态
        if "health_deducted" in st.session_state: del st.session_state.health_deducted
        if "score_added" in st.session_state: del st.session_state.score_added
        st.rerun()