import streamlit as st

# إعداد الصفحة لتظهر بشكل احترافي
st.set_page_config(page_title="رادار الكرش الرمضاني", page_icon="🌙", layout="centered")

# إضافة لمسات جمالية وألوان رمضانية (CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #0c2461;
        color: #f1c40f;
        direction: rtl;
        text-align: center;
    }
    .stRadio [data-testid="stMarkdownContainer"] p {
        font-size: 20px;
        color: white;
    }
    .stButton>button {
        background-color: #f1c40f;
        color: #0c2461;
        font-weight: bold;
        border-radius: 50px;
        border: none;
        height: 3em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_index=True)

# محتوى البرنامج
st.title("🌙 ميزان الكرش والسمبوسة 🥟")
st.write("### هل نجحت في ملء الكرش بنجاح؟")

# خيار المستخدم
answer = st.radio("", ["نعم.. تم الامتلاء بنجاح! ✅", "لا.. خيبة أمل كبيرة! ❌"], index=0)

# عند الضغط على الزر
if st.button("أظهر النتيجة الآن"):
    if "نعم" in answer:
        st.balloons() # تأثير احتفالي
        st.header("✨ بوركت جهودك يا صديقي! ✨")
        st.success("تقبل الله طاعاتك.. وصحة وهنا على قلبك!")
        st.write("### 🥟 جائزتك: طبق سمبوسة إضافي!")
    else:
        st.error("خيبة أمل يا صديقي.. 😔")
        st.write("### أين الهمة؟ السمبوسة بانتظارك في السحور!")

st.markdown("---")
st.caption("رمضان كريم | تم البرمجة بحب 🌙")
