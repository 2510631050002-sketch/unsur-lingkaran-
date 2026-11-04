
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge, Arc

# =====================================
# KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Mengenal Unsur Lingkaran",
    page_icon="⭕",
    layout="wide"
)

# =====================================
# DESAIN
# =====================================

st.markdown("""
<style>
.stApp {
    background-color: #F7FAF5;
}

h1, h2, h3 {
    color: #214D35;
}

.stButton button {
    background-color: #DDEFE0;
    color: #214D35;
    border-radius: 10px;
    border: 1px solid #B8D5BC;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #C4E2CA;
    color: #214D35;
}
</style>
""", unsafe_allow_html=True)

# =====================================
# DATA UNSUR LINGKARAN
# =====================================

unsur = {
    "Jari-Jari": {
        "definisi": "Jari-jari adalah garis dari titik pusat lingkaran menuju satu titik pada keliling lingkaran.",
        "simbol": "r",
        "contoh": "Garis dari titik O menuju titik A."
    },

    "Diameter": {
        "definisi": "Diameter adalah garis lurus yang melalui titik pusat dan menghubungkan dua titik pada keliling lingkaran.",
        "simbol": "d",
        "contoh": "Panjang diameter adalah dua kali jari-jari."
    },

    "Tali Busur": {
        "definisi": "Tali busur adalah garis lurus yang menghubungkan dua titik pada keliling lingkaran.",
        "simbol": "-",
        "contoh": "Garis yang menghubungkan titik A dan B."
    },

    "Busur": {
        "definisi": "Busur adalah garis lengkung yang merupakan bagian dari keliling lingkaran.",
        "simbol": "-",
        "contoh": "Bagian lengkung antara titik A dan B."
    },

    "Juring": {
        "definisi": "Juring adalah daerah dalam lingkaran yang dibatasi oleh dua jari-jari dan sebuah busur.",
        "simbol": "-",
        "contoh": "Bentuknya seperti potongan pizza."
    },

    "Tembereng": {
        "definisi": "Tembereng adalah daerah dalam lingkaran yang dibatasi oleh sebuah tali busur dan busur lingkaran.",
        "simbol": "-",
        "contoh": "Daerah di antara tali busur dan busur."
    },

    "Apotema": {
        "definisi": "Apotema adalah garis dari titik pusat lingkaran yang tegak lurus terhadap tali busur.",
        "simbol": "-",
        "contoh": "Jarak terpendek titik pusat terhadap tali busur."
    }
}

# =====================================
# GAMBAR LINGKARAN
# =====================================

def gambar_lingkaran(pilihan):

    fig, ax = plt.subplots(figsize=(6, 6))

    fig.patch.set_facecolor("#F7FAF5")
    ax.set_facecolor("#F7FAF5")

    # Titik pusat
    O = np.array([0, 0])

    # Titik A dan B
    A = np.array([np.cos(np.radians(45)),
                  np.sin(np.radians(45))])

    B = np.array([np.cos(np.radians(-45)),
                  np.sin(np.radians(-45))])

    # Lingkaran utama
    lingkaran = Circle(
        O, 1,
        fill=False,
        color="#214D35",
        linewidth=3
    )

    ax.add_patch(lingkaran)

    # Koordinat garis
    ax.plot(O[0], O[1], "o", color="#214D35")

    # Jari-jari
    if pilihan == "Jari-Jari":
        ax.plot([0, 1], [0, 0],
                color="#E09F3E", linewidth=5)
        ax.text(0.5, -0.12, "r", fontsize=14)

    # Diameter
    elif pilihan == "Diameter":
        ax.plot([-1, 1], [0, 0],
                color="#E09F3E", linewidth=5)
        ax.text(0, -0.12, "d", fontsize=14)

    # Tali busur
    elif pilihan == "Tali Busur":
        ax.plot(
            [A[0], B[0]],
            [A[1], B[1]],
            color="#E09F3E",
            linewidth=5
        )

    # Busur
    elif pilihan == "Busur":
        busur = Arc(
            O, 2, 2,
            theta1=-45,
            theta2=45,
            color="#E09F3E",
            linewidth=6
        )
        ax.add_patch(busur)

    # Juring
    elif pilihan == "Juring":
        juring = Wedge(
            O, 1,
            -45, 45,
            facecolor="#F5D77A",
            alpha=0.8,
            edgecolor="#E09F3E",
            linewidth=2
        )
        ax.add_patch(juring)

    # Tembereng
    elif pilihan == "Tembereng":
        tembereng = Wedge(
            O, 1,
            45, 135,
            facecolor="#F5D77A",
            alpha=0.8,
            edgecolor="#E09F3E",
            linewidth=2
        )

        ax.add_patch(tembereng)

        P = np.array([
            np.cos(np.radians(45)),
            np.sin(np.radians(45))
        ])

        Q = np.array([
            np.cos(np.radians(135)),
            np.sin(np.radians(135))
        ])

        ax.plot(
            [P[0], Q[0]],
            [P[1], Q[1]],
            color="#E09F3E",
            linewidth=3
        )

    # Apotema
    elif pilihan == "Apotema":
        P = np.array([0.7, 0])
        Q = np.array([0.7, np.sqrt(1 - 0.7**2)])

        ax.plot(
            [0, 0.7],
            [0, 0],
            color="#214D35",
            linewidth=2
        )

        ax.plot(
            [0.7, 0.7],
            [0, Q[1]],
            color="#E09F3E",
            linewidth=5
        )

        ax.plot(
            [0, Q[0]],
            [0, Q[1]],
            color="#214D35",
            linewidth=2
        )

        ax.text(0.73, 0.3, "Apotema", fontsize=10)

    # Label titik pusat
    ax.text(-0.12, -0.12, "O", fontsize=13,
            fontweight="bold")

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()

    return fig


