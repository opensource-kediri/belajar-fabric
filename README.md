belajar-fabric
==============

Fabric merupakan sebuah pustaka (library) Python (2.5-2.7) dan *command line tool* untuk *streamlining script* menggunakan SSH yang bermafaat sebagai alat bantu penyebaran (*deployment*) atau juga dapat membantu pekerjaan yang berhubungan dengan *System Administration*.

Kebutuhan Sistem
----------------

Sebelum melakukan installasi, pastikan kamu sudah menyiapkan tools di bawah:
- OS Linux
- SSH server sebagai target percobaan
- Git (optional, digunakan untuk menggandakan (clone) source code project ini)

Installasi
----------

`$ sudo apt-get install python-dev python-setuptools`

`$ sudo easy_install pip`

`$ sudo pip install pycrypto`

`$ sudo pip install nose`

`$ sudo pip install fabric`


Cara Mengikuti Materi Ini
-------------------------
- Clone Source Code

`$ git clone git@github.com:opensource-kediri/belajar-fabric.git`

Setelah berhasil menggandakan (clone) source code, ikuti langkah tahap demi tahap dengan cara melakukan checkout setiap tag.

Berikut penjelasan setiap tahapan.

- Tahap #1

Deskripsi : Tahapan ini berisi source sederhana dalam implementasi di fabric.

Caranya:

`git checkout chapter-01`

Kamu bisa lihat isi source code nya masih sangat sederhana.

`$ cat fabfile.py`

```
from fabric.api import run

def hostname():
    hostname = run('hostname')
    print '-------------------------------'
    print 'hostname : %s' %hostname
    print '-------------------------------'


def ping_google():
    run('ping -c 4 google.com')

```

Kemudian coba eksekusi dengan cara

`$ fab -H user@<ip_atau_hostname> <nama_function>`

maka secara otomatis dari local (laptop) kamu bisa melihat hostname dan melakukan perintah ping tanpa harus secara manual login kedalam ssh.

Berikut contohnya:

```
fananimi-macbook:belajar-fabric fanani$ fab -H fanani@tuxhero.com hostname
[fanani@tuxhero.com] Executing task 'hostname'
[fanani@tuxhero.com] run: hostname
[fanani@tuxhero.com] Login password for 'fanani': 
[fanani@tuxhero.com] out: tuxhero
[fanani@tuxhero.com] out: 

-------------------------------
hostname : tuxhero
-------------------------------

Done.
Disconnecting from tuxhero.com... done.
fananimi-macbook:belajar-fabric fanani$ 
```

Tanya Jawab
-----------

Untuk tanya jawab bisa di tanyakan di HipChat Channel berikut https://opensource-kediri.hipchat.com/invite/172646/bfdf1d83b070e0d304170b65647ca8a1
