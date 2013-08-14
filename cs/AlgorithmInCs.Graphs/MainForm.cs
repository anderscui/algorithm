using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace AlgorithmInCs.Figures
{
    public partial class MainForm : Form
    {
        private bool drawEllipse = false;

        public MainForm()
        {
            InitializeComponent();

            SetStyle(ControlStyles.ResizeRedraw, true);
        }

        private void btnDrawEllipse_Click(object sender, System.EventArgs e)
        {
            drawEllipse = !drawEllipse;
            Invalidate(true);
            Update();

            //Refresh();
        }

        private void MainForm_Paint(object sender, PaintEventArgs e)
        {
            //if(!drawEllipse) return;
            //e.Graphics.FillEllipse(Brushes.DarkBlue, ClientRectangle);
        }

        private void btnDrawArc_Click(object sender, System.EventArgs e)
        {
            Refresh();
            using (var g = CreateGraphics())
            {
                g.DrawArc(Pens.Black, 0, 0, 100, 100, 0, 360);
            }
        }

        private void btnDrawLines_Click(object sender, System.EventArgs e)
        {
            Invalidate(true);
            Update();

            using (var g = CreateGraphics())
            {
                g.DrawPolygon(Pens.BlueViolet,
                    new[] { new Point(10, 10), 
                    new Point(110, 10),
                    new Point(110, 110) 
                });
            }
        }

        GraphicsPath GetRoundedRectPath(Rectangle rect, int radius)
        {
            var diameter = 2 * radius;
            var arcRect = new Rectangle(rect.Location, new Size(diameter, diameter));

            var path = new GraphicsPath();
            path.AddArc(arcRect, 180, 90);

            arcRect.X = rect.Right - diameter;
            path.AddArc(arcRect, 270, 90);

            arcRect.Y = rect.Bottom - diameter;
            path.AddArc(arcRect, 0, 90);

            arcRect.X = rect.Left;
            path.AddArc(arcRect, 90, 90);

            path.CloseFigure();
            return path;
        }

        private void btnDrawPath_Click(object sender, System.EventArgs e)
        {
            int width = ClientRectangle.Width;
            int height = ClientRectangle.Height;

            var rect = new Rectangle(10, 10, width - 20, height - 20);
            using (var g = CreateGraphics())
            {
                using (var path = GetRoundedRectPath(rect, width / 50))
                {
                    g.FillPath(Brushes.DarkGreen, path);
                    g.DrawPath(Pens.Black, path);
                }
            }
        }

        private void btnDrawRuler_Click(object sender, System.EventArgs e)
        {
            //var rect = this.ClientRectangle;
            //var size = this.ClientSize;

            int totalWidth = ClientSize.Width - 20;
            totalWidth = totalWidth - totalWidth % 10;

            int left = 10;
            int right = left + totalWidth;

            var leftEnd = new Point(left, 200);
            var rightEnd = new Point(right, 200);
            var cents = 10;
            var height = 100;

            using (var g = CreateGraphics())
            {
                DrawRuler(g, leftEnd, rightEnd, 1);
                g.DrawLine(Pens.BlueViolet, right, leftEnd.Y, right, leftEnd.Y - Heights[0]);
            }
        }

        private int[] Steps = {10, 2, 5};
        private int[] Heights = {40, 25, 12};
        private void DrawRuler(Graphics g, Point leftEnd, Point rightEnd, int step)
        {
            if(step > Steps.Length)
                return;

            var cents = Steps[step - 1];
            var height = Heights[step - 1];
            var totalWidth = rightEnd.X - leftEnd.X;
            var widthPerCent = totalWidth / cents;

            for (int x = leftEnd.X; x < rightEnd.X; x += widthPerCent)
            {
                g.DrawLine(Pens.BlueViolet, x, leftEnd.Y, x, leftEnd.Y - height);
                DrawRuler(g, new Point() { X = x, Y = leftEnd.Y },
                             new Point() { X = x + widthPerCent, Y = leftEnd.Y },
                             step + 1);
            }
        }
    }
}