# =====================================
# JUDUL APLIKASI
# =====================================

st.title("⭕ Mengenal Unsur-Unsur Lingkaran")

st.markdown("""
Yuk, belajar mengenal bagian-bagian lingkaran!
Tekan tombol di bawah untuk mengetahui nama,
bentuk, dan pengertian setiap unsur lingkaran.
""")

st.divider()

# =====================================
# PILIHAN UNSUR
# =====================================

st.subheader("Pilih Unsur Lingkaran")

pilihan = st.selectbox(
    "Pilih salah satu unsur:",
    list(unsur.keys())
)

# =====================================
# TAMPILAN UTAMA
# =====================================

col1, col2 = st.columns([1.2, 1])

with col1:

    st.subheader("Visualisasi Lingkaran")

    fig = gambar_lingkaran(pilihan)

    st.pyplot(fig, use_container_width=True)

    plt.close(fig)

with col2:

    st.subheader(pilihan)

    st.success(unsur[pilihan]["definisi"])

    st.markdown("### Contoh")

    st.info(unsur[pilihan]["contoh"])

    if unsur[pilihan]["simbol"] != "-":
        st.markdown(
            f"**Simbol:** {unsur[pilihan]['simbol']}"
        )

st.divider()

# =====================================
# KUIS
# =====================================

st.subheader("🎯 Ayo Berlatih!")

st.write(
    "Pilih jawaban yang tepat berdasarkan pengertian berikut."
)

soal = {
    "Garis dari titik pusat menuju keliling lingkaran disebut ...": [
        "Diameter",
        "Jari-Jari",
        "Busur",
        "Tembereng"
    ],

    "Daerah yang dibatasi dua jari-jari dan sebuah busur disebut ...": [
        "Tali Busur",
        "Apotema",
        "Juring",
        "Diameter"
    ],

    "Garis yang melalui titik pusat dan menghubungkan dua titik pada keliling disebut ...": [
        "Busur",
        "Diameter",
        "Juring",
        "Apotema"
    ]
}

kunci = [
    "Jari-Jari",
    "Juring",
    "Diameter"
]

if "jawaban" not in st.session_state:
    st.session_state.jawaban = {}

for i, (pertanyaan, opsi) in enumerate(soal.items()):

    st.markdown(f"**{i+1}. {pertanyaan}**")

    st.session_state.jawaban[i] = st.radio(
        "Pilih jawaban:",
        opsi,
        key=f"soal_{i}",
        index=None
    )

if st.button("Periksa Jawaban"):

    if any(v is None for v in st.session_state.jawaban.values()):

        st.warning("Jawab semua soal terlebih dahulu.")

    else:

        skor = 0

        for i in range(len(kunci)):

            if st.session_state.jawaban[i] == kunci[i]:
                skor += 1
                st.success(f"Soal {i+1}: Benar!")

            else:
                st.error(
                    f"Soal {i+1}: Salah. "
                    f"Jawaban benar: {kunci[i]}"
                )

        st.metric(
            "Nilai Akhir",
            f"{round(skor/len(kunci)*100)}"
        )

st.divider()

st.caption(
    "Media Pembelajaran Matematika | Materi Unsur-Unsur Lingkaran"
)
