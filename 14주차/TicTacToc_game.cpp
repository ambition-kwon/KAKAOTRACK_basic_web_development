using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TicTacToc
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = this.CreateGraphics();
            Pen p = new Pen(new SolidBrush(Color.Gray), 10);

            g.DrawLine(p, 50 + 25, 30, 50 + 25, 320);
            g.DrawLine(p, 150 + 25, 30, 150 + 25, 320);
            g.DrawLine(p, 250 + 25, 30, 250 + 25, 320);

            g.DrawLine(p, 30, 50 + 25, 320, 50 + 25);
            g.DrawLine(p, 30, 150 + 25, 320, 150 + 25);
            g.DrawLine(p, 30, 250 + 25, 320, 250 + 25);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void MainForm_MouseDown(object sender, MouseEventArgs e)
        {
            Graphics g = this.CreateGraphics();
            if (e.Button == MouseButtons.Left)
            {
                for (int i = 0; i < 3; i++)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        g.DrawEllipse(
                            new Pen(new SolidBrush(Color.Red), 7),
                            i * 100 + 50,
                            j * 100 + 50,
                            50,
                            50);
                    }
                }
            }
            else
            {
                for (int i = 0; i < 3; i++)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        g.DrawLine(new Pen(new SolidBrush(Color.Blue), 7),
                            i * 100 + 50, j * 100 + 50,
                             i * 100 + 100, j * 100 + 100);
                        g.DrawLine(new Pen(new SolidBrush(Color.Blue), 7),
                            i * 100 + 100, j * 100 + 50,
                             i * 100 + 50, j * 100 + 100);
                    }
                }
            }
        }
    }
}
