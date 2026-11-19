# Skenario: v1 aman, v2 gagal, rollback, v2 aman

## 1. Push v1 (aman)
git init -b main
git add . && git commit -m "feat: v1.0.0 aman"
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
git tag v1.0.0 && git push origin v1.0.0
=> Actions hijau, Release v1.0.0 terbit.

## 2. Push v2 (sengaja rusak)
Di kalkulator.py: ubah __version__ jadi "2.0.0", lalu hapus dua baris ini di fungsi bagi:
    if b == 0:
        raise ValueError("Pembagi tidak boleh nol")

git commit -am "feat: v2.0.0 rusak"
git push origin main
git tag v2.0.0 && git push origin v2.0.0
=> CI merah (test_bagi_nol gagal), muncul anotasi "CI GAGAL", GitHub kirim email.
=> Job rilis berhenti di langkah tes, tidak ada Release v2.0.0.

## 3. Rollback
git revert --no-edit HEAD        # buat commit pembatal, riwayat tetap utuh
git push origin main
git tag -d v2.0.0                # hapus tag rusak di lokal
git push origin --delete v2.0.0  # hapus tag rusak di GitHub
=> CI hijau lagi, __version__ kembali "1.0.0".

Jika rilis rusak sudah terlanjur terbit:
gh release delete v2.0.0 --cleanup-tag --yes

## 4. Upload v2 yang aman
Ubah __version__ jadi "2.0.0", tambah fungsi pangkat dan tesnya, lalu:
git commit -am "feat: v2.0.0 aman (tambah pangkat)"
git push origin main
git tag v2.0.0 && git push origin v2.0.0
=> CI hijau, Release v2.0.0 terbit.
