import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="죠죠 3부 스탠드 도감",
    page_icon="⭐",
    layout="wide"
)

# -------------------------------------------------------------------
# 🔊 효과음 재생을 위한 JavaScript 함수 설정
# -------------------------------------------------------------------
# 외부 오디오 파일 URL (죠타로의 오라오라 효과음/음성 파일)
ORA_SOUND_URL = "https://www.myinstants.com/media/sounds/ora-ora-ora.mp3"

def play_ora_sound():
    """버튼 클릭 시 JavaScript를 이용해 오디오를 재생하는 컴포넌트"""
    js_code = f"""
        <script>
            var audio = new Audio('{ORA_SOUND_URL}');
            audio.play();
        </script>
    """
    components.html(js_code, height=0, width=0)

# 헤더 타이틀 및 설명
st.title("⭐ 죠죠의 기묘한 모험 3부: 스탠드 도감 ⭐")
st.markdown("주인공 일러스트(버튼)를 클릭하면 **오라!** 소리와 함께 해당 캐릭터의 스탠드 정보가 출력됩니다!")

# 캐릭터 데이터베이스
characters = {
    "쿠죠 죠타로": {
        "stand": "스타 플래티나 (Star Platinum)",
        "image": "https://i.namu.wiki/i/0kggSR3vldNGwx71zBWkQnuiSNn_kdI0HsvAEZA4T5HsNHRC6PJT49aZYQF_hUXs-KJ-PQIm3xKFEX4sUWUGUA.webp",
        "description": "압도적인 파괴력과 정밀성, 그리고 눈으로 쫓을 수 없는 스피드를 자랑하는 근거리 파워형 스탠드.",
        "skills": [
            "오라오라 러시: 초고속 연속 펀치 공격",
            "스타 핑거: 손가락을 순간적으로 늘려 적을 찌르는 공격",
            "정밀한 시각 & 정밀 동작: 미세한 움직임과 대상을 정확히 관찰 및 포착",
            "시간 정지 (시간을 멈춰라): 시간의 흐름을 몇 초간 멈춤"
        ]
    },
    "조셉 죠스타": {
        "stand": "허밋 퍼플 (Hermit Purple)",
        "image": "https://i.namu.wiki/i/zrS1cSjogLQLAOJS231-AlUAOIG3709TFniGG2Fd44ykDoHDuMBL3XAFRF3VXNMIXGypvs8OtW3Lfsr-Wb7eiQ.webp",
        "description": "가시가 돋친 덩굴 형태의 스탠드로, 염사 및 비전(미래/위치 추적) 능력에 특화되어 있음.",
        "skills": [
            "염사 (기계/사진 염사): 카메라나 TV 등을 부수거나 작동시켜 원하는 정보를 영상화",
            "파문 전도: 덩굴을 통해 파문 에너지를 전달하여 공격 및 방어",
            "지도/지형 탐색: 모래나 지도 위에 스탠드를 펼쳐 목적지의 위치 추적"
        ]
    },
    "무하마드 압둘": {
        "stand": "매지션즈 레드 (Magician's Red)",
        "image": "https://i.namu.wiki/i/dI_bJ1KpZELcZWA8o3ZlDFnK4jXgZW4NekfzY8wntuE6ifGRlvocAkLa6-CDvS-BJEiqSiS_A3y0kePGASVo8w.webp",
        "description": "조류 머리를 한 도인 형태의 스탠드로, 고열의 화염을 자유자재로 조종함.",
        "skills": [
            "크로스 파이어 허리케인: 앙크(Ankh) 모양의 고열 화염 탄환을 연사",
            "생체 탐지 (파이어 디텍터): 생명체의 생체 열을 감지하여 적의 위치 추적",
            "레드 바인드: 화염으로 만든 밧줄로 적을 묶어 구속 및 구움"
        ]
    },
    "카쿄인 노리아키": {
        "stand": "하이에로판트 그린 (Hierophant Green)",
        "image": "https://i.namu.wiki/i/RxGjfESvafY_E-RtoRe2VoYZyeUdrmbu-csFlT_kREWhp9j_RGRXTS-DG3byCusAWQhJWaMPpmGfemQOyRZpfQ.webp",
        "description": "줄기 형태로 몸을 해체할 수 있는 원거리 조종형 스탠드.",
        "skills": [
            "에메랄드 스플래시: 에메랄드 모양의 결정체 체액을 고속으로 분사하는 중거리 격파 기술",
            "스탠드 침투 및 세뇌: 타인의 몸속으로 침투하여 상대를 조종",
            "반경 20미터 에메랄드 스플래시: 스탠드 줄기를 20m 결계로 펼쳐 촉발 시 전방위 사격"
        ]
    },
    "장 피에르 폴나레프": {
        "stand": "실버 채리엇 (Silver Chariot)",
        "image": "https://i.namu.wiki/i/ICgsObo8cD7C2wOp2Rt0NP7j7Jxd3DhTZyVbFDgVKXODZyd3EBDglk93uIOoSHf0nWvOYmqPHgsZOqX7H5ey1w.webp",
        "description": "갑옷을 입은 기사 형태의 스탠드로, 레이피어를 사용한 초고속 검술에 특화됨.",
        "skills": [
            "고속 검술 및 찌르기: 눈에 보이지 않을 정도의 정밀하고 빠른 검술",
            "갑옷 탈복 (갑옷 벗기): 갑옷을 벗어 던져 방어력을 낮추는 대신 잔상이 생길 정도의 초고속 이동 가능",
            "검신 분사 (레이피어 검신 날리기): 레이피어 칼날을 강하게 튕겨내어 예상치 못한 각도에서 적을 공격"
        ]
    },
    "이기": {
        "stand": "더 풀 (The Fool)",
        "image": "https://i.namu.wiki/i/b6ftOlSoLGIRAZLySHzZ8lmCAEne6zY0bBU9CXcH0tOY3vih2s6DkXwa_7Z2J0Yg3PGnxLqBzxH7qgkM9OyeZQ.webp",
        "description": "모래로 구성된 스탠드로, 형태 변형이 자유롭고 물질 형태이기에 물리 공격에 파괴되지 않음.",
        "skills": [
            "모래 변형 및 글라이더: 모래를 입혀 날개를 만들어 공중을 비행",
            "의태/환영 생성: 모래를 이용해 타인(예: DIO 등)의 모습으로 완벽하게 변장",
            "물리 공격 무효화: 모래 덩어리이므로 베거나 찔려도 본체에 직접적인 데미지가 없음"
        ]
    }
}

# 세션 상태(Session State) 초기화
if "selected_char" not in st.session_state:
    st.session_state.selected_char = "쿠죠 죠타로"
if "play_sound" not in st.session_state:
    st.session_state.play_sound = False

st.write("---")
st.subheader("👥 캐릭터를 선택하세요")

# 캐릭터 일러스트 버튼 배치
cols = st.columns(len(characters))

for idx, (name, info) in enumerate(characters.items()):
    with cols[idx]:
        st.image(info["image"], use_container_width=True)
        # 버튼을 누르면 캐릭터 변경 및 음성 재생 플래그 설정
        if st.button(name, key=f"btn_{name}", use_container_width=True):
            st.session_state.selected_char = name
            st.session_state.play_sound = True

# 소리 재생 플래그가 True이면 소리를 내고 초기화
if st.session_state.play_sound:
    play_ora_sound()
    st.session_state.play_sound = False

st.write("---")

# 선택된 캐릭터 상세 정보 출력
selected_name = st.session_state.selected_char
char_data = characters[selected_name]

col_img, col_info = st.columns([1, 2])

with col_img:
    st.image(char_data["image"], caption=f"{
