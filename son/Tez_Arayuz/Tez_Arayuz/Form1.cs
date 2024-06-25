using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;// buraya python exe dosyasının exe yolunu ekledi
using System.Globalization;
using System.Drawing.Drawing2D;
using System.Media;

namespace Tez_Arayuz
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        

        private void playSimpleSound()
        {
            SoundPlayer simpleSound = new SoundPlayer(@"D:\PAÜ DERS\TEZ\Projeler\son\Tez_Arayuz\mix_09s-_audio-joiner.com_.wav");
            simpleSound.Play();

        }



        public void pyCalistir()
        {
            var path = "main.py";
            var info = new ProcessStartInfo("python")
            {
                Arguments = path,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                WorkingDirectory = @"D:/PAÜ DERS/TEZ/Projeler/son",
                CreateNoWindow = true,
                StandardOutputEncoding = Encoding.UTF8,
                StandardErrorEncoding = Encoding.UTF8
            };
            var process = new Process();
            process.StartInfo = info;

            process.Start();
            string output = process.StandardOutput.ReadToEnd();
            Console.WriteLine(output);
            MessageBox.Show(output);
            string err = process.StandardError.ReadToEnd();
            Console.WriteLine(err);
            //MessageBox.Show(err);
            process.WaitForExit();
        }

        

        private void Form1_Load(object sender, EventArgs e)
        {
            //pyCalistir();
            playSimpleSound();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            // BURADA EKRANA TIKLANDIĞI ZAMAN DİĞER FORMA GEÇİŞ İŞLEMİNİ YAPTIK
            // THİS.HİDE İSE ÖNCEKİ FORMUN GİZLENMESİ İÇİN YAZILMIŞTIR
            Fr_main fr_main = new Fr_main();
            fr_main.Show();
            this.Hide();
        }
    }
}
