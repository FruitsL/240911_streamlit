import streamlit as st
import pyshorteners

# 앱 제목
st.title("URL 줄이기 앱")

# 사용자로부터 URL 입력 받기
long_url = st.text_input("줄이고 싶은 URL을 입력하세요:")

# URL 줄이기 버튼
if st.button("줄이기"):
    if long_url:
        try:
            # URL 줄이기
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(long_url)
            
            # 결과 출력
            st.success(f"짧아진 URL: {short_url}")
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("URL을 입력해주세요.")
