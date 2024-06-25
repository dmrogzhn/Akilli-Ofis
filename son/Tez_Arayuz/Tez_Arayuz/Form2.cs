using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Media;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Tez_Arayuz
{
    public partial class Fr_main : Form
    {
        public Fr_main()
        {
            InitializeComponent();

        }
        public SqlConnection connection = new SqlConnection("Data Source=DESKTOP-S3S5IBG\\SQLEXPRESS;Initial Catalog=lisans_tez;User ID=sa;Password=s");

        private void playSimpleSound()
        {
            SoundPlayer simpleSound = new SoundPlayer(@"D:\PAÜ DERS\TEZ\Projeler\son\Tez_Arayuz\BÖRÜ-2039-HOŞ-GELDİN-BAŞKAN-ZİL-SESİ-[AudioTrimmer.com].wav");
            simpleSound.Play();
        }

        public void onay()
        {
            SoundPlayer simpleSound = new SoundPlayer(@"D:\PAÜ DERS\TEZ\Projeler\son\Tez_Arayuz\anlasildi_baskan.wav");
            simpleSound.Play();
        }

        public void iptal()
        {
            SoundPlayer simpleSound = new SoundPlayer(@"D:\PAÜ DERS\TEZ\Projeler\son\Tez_Arayuz\iptal_edildi.wav");
            simpleSound.Play();
        }

        public void duygu(string duygu)
        {
            string gelen = duygu.Trim();
            string dosyaYolu = $"D:\\PAÜ DERS\\TEZ/Projeler/son/Tez_Arayuz/{gelen}.png";
            
            pbox_duygu.Image = Image.FromFile(dosyaYolu);
        }

        public void icecek ( string icecek)
        {
            string gelen = icecek.Trim();
            string dosyaYolu = $"D:\\PAÜ DERS\\TEZ/Projeler/son/Tez_Arayuz/{gelen}.png";

            pbox_icecek.Image = Image.FromFile(dosyaYolu);
        }

        public void muzik(string muzik)
        {
            string gelen = muzik.Trim();
            string dosyaYolu = $"D:\\PAÜ DERS\\TEZ/Projeler/son/Tez_Arayuz/{gelen}.png";

            pbox_muzik.Image = Image.FromFile(dosyaYolu);

        }

        public void koku(string koku)
        {
            string gelen = koku.Trim();
            string dosyaYolu = $"D:\\PAÜ DERS\\TEZ/Projeler/son/Tez_Arayuz/{gelen}.png";

            pbox_koku.Image = Image.FromFile(dosyaYolu);

        }

        public void label(string muzik, string koku, string icecek, int klima, string duygu)
        {
            lbl_duygu.Text = duygu.Trim();
            lbl_muzik.Text = muzik.Trim();
            lbl_koku.Text = koku.Trim();
            lbl_icecek.Text = icecek.Trim();
            lbl_klima.Text = klima.ToString();
        }

        private void Fr_main_Load(object sender, EventArgs e)
        {

            connection.Open();

            SqlCommand command = new SqlCommand("SELECT TOP 1 muzik, koku, icecek, klima, duygu FROM tbl_sonuclar ORDER BY SonucID DESC",connection);
            SqlDataAdapter adapter = new SqlDataAdapter(command);
            DataTable dataTable = new DataTable();
            adapter.Fill(dataTable);
            DataRow row = dataTable.Rows[0];

            string muzik_ = row["muzik"].ToString().Trim();
            string koku_ = row["koku"].ToString().Trim();
            string icecek_ = row["icecek"].ToString().Trim();
            int klima_ = Convert.ToInt32(row["klima"]);
            string duygu_ = row["duygu"].ToString().Trim();

            connection.Close();
            label(muzik_, koku_, icecek_, klima_, duygu_);
            muzik(muzik_);
            icecek(icecek_);
            koku(koku_);
            duygu(duygu_);


            playSimpleSound();
        }

        private void btn_onay_Click(object sender, EventArgs e)
        {
            onay();
            
        }

        private void btn_red_Click(object sender, EventArgs e)
        {
            iptal();
            MessageBox.Show("Komutlar İptal Eildi!!");
            Environment.Exit(0);
        }
    }
}
