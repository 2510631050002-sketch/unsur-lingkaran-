
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge
from matplotlib.patches import Polygon

# ==========================================
# 1. KONFIGURASI APLIKASI
# ==========================================

st.set_page_config(
    page_title="Media Interaktif Lingkaran",
    page_icon="⭕",
    layout="wide"
)

# ==========================================
# 2. DESAIN APLIKASI
# ==========================================

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

.info-card {
    background-color: #DDEFE0;
    padding: 20px;
    border-radius: 15px;
    color: #214D35;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. DATA UNSUR LINGKARAN
# ==========================================

unsur = {
    "Titik Pusat": {
        "definisi": "Titik pusat adalah titik yang berada tepat di tengah lingkaran.",
        "simbol": "O",
        "contoh": "Titik tengah pada sebuah lingkaran."
    },

    "Jari-Jari": {
        "definisi": "Jari-jari adalah garis dari titik pusat lingkaran menuju satu titik pada keliling lingkaran.",
        "simbol": "r",
        "contoh": "Garis dari titik O menuju titik pada keliling."
    },

    "Diameter": {
        "definisi": "Diameter adalah garis lurus yang melalui titik pusat dan menghubungkan dua titik pada keliling lingkaran.",
        "simbol": "d",
        "contoh": "Panjang diameter adalah dua kali jari-jari."
    },

    "Tali Busur": {
        "definisi": "Tali busur adalah garis lurus yang menghubungkan dua titik pada keliling lingkaran.",
        "simbol": "-",
        "contoh": "Garis lurus yang menghubungkan titik A dan B."
    },

    "Busur": {
        "definisi": "Busur adalah garis lengkung yang merupakan bagian dari keliling lingkaran.",
        "simbol": "-",
        "contoh": "Bagian lengkung antara dua titik pada keliling."
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

# ==========================================
# 4. FUNGSI GAMBAR LINGKARAN
# ==========================================

def gambar_lingkaran(pilihan):

    fig, ax = plt.subplots(figsize=(6, 6))

    fig.patch.set_facecolor("#F7FAF5")
    ax.set_facecolor("#F7FAF5")

    hijau = "#214D35"
    kuning = "#F2B632"
    biru = "#3996C5"

    O = np.array([0.0, 0.0])

    # Lingkaran utama
    lingkaran = Circle(
        O, 1,
        fill=False,
        color=hijau,
        linewidth=3
    )

    ax.add_patch(lingkaran)

    # Koordinat bantu
    A = np.array([
        np.cos(np.radians(45)),
        np.sin(np.radians(45))
    ])

    B = np.array([
        np.cos(np.radians(-45)),
        np.sin(np.radians(-45))
    ])

    # Titik pusat
    if pilihan == "Titik Pusat":

        ax.scatter(
            0, 0,
            s=350,
            color=kuning,
            edgecolors="#C58A16",
            linewidths=2,
            zorder=10
        )

        ax.text(
            0.08, 0.08,
            "O (Pusat)",
            fontsize=12,
            color=hijau,
            fontweight="bold"
        )

    # Jari-jari
    elif pilihan == "Jari-Jari":

        ax.plot(
            [0, 1], [0, 0],
            color=kuning,
            linewidth=5,
            solid_capstyle="round"
        )

        ax.text(0.5, 0.08, "r", fontsize=15,
                color=hijau, fontweight="bold")

        ax.scatter(0, 0, color=hijau, s=40, zorder=5)

    # Diameter
    elif pilihan == "Diameter":

        ax.plot(
            [-1, 1], [0, 0],
            color=kuning,
            linewidth=5,
            solid_capstyle="round"
        )

        ax.text(0, 0.08, "d", fontsize=16,
                ha="center", color=hijau,
                fontweight="bold")

    # Tali busur
    elif pilihan == "Tali Busur":

        y = 0.5
        x = np.sqrt(1-y**2)

        ax.plot(
            [-x, x], [y, y],
            color=kuning,
            linewidth=5,
            solid_capstyle="round"
        )

        ax.scatter([-x, x], [y, y],
                   color=biru, s=55, zorder=5)

        ax.text(0, y+0.09, "Tali Busur",
                ha="center", color=hijau,
                fontsize=11)

    # Busur
    elif pilihan == "Busur":

        busur = np.linspace(25, 100, 100)

        x = np.cos(np.radians(busur))
        y = np.sin(np.radians(busur))

        ax.plot(
            x, y,
            color=kuning,
            linewidth=7,
            solid_capstyle="round"
        )

    # Juring
    elif pilihan == "Juring":

        juring = Wedge(
            O, 1,
            25, 100,
            facecolor=kuning,
            alpha=0.65,
            edgecolor="#C58A16",
            linewidth=2
        )

        ax.add_patch(juring)

        ax.plot(
            [0, np.cos(np.radians(25))],
            [0, np.sin(np.radians(25))],
            color=hijau, linewidth=2
        )

        ax.plot(
            [0, np.cos(np.radians(100))],
            [0, np.sin(np.radians(100))],
            color=hijau, linewidth=2
        )

        ax.text(
            0.45, 0.45,
            "Juring",
            fontsize=13,
            color=hijau,
            fontweight="bold"
        )

    # Tembereng
    elif pilihan == "Tembereng":

        sudut = np.linspace(30, 150, 100)

        busur_x = np.cos(np.radians(sudut))
        busur_y = np.sin(np.radians(sudut))

        titik = np.column_stack((
            np.concatenate([busur_x, [busur_x[-1], busur_x[0]]]),
            np.concatenate([busur_y, [busur_y[-1], busur_y[0]]])
        ))

        area = Polygon(
            titik,
            closed=True,
            facecolor=kuning,
            alpha=0.75,
            edgecolor="#C58A16",
            linewidth=2
        )

        ax.add_patch(area)

        ax.plot(
            [busur_x[0], busur_x[-1]],
            [busur_y[0], busur_y[-1]],
            color=hijau,
            linewidth=3
        )

        ax.text(
            0, 0.82,
            "Tembereng",
            fontsize=12,
            ha="center",
            color=hijau,
            fontweight="bold"
        )

    # Apotema
    elif pilihan == "Apotema":

        y = 0.5
        x = np.sqrt(1-y**2)

        ax.plot(
            [-x, x], [y, y],
            color=biru,
            linewidth=3
        )

        ax.plot(
            [0, 0], [0, y],
            color=kuning,
            linewidth=5
        )

        # Tanda sudut siku-siku
        ax.plot(
            [0, 0.08, 0.08],
            [0.5, 0.5, 0.58],
            color=hijau,
            linewidth=2
        )

        ax.scatter(0, 0, color=hijau, s=40)

        ax.text(
            0.08, 0.25,
            "Apotema",
            fontsize=11,
            color=hijau,
            fontweight="bold"
        )

    # Titik pusat selalu terlihat
    if pilihan != "Titik Pusat":
        ax.scatter(
            0, 0,
            color=hijau,
            s=45,
            zorder=10
        )
        ax.text(
            -0.12, -0.12,
            "O",
            fontsize=12,
            color=hijau,
            fontweight="bold"
        )

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()

    return fig


# ==========================================
# 5. JUDUL APLIKASI
# ==========================================

st.title("⭕ Mengenal Unsur-Unsur Lingkaran")

st.markdown("""
Selamat datang di media pembelajaran matematika!

Yuk, kenali bagian-bagian lingkaran dengan cara
yang menyenangkan. Pilih salah satu unsur dan
perhatikan lampu yang menyala!
""")

st.divider()

# ==========================================
# 6. PILIHAN UNSUR
# ==========================================

st.subheader("💡 Pilih Unsur Lingkaran")

pilihan = st.selectbox(
    "Unsur lingkaran:",
    list(unsur.keys())
)

# ==========================================
# 7. LAMPU LED KETAP-KETIP
# ==========================================

nama_lampu = list(unsur.keys())

lampu_html = ""

for i, nama in enumerate(nama_lampu):

    aktif = nama == pilihan

    warna = "#FFD700" if aktif else "#AAB5AA"

    efek = "active" if aktif else "inactive"

    lampu_html += f"""
    <div class="lampu-item">
        <div class="lampu {efek}"
             style="--warna:{warna};
                    animation-delay:{i * 0.15}s;">
        </div>

        <div class="lampu-label">
            {nama}
        </div>
    </div>
    """

st.markdown("""
<style>

.lampu-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 18px;
    background: #214D35;
    padding: 25px 12px;
    border-radius: 18px;
    margin: 15px 0;
}

.lampu-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    min-width: 75px;
}

.lampu {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: var(--warna);
}

.lampu.active {
    animation: kedip 0.8s infinite alternate;
}

.lampu.inactive {
    opacity: 0.35;
}

.lampu-label {
    color: white;
    font-size: 11px;
    font-weight: bold;
    text-align: center;
}

@keyframes kedip {
    from {
        opacity: 0.25;
        box-shadow: 0 0 3px var(--warna);
        transform: scale(0.8);
    }

    to {
        opacity: 1;
        box-shadow:
            0 0 10px var(--warna),
            0 0 25px var(--warna),
            0 0 40px var(--warna);
        transform: scale(1.25);
    }
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="lampu-container">
        {lampu_html}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <h3 style="text-align:center;color:#214D35;">
        ✨ {pilihan.upper()} ✨
    </h3>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 8. VISUALISASI DAN PENJELASAN
# ==========================================

st.divider()

col1, col2 = st.columns([1.2, 1])

with col1:

    st.subheader("🔵 Visualisasi Lingkaran")

    fig = gambar_lingkaran(pilihan)

    st.pyplot(fig, use_container_width=True)

    plt.close(fig)

with col2:

    st.subheader(f"📖 {pilihan}")

    st.markdown(
        f"""
        <div class="info-card">
            <h4>Pengertian</h4>
            <p>{unsur[pilihan]['definisi']}</p>
            <hr>
            <h4>Contoh</h4>
            <p>{unsur[pilihan]['contoh']}</p>
            <h4>Simbol</h4>
            <p>{unsur[pilihan]['simbol']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ==========================================
# 9. KUIS PILIHAN GANDA
# ==========================================

st.subheader("🎯 Ayo Berlatih!")

st.write(
    "Jawablah pertanyaan berikut untuk menguji pemahamanmu."
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
    ],

    "Garis lurus yang menghubungkan dua titik pada keliling disebut ...": [
        "Tali Busur",
        "Juring",
        "Jari-Jari",
        "Tembereng"
    ],

    "Daerah yang dibatasi tali busur dan busur disebut ...": [
        "Apotema",
        "Tembereng",
        "Diameter",
        "Jari-Jari"
    ]
}

kunci = [
    "Jari-Jari",
    "Juring",
    "Diameter",
    "Tali Busur",
    "Tembereng"
]

if "hasil_kuis" not in st.session_state:
    st.session_state.hasil_kuis = False

jawaban = []

with st.form("form_kuis"):

    for i, (pertanyaan, opsi) in enumerate(soal.items()):

        st.markdown(f"**{i+1}. {pertanyaan}**")

        jawab = st.radio(
            "Pilih jawaban:",
            opsi,
            key=f"jawaban_{i}",
            index=None
        )

        jawaban.append(jawab)

    periksa = st.form_submit_button("Periksa Jawaban")

if periksa:

    if any(j is None for j in jawaban):

        st.warning("Silakan jawab semua soal terlebih dahulu.")

    else:

        skor = sum(
            1 for i in range(len(kunci))
            if jawaban[i] == kunci[i]
        )

        nilai = int(skor / len(kunci) * 100)

        st.session_state.hasil_kuis = True
        st.session_state.skor = skor
        st.session_state.nilai = nilai
        st.session_state.jawaban_akhir = jawaban

if st.session_state.hasil_kuis:

    st.divider()

    st.subheader("📊 Hasil Belajarmu")

    st.metric(
        "Nilai Akhir",
        st.session_state.nilai
    )

    st.write(
        f"Jawaban benar: {st.session_state.skor} dari {len(kunci)} soal."
    )

    for i, benar in enumerate(kunci):

        if st.session_state.jawaban_akhir[i] == benar:

            st.success(f"Soal {i+1}: Benar!")

        else:

            st.error(
                f"Soal {i+1}: Salah. "
                f"Jawaban benar: {benar}"
            )

    if st.session_state.nilai >= 80:
        st.balloons()
        st.success("Hebat! Kamu sudah memahami unsur lingkaran!")

    else:
        st.info("Tetap semangat! Yuk, pelajari kembali materinya.")

    if st.button("Ulangi Kuis"):

        st.session_state.hasil_kuis = False

        for i in range(len(kunci)):
            if f"jawaban_{i}" in st.session_state:
                del st.session_state[f"jawaban_{i}"]

        st.rerun()

# ==========================================
# 10. PENUTUP
# ==========================================

st.divider()

st.markdown("""
<div style="
    background-color:#DDEFE0;
    padding:18px;
    border-radius:15px;
    text-align:center;
    color:#214D35;
">
    <h3>🌻 Selamat Belajar! 🌻</h3>
    <p>Matematika menjadi lebih menyenangkan
    ketika kita belajar sambil mencoba.</p>
</div>
""", unsafe_allow_html=True)
