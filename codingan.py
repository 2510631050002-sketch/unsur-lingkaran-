
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mengenal Unsur Lingkaran",
    page_icon="⭕",
    layout="wide"
)

# =========================
# JUDUL APLIKASI
# =========================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background-color: #F7FAF5;
}

h1, h2, h3 {
    color: #214D35;
}

.keterangan {
    background: #E5F1E5;
    padding: 18px;
    border-radius: 15px;
    color: #214D35;
    margin-top: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("⭕ Mengenal Unsur-Unsur Lingkaran")
st.write(
    "Ayo kenali bagian-bagian lingkaran! "
    "Pilih salah satu unsur, kemudian amati bagian lingkaran "
    "yang berkedip."
)

# =========================
# DATA UNSUR LINGKARAN
# =========================

unsur = {
    "Titik Pusat": {
        "definisi": "Titik pusat adalah titik yang berada tepat di tengah lingkaran. Pada gambar, titik pusat diberi nama O.",
        "rumus": "Dilambangkan dengan titik O."
    },
    "Jari-jari": {
        "definisi": "Jari-jari adalah garis yang menghubungkan titik pusat lingkaran dengan satu titik pada keliling lingkaran.",
        "rumus": "r = d ÷ 2"
    },
    "Diameter": {
        "definisi": "Diameter adalah garis lurus yang melewati titik pusat dan menghubungkan dua titik pada keliling lingkaran.",
        "rumus": "d = 2 × r"
    },
    "Tali Busur": {
        "definisi": "Tali busur adalah garis lurus yang menghubungkan dua titik pada keliling lingkaran.",
        "rumus": "Tidak harus melewati titik pusat."
    },
    "Busur": {
        "definisi": "Busur adalah garis lengkung yang merupakan bagian dari keliling lingkaran.",
        "rumus": "Bagian dari keliling lingkaran."
    },
    "Juring": {
        "definisi": "Juring adalah daerah di dalam lingkaran yang dibatasi oleh dua jari-jari dan satu busur.",
        "rumus": "Berbentuk seperti potongan kue."
    },
    "Tembereng": {
        "definisi": "Tembereng adalah daerah di dalam lingkaran yang dibatasi oleh satu tali busur dan satu busur lingkaran.",
        "rumus": "Berada di antara tali busur dan busur."
    }
}

# =========================
# PILIH UNSUR
# =========================

pilihan = st.selectbox(
    "Pilih unsur lingkaran yang ingin dipelajari:",
    list(unsur.keys())
)

# =========================
# GAMBAR LINGKARAN SVG
# =========================

def kelas(nama):
    return "blink" if pilihan == nama else ""

svg = f"""
<svg viewBox="0 0 500 450"
     xmlns="http://www.w3.org/2000/svg"
     width="100%" height="430">

    <!-- Lingkaran utama -->
    <circle cx="250" cy="220" r="150"
            fill="#F5FAF3"
            stroke="#214D35"
            stroke-width="4"/>

    <!-- Tembereng -->
    <g class="{kelas('Tembereng')}">
        <path d="M 372.9 306.0
                 A 150 150 0 0 1 211.2 365.0
                 L 372.9 306.0 Z"
              fill="#F4C95D"
              fill-opacity="0.55"
              stroke="#D49B19"
              stroke-width="2"/>
    </g>

    <!-- Juring -->
    <g class="{kelas('Juring')}">
        <path d="M 250 220
                 L 364.9 123.6
                 A 150 150 0 0 1 391 169
                 Z"
              fill="#7DBB91"
              fill-opacity="0.55"
              stroke="#398052"
              stroke-width="2"/>
    </g>

    <!-- Diameter -->
    <g class="{kelas('Diameter')}">
        <line x1="100" y1="220"
              x2="400" y2="220"
              stroke="#E05B4B"
              stroke-width="5"
              stroke-linecap="round"/>
    </g>

    <!-- Jari-jari -->
    <g class="{kelas('Jari-jari')}">
        <line x1="250" y1="220"
              x2="364.9" y2="123.6"
              stroke="#2877C7"
              stroke-width="5"
              stroke-linecap="round"/>
    </g>

    <!-- Tali busur -->
    <g class="{kelas('Tali Busur')}">
        <line x1="372.9" y1="306"
              x2="211.2" y2="365"
              stroke="#9B59B6"
              stroke-width="5"
              stroke-linecap="round"/>
    </g>

    <!-- Busur -->
    <g class="{kelas('Busur')}">
        <path d="M 372.9 306
                 A 150 150 0 0 1 211.2 365"
              fill="none"
              stroke="#E58A22"
              stroke-width="7"
              stroke-linecap="round"/>
    </g>

    <!-- Titik pusat -->
    <g class="{kelas('Titik Pusat')}">
        <circle cx="250" cy="220" r="8"
                fill="#E04444"
                stroke="#FFFFFF"
                stroke-width="2"/>
    </g>

    <!-- Titik-titik penanda -->
    <circle cx="100" cy="220" r="4" fill="#214D35"/>
    <circle cx="400" cy="220" r="4" fill="#214D35"/>
    <circle cx="364.9" cy="123.6" r="4" fill="#214D35"/>
    <circle cx="372.9" cy="306" r="4" fill="#214D35"/>
    <circle cx="211.2" cy="365" r="4" fill="#214D35"/>

    <!-- Label -->
    <text x="262" y="211" font-size="17"
          font-weight="bold" fill="#214D35">O</text>

    <text x="315" y="160" font-size="15"
          fill="#2877C7">r</text>

    <text x="250" y="205" font-size="13"
          fill="#E05B4B"> </text>

    <text x="245" y="242" font-size="13"
          fill="#214D35">Pusat</text>

    <text x="244" y="80" font-size="17"
          font-weight="bold" fill="#214D35">LINGKARAN</text>

</svg>
"""

# =========================
# ANIMASI BERKEDIP
# =========================

css = """
<style>
body {
    margin: 0;
    background: transparent;
}

svg {
    display: block;
    margin: auto;
}

.blink {
    animation: berkedip 0.8s infinite alternate;
}

@keyframes berkedip {
    from {
        opacity: 0.25;
        filter: drop-shadow(0px 0px 0px transparent);
    }
    to {
        opacity: 1;
        filter: drop-shadow(0px 0px 9px #F2B705);
    }
}
</style>
"""

html = f"""
<html>
<head>{css}</head>
<body>
{svg}
</body>
</html>
"""

# =========================
# TAMPILAN UTAMA
# =========================

kiri, kanan = st.columns([1.5, 1])

with kiri:
    st.subheader("Visualisasi Lingkaran")

    components.html(
        html,
        height=450,
        scrolling=False
    )

    st.caption(
        "Amati bagian yang berkedip pada gambar lingkaran."
    )

with kanan:
    st.subheader("Yuk, Pelajari!")

    st.markdown(
        f"""
        <div class="keterangan">
            <h3>{pilihan}</h3>
            <p>{unsur[pilihan]["definisi"]}</p>
            <b>{unsur[pilihan]["rumus"]}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.success(
        f"Sekarang bagian **{pilihan}** sedang ditampilkan."
    )

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#55745D;">
        <b>Media Pembelajaran Matematika</b><br>
        Mengenal Unsur-Unsur Lingkaran
    </div>
    """,
    unsafe_allow_html=True
)
