import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(background="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("App Menyapa")



NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


style = ttk.Style()
# Tombol Primary (biru)
style.configure("Primary.TButton",
                foreground="white",
                background="#0d6efd",   # biru bootstrap
                font=("Arial", 11, "bold"),
                padding=6)
style.map("Primary.TButton",
          background=[("active", "#0b5ed7")])

# Tombol Danger (merah)
style.configure("Danger.TButton",
                foreground="white",
                background="#dc3545",   # merah bootstrap
                font=("Arial", 11, "bold"),
                padding=6)
style.map("Danger.TButton",
          background=[("active", "#bb2d3b")])



# Frame
inputFrame = ttk.Frame(window)
inputFrame.pack(padx=10, pady=10, fill="x", expand=True)



# Komponen
# Label Nama Depan
namaDepanLabel = ttk.Label(inputFrame, text="Nama Depan")
namaDepanLabel.pack(padx=10, fill="x", expand=True)

#Entri (Input)
namaDepanEntry = ttk.Entry(inputFrame, textvariable=NAMA_DEPAN)
namaDepanEntry.pack(padx=10, fill="x", expand=True)

# Label Nama Belakang
namaBelakangLabel = ttk.Label(inputFrame, text="Nama Belakang")
namaBelakangLabel.pack(padx=10, fill="x", expand=True)

#Entri (Input)
namaBelakangEntry = ttk.Entry(inputFrame, textvariable=NAMA_BELAKANG)
namaBelakangEntry.pack(padx=10, fill="x", expand=True)

# Tombol Menyapa
def tombolKlik():
    namaDepan = NAMA_DEPAN.get()
    namaBelakang = NAMA_BELAKANG.get()

    pesan = f"Hello {namaDepan} {namaBelakang}, Selamat Datang di Python Programming"
    showinfo(title="Pemberitahuan!!!!", message=pesan)

tombol_sapa = ttk.Button(inputFrame, text="Sapa!", style="Primary.TButton", command=tombolKlik)
tombol_sapa.pack(expand=True, padx=10, pady=10, side="left")

# Tombol keluar
exit_button = ttk.Button(inputFrame, text="Keluar", style="Danger.TButton", command=window.destroy)
exit_button.pack(expand=True, padx=10, pady=10, side="left")

window.mainloop()