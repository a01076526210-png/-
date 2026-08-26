import streamlit as st

# 1. 페이지 설정 (아이콘, 타이틀, 레이아웃)
st.set_page_config(
    page_title="✨MBTI 진로 탐색 파라다이스 🌈",
    page_icon="🦄",
    layout="wide"
)

# 커스텀 CSS (화려한 배경 그라데이션 및 카드 스타일링)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .mbti-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border: 2px solid #ff9a9e;
        text-align: center;
        margin-bottom: 20px;
    }
    .job-badge {
        background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
        color: #2c3e50;
        padding: 12px;
        border-radius: 15px;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. MBTI 데이터 베이스 (이모지 및 풍부한 정보 추가)
mbti_db = {
    "ISTJ": {"title": "📐 꼼꼼한 원칙주의자", "color": "🔵", "jobs": ["📊 회계사", "💻 데이터 분석가", "⚖️ 사법관", "🏗️ 시스템 엔지니어"], "trait": "체계적이고 신중하며 책임감이 매우 강합니다! 데이터와 명확한 규칙이 있는 직무에서 최고의 능력을 발휘해요! 🔍"},
    "ISFJ": {"title": "🛡️ 따뜻한 수호자", "color": "💗", "jobs": ["🩺 간호사", "🏫 초등교사", "🤝 사회복지사", "📋 HR 담당자"], "trait": "이타적이고 세심하여 타인을 돕는 일에서 큰 보람을 느낍니다! 안정적이고 조화로운 환경이 딱이에요! 🌸"},
    "INFJ": {"title": "🔮 통찰력 있는 예언자", "color": "🟣", "jobs": ["💬 심리상담사", "✍️ 작가", "🧭 진로 컨설턴트", "🎨 UX 디자이너"], "trait": "깊은 통찰력과 이상을 가지고 사람들의 성장을 돕습니다! 가치 있는 일에 열정을 다하는 스타일이에요! 🌟"},
    "INTJ": {"title": "용의주도한 전략가", "color": "🖤", "jobs": ["💼 경영 컨설턴트", "🔬 AI 연구원", "📈 투자 분석가", "🧠 뇌과학자"], "trait": "독립적이고 분석적이며 장기적 전략을 잘 세웁니다! 복잡한 문제를 해결하는 지적인 도전이 최고죠! ♟️"},
    "ISTP": {"title": "🛠️ 만능 만능 재주꾼", "color": "🟢", "jobs": ["⚙️ 기계 엔지니어", "✈️ 파일럿", "🗄️ DB 관리자", "🚑 응급구조사"], "trait": "객관적이고 적응력이 뛰어나며 도구와 시스템을 손쉽게 다룹니다! 위기 관리 능력이 완벽해요! ⚡"},
    "ISFP": {"title": "🎨 자유로운 예술가", "color": "🎨", "jobs": ["🖼️ 그래픽 디자이너", "📸 사진작가", "🐾 수의사", "👗 패션 디자이너"], "trait": "온화하고 감각적이며 자신만의 독창적인 예술성을 추구합니다! 자율성이 보장될 때 빛을 발해요! 🌈"},
    "INFP": {"title": "🦄 꿈꾸는 중재자", "color": "🌸", "jobs": ["🎬 콘텐츠 크리에이터", "📖 소설가", "🌐 번역가", "🌿 환경 운동가"], "trait": "낭만적이고 이상주의적입니다! 자신의 가치관과 일치하는 정서 깊은 분야에서 능력을 펼쳐요! 💫"},
    "INTP": {"title": "💡 호기심 천재 사색가", "color": "🧪", "jobs": ["💻 소프트웨어 아키텍트", "🔭 물리학자", "📐 금융 공학자", "🧠 철학 연구원"], "trait": "지적 호기심이 폭발하는 비판적 사고의 소유자! 새로운 이론과 원리를 탐구할 때 가장 행복해요! 🌌"},
    "ESTP": {"title": "🔥 모험을 즐기는 활동가", "color": "🟠", "jobs": ["💰 자산관리사", "🚀 스타트업 창업가", "⚽ 스포츠 감독", "📢 마케터"], "trait": "모험과 위험을 두려워하지 않는 대담함! 스릴 넘치고 빠른 판단이 필요한 현장에서 맹활약해요! 🏎️"},
    "ESFP": {"title": "🎉 흥 넘치는 연예인", "color": "🟡", "jobs": ["🎪 이벤트 기획자", "🎭 연기자/뮤지컬 배우", "✈️ 여행 가이드", "📢 PR 전문가"], "trait": "에너지 방출! 타인에게 즐거움을 주는 사교왕입니다! 늘 활기차고 밝은 현장이 어울려요! 🎤"},
    "ENFP": {"title": "🎈 비타민 활동가", "color": "💛", "jobs": ["✍️ 카피라이터", "💡 광고 기획자", "🎙️ 행사 MC", "🚀 캠페인 리더"], "trait": "상상력이 무궁무진하며 에너지가 넘칩니다! 사람들에게 긍정적 영감을 주는 프로젝트에 딱이에요! 💥"},
    "ENTP": {"title": "⚡ 아이디어 폭발 변론가", "color": "🔴", "jobs": ["🦄 벤처 투자자", "⚖️ 변호사", "📱 프로덕트 매니저", "🎯 정치 전략가"], "trait": "독창적이고 도전 정신이 넘칩니다! 기발한 아이디어로 기존 틀을 깨부수는 혁신가예요! 💥"},
    "ESTJ": {"title": "👑 카리스마 관리자", "color": "🟦", "jobs": ["🏛️ 프로젝트 매니저", "📊 운영 이사", "🏫 학교 행정가", "👮 경찰 간부"], "trait": "체계적이고 리더십이 뛰어난 실용주의자! 조직을 결단력 있게 이끌고 목표를 달성해냅니다! 🎖️"},
    "ESFJ": {"title": "🎁 친절한 핵인싸", "color": "🧡", "jobs": ["🤝 인사 관리자(HR)", "✈️ 승무원", "🎧 CSM 전문가", "🏫 초등 교사"], "trait": "친절하고 조화로운 관계를 만들어가는 분위기 메이커! 타인을 챙기고 돕는 직무에 특화되어 있어요! 💌"},
    "ENFJ": {"title": "🌟 빛나는 사회운동가", "color": "✨", "jobs": ["🧭 진로진학 교사", "🌱 NGO 대표", "🎯 HRD 교육 전문가", "🎤 아나운서"], "trait": "카리스마와 따뜻함을 겸비한 타고난 지도자! 타인의 잠재력을 끌어올려 성장시키는 스페셜리스트! 🏆"},
    "ENTJ": {"title": "🔥 대담한 야망가 통솔자", "color": "👑", "jobs": ["🏢 CEO / 대표", "📈 경영 전략가", "🏦 Investment Banker", "🏛️ 정치인"], "trait": "철저한 계획 수립과 리더십을 갖춘 대담한 지도자! 명확한 비전으로 성공을 향해 나아갑니다! 🚀"}
}

# 3. 메인 헤더 레이아웃
st.markdown("<h1 style='text-align: center;'>🌈 ✨ MBTI 맞춤형 진로 탐색 드림랜드 ✨ 🌈</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #555;'>나의 성격에 딱 맞는 인생 직업을 찾아보세요! 🎉 🚀</h4>", unsafe_allow_html=True)

st.write("")
st.write("")

# 4. 사이드바 / 메인 선택창
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    selected_mbti = st.selectbox(
        "🔮 **당신의 MBTI를 선택해 보세요!** 🔮",
        options=list(mbti_db.keys()),
        index=0
    )

st.divider()

# 5. 선택된 MBTI 정보 카드 화려하게 출력
if selected_mbti:
    info = mbti_db[selected_mbti]
    
    # 축하 효과 팡파르! 🎉
    st.balloons()
    
    # 대표 헤더 박스
    st.markdown(f"""
        <div class="mbti-card">
            <h1 style="color: #ff4b4b; margin-bottom: 0px;">{info['color']} {selected_mbti} {info['color']}</h1>
            <h2 style="color: #333; margin-top: 10px;">{info['title']}</h2>
            <hr style="border: 1px solid #eee;">
            <p style="font-size: 1.2rem; line-height: 1.8; color: #555;">{info['trait']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("<h2 style='text-align: center;'>🎯 🔥 추천하는 베스트 직업 TOP 4 🔥 🎯</h2>", unsafe_allow_html=True)
    st.write("")
    
    # 4개의 컬럼으로 카드 배치
    j_cols = st.columns(4)
    for idx, job in enumerate(info["jobs"]):
        with j_cols[idx]:
            st.markdown(f"""
                <div class="job-badge">
                    {job}
                </div>
            """, unsafe_allow_html=True)

st.write("")
st.write("")
st.divider()

# 6. 하단 푸터 및 팁
st.info("💡 **진로 교육 Tip:** MBTI는 나를 이해하는 흥미로운 가이드일 뿐! 여러분의 가능성은 무한하답니다 ⭐ 🌈")
