# File Sharing Me

Repo Telegram Bot Yang Dapat Menyimpan File, Video dan Dokumen dan Dapat Diakses Melalui Tautan Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang.....😇.

##
### Cara install
#### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/renggi06/File-Sharing-Me)</br>
<a href="https://youtu.be/LCrkRTMkmzE">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

#### Deploy in your VPS
````bash
git clone https://github.com/renggi06/File-Sharing-Me
cd File-Sharing-Me
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Perintah Khusus Admin atau Owner Bot

```
/start - Perintah Start Untuk Memulai Bot Atau Mendapatkan File,Video,Dokumen.

/batch - Perintah Batch Untuk Membuat Lebih Dari Satu Postingan File,Video,Dokumen di 1 Link Bot.

/genlink - Perintah Genlink Untuk Membuat Satu Postingan di 1 Link Bot.

/users - Perintah Users Untuk Melihat Statistik Yang Menggunakan Bot.

/broadcast - Perintah Broadcast Untuk Menyiarkan Pesan atau Broadcast Pesan ke Semua Pengguna Bot.

/uptime - Perintah Uptime Untuk Melihat Status Bot Aktif.
```

### Perintah Khusus User atau Pengguna Bot
```
/ping - Perintah Ping Untuk Mengecek Status Bot.
```

### Variables 

* `API_HASH` Dapatkan API_HASH Dari my.telegram.org
* `API_ID` Dapatkan API_ID Dari my.telegram.org
* `TG_BOT_TOKEN` Dapatkan Token Bot Dari @BotFather
* `OWNER_ID` Masukkan ID Telegram OWNER
* `CHANNEL_ID` Channel ID Kamu, Contoh: -100xxxxxxxx
* `ADMINS` ID Admin Bot
* `START_MESSAGE` Pesan Start 
* `FORCE_SUB_MESSAGE` Pesan Force Subs 
* `FORCE_SUB_CHANNEL` Force Subs
* `FORCE_SUB_CHANNEL2` Force Subs 2
* `PROTECT_CONTENT` Protect_Contect True

### Extra Variables

* `CUSTOM_CAPTION` Masukkan Teks Kustom Kamu Jika Kamu Ingin Mengatur Teks Kustom, Kamu Dapat Menggunakan HTML dan Isian Untuk Pemformatan (Hanya Untuk Dokumen). Put Your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/renggi06/File-Sharing-Me/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents).
* `DISABLE_CHANNEL_BUTTON` Masukan True Untuk Nonaktifkan Tombol Berbagi Saluran, Default Jika False. Put True to Disable Channel Share Button, Default if False.

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - Nama Depan Pengguna. User First Name
* `{last}` - Nama Depan Belakang User Last Name
* `{id}` - ID Pengguna. User ID
* `{mention}` - Sebutkan Penggunanya. Mention The User
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - Nama File Dokumen. file name of the Document
* `{previouscaption}` - Keterangan Asli. Original Caption

##

   **Jangan Lupa Bintangnya ⭐⭐⭐**
