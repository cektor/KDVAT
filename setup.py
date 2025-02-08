from setuptools import setup, find_packages

setup(
    name="kdvat",  # Paket adı
    version="1.0",  # Paket sürümü
    description="This program was developed to facilitate VAT calculations",  # Paket açıklaması
    author="Fatih Önder",  # Paket sahibi adı
    author_email="fatih@algyazilim.com",  # Paket sahibi e-posta adresi
    url="https://github.com/cektor/KDVAT",  # Paket deposu URL'si
    packages=find_packages(),  # Otomatik olarak tüm alt paketleri bulur
    install_requires=[
        'PyQt5',  
        'openpyxl',  
        'requests',
        'matplotlib',
        'defusedxml',
    ],
    package_data={
        'kdvat': ['*.png', '*.desktop'],  # 'kimoki' paketine dahil dosyalar
    },
    data_files=[
        ('share/applications', ['kdvat.desktop']),  # Uygulama menüsüne .desktop dosyasını ekler
        ('share/icons/hicolor/48x48/apps', ['kdv.png']),  # Simgeyi uygun yere ekler
    ],
    entry_points={
        'gui_scripts': [
            'kdvat=kdvat:main',  
        ]
    },
)
