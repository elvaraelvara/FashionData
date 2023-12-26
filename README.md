# Dataset
 menggunakan dataset https://github.com/rfajri27/a555-dashboard/blob/main/all_data.csv 

Dataset yang diberikan terlihat seperti data penjualan produk fashion. Setiap baris mewakili satu transaksi atau pembelian, dan setiap kolom memberikan informasi spesifik tentang transaksi tersebut. Berikut adalah penjelasan untuk setiap kolom dalam dataset:

sales_id: ID penjualan atau nomor urut penjualan.

order_id: ID pesanan atau nomor urut pesanan.

product_id: ID produk atau nomor urut produk.

price_per_unit: Harga per unit produk.

quantity_x: Jumlah unit yang dibeli (pada saat pembelian).

total_price: Total harga pembelian (jumlah unit * harga per unit).

product_type: Jenis produk yang dibeli.

product_name: Nama produk.

size: Ukuran produk (misalnya, S, M, L, XS).

colour: Warna produk.

price: Harga produk.

quantity_y: Jumlah produk dalam stok (pada saat pembelian).

description: Deskripsi produk.

customer_id: ID pelanggan atau nomor urut pelanggan.

payment: Metode pembayaran yang digunakan.

order_date: Tanggal pembelian.

delivery_date: Tanggal pengiriman.

delivery_time: Waktu pengiriman.

customer_name: Nama pelanggan.

gender: Jenis kelamin pelanggan.

age: Usia pelanggan.

home_address: Alamat rumah pelanggan.

zip_code: Kode pos pelanggan.

city: Kota pelanggan.

state: Negara bagian atau provinsi.

country: Negara.

status: Status pembelian atau akun pelanggan (misalnya, Active).

age_group: Grup usia pelanggan (misalnya, Seniors, Adults).

# Setup environment


```
python -m venv venv

.\venv\Scripts\activate

pip install pandas numpy matplotlib seaborn streamlit
```

# Run steamlit 

```
streamlit run streamlit.py
```


